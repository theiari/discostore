import uvicorn
import os, json
import time as time_module
import logging
from fastapi import Depends, FastAPI, HTTPException, Request, status, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from pydantic_classes import *
from sql_alchemy import *

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

############################################
#
#   Initialize the database
#
############################################

def init_db():
    SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data/Library.db")
    # Ensure local SQLite directory exists (safe no-op for other DBs)
    os.makedirs("data", exist_ok=True)
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
        pool_size=10,
        max_overflow=20,
        pool_pre_ping=True,
        echo=False
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    return SessionLocal

app = FastAPI(
    title="Library API",
    description="Auto-generated REST API with full CRUD operations, relationship management, and advanced features",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_tags=[
        {"name": "System", "description": "System health and statistics"},
        {"name": "Track", "description": "Operations for Track entities"},
        {"name": "Track Relationships", "description": "Manage Track relationships"},
        {"name": "Track Methods", "description": "Execute Track methods"},
        {"name": "Artist", "description": "Operations for Artist entities"},
        {"name": "Artist Relationships", "description": "Manage Artist relationships"},
        {"name": "Artist Methods", "description": "Execute Artist methods"},
        {"name": "Album", "description": "Operations for Album entities"},
        {"name": "Album Relationships", "description": "Manage Album relationships"},
        {"name": "Album Methods", "description": "Execute Album methods"},
        {"name": "CartItem", "description": "Operations for CartItem entities"},
        {"name": "CartItem Relationships", "description": "Manage CartItem relationships"},
        {"name": "CartItem Methods", "description": "Execute CartItem methods"},
        {"name": "Payment", "description": "Operations for Payment entities"},
        {"name": "Payment Relationships", "description": "Manage Payment relationships"},
        {"name": "Payment Methods", "description": "Execute Payment methods"},
        {"name": "OrderItem", "description": "Operations for OrderItem entities"},
        {"name": "OrderItem Relationships", "description": "Manage OrderItem relationships"},
        {"name": "OrderItem Methods", "description": "Execute OrderItem methods"},
        {"name": "Address", "description": "Operations for Address entities"},
        {"name": "Address Relationships", "description": "Manage Address relationships"},
        {"name": "Address Methods", "description": "Execute Address methods"},
        {"name": "Review", "description": "Operations for Review entities"},
        {"name": "Review Relationships", "description": "Manage Review relationships"},
        {"name": "Review Methods", "description": "Execute Review methods"},
        {"name": "Cart", "description": "Operations for Cart entities"},
        {"name": "Cart Relationships", "description": "Manage Cart relationships"},
        {"name": "Cart Methods", "description": "Execute Cart methods"},
        {"name": "Order", "description": "Operations for Order entities"},
        {"name": "Order Relationships", "description": "Manage Order relationships"},
        {"name": "Order Methods", "description": "Execute Order methods"},
        {"name": "User", "description": "Operations for User entities"},
        {"name": "User Methods", "description": "Execute User methods"},
        {"name": "Customer", "description": "Operations for Customer entities"},
        {"name": "Customer Relationships", "description": "Manage Customer relationships"},
        {"name": "Customer Methods", "description": "Execute Customer methods"},
        {"name": "Admin", "description": "Operations for Admin entities"},
        {"name": "Admin Methods", "description": "Execute Admin methods"},
    ]
)

# Enable CORS for all origins (for development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

############################################
#
#   Middleware
#
############################################

# Request logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log all incoming requests and responses."""
    logger.info(f"Incoming request: {request.method} {request.url.path}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response

# Request timing middleware
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """Add processing time header to all responses."""
    start_time = time_module.time()
    response = await call_next(request)
    process_time = time_module.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

############################################
#
#   Exception Handlers
#
############################################

# Global exception handlers
@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    """Handle ValueError exceptions."""
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error": "Bad Request",
            "message": str(exc),
            "detail": "Invalid input data provided"
        }
    )


@app.exception_handler(IntegrityError)
async def integrity_error_handler(request: Request, exc: IntegrityError):
    """Handle database integrity errors."""
    logger.error(f"Database integrity error: {exc}")

    # Extract more detailed error information
    error_detail = str(exc.orig) if hasattr(exc, 'orig') else str(exc)

    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "error": "Conflict",
            "message": "Data conflict occurred",
            "detail": error_detail
        }
    )


@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_error_handler(request: Request, exc: SQLAlchemyError):
    """Handle general SQLAlchemy errors."""
    logger.error(f"Database error: {exc}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "Internal Server Error",
            "message": "Database operation failed",
            "detail": "An internal database error occurred"
        }
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Handle HTTP exceptions with consistent format."""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail if isinstance(exc.detail, str) else "HTTP Error",
            "message": exc.detail,
            "detail": f"HTTP {exc.status_code} error occurred"
        }
    )

# Initialize database session
SessionLocal = init_db()
# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        logger.error("Database session rollback due to exception")
        raise
    finally:
        db.close()

############################################
#
#   Global API endpoints
#
############################################

@app.get("/", tags=["System"])
def root():
    """Root endpoint - API information"""
    return {
        "name": "Library API",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health", tags=["System"])
def health_check():
    """Health check endpoint for monitoring"""
    from datetime import datetime
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "database": "connected"
    }


@app.get("/statistics", tags=["System"])
def get_statistics(database: Session = Depends(get_db)):
    """Get database statistics for all entities"""
    stats = {}
    stats["track_count"] = database.query(Track).count()
    stats["artist_count"] = database.query(Artist).count()
    stats["album_count"] = database.query(Album).count()
    stats["cartitem_count"] = database.query(CartItem).count()
    stats["payment_count"] = database.query(Payment).count()
    stats["orderitem_count"] = database.query(OrderItem).count()
    stats["address_count"] = database.query(Address).count()
    stats["review_count"] = database.query(Review).count()
    stats["cart_count"] = database.query(Cart).count()
    stats["order_count"] = database.query(Order).count()
    stats["user_count"] = database.query(User).count()
    stats["customer_count"] = database.query(Customer).count()
    stats["admin_count"] = database.query(Admin).count()
    stats["total_entities"] = sum(stats.values())
    return stats


############################################
#
#   BESSER Action Language standard lib
#
############################################


async def BAL_size(sequence:list) -> int:
    return len(sequence)

async def BAL_is_empty(sequence:list) -> bool:
    return len(sequence) == 0

async def BAL_add(sequence:list, elem) -> None:
    sequence.append(elem)

async def BAL_remove(sequence:list, elem) -> None:
    sequence.remove(elem)

async def BAL_contains(sequence:list, elem) -> bool:
    return elem in sequence

async def BAL_filter(sequence:list, predicate) -> list:
    return [elem for elem in sequence if predicate(elem)]

async def BAL_forall(sequence:list, predicate) -> bool:
    for elem in sequence:
        if not predicate(elem):
            return False
    return True

async def BAL_exists(sequence:list, predicate) -> bool:
    for elem in sequence:
        if predicate(elem):
            return True
    return False

async def BAL_one(sequence:list, predicate) -> bool:
    found = False
    for elem in sequence:
        if predicate(elem):
            if found:
                return False
            found = True
    return found

async def BAL_is_unique(sequence:list, mapping) -> bool:
    mapped = [mapping(elem) for elem in sequence]
    return len(set(mapped)) == len(mapped)

async def BAL_map(sequence:list, mapping) -> list:
    return [mapping(elem) for elem in sequence]

async def BAL_reduce(sequence:list, reduce_fn, aggregator) -> any:
    for elem in sequence:
        aggregator = reduce_fn(aggregator, elem)
    return aggregator


############################################
#
#   Track functions
#
############################################

@app.get("/track/", response_model=None, tags=["Track"])
def get_all_track(detailed: bool = False, database: Session = Depends(get_db)) -> list:
    from sqlalchemy.orm import joinedload

    # Use detailed=true to get entities with eagerly loaded relationships (for tables with lookup columns)
    if detailed:
        # Eagerly load all relationships to avoid N+1 queries
        query = database.query(Track)
        query = query.options(joinedload(Track.album_1))
        track_list = query.all()

        # Serialize with relationships included
        result = []
        for track_item in track_list:
            item_dict = track_item.__dict__.copy()
            item_dict.pop('_sa_instance_state', None)

            # Add many-to-one relationships (foreign keys for lookup columns)
            if track_item.album_1:
                related_obj = track_item.album_1
                related_dict = related_obj.__dict__.copy()
                related_dict.pop('_sa_instance_state', None)
                item_dict['album_1'] = related_dict
            else:
                item_dict['album_1'] = None


            result.append(item_dict)
        return result
    else:
        # Default: return flat entities (faster for charts/widgets without lookup columns)
        return database.query(Track).all()


@app.get("/track/count/", response_model=None, tags=["Track"])
def get_count_track(database: Session = Depends(get_db)) -> dict:
    """Get the total count of Track entities"""
    count = database.query(Track).count()
    return {"count": count}


@app.get("/track/paginated/", response_model=None, tags=["Track"])
def get_paginated_track(skip: int = 0, limit: int = 100, detailed: bool = False, database: Session = Depends(get_db)) -> dict:
    """Get paginated list of Track entities"""
    total = database.query(Track).count()
    track_list = database.query(Track).offset(skip).limit(limit).all()
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": track_list
    }


@app.get("/track/search/", response_model=None, tags=["Track"])
def search_track(
    database: Session = Depends(get_db)
) -> list:
    """Search Track entities by attributes"""
    query = database.query(Track)


    results = query.all()
    return results


@app.get("/track/{track_id}/", response_model=None, tags=["Track"])
async def get_track(track_id: int, database: Session = Depends(get_db)) -> Track:
    db_track = database.query(Track).filter(Track.id == track_id).first()
    if db_track is None:
        raise HTTPException(status_code=404, detail="Track not found")

    response_data = {
        "track": db_track,
}
    return response_data



@app.post("/track/", response_model=None, tags=["Track"])
async def create_track(track_data: TrackCreate, database: Session = Depends(get_db)) -> Track:

    if track_data.album_1 is not None:
        db_album_1 = database.query(Album).filter(Album.id == track_data.album_1).first()
        if not db_album_1:
            raise HTTPException(status_code=400, detail="Album not found")
    else:
        raise HTTPException(status_code=400, detail="Album ID is required")

    db_track = Track(
        duration=track_data.duration,        title=track_data.title,        truckNumber=track_data.truckNumber,        Id=track_data.Id,        album_1_id=track_data.album_1        )

    database.add(db_track)
    database.commit()
    database.refresh(db_track)




    return db_track


@app.post("/track/bulk/", response_model=None, tags=["Track"])
async def bulk_create_track(items: list[TrackCreate], database: Session = Depends(get_db)) -> dict:
    """Create multiple Track entities at once"""
    created_items = []
    errors = []

    for idx, item_data in enumerate(items):
        try:
            # Basic validation for each item
            if not item_data.album_1:
                raise ValueError("Album ID is required")

            db_track = Track(
                duration=item_data.duration,                title=item_data.title,                truckNumber=item_data.truckNumber,                Id=item_data.Id,                album_1_id=item_data.album_1            )
            database.add(db_track)
            database.flush()  # Get ID without committing
            created_items.append(db_track.id)
        except Exception as e:
            errors.append({"index": idx, "error": str(e)})

    if errors:
        database.rollback()
        raise HTTPException(status_code=400, detail={"message": "Bulk creation failed", "errors": errors})

    database.commit()
    return {
        "created_count": len(created_items),
        "created_ids": created_items,
        "message": f"Successfully created {len(created_items)} Track entities"
    }


@app.delete("/track/bulk/", response_model=None, tags=["Track"])
async def bulk_delete_track(ids: list[int], database: Session = Depends(get_db)) -> dict:
    """Delete multiple Track entities at once"""
    deleted_count = 0
    not_found = []

    for item_id in ids:
        db_track = database.query(Track).filter(Track.id == item_id).first()
        if db_track:
            database.delete(db_track)
            deleted_count += 1
        else:
            not_found.append(item_id)

    database.commit()

    return {
        "deleted_count": deleted_count,
        "not_found": not_found,
        "message": f"Successfully deleted {deleted_count} Track entities"
    }

@app.put("/track/{track_id}/", response_model=None, tags=["Track"])
async def update_track(track_id: int, track_data: TrackCreate, database: Session = Depends(get_db)) -> Track:
    db_track = database.query(Track).filter(Track.id == track_id).first()
    if db_track is None:
        raise HTTPException(status_code=404, detail="Track not found")

    setattr(db_track, 'duration', track_data.duration)
    setattr(db_track, 'title', track_data.title)
    setattr(db_track, 'truckNumber', track_data.truckNumber)
    setattr(db_track, 'Id', track_data.Id)
    if track_data.album_1 is not None:
        db_album_1 = database.query(Album).filter(Album.id == track_data.album_1).first()
        if not db_album_1:
            raise HTTPException(status_code=400, detail="Album not found")
        setattr(db_track, 'album_1_id', track_data.album_1)
    database.commit()
    database.refresh(db_track)

    return db_track


@app.delete("/track/{track_id}/", response_model=None, tags=["Track"])
async def delete_track(track_id: int, database: Session = Depends(get_db)):
    db_track = database.query(Track).filter(Track.id == track_id).first()
    if db_track is None:
        raise HTTPException(status_code=404, detail="Track not found")
    database.delete(db_track)
    database.commit()
    return db_track




############################################
#   Track Method Endpoints
############################################




@app.post("/track/methods/getOverallDuration/", response_model=None, tags=["Track Methods"])
async def track_getOverallDuration(
    database: Session = Depends(get_db)
):
    """
    Execute the getOverallDuration class method on Track.
    This method operates on all Track entities or performs class-level operations.
    """
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output


        # Method body not defined
        result = None

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Handle result serialization
        if hasattr(result, '__iter__') and not isinstance(result, (str, dict)):
            # It's a list of entities
            result_data = []
            for item in result:
                if hasattr(item, '__dict__'):
                    item_dict = {k: v for k, v in item.__dict__.items() if not k.startswith('_')}
                    result_data.append(item_dict)
                else:
                    result_data.append(str(item))
            result = result_data
        elif hasattr(result, '__dict__'):
            result = {k: v for k, v in result.__dict__.items() if not k.startswith('_')}

        return {
            "class": "Track",
            "method": "getOverallDuration",
            "status": "executed",
            "result": result,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")




############################################
#
#   Artist functions
#
############################################

@app.get("/artist/", response_model=None, tags=["Artist"])
def get_all_artist(detailed: bool = False, database: Session = Depends(get_db)) -> list:
    from sqlalchemy.orm import joinedload

    # Use detailed=true to get entities with eagerly loaded relationships (for tables with lookup columns)
    if detailed:
        # Eagerly load all relationships to avoid N+1 queries
        query = database.query(Artist)
        query = query.options(joinedload(Artist.album))
        artist_list = query.all()

        # Serialize with relationships included
        result = []
        for artist_item in artist_list:
            item_dict = artist_item.__dict__.copy()
            item_dict.pop('_sa_instance_state', None)

            # Add many-to-one relationships (foreign keys for lookup columns)
            if artist_item.album:
                related_obj = artist_item.album
                related_dict = related_obj.__dict__.copy()
                related_dict.pop('_sa_instance_state', None)
                item_dict['album'] = related_dict
            else:
                item_dict['album'] = None


            result.append(item_dict)
        return result
    else:
        # Default: return flat entities (faster for charts/widgets without lookup columns)
        return database.query(Artist).all()


@app.get("/artist/count/", response_model=None, tags=["Artist"])
def get_count_artist(database: Session = Depends(get_db)) -> dict:
    """Get the total count of Artist entities"""
    count = database.query(Artist).count()
    return {"count": count}


@app.get("/artist/paginated/", response_model=None, tags=["Artist"])
def get_paginated_artist(skip: int = 0, limit: int = 100, detailed: bool = False, database: Session = Depends(get_db)) -> dict:
    """Get paginated list of Artist entities"""
    total = database.query(Artist).count()
    artist_list = database.query(Artist).offset(skip).limit(limit).all()
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": artist_list
    }


@app.get("/artist/search/", response_model=None, tags=["Artist"])
def search_artist(
    database: Session = Depends(get_db)
) -> list:
    """Search Artist entities by attributes"""
    query = database.query(Artist)


    results = query.all()
    return results


@app.get("/artist/{artist_id}/", response_model=None, tags=["Artist"])
async def get_artist(artist_id: int, database: Session = Depends(get_db)) -> Artist:
    db_artist = database.query(Artist).filter(Artist.id == artist_id).first()
    if db_artist is None:
        raise HTTPException(status_code=404, detail="Artist not found")

    response_data = {
        "artist": db_artist,
}
    return response_data



@app.post("/artist/", response_model=None, tags=["Artist"])
async def create_artist(artist_data: ArtistCreate, database: Session = Depends(get_db)) -> Artist:

    if artist_data.album is not None:
        db_album = database.query(Album).filter(Album.id == artist_data.album).first()
        if not db_album:
            raise HTTPException(status_code=400, detail="Album not found")
    else:
        raise HTTPException(status_code=400, detail="Album ID is required")

    db_artist = Artist(
        Id=artist_data.Id,        bio=artist_data.bio,        name=artist_data.name,        country=artist_data.country,        album_id=artist_data.album        )

    database.add(db_artist)
    database.commit()
    database.refresh(db_artist)




    return db_artist


@app.post("/artist/bulk/", response_model=None, tags=["Artist"])
async def bulk_create_artist(items: list[ArtistCreate], database: Session = Depends(get_db)) -> dict:
    """Create multiple Artist entities at once"""
    created_items = []
    errors = []

    for idx, item_data in enumerate(items):
        try:
            # Basic validation for each item
            if not item_data.album:
                raise ValueError("Album ID is required")

            db_artist = Artist(
                Id=item_data.Id,                bio=item_data.bio,                name=item_data.name,                country=item_data.country,                album_id=item_data.album            )
            database.add(db_artist)
            database.flush()  # Get ID without committing
            created_items.append(db_artist.id)
        except Exception as e:
            errors.append({"index": idx, "error": str(e)})

    if errors:
        database.rollback()
        raise HTTPException(status_code=400, detail={"message": "Bulk creation failed", "errors": errors})

    database.commit()
    return {
        "created_count": len(created_items),
        "created_ids": created_items,
        "message": f"Successfully created {len(created_items)} Artist entities"
    }


@app.delete("/artist/bulk/", response_model=None, tags=["Artist"])
async def bulk_delete_artist(ids: list[int], database: Session = Depends(get_db)) -> dict:
    """Delete multiple Artist entities at once"""
    deleted_count = 0
    not_found = []

    for item_id in ids:
        db_artist = database.query(Artist).filter(Artist.id == item_id).first()
        if db_artist:
            database.delete(db_artist)
            deleted_count += 1
        else:
            not_found.append(item_id)

    database.commit()

    return {
        "deleted_count": deleted_count,
        "not_found": not_found,
        "message": f"Successfully deleted {deleted_count} Artist entities"
    }

@app.put("/artist/{artist_id}/", response_model=None, tags=["Artist"])
async def update_artist(artist_id: int, artist_data: ArtistCreate, database: Session = Depends(get_db)) -> Artist:
    db_artist = database.query(Artist).filter(Artist.id == artist_id).first()
    if db_artist is None:
        raise HTTPException(status_code=404, detail="Artist not found")

    setattr(db_artist, 'Id', artist_data.Id)
    setattr(db_artist, 'bio', artist_data.bio)
    setattr(db_artist, 'name', artist_data.name)
    setattr(db_artist, 'country', artist_data.country)
    if artist_data.album is not None:
        db_album = database.query(Album).filter(Album.id == artist_data.album).first()
        if not db_album:
            raise HTTPException(status_code=400, detail="Album not found")
        setattr(db_artist, 'album_id', artist_data.album)
    database.commit()
    database.refresh(db_artist)

    return db_artist


@app.delete("/artist/{artist_id}/", response_model=None, tags=["Artist"])
async def delete_artist(artist_id: int, database: Session = Depends(get_db)):
    db_artist = database.query(Artist).filter(Artist.id == artist_id).first()
    if db_artist is None:
        raise HTTPException(status_code=404, detail="Artist not found")
    database.delete(db_artist)
    database.commit()
    return db_artist




############################################
#   Artist Method Endpoints
############################################




@app.post("/artist/methods/getDiscography/", response_model=None, tags=["Artist Methods"])
async def artist_getDiscography(
    database: Session = Depends(get_db)
):
    """
    Execute the getDiscography class method on Artist.
    This method operates on all Artist entities or performs class-level operations.
    """
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output


        # Method body not defined
        result = None

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Handle result serialization
        if hasattr(result, '__iter__') and not isinstance(result, (str, dict)):
            # It's a list of entities
            result_data = []
            for item in result:
                if hasattr(item, '__dict__'):
                    item_dict = {k: v for k, v in item.__dict__.items() if not k.startswith('_')}
                    result_data.append(item_dict)
                else:
                    result_data.append(str(item))
            result = result_data
        elif hasattr(result, '__dict__'):
            result = {k: v for k, v in result.__dict__.items() if not k.startswith('_')}

        return {
            "class": "Artist",
            "method": "getDiscography",
            "status": "executed",
            "result": result,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")




############################################
#
#   Album functions
#
############################################

@app.get("/album/", response_model=None, tags=["Album"])
def get_all_album(detailed: bool = False, database: Session = Depends(get_db)) -> list:
    from sqlalchemy.orm import joinedload

    # Use detailed=true to get entities with eagerly loaded relationships (for tables with lookup columns)
    if detailed:
        # Eagerly load all relationships to avoid N+1 queries
        query = database.query(Album)
        query = query.options(joinedload(Album.orderitem))
        album_list = query.all()

        # Serialize with relationships included
        result = []
        for album_item in album_list:
            item_dict = album_item.__dict__.copy()
            item_dict.pop('_sa_instance_state', None)

            # Add many-to-one relationships (foreign keys for lookup columns)
            if album_item.orderitem:
                related_obj = album_item.orderitem
                related_dict = related_obj.__dict__.copy()
                related_dict.pop('_sa_instance_state', None)
                item_dict['orderitem'] = related_dict
            else:
                item_dict['orderitem'] = None

            # Add many-to-many and one-to-many relationship objects (full details)
            artist_list = database.query(Artist).filter(Artist.album_id == album_item.id).all()
            item_dict['createdBy'] = []
            for artist_obj in artist_list:
                artist_dict = artist_obj.__dict__.copy()
                artist_dict.pop('_sa_instance_state', None)
                item_dict['createdBy'].append(artist_dict)
            track_list = database.query(Track).filter(Track.album_1_id == album_item.id).all()
            item_dict['contains'] = []
            for track_obj in track_list:
                track_dict = track_obj.__dict__.copy()
                track_dict.pop('_sa_instance_state', None)
                item_dict['contains'].append(track_dict)

            result.append(item_dict)
        return result
    else:
        # Default: return flat entities (faster for charts/widgets without lookup columns)
        return database.query(Album).all()


@app.get("/album/count/", response_model=None, tags=["Album"])
def get_count_album(database: Session = Depends(get_db)) -> dict:
    """Get the total count of Album entities"""
    count = database.query(Album).count()
    return {"count": count}


@app.get("/album/paginated/", response_model=None, tags=["Album"])
def get_paginated_album(skip: int = 0, limit: int = 100, detailed: bool = False, database: Session = Depends(get_db)) -> dict:
    """Get paginated list of Album entities"""
    total = database.query(Album).count()
    album_list = database.query(Album).offset(skip).limit(limit).all()
    # By default, return flat entities (for charts/widgets)
    # Use detailed=true to get entities with relationships
    if not detailed:
        return {
            "total": total,
            "skip": skip,
            "limit": limit,
            "data": album_list
        }

    result = []
    for album_item in album_list:
        createdBy_ids = database.query(Artist.id).filter(Artist.album_id == album_item.id).all()
        contains_ids = database.query(Track.id).filter(Track.album_1_id == album_item.id).all()
        item_data = {
            "album": album_item,
            "createdBy_ids": [x[0] for x in createdBy_ids],            "contains_ids": [x[0] for x in contains_ids]        }
        result.append(item_data)
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": result
    }


@app.get("/album/search/", response_model=None, tags=["Album"])
def search_album(
    database: Session = Depends(get_db)
) -> list:
    """Search Album entities by attributes"""
    query = database.query(Album)


    results = query.all()
    return results


@app.get("/album/{album_id}/", response_model=None, tags=["Album"])
async def get_album(album_id: int, database: Session = Depends(get_db)) -> Album:
    db_album = database.query(Album).filter(Album.id == album_id).first()
    if db_album is None:
        raise HTTPException(status_code=404, detail="Album not found")

    createdBy_ids = database.query(Artist.id).filter(Artist.album_id == db_album.id).all()
    contains_ids = database.query(Track.id).filter(Track.album_1_id == db_album.id).all()
    response_data = {
        "album": db_album,
        "createdBy_ids": [x[0] for x in createdBy_ids],        "contains_ids": [x[0] for x in contains_ids]}
    return response_data



@app.post("/album/", response_model=None, tags=["Album"])
async def create_album(album_data: AlbumCreate, database: Session = Depends(get_db)) -> Album:

    if album_data.orderitem is not None:
        db_orderitem = database.query(OrderItem).filter(OrderItem.id == album_data.orderitem).first()
        if not db_orderitem:
            raise HTTPException(status_code=400, detail="OrderItem not found")
    else:
        raise HTTPException(status_code=400, detail="OrderItem ID is required")

    db_album = Album(
        format=album_data.format,        stockQuantity=album_data.stockQuantity,        price=album_data.price,        artist=album_data.artist,        releaseYear=album_data.releaseYear,        Id=album_data.Id,        title=album_data.title,        orderitem_id=album_data.orderitem        )

    database.add(db_album)
    database.commit()
    database.refresh(db_album)

    if album_data.createdBy:
        # Validate that all Artist IDs exist
        for artist_id in album_data.createdBy:
            db_artist = database.query(Artist).filter(Artist.id == artist_id).first()
            if not db_artist:
                raise HTTPException(status_code=400, detail=f"Artist with id {artist_id} not found")

        # Update the related entities with the new foreign key
        database.query(Artist).filter(Artist.id.in_(album_data.createdBy)).update(
            {Artist.album_id: db_album.id}, synchronize_session=False
        )
        database.commit()
    if album_data.contains:
        # Validate that all Track IDs exist
        for track_id in album_data.contains:
            db_track = database.query(Track).filter(Track.id == track_id).first()
            if not db_track:
                raise HTTPException(status_code=400, detail=f"Track with id {track_id} not found")

        # Update the related entities with the new foreign key
        database.query(Track).filter(Track.id.in_(album_data.contains)).update(
            {Track.album_1_id: db_album.id}, synchronize_session=False
        )
        database.commit()



    createdBy_ids = database.query(Artist.id).filter(Artist.album_id == db_album.id).all()
    contains_ids = database.query(Track.id).filter(Track.album_1_id == db_album.id).all()
    response_data = {
        "album": db_album,
        "createdBy_ids": [x[0] for x in createdBy_ids],        "contains_ids": [x[0] for x in contains_ids]    }
    return response_data


@app.post("/album/bulk/", response_model=None, tags=["Album"])
async def bulk_create_album(items: list[AlbumCreate], database: Session = Depends(get_db)) -> dict:
    """Create multiple Album entities at once"""
    created_items = []
    errors = []

    for idx, item_data in enumerate(items):
        try:
            # Basic validation for each item
            if not item_data.orderitem:
                raise ValueError("OrderItem ID is required")

            db_album = Album(
                format=item_data.format,                stockQuantity=item_data.stockQuantity,                price=item_data.price,                artist=item_data.artist,                releaseYear=item_data.releaseYear,                Id=item_data.Id,                title=item_data.title,                orderitem_id=item_data.orderitem            )
            database.add(db_album)
            database.flush()  # Get ID without committing
            created_items.append(db_album.id)
        except Exception as e:
            errors.append({"index": idx, "error": str(e)})

    if errors:
        database.rollback()
        raise HTTPException(status_code=400, detail={"message": "Bulk creation failed", "errors": errors})

    database.commit()
    return {
        "created_count": len(created_items),
        "created_ids": created_items,
        "message": f"Successfully created {len(created_items)} Album entities"
    }


@app.delete("/album/bulk/", response_model=None, tags=["Album"])
async def bulk_delete_album(ids: list[int], database: Session = Depends(get_db)) -> dict:
    """Delete multiple Album entities at once"""
    deleted_count = 0
    not_found = []

    for item_id in ids:
        db_album = database.query(Album).filter(Album.id == item_id).first()
        if db_album:
            database.delete(db_album)
            deleted_count += 1
        else:
            not_found.append(item_id)

    database.commit()

    return {
        "deleted_count": deleted_count,
        "not_found": not_found,
        "message": f"Successfully deleted {deleted_count} Album entities"
    }

@app.put("/album/{album_id}/", response_model=None, tags=["Album"])
async def update_album(album_id: int, album_data: AlbumCreate, database: Session = Depends(get_db)) -> Album:
    db_album = database.query(Album).filter(Album.id == album_id).first()
    if db_album is None:
        raise HTTPException(status_code=404, detail="Album not found")

    setattr(db_album, 'format', album_data.format)
    setattr(db_album, 'stockQuantity', album_data.stockQuantity)
    setattr(db_album, 'price', album_data.price)
    setattr(db_album, 'artist', album_data.artist)
    setattr(db_album, 'releaseYear', album_data.releaseYear)
    setattr(db_album, 'Id', album_data.Id)
    setattr(db_album, 'title', album_data.title)
    if album_data.orderitem is not None:
        db_orderitem = database.query(OrderItem).filter(OrderItem.id == album_data.orderitem).first()
        if not db_orderitem:
            raise HTTPException(status_code=400, detail="OrderItem not found")
        setattr(db_album, 'orderitem_id', album_data.orderitem)
    if album_data.createdBy is not None:
        # Clear all existing relationships (set foreign key to NULL)
        database.query(Artist).filter(Artist.album_id == db_album.id).update(
            {Artist.album_id: None}, synchronize_session=False
        )

        # Set new relationships if list is not empty
        if album_data.createdBy:
            # Validate that all IDs exist
            for artist_id in album_data.createdBy:
                db_artist = database.query(Artist).filter(Artist.id == artist_id).first()
                if not db_artist:
                    raise HTTPException(status_code=400, detail=f"Artist with id {artist_id} not found")

            # Update the related entities with the new foreign key
            database.query(Artist).filter(Artist.id.in_(album_data.createdBy)).update(
                {Artist.album_id: db_album.id}, synchronize_session=False
            )
    if album_data.contains is not None:
        # Clear all existing relationships (set foreign key to NULL)
        database.query(Track).filter(Track.album_1_id == db_album.id).update(
            {Track.album_1_id: None}, synchronize_session=False
        )

        # Set new relationships if list is not empty
        if album_data.contains:
            # Validate that all IDs exist
            for track_id in album_data.contains:
                db_track = database.query(Track).filter(Track.id == track_id).first()
                if not db_track:
                    raise HTTPException(status_code=400, detail=f"Track with id {track_id} not found")

            # Update the related entities with the new foreign key
            database.query(Track).filter(Track.id.in_(album_data.contains)).update(
                {Track.album_1_id: db_album.id}, synchronize_session=False
            )
    database.commit()
    database.refresh(db_album)

    createdBy_ids = database.query(Artist.id).filter(Artist.album_id == db_album.id).all()
    contains_ids = database.query(Track.id).filter(Track.album_1_id == db_album.id).all()
    response_data = {
        "album": db_album,
        "createdBy_ids": [x[0] for x in createdBy_ids],        "contains_ids": [x[0] for x in contains_ids]    }
    return response_data


@app.delete("/album/{album_id}/", response_model=None, tags=["Album"])
async def delete_album(album_id: int, database: Session = Depends(get_db)):
    db_album = database.query(Album).filter(Album.id == album_id).first()
    if db_album is None:
        raise HTTPException(status_code=404, detail="Album not found")
    database.delete(db_album)
    database.commit()
    return db_album


@app.get("/album/{album_id}/createdBy/", response_model=None, tags=["Album Relationships"])
async def get_createdBy_of_album(album_id: int, database: Session = Depends(get_db)):
    """Get all Artist entities related to this Album through createdBy"""
    db_album = database.query(Album).filter(Album.id == album_id).first()
    if db_album is None:
        raise HTTPException(status_code=404, detail="Album not found")

    createdBy_list = database.query(Artist).filter(Artist.album_id == album_id).all()

    return {
        "album_id": album_id,
        "createdBy_count": len(createdBy_list),
        "createdBy": createdBy_list
    }

@app.get("/album/{album_id}/contains/", response_model=None, tags=["Album Relationships"])
async def get_contains_of_album(album_id: int, database: Session = Depends(get_db)):
    """Get all Track entities related to this Album through contains"""
    db_album = database.query(Album).filter(Album.id == album_id).first()
    if db_album is None:
        raise HTTPException(status_code=404, detail="Album not found")

    contains_list = database.query(Track).filter(Track.album_1_id == album_id).all()

    return {
        "album_id": album_id,
        "contains_count": len(contains_list),
        "contains": contains_list
    }



############################################
#   Album Method Endpoints
############################################




@app.post("/album/methods/isAvailable/", response_model=None, tags=["Album Methods"])
async def album_isAvailable(
    database: Session = Depends(get_db)
):
    """
    Execute the isAvailable class method on Album.
    This method operates on all Album entities or performs class-level operations.
    """
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output


        # Method body not defined
        result = None

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Handle result serialization
        if hasattr(result, '__iter__') and not isinstance(result, (str, dict)):
            # It's a list of entities
            result_data = []
            for item in result:
                if hasattr(item, '__dict__'):
                    item_dict = {k: v for k, v in item.__dict__.items() if not k.startswith('_')}
                    result_data.append(item_dict)
                else:
                    result_data.append(str(item))
            result = result_data
        elif hasattr(result, '__dict__'):
            result = {k: v for k, v in result.__dict__.items() if not k.startswith('_')}

        return {
            "class": "Album",
            "method": "isAvailable",
            "status": "executed",
            "result": result,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")






@app.post("/album/methods/updateStock/", response_model=None, tags=["Album Methods"])
async def album_updateStock(
    database: Session = Depends(get_db)
):
    """
    Execute the updateStock class method on Album.
    This method operates on all Album entities or performs class-level operations.
    """
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output


        # Method body not defined
        result = None

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Handle result serialization
        if hasattr(result, '__iter__') and not isinstance(result, (str, dict)):
            # It's a list of entities
            result_data = []
            for item in result:
                if hasattr(item, '__dict__'):
                    item_dict = {k: v for k, v in item.__dict__.items() if not k.startswith('_')}
                    result_data.append(item_dict)
                else:
                    result_data.append(str(item))
            result = result_data
        elif hasattr(result, '__dict__'):
            result = {k: v for k, v in result.__dict__.items() if not k.startswith('_')}

        return {
            "class": "Album",
            "method": "updateStock",
            "status": "executed",
            "result": result,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")




############################################
#
#   CartItem functions
#
############################################

@app.get("/cartitem/", response_model=None, tags=["CartItem"])
def get_all_cartitem(detailed: bool = False, database: Session = Depends(get_db)) -> list:
    from sqlalchemy.orm import joinedload

    # Use detailed=true to get entities with eagerly loaded relationships (for tables with lookup columns)
    if detailed:
        # Eagerly load all relationships to avoid N+1 queries
        query = database.query(CartItem)
        query = query.options(joinedload(CartItem.cart))
        cartitem_list = query.all()

        # Serialize with relationships included
        result = []
        for cartitem_item in cartitem_list:
            item_dict = cartitem_item.__dict__.copy()
            item_dict.pop('_sa_instance_state', None)

            # Add many-to-one relationships (foreign keys for lookup columns)
            if cartitem_item.cart:
                related_obj = cartitem_item.cart
                related_dict = related_obj.__dict__.copy()
                related_dict.pop('_sa_instance_state', None)
                item_dict['cart'] = related_dict
            else:
                item_dict['cart'] = None


            result.append(item_dict)
        return result
    else:
        # Default: return flat entities (faster for charts/widgets without lookup columns)
        return database.query(CartItem).all()


@app.get("/cartitem/count/", response_model=None, tags=["CartItem"])
def get_count_cartitem(database: Session = Depends(get_db)) -> dict:
    """Get the total count of CartItem entities"""
    count = database.query(CartItem).count()
    return {"count": count}


@app.get("/cartitem/paginated/", response_model=None, tags=["CartItem"])
def get_paginated_cartitem(skip: int = 0, limit: int = 100, detailed: bool = False, database: Session = Depends(get_db)) -> dict:
    """Get paginated list of CartItem entities"""
    total = database.query(CartItem).count()
    cartitem_list = database.query(CartItem).offset(skip).limit(limit).all()
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": cartitem_list
    }


@app.get("/cartitem/search/", response_model=None, tags=["CartItem"])
def search_cartitem(
    database: Session = Depends(get_db)
) -> list:
    """Search CartItem entities by attributes"""
    query = database.query(CartItem)


    results = query.all()
    return results


@app.get("/cartitem/{cartitem_id}/", response_model=None, tags=["CartItem"])
async def get_cartitem(cartitem_id: int, database: Session = Depends(get_db)) -> CartItem:
    db_cartitem = database.query(CartItem).filter(CartItem.id == cartitem_id).first()
    if db_cartitem is None:
        raise HTTPException(status_code=404, detail="CartItem not found")

    response_data = {
        "cartitem": db_cartitem,
}
    return response_data



@app.post("/cartitem/", response_model=None, tags=["CartItem"])
async def create_cartitem(cartitem_data: CartItemCreate, database: Session = Depends(get_db)) -> CartItem:

    if cartitem_data.cart is not None:
        db_cart = database.query(Cart).filter(Cart.id == cartitem_data.cart).first()
        if not db_cart:
            raise HTTPException(status_code=400, detail="Cart not found")
    else:
        raise HTTPException(status_code=400, detail="Cart ID is required")

    db_cartitem = CartItem(
        unintPrice=cartitem_data.unintPrice,        quantity=cartitem_data.quantity,        cart_id=cartitem_data.cart        )

    database.add(db_cartitem)
    database.commit()
    database.refresh(db_cartitem)




    return db_cartitem


@app.post("/cartitem/bulk/", response_model=None, tags=["CartItem"])
async def bulk_create_cartitem(items: list[CartItemCreate], database: Session = Depends(get_db)) -> dict:
    """Create multiple CartItem entities at once"""
    created_items = []
    errors = []

    for idx, item_data in enumerate(items):
        try:
            # Basic validation for each item
            if not item_data.cart:
                raise ValueError("Cart ID is required")

            db_cartitem = CartItem(
                unintPrice=item_data.unintPrice,                quantity=item_data.quantity,                cart_id=item_data.cart            )
            database.add(db_cartitem)
            database.flush()  # Get ID without committing
            created_items.append(db_cartitem.id)
        except Exception as e:
            errors.append({"index": idx, "error": str(e)})

    if errors:
        database.rollback()
        raise HTTPException(status_code=400, detail={"message": "Bulk creation failed", "errors": errors})

    database.commit()
    return {
        "created_count": len(created_items),
        "created_ids": created_items,
        "message": f"Successfully created {len(created_items)} CartItem entities"
    }


@app.delete("/cartitem/bulk/", response_model=None, tags=["CartItem"])
async def bulk_delete_cartitem(ids: list[int], database: Session = Depends(get_db)) -> dict:
    """Delete multiple CartItem entities at once"""
    deleted_count = 0
    not_found = []

    for item_id in ids:
        db_cartitem = database.query(CartItem).filter(CartItem.id == item_id).first()
        if db_cartitem:
            database.delete(db_cartitem)
            deleted_count += 1
        else:
            not_found.append(item_id)

    database.commit()

    return {
        "deleted_count": deleted_count,
        "not_found": not_found,
        "message": f"Successfully deleted {deleted_count} CartItem entities"
    }

@app.put("/cartitem/{cartitem_id}/", response_model=None, tags=["CartItem"])
async def update_cartitem(cartitem_id: int, cartitem_data: CartItemCreate, database: Session = Depends(get_db)) -> CartItem:
    db_cartitem = database.query(CartItem).filter(CartItem.id == cartitem_id).first()
    if db_cartitem is None:
        raise HTTPException(status_code=404, detail="CartItem not found")

    setattr(db_cartitem, 'unintPrice', cartitem_data.unintPrice)
    setattr(db_cartitem, 'quantity', cartitem_data.quantity)
    if cartitem_data.cart is not None:
        db_cart = database.query(Cart).filter(Cart.id == cartitem_data.cart).first()
        if not db_cart:
            raise HTTPException(status_code=400, detail="Cart not found")
        setattr(db_cartitem, 'cart_id', cartitem_data.cart)
    database.commit()
    database.refresh(db_cartitem)

    return db_cartitem


@app.delete("/cartitem/{cartitem_id}/", response_model=None, tags=["CartItem"])
async def delete_cartitem(cartitem_id: int, database: Session = Depends(get_db)):
    db_cartitem = database.query(CartItem).filter(CartItem.id == cartitem_id).first()
    if db_cartitem is None:
        raise HTTPException(status_code=404, detail="CartItem not found")
    database.delete(db_cartitem)
    database.commit()
    return db_cartitem




############################################
#   CartItem Method Endpoints
############################################




@app.post("/cartitem/methods/getSubtotal/", response_model=None, tags=["CartItem Methods"])
async def cartitem_getSubtotal(
    database: Session = Depends(get_db)
):
    """
    Execute the getSubtotal class method on CartItem.
    This method operates on all CartItem entities or performs class-level operations.
    """
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output


        # Method body not defined
        result = None

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Handle result serialization
        if hasattr(result, '__iter__') and not isinstance(result, (str, dict)):
            # It's a list of entities
            result_data = []
            for item in result:
                if hasattr(item, '__dict__'):
                    item_dict = {k: v for k, v in item.__dict__.items() if not k.startswith('_')}
                    result_data.append(item_dict)
                else:
                    result_data.append(str(item))
            result = result_data
        elif hasattr(result, '__dict__'):
            result = {k: v for k, v in result.__dict__.items() if not k.startswith('_')}

        return {
            "class": "CartItem",
            "method": "getSubtotal",
            "status": "executed",
            "result": result,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")




############################################
#
#   Payment functions
#
############################################

@app.get("/payment/", response_model=None, tags=["Payment"])
def get_all_payment(detailed: bool = False, database: Session = Depends(get_db)) -> list:
    from sqlalchemy.orm import joinedload

    # Use detailed=true to get entities with eagerly loaded relationships (for tables with lookup columns)
    if detailed:
        # Eagerly load all relationships to avoid N+1 queries
        query = database.query(Payment)
        query = query.options(joinedload(Payment.order_1))
        payment_list = query.all()

        # Serialize with relationships included
        result = []
        for payment_item in payment_list:
            item_dict = payment_item.__dict__.copy()
            item_dict.pop('_sa_instance_state', None)

            # Add many-to-one relationships (foreign keys for lookup columns)
            if payment_item.order_1:
                related_obj = payment_item.order_1
                related_dict = related_obj.__dict__.copy()
                related_dict.pop('_sa_instance_state', None)
                item_dict['order_1'] = related_dict
            else:
                item_dict['order_1'] = None


            result.append(item_dict)
        return result
    else:
        # Default: return flat entities (faster for charts/widgets without lookup columns)
        return database.query(Payment).all()


@app.get("/payment/count/", response_model=None, tags=["Payment"])
def get_count_payment(database: Session = Depends(get_db)) -> dict:
    """Get the total count of Payment entities"""
    count = database.query(Payment).count()
    return {"count": count}


@app.get("/payment/paginated/", response_model=None, tags=["Payment"])
def get_paginated_payment(skip: int = 0, limit: int = 100, detailed: bool = False, database: Session = Depends(get_db)) -> dict:
    """Get paginated list of Payment entities"""
    total = database.query(Payment).count()
    payment_list = database.query(Payment).offset(skip).limit(limit).all()
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": payment_list
    }


@app.get("/payment/search/", response_model=None, tags=["Payment"])
def search_payment(
    database: Session = Depends(get_db)
) -> list:
    """Search Payment entities by attributes"""
    query = database.query(Payment)


    results = query.all()
    return results


@app.get("/payment/{payment_id}/", response_model=None, tags=["Payment"])
async def get_payment(payment_id: int, database: Session = Depends(get_db)) -> Payment:
    db_payment = database.query(Payment).filter(Payment.id == payment_id).first()
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")

    response_data = {
        "payment": db_payment,
}
    return response_data



@app.post("/payment/", response_model=None, tags=["Payment"])
async def create_payment(payment_data: PaymentCreate, database: Session = Depends(get_db)) -> Payment:


    db_payment = Payment(
        Id=payment_data.Id,        method=payment_data.method,        amount=payment_data.amount        )

    database.add(db_payment)
    database.commit()
    database.refresh(db_payment)




    return db_payment


@app.post("/payment/bulk/", response_model=None, tags=["Payment"])
async def bulk_create_payment(items: list[PaymentCreate], database: Session = Depends(get_db)) -> dict:
    """Create multiple Payment entities at once"""
    created_items = []
    errors = []

    for idx, item_data in enumerate(items):
        try:
            # Basic validation for each item

            db_payment = Payment(
                Id=item_data.Id,                method=item_data.method,                amount=item_data.amount            )
            database.add(db_payment)
            database.flush()  # Get ID without committing
            created_items.append(db_payment.id)
        except Exception as e:
            errors.append({"index": idx, "error": str(e)})

    if errors:
        database.rollback()
        raise HTTPException(status_code=400, detail={"message": "Bulk creation failed", "errors": errors})

    database.commit()
    return {
        "created_count": len(created_items),
        "created_ids": created_items,
        "message": f"Successfully created {len(created_items)} Payment entities"
    }


@app.delete("/payment/bulk/", response_model=None, tags=["Payment"])
async def bulk_delete_payment(ids: list[int], database: Session = Depends(get_db)) -> dict:
    """Delete multiple Payment entities at once"""
    deleted_count = 0
    not_found = []

    for item_id in ids:
        db_payment = database.query(Payment).filter(Payment.id == item_id).first()
        if db_payment:
            database.delete(db_payment)
            deleted_count += 1
        else:
            not_found.append(item_id)

    database.commit()

    return {
        "deleted_count": deleted_count,
        "not_found": not_found,
        "message": f"Successfully deleted {deleted_count} Payment entities"
    }

@app.put("/payment/{payment_id}/", response_model=None, tags=["Payment"])
async def update_payment(payment_id: int, payment_data: PaymentCreate, database: Session = Depends(get_db)) -> Payment:
    db_payment = database.query(Payment).filter(Payment.id == payment_id).first()
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")

    setattr(db_payment, 'Id', payment_data.Id)
    setattr(db_payment, 'method', payment_data.method)
    setattr(db_payment, 'amount', payment_data.amount)
    database.commit()
    database.refresh(db_payment)

    return db_payment


@app.delete("/payment/{payment_id}/", response_model=None, tags=["Payment"])
async def delete_payment(payment_id: int, database: Session = Depends(get_db)):
    db_payment = database.query(Payment).filter(Payment.id == payment_id).first()
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    database.delete(db_payment)
    database.commit()
    return db_payment




############################################
#   Payment Method Endpoints
############################################




@app.post("/payment/methods/validate/", response_model=None, tags=["Payment Methods"])
async def payment_validate(
    database: Session = Depends(get_db)
):
    """
    Execute the validate class method on Payment.
    This method operates on all Payment entities or performs class-level operations.
    """
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output


        # Method body not defined
        result = None

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Handle result serialization
        if hasattr(result, '__iter__') and not isinstance(result, (str, dict)):
            # It's a list of entities
            result_data = []
            for item in result:
                if hasattr(item, '__dict__'):
                    item_dict = {k: v for k, v in item.__dict__.items() if not k.startswith('_')}
                    result_data.append(item_dict)
                else:
                    result_data.append(str(item))
            result = result_data
        elif hasattr(result, '__dict__'):
            result = {k: v for k, v in result.__dict__.items() if not k.startswith('_')}

        return {
            "class": "Payment",
            "method": "validate",
            "status": "executed",
            "result": result,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")




############################################
#
#   OrderItem functions
#
############################################

@app.get("/orderitem/", response_model=None, tags=["OrderItem"])
def get_all_orderitem(detailed: bool = False, database: Session = Depends(get_db)) -> list:
    from sqlalchemy.orm import joinedload

    # Use detailed=true to get entities with eagerly loaded relationships (for tables with lookup columns)
    if detailed:
        # Eagerly load all relationships to avoid N+1 queries
        query = database.query(OrderItem)
        query = query.options(joinedload(OrderItem.refersTo))
        query = query.options(joinedload(OrderItem.order))
        orderitem_list = query.all()

        # Serialize with relationships included
        result = []
        for orderitem_item in orderitem_list:
            item_dict = orderitem_item.__dict__.copy()
            item_dict.pop('_sa_instance_state', None)

            # Add many-to-one relationships (foreign keys for lookup columns)
            if orderitem_item.refersTo:
                related_obj = orderitem_item.refersTo
                related_dict = related_obj.__dict__.copy()
                related_dict.pop('_sa_instance_state', None)
                item_dict['refersTo'] = related_dict
            else:
                item_dict['refersTo'] = None
            if orderitem_item.order:
                related_obj = orderitem_item.order
                related_dict = related_obj.__dict__.copy()
                related_dict.pop('_sa_instance_state', None)
                item_dict['order'] = related_dict
            else:
                item_dict['order'] = None


            result.append(item_dict)
        return result
    else:
        # Default: return flat entities (faster for charts/widgets without lookup columns)
        return database.query(OrderItem).all()


@app.get("/orderitem/count/", response_model=None, tags=["OrderItem"])
def get_count_orderitem(database: Session = Depends(get_db)) -> dict:
    """Get the total count of OrderItem entities"""
    count = database.query(OrderItem).count()
    return {"count": count}


@app.get("/orderitem/paginated/", response_model=None, tags=["OrderItem"])
def get_paginated_orderitem(skip: int = 0, limit: int = 100, detailed: bool = False, database: Session = Depends(get_db)) -> dict:
    """Get paginated list of OrderItem entities"""
    total = database.query(OrderItem).count()
    orderitem_list = database.query(OrderItem).offset(skip).limit(limit).all()
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": orderitem_list
    }


@app.get("/orderitem/search/", response_model=None, tags=["OrderItem"])
def search_orderitem(
    database: Session = Depends(get_db)
) -> list:
    """Search OrderItem entities by attributes"""
    query = database.query(OrderItem)


    results = query.all()
    return results


@app.get("/orderitem/{orderitem_id}/", response_model=None, tags=["OrderItem"])
async def get_orderitem(orderitem_id: int, database: Session = Depends(get_db)) -> OrderItem:
    db_orderitem = database.query(OrderItem).filter(OrderItem.id == orderitem_id).first()
    if db_orderitem is None:
        raise HTTPException(status_code=404, detail="OrderItem not found")

    response_data = {
        "orderitem": db_orderitem,
}
    return response_data



@app.post("/orderitem/", response_model=None, tags=["OrderItem"])
async def create_orderitem(orderitem_data: OrderItemCreate, database: Session = Depends(get_db)) -> OrderItem:

    if orderitem_data.order is not None:
        db_order = database.query(Order).filter(Order.id == orderitem_data.order).first()
        if not db_order:
            raise HTTPException(status_code=400, detail="Order not found")
    else:
        raise HTTPException(status_code=400, detail="Order ID is required")

    db_orderitem = OrderItem(
        quantity=orderitem_data.quantity,        unintPrice=orderitem_data.unintPrice,        order_id=orderitem_data.order        )

    database.add(db_orderitem)
    database.commit()
    database.refresh(db_orderitem)




    return db_orderitem


@app.post("/orderitem/bulk/", response_model=None, tags=["OrderItem"])
async def bulk_create_orderitem(items: list[OrderItemCreate], database: Session = Depends(get_db)) -> dict:
    """Create multiple OrderItem entities at once"""
    created_items = []
    errors = []

    for idx, item_data in enumerate(items):
        try:
            # Basic validation for each item
            if not item_data.order:
                raise ValueError("Order ID is required")

            db_orderitem = OrderItem(
                quantity=item_data.quantity,                unintPrice=item_data.unintPrice,                order_id=item_data.order            )
            database.add(db_orderitem)
            database.flush()  # Get ID without committing
            created_items.append(db_orderitem.id)
        except Exception as e:
            errors.append({"index": idx, "error": str(e)})

    if errors:
        database.rollback()
        raise HTTPException(status_code=400, detail={"message": "Bulk creation failed", "errors": errors})

    database.commit()
    return {
        "created_count": len(created_items),
        "created_ids": created_items,
        "message": f"Successfully created {len(created_items)} OrderItem entities"
    }


@app.delete("/orderitem/bulk/", response_model=None, tags=["OrderItem"])
async def bulk_delete_orderitem(ids: list[int], database: Session = Depends(get_db)) -> dict:
    """Delete multiple OrderItem entities at once"""
    deleted_count = 0
    not_found = []

    for item_id in ids:
        db_orderitem = database.query(OrderItem).filter(OrderItem.id == item_id).first()
        if db_orderitem:
            database.delete(db_orderitem)
            deleted_count += 1
        else:
            not_found.append(item_id)

    database.commit()

    return {
        "deleted_count": deleted_count,
        "not_found": not_found,
        "message": f"Successfully deleted {deleted_count} OrderItem entities"
    }

@app.put("/orderitem/{orderitem_id}/", response_model=None, tags=["OrderItem"])
async def update_orderitem(orderitem_id: int, orderitem_data: OrderItemCreate, database: Session = Depends(get_db)) -> OrderItem:
    db_orderitem = database.query(OrderItem).filter(OrderItem.id == orderitem_id).first()
    if db_orderitem is None:
        raise HTTPException(status_code=404, detail="OrderItem not found")

    setattr(db_orderitem, 'quantity', orderitem_data.quantity)
    setattr(db_orderitem, 'unintPrice', orderitem_data.unintPrice)
    if orderitem_data.order is not None:
        db_order = database.query(Order).filter(Order.id == orderitem_data.order).first()
        if not db_order:
            raise HTTPException(status_code=400, detail="Order not found")
        setattr(db_orderitem, 'order_id', orderitem_data.order)
    database.commit()
    database.refresh(db_orderitem)

    return db_orderitem


@app.delete("/orderitem/{orderitem_id}/", response_model=None, tags=["OrderItem"])
async def delete_orderitem(orderitem_id: int, database: Session = Depends(get_db)):
    db_orderitem = database.query(OrderItem).filter(OrderItem.id == orderitem_id).first()
    if db_orderitem is None:
        raise HTTPException(status_code=404, detail="OrderItem not found")
    database.delete(db_orderitem)
    database.commit()
    return db_orderitem




############################################
#   OrderItem Method Endpoints
############################################




@app.post("/orderitem/methods/getSubtotal/", response_model=None, tags=["OrderItem Methods"])
async def orderitem_getSubtotal(
    database: Session = Depends(get_db)
):
    """
    Execute the getSubtotal class method on OrderItem.
    This method operates on all OrderItem entities or performs class-level operations.
    """
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output


        # Method body not defined
        result = None

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Handle result serialization
        if hasattr(result, '__iter__') and not isinstance(result, (str, dict)):
            # It's a list of entities
            result_data = []
            for item in result:
                if hasattr(item, '__dict__'):
                    item_dict = {k: v for k, v in item.__dict__.items() if not k.startswith('_')}
                    result_data.append(item_dict)
                else:
                    result_data.append(str(item))
            result = result_data
        elif hasattr(result, '__dict__'):
            result = {k: v for k, v in result.__dict__.items() if not k.startswith('_')}

        return {
            "class": "OrderItem",
            "method": "getSubtotal",
            "status": "executed",
            "result": result,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")




############################################
#
#   Address functions
#
############################################

@app.get("/address/", response_model=None, tags=["Address"])
def get_all_address(detailed: bool = False, database: Session = Depends(get_db)) -> list:
    from sqlalchemy.orm import joinedload

    # Use detailed=true to get entities with eagerly loaded relationships (for tables with lookup columns)
    if detailed:
        # Eagerly load all relationships to avoid N+1 queries
        query = database.query(Address)
        query = query.options(joinedload(Address.customer_3))
        query = query.options(joinedload(Address.order_2))
        address_list = query.all()

        # Serialize with relationships included
        result = []
        for address_item in address_list:
            item_dict = address_item.__dict__.copy()
            item_dict.pop('_sa_instance_state', None)

            # Add many-to-one relationships (foreign keys for lookup columns)
            if address_item.customer_3:
                related_obj = address_item.customer_3
                related_dict = related_obj.__dict__.copy()
                related_dict.pop('_sa_instance_state', None)
                item_dict['customer_3'] = related_dict
            else:
                item_dict['customer_3'] = None
            if address_item.order_2:
                related_obj = address_item.order_2
                related_dict = related_obj.__dict__.copy()
                related_dict.pop('_sa_instance_state', None)
                item_dict['order_2'] = related_dict
            else:
                item_dict['order_2'] = None


            result.append(item_dict)
        return result
    else:
        # Default: return flat entities (faster for charts/widgets without lookup columns)
        return database.query(Address).all()


@app.get("/address/count/", response_model=None, tags=["Address"])
def get_count_address(database: Session = Depends(get_db)) -> dict:
    """Get the total count of Address entities"""
    count = database.query(Address).count()
    return {"count": count}


@app.get("/address/paginated/", response_model=None, tags=["Address"])
def get_paginated_address(skip: int = 0, limit: int = 100, detailed: bool = False, database: Session = Depends(get_db)) -> dict:
    """Get paginated list of Address entities"""
    total = database.query(Address).count()
    address_list = database.query(Address).offset(skip).limit(limit).all()
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": address_list
    }


@app.get("/address/search/", response_model=None, tags=["Address"])
def search_address(
    database: Session = Depends(get_db)
) -> list:
    """Search Address entities by attributes"""
    query = database.query(Address)


    results = query.all()
    return results


@app.get("/address/{address_id}/", response_model=None, tags=["Address"])
async def get_address(address_id: int, database: Session = Depends(get_db)) -> Address:
    db_address = database.query(Address).filter(Address.id == address_id).first()
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")

    response_data = {
        "address": db_address,
}
    return response_data



@app.post("/address/", response_model=None, tags=["Address"])
async def create_address(address_data: AddressCreate, database: Session = Depends(get_db)) -> Address:

    if address_data.customer_3 is not None:
        db_customer_3 = database.query(Customer).filter(Customer.id == address_data.customer_3).first()
        if not db_customer_3:
            raise HTTPException(status_code=400, detail="Customer not found")
    else:
        raise HTTPException(status_code=400, detail="Customer ID is required")
    if address_data.order_2 is not None:
        db_order_2 = database.query(Order).filter(Order.id == address_data.order_2).first()
        if not db_order_2:
            raise HTTPException(status_code=400, detail="Order not found")
    else:
        raise HTTPException(status_code=400, detail="Order ID is required")

    db_address = Address(
        street=address_data.street,        city=address_data.city,        zip_code=address_data.zip_code,        Id=address_data.Id,        customer_3_id=address_data.customer_3,        order_2_id=address_data.order_2        )

    database.add(db_address)
    database.commit()
    database.refresh(db_address)




    return db_address


@app.post("/address/bulk/", response_model=None, tags=["Address"])
async def bulk_create_address(items: list[AddressCreate], database: Session = Depends(get_db)) -> dict:
    """Create multiple Address entities at once"""
    created_items = []
    errors = []

    for idx, item_data in enumerate(items):
        try:
            # Basic validation for each item
            if not item_data.customer_3:
                raise ValueError("Customer ID is required")
            if not item_data.order_2:
                raise ValueError("Order ID is required")

            db_address = Address(
                street=item_data.street,                city=item_data.city,                zip_code=item_data.zip_code,                Id=item_data.Id,                customer_3_id=item_data.customer_3,                order_2_id=item_data.order_2            )
            database.add(db_address)
            database.flush()  # Get ID without committing
            created_items.append(db_address.id)
        except Exception as e:
            errors.append({"index": idx, "error": str(e)})

    if errors:
        database.rollback()
        raise HTTPException(status_code=400, detail={"message": "Bulk creation failed", "errors": errors})

    database.commit()
    return {
        "created_count": len(created_items),
        "created_ids": created_items,
        "message": f"Successfully created {len(created_items)} Address entities"
    }


@app.delete("/address/bulk/", response_model=None, tags=["Address"])
async def bulk_delete_address(ids: list[int], database: Session = Depends(get_db)) -> dict:
    """Delete multiple Address entities at once"""
    deleted_count = 0
    not_found = []

    for item_id in ids:
        db_address = database.query(Address).filter(Address.id == item_id).first()
        if db_address:
            database.delete(db_address)
            deleted_count += 1
        else:
            not_found.append(item_id)

    database.commit()

    return {
        "deleted_count": deleted_count,
        "not_found": not_found,
        "message": f"Successfully deleted {deleted_count} Address entities"
    }

@app.put("/address/{address_id}/", response_model=None, tags=["Address"])
async def update_address(address_id: int, address_data: AddressCreate, database: Session = Depends(get_db)) -> Address:
    db_address = database.query(Address).filter(Address.id == address_id).first()
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")

    setattr(db_address, 'street', address_data.street)
    setattr(db_address, 'city', address_data.city)
    setattr(db_address, 'zip_code', address_data.zip_code)
    setattr(db_address, 'Id', address_data.Id)
    if address_data.customer_3 is not None:
        db_customer_3 = database.query(Customer).filter(Customer.id == address_data.customer_3).first()
        if not db_customer_3:
            raise HTTPException(status_code=400, detail="Customer not found")
        setattr(db_address, 'customer_3_id', address_data.customer_3)
    if address_data.order_2 is not None:
        db_order_2 = database.query(Order).filter(Order.id == address_data.order_2).first()
        if not db_order_2:
            raise HTTPException(status_code=400, detail="Order not found")
        setattr(db_address, 'order_2_id', address_data.order_2)
    database.commit()
    database.refresh(db_address)

    return db_address


@app.delete("/address/{address_id}/", response_model=None, tags=["Address"])
async def delete_address(address_id: int, database: Session = Depends(get_db)):
    db_address = database.query(Address).filter(Address.id == address_id).first()
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    database.delete(db_address)
    database.commit()
    return db_address




############################################
#   Address Method Endpoints
############################################




@app.post("/address/methods/validate/", response_model=None, tags=["Address Methods"])
async def address_validate(
    database: Session = Depends(get_db)
):
    """
    Execute the validate class method on Address.
    This method operates on all Address entities or performs class-level operations.
    """
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output


        # Method body not defined
        result = None

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Handle result serialization
        if hasattr(result, '__iter__') and not isinstance(result, (str, dict)):
            # It's a list of entities
            result_data = []
            for item in result:
                if hasattr(item, '__dict__'):
                    item_dict = {k: v for k, v in item.__dict__.items() if not k.startswith('_')}
                    result_data.append(item_dict)
                else:
                    result_data.append(str(item))
            result = result_data
        elif hasattr(result, '__dict__'):
            result = {k: v for k, v in result.__dict__.items() if not k.startswith('_')}

        return {
            "class": "Address",
            "method": "validate",
            "status": "executed",
            "result": result,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")




############################################
#
#   Review functions
#
############################################

@app.get("/review/", response_model=None, tags=["Review"])
def get_all_review(detailed: bool = False, database: Session = Depends(get_db)) -> list:
    from sqlalchemy.orm import joinedload

    # Use detailed=true to get entities with eagerly loaded relationships (for tables with lookup columns)
    if detailed:
        # Eagerly load all relationships to avoid N+1 queries
        query = database.query(Review)
        query = query.options(joinedload(Review.customer_2))
        review_list = query.all()

        # Serialize with relationships included
        result = []
        for review_item in review_list:
            item_dict = review_item.__dict__.copy()
            item_dict.pop('_sa_instance_state', None)

            # Add many-to-one relationships (foreign keys for lookup columns)
            if review_item.customer_2:
                related_obj = review_item.customer_2
                related_dict = related_obj.__dict__.copy()
                related_dict.pop('_sa_instance_state', None)
                item_dict['customer_2'] = related_dict
            else:
                item_dict['customer_2'] = None


            result.append(item_dict)
        return result
    else:
        # Default: return flat entities (faster for charts/widgets without lookup columns)
        return database.query(Review).all()


@app.get("/review/count/", response_model=None, tags=["Review"])
def get_count_review(database: Session = Depends(get_db)) -> dict:
    """Get the total count of Review entities"""
    count = database.query(Review).count()
    return {"count": count}


@app.get("/review/paginated/", response_model=None, tags=["Review"])
def get_paginated_review(skip: int = 0, limit: int = 100, detailed: bool = False, database: Session = Depends(get_db)) -> dict:
    """Get paginated list of Review entities"""
    total = database.query(Review).count()
    review_list = database.query(Review).offset(skip).limit(limit).all()
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": review_list
    }


@app.get("/review/search/", response_model=None, tags=["Review"])
def search_review(
    database: Session = Depends(get_db)
) -> list:
    """Search Review entities by attributes"""
    query = database.query(Review)


    results = query.all()
    return results


@app.get("/review/{review_id}/", response_model=None, tags=["Review"])
async def get_review(review_id: int, database: Session = Depends(get_db)) -> Review:
    db_review = database.query(Review).filter(Review.id == review_id).first()
    if db_review is None:
        raise HTTPException(status_code=404, detail="Review not found")

    response_data = {
        "review": db_review,
}
    return response_data



@app.post("/review/", response_model=None, tags=["Review"])
async def create_review(review_data: ReviewCreate, database: Session = Depends(get_db)) -> Review:

    if review_data.customer_2 is not None:
        db_customer_2 = database.query(Customer).filter(Customer.id == review_data.customer_2).first()
        if not db_customer_2:
            raise HTTPException(status_code=400, detail="Customer not found")
    else:
        raise HTTPException(status_code=400, detail="Customer ID is required")

    db_review = Review(
        rating=review_data.rating,        Id=review_data.Id,        comment=review_data.comment,        customer_2_id=review_data.customer_2        )

    database.add(db_review)
    database.commit()
    database.refresh(db_review)




    return db_review


@app.post("/review/bulk/", response_model=None, tags=["Review"])
async def bulk_create_review(items: list[ReviewCreate], database: Session = Depends(get_db)) -> dict:
    """Create multiple Review entities at once"""
    created_items = []
    errors = []

    for idx, item_data in enumerate(items):
        try:
            # Basic validation for each item
            if not item_data.customer_2:
                raise ValueError("Customer ID is required")

            db_review = Review(
                rating=item_data.rating,                Id=item_data.Id,                comment=item_data.comment,                customer_2_id=item_data.customer_2            )
            database.add(db_review)
            database.flush()  # Get ID without committing
            created_items.append(db_review.id)
        except Exception as e:
            errors.append({"index": idx, "error": str(e)})

    if errors:
        database.rollback()
        raise HTTPException(status_code=400, detail={"message": "Bulk creation failed", "errors": errors})

    database.commit()
    return {
        "created_count": len(created_items),
        "created_ids": created_items,
        "message": f"Successfully created {len(created_items)} Review entities"
    }


@app.delete("/review/bulk/", response_model=None, tags=["Review"])
async def bulk_delete_review(ids: list[int], database: Session = Depends(get_db)) -> dict:
    """Delete multiple Review entities at once"""
    deleted_count = 0
    not_found = []

    for item_id in ids:
        db_review = database.query(Review).filter(Review.id == item_id).first()
        if db_review:
            database.delete(db_review)
            deleted_count += 1
        else:
            not_found.append(item_id)

    database.commit()

    return {
        "deleted_count": deleted_count,
        "not_found": not_found,
        "message": f"Successfully deleted {deleted_count} Review entities"
    }

@app.put("/review/{review_id}/", response_model=None, tags=["Review"])
async def update_review(review_id: int, review_data: ReviewCreate, database: Session = Depends(get_db)) -> Review:
    db_review = database.query(Review).filter(Review.id == review_id).first()
    if db_review is None:
        raise HTTPException(status_code=404, detail="Review not found")

    setattr(db_review, 'rating', review_data.rating)
    setattr(db_review, 'Id', review_data.Id)
    setattr(db_review, 'comment', review_data.comment)
    if review_data.customer_2 is not None:
        db_customer_2 = database.query(Customer).filter(Customer.id == review_data.customer_2).first()
        if not db_customer_2:
            raise HTTPException(status_code=400, detail="Customer not found")
        setattr(db_review, 'customer_2_id', review_data.customer_2)
    database.commit()
    database.refresh(db_review)

    return db_review


@app.delete("/review/{review_id}/", response_model=None, tags=["Review"])
async def delete_review(review_id: int, database: Session = Depends(get_db)):
    db_review = database.query(Review).filter(Review.id == review_id).first()
    if db_review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    database.delete(db_review)
    database.commit()
    return db_review




############################################
#   Review Method Endpoints
############################################




@app.post("/review/methods/isVerified/", response_model=None, tags=["Review Methods"])
async def review_isVerified(
    database: Session = Depends(get_db)
):
    """
    Execute the isVerified class method on Review.
    This method operates on all Review entities or performs class-level operations.
    """
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output


        # Method body not defined
        result = None

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Handle result serialization
        if hasattr(result, '__iter__') and not isinstance(result, (str, dict)):
            # It's a list of entities
            result_data = []
            for item in result:
                if hasattr(item, '__dict__'):
                    item_dict = {k: v for k, v in item.__dict__.items() if not k.startswith('_')}
                    result_data.append(item_dict)
                else:
                    result_data.append(str(item))
            result = result_data
        elif hasattr(result, '__dict__'):
            result = {k: v for k, v in result.__dict__.items() if not k.startswith('_')}

        return {
            "class": "Review",
            "method": "isVerified",
            "status": "executed",
            "result": result,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")




############################################
#
#   Cart functions
#
############################################

@app.get("/cart/", response_model=None, tags=["Cart"])
def get_all_cart(detailed: bool = False, database: Session = Depends(get_db)) -> list:
    from sqlalchemy.orm import joinedload

    # Use detailed=true to get entities with eagerly loaded relationships (for tables with lookup columns)
    if detailed:
        # Eagerly load all relationships to avoid N+1 queries
        query = database.query(Cart)
        cart_list = query.all()

        # Serialize with relationships included
        result = []
        for cart_item in cart_list:
            item_dict = cart_item.__dict__.copy()
            item_dict.pop('_sa_instance_state', None)

            # Add many-to-one relationships (foreign keys for lookup columns)

            # Add many-to-many and one-to-many relationship objects (full details)
            cartitem_list = database.query(CartItem).filter(CartItem.cart_id == cart_item.id).all()
            item_dict['cartitem'] = []
            for cartitem_obj in cartitem_list:
                cartitem_dict = cartitem_obj.__dict__.copy()
                cartitem_dict.pop('_sa_instance_state', None)
                item_dict['cartitem'].append(cartitem_dict)

            result.append(item_dict)
        return result
    else:
        # Default: return flat entities (faster for charts/widgets without lookup columns)
        return database.query(Cart).all()


@app.get("/cart/count/", response_model=None, tags=["Cart"])
def get_count_cart(database: Session = Depends(get_db)) -> dict:
    """Get the total count of Cart entities"""
    count = database.query(Cart).count()
    return {"count": count}


@app.get("/cart/paginated/", response_model=None, tags=["Cart"])
def get_paginated_cart(skip: int = 0, limit: int = 100, detailed: bool = False, database: Session = Depends(get_db)) -> dict:
    """Get paginated list of Cart entities"""
    total = database.query(Cart).count()
    cart_list = database.query(Cart).offset(skip).limit(limit).all()
    # By default, return flat entities (for charts/widgets)
    # Use detailed=true to get entities with relationships
    if not detailed:
        return {
            "total": total,
            "skip": skip,
            "limit": limit,
            "data": cart_list
        }

    result = []
    for cart_item in cart_list:
        cartitem_ids = database.query(CartItem.id).filter(CartItem.cart_id == cart_item.id).all()
        item_data = {
            "cart": cart_item,
            "cartitem_ids": [x[0] for x in cartitem_ids]        }
        result.append(item_data)
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": result
    }


@app.get("/cart/search/", response_model=None, tags=["Cart"])
def search_cart(
    database: Session = Depends(get_db)
) -> list:
    """Search Cart entities by attributes"""
    query = database.query(Cart)


    results = query.all()
    return results


@app.get("/cart/{cart_id}/", response_model=None, tags=["Cart"])
async def get_cart(cart_id: int, database: Session = Depends(get_db)) -> Cart:
    db_cart = database.query(Cart).filter(Cart.id == cart_id).first()
    if db_cart is None:
        raise HTTPException(status_code=404, detail="Cart not found")

    cartitem_ids = database.query(CartItem.id).filter(CartItem.cart_id == db_cart.id).all()
    response_data = {
        "cart": db_cart,
        "cartitem_ids": [x[0] for x in cartitem_ids]}
    return response_data



@app.post("/cart/", response_model=None, tags=["Cart"])
async def create_cart(cart_data: CartCreate, database: Session = Depends(get_db)) -> Cart:


    db_cart = Cart(
        Id=cart_data.Id        )

    database.add(db_cart)
    database.commit()
    database.refresh(db_cart)

    if cart_data.cartitem:
        # Validate that all CartItem IDs exist
        for cartitem_id in cart_data.cartitem:
            db_cartitem = database.query(CartItem).filter(CartItem.id == cartitem_id).first()
            if not db_cartitem:
                raise HTTPException(status_code=400, detail=f"CartItem with id {cartitem_id} not found")

        # Update the related entities with the new foreign key
        database.query(CartItem).filter(CartItem.id.in_(cart_data.cartitem)).update(
            {CartItem.cart_id: db_cart.id}, synchronize_session=False
        )
        database.commit()



    cartitem_ids = database.query(CartItem.id).filter(CartItem.cart_id == db_cart.id).all()
    response_data = {
        "cart": db_cart,
        "cartitem_ids": [x[0] for x in cartitem_ids]    }
    return response_data


@app.post("/cart/bulk/", response_model=None, tags=["Cart"])
async def bulk_create_cart(items: list[CartCreate], database: Session = Depends(get_db)) -> dict:
    """Create multiple Cart entities at once"""
    created_items = []
    errors = []

    for idx, item_data in enumerate(items):
        try:
            # Basic validation for each item

            db_cart = Cart(
                Id=item_data.Id            )
            database.add(db_cart)
            database.flush()  # Get ID without committing
            created_items.append(db_cart.id)
        except Exception as e:
            errors.append({"index": idx, "error": str(e)})

    if errors:
        database.rollback()
        raise HTTPException(status_code=400, detail={"message": "Bulk creation failed", "errors": errors})

    database.commit()
    return {
        "created_count": len(created_items),
        "created_ids": created_items,
        "message": f"Successfully created {len(created_items)} Cart entities"
    }


@app.delete("/cart/bulk/", response_model=None, tags=["Cart"])
async def bulk_delete_cart(ids: list[int], database: Session = Depends(get_db)) -> dict:
    """Delete multiple Cart entities at once"""
    deleted_count = 0
    not_found = []

    for item_id in ids:
        db_cart = database.query(Cart).filter(Cart.id == item_id).first()
        if db_cart:
            database.delete(db_cart)
            deleted_count += 1
        else:
            not_found.append(item_id)

    database.commit()

    return {
        "deleted_count": deleted_count,
        "not_found": not_found,
        "message": f"Successfully deleted {deleted_count} Cart entities"
    }

@app.put("/cart/{cart_id}/", response_model=None, tags=["Cart"])
async def update_cart(cart_id: int, cart_data: CartCreate, database: Session = Depends(get_db)) -> Cart:
    db_cart = database.query(Cart).filter(Cart.id == cart_id).first()
    if db_cart is None:
        raise HTTPException(status_code=404, detail="Cart not found")

    setattr(db_cart, 'Id', cart_data.Id)
    if cart_data.cartitem is not None:
        # Clear all existing relationships (set foreign key to NULL)
        database.query(CartItem).filter(CartItem.cart_id == db_cart.id).update(
            {CartItem.cart_id: None}, synchronize_session=False
        )

        # Set new relationships if list is not empty
        if cart_data.cartitem:
            # Validate that all IDs exist
            for cartitem_id in cart_data.cartitem:
                db_cartitem = database.query(CartItem).filter(CartItem.id == cartitem_id).first()
                if not db_cartitem:
                    raise HTTPException(status_code=400, detail=f"CartItem with id {cartitem_id} not found")

            # Update the related entities with the new foreign key
            database.query(CartItem).filter(CartItem.id.in_(cart_data.cartitem)).update(
                {CartItem.cart_id: db_cart.id}, synchronize_session=False
            )
    database.commit()
    database.refresh(db_cart)

    cartitem_ids = database.query(CartItem.id).filter(CartItem.cart_id == db_cart.id).all()
    response_data = {
        "cart": db_cart,
        "cartitem_ids": [x[0] for x in cartitem_ids]    }
    return response_data


@app.delete("/cart/{cart_id}/", response_model=None, tags=["Cart"])
async def delete_cart(cart_id: int, database: Session = Depends(get_db)):
    db_cart = database.query(Cart).filter(Cart.id == cart_id).first()
    if db_cart is None:
        raise HTTPException(status_code=404, detail="Cart not found")
    database.delete(db_cart)
    database.commit()
    return db_cart


@app.get("/cart/{cart_id}/cartitem/", response_model=None, tags=["Cart Relationships"])
async def get_cartitem_of_cart(cart_id: int, database: Session = Depends(get_db)):
    """Get all CartItem entities related to this Cart through cartitem"""
    db_cart = database.query(Cart).filter(Cart.id == cart_id).first()
    if db_cart is None:
        raise HTTPException(status_code=404, detail="Cart not found")

    cartitem_list = database.query(CartItem).filter(CartItem.cart_id == cart_id).all()

    return {
        "cart_id": cart_id,
        "cartitem_count": len(cartitem_list),
        "cartitem": cartitem_list
    }



############################################
#   Cart Method Endpoints
############################################




@app.post("/cart/methods/getTotal/", response_model=None, tags=["Cart Methods"])
async def cart_getTotal(
    database: Session = Depends(get_db)
):
    """
    Execute the getTotal class method on Cart.
    This method operates on all Cart entities or performs class-level operations.
    """
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output


        # Method body not defined
        result = None

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Handle result serialization
        if hasattr(result, '__iter__') and not isinstance(result, (str, dict)):
            # It's a list of entities
            result_data = []
            for item in result:
                if hasattr(item, '__dict__'):
                    item_dict = {k: v for k, v in item.__dict__.items() if not k.startswith('_')}
                    result_data.append(item_dict)
                else:
                    result_data.append(str(item))
            result = result_data
        elif hasattr(result, '__dict__'):
            result = {k: v for k, v in result.__dict__.items() if not k.startswith('_')}

        return {
            "class": "Cart",
            "method": "getTotal",
            "status": "executed",
            "result": result,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")






@app.post("/cart/methods/addItem/", response_model=None, tags=["Cart Methods"])
async def cart_addItem(
    database: Session = Depends(get_db)
):
    """
    Execute the addItem class method on Cart.
    This method operates on all Cart entities or performs class-level operations.
    """
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output


        # Method body not defined
        result = None

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Handle result serialization
        if hasattr(result, '__iter__') and not isinstance(result, (str, dict)):
            # It's a list of entities
            result_data = []
            for item in result:
                if hasattr(item, '__dict__'):
                    item_dict = {k: v for k, v in item.__dict__.items() if not k.startswith('_')}
                    result_data.append(item_dict)
                else:
                    result_data.append(str(item))
            result = result_data
        elif hasattr(result, '__dict__'):
            result = {k: v for k, v in result.__dict__.items() if not k.startswith('_')}

        return {
            "class": "Cart",
            "method": "addItem",
            "status": "executed",
            "result": result,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")






@app.post("/cart/methods/clear/", response_model=None, tags=["Cart Methods"])
async def cart_clear(
    database: Session = Depends(get_db)
):
    """
    Execute the clear class method on Cart.
    This method operates on all Cart entities or performs class-level operations.
    """
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output


        # Method body not defined
        result = None

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Handle result serialization
        if hasattr(result, '__iter__') and not isinstance(result, (str, dict)):
            # It's a list of entities
            result_data = []
            for item in result:
                if hasattr(item, '__dict__'):
                    item_dict = {k: v for k, v in item.__dict__.items() if not k.startswith('_')}
                    result_data.append(item_dict)
                else:
                    result_data.append(str(item))
            result = result_data
        elif hasattr(result, '__dict__'):
            result = {k: v for k, v in result.__dict__.items() if not k.startswith('_')}

        return {
            "class": "Cart",
            "method": "clear",
            "status": "executed",
            "result": result,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")






@app.post("/cart/methods/removeItem/", response_model=None, tags=["Cart Methods"])
async def cart_removeItem(
    database: Session = Depends(get_db)
):
    """
    Execute the removeItem class method on Cart.
    This method operates on all Cart entities or performs class-level operations.
    """
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output


        # Method body not defined
        result = None

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Handle result serialization
        if hasattr(result, '__iter__') and not isinstance(result, (str, dict)):
            # It's a list of entities
            result_data = []
            for item in result:
                if hasattr(item, '__dict__'):
                    item_dict = {k: v for k, v in item.__dict__.items() if not k.startswith('_')}
                    result_data.append(item_dict)
                else:
                    result_data.append(str(item))
            result = result_data
        elif hasattr(result, '__dict__'):
            result = {k: v for k, v in result.__dict__.items() if not k.startswith('_')}

        return {
            "class": "Cart",
            "method": "removeItem",
            "status": "executed",
            "result": result,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")




############################################
#
#   Order functions
#
############################################

@app.get("/order/", response_model=None, tags=["Order"])
def get_all_order(detailed: bool = False, database: Session = Depends(get_db)) -> list:
    from sqlalchemy.orm import joinedload

    # Use detailed=true to get entities with eagerly loaded relationships (for tables with lookup columns)
    if detailed:
        # Eagerly load all relationships to avoid N+1 queries
        query = database.query(Order)
        query = query.options(joinedload(Order.paidVia))
        query = query.options(joinedload(Order.shipsTo))
        order_list = query.all()

        # Serialize with relationships included
        result = []
        for order_item in order_list:
            item_dict = order_item.__dict__.copy()
            item_dict.pop('_sa_instance_state', None)

            # Add many-to-one relationships (foreign keys for lookup columns)
            if order_item.paidVia:
                related_obj = order_item.paidVia
                related_dict = related_obj.__dict__.copy()
                related_dict.pop('_sa_instance_state', None)
                item_dict['paidVia'] = related_dict
            else:
                item_dict['paidVia'] = None
            if order_item.shipsTo:
                related_obj = order_item.shipsTo
                related_dict = related_obj.__dict__.copy()
                related_dict.pop('_sa_instance_state', None)
                item_dict['shipsTo'] = related_dict
            else:
                item_dict['shipsTo'] = None

            # Add many-to-many and one-to-many relationship objects (full details)
            orderitem_list = database.query(OrderItem).filter(OrderItem.order_id == order_item.id).all()
            item_dict['contains'] = []
            for orderitem_obj in orderitem_list:
                orderitem_dict = orderitem_obj.__dict__.copy()
                orderitem_dict.pop('_sa_instance_state', None)
                item_dict['contains'].append(orderitem_dict)

            result.append(item_dict)
        return result
    else:
        # Default: return flat entities (faster for charts/widgets without lookup columns)
        return database.query(Order).all()


@app.get("/order/count/", response_model=None, tags=["Order"])
def get_count_order(database: Session = Depends(get_db)) -> dict:
    """Get the total count of Order entities"""
    count = database.query(Order).count()
    return {"count": count}


@app.get("/order/paginated/", response_model=None, tags=["Order"])
def get_paginated_order(skip: int = 0, limit: int = 100, detailed: bool = False, database: Session = Depends(get_db)) -> dict:
    """Get paginated list of Order entities"""
    total = database.query(Order).count()
    order_list = database.query(Order).offset(skip).limit(limit).all()
    # By default, return flat entities (for charts/widgets)
    # Use detailed=true to get entities with relationships
    if not detailed:
        return {
            "total": total,
            "skip": skip,
            "limit": limit,
            "data": order_list
        }

    result = []
    for order_item in order_list:
        contains_ids = database.query(OrderItem.id).filter(OrderItem.order_id == order_item.id).all()
        item_data = {
            "order": order_item,
            "contains_ids": [x[0] for x in contains_ids]        }
        result.append(item_data)
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": result
    }


@app.get("/order/search/", response_model=None, tags=["Order"])
def search_order(
    database: Session = Depends(get_db)
) -> list:
    """Search Order entities by attributes"""
    query = database.query(Order)


    results = query.all()
    return results


@app.get("/order/{order_id}/", response_model=None, tags=["Order"])
async def get_order(order_id: int, database: Session = Depends(get_db)) -> Order:
    db_order = database.query(Order).filter(Order.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    contains_ids = database.query(OrderItem.id).filter(OrderItem.order_id == db_order.id).all()
    response_data = {
        "order": db_order,
        "contains_ids": [x[0] for x in contains_ids]}
    return response_data



@app.post("/order/", response_model=None, tags=["Order"])
async def create_order(order_data: OrderCreate, database: Session = Depends(get_db)) -> Order:

    if order_data.paidVia is not None:
        db_paidVia = database.query(Payment).filter(Payment.id == order_data.paidVia).first()
        if not db_paidVia:
            raise HTTPException(status_code=400, detail="Payment not found")
    else:
        raise HTTPException(status_code=400, detail="Payment ID is required")

    db_order = Order(
        totalAmount=order_data.totalAmount,        Id=order_data.Id,        status=order_data.status,        paidVia_id=order_data.paidVia        )

    database.add(db_order)
    database.commit()
    database.refresh(db_order)

    if order_data.contains:
        # Validate that all OrderItem IDs exist
        for orderitem_id in order_data.contains:
            db_orderitem = database.query(OrderItem).filter(OrderItem.id == orderitem_id).first()
            if not db_orderitem:
                raise HTTPException(status_code=400, detail=f"OrderItem with id {orderitem_id} not found")

        # Update the related entities with the new foreign key
        database.query(OrderItem).filter(OrderItem.id.in_(order_data.contains)).update(
            {OrderItem.order_id: db_order.id}, synchronize_session=False
        )
        database.commit()



    contains_ids = database.query(OrderItem.id).filter(OrderItem.order_id == db_order.id).all()
    response_data = {
        "order": db_order,
        "contains_ids": [x[0] for x in contains_ids]    }
    return response_data


@app.post("/order/bulk/", response_model=None, tags=["Order"])
async def bulk_create_order(items: list[OrderCreate], database: Session = Depends(get_db)) -> dict:
    """Create multiple Order entities at once"""
    created_items = []
    errors = []

    for idx, item_data in enumerate(items):
        try:
            # Basic validation for each item
            if not item_data.paidVia:
                raise ValueError("Payment ID is required")

            db_order = Order(
                totalAmount=item_data.totalAmount,                Id=item_data.Id,                status=item_data.status,                paidVia_id=item_data.paidVia            )
            database.add(db_order)
            database.flush()  # Get ID without committing
            created_items.append(db_order.id)
        except Exception as e:
            errors.append({"index": idx, "error": str(e)})

    if errors:
        database.rollback()
        raise HTTPException(status_code=400, detail={"message": "Bulk creation failed", "errors": errors})

    database.commit()
    return {
        "created_count": len(created_items),
        "created_ids": created_items,
        "message": f"Successfully created {len(created_items)} Order entities"
    }


@app.delete("/order/bulk/", response_model=None, tags=["Order"])
async def bulk_delete_order(ids: list[int], database: Session = Depends(get_db)) -> dict:
    """Delete multiple Order entities at once"""
    deleted_count = 0
    not_found = []

    for item_id in ids:
        db_order = database.query(Order).filter(Order.id == item_id).first()
        if db_order:
            database.delete(db_order)
            deleted_count += 1
        else:
            not_found.append(item_id)

    database.commit()

    return {
        "deleted_count": deleted_count,
        "not_found": not_found,
        "message": f"Successfully deleted {deleted_count} Order entities"
    }

@app.put("/order/{order_id}/", response_model=None, tags=["Order"])
async def update_order(order_id: int, order_data: OrderCreate, database: Session = Depends(get_db)) -> Order:
    db_order = database.query(Order).filter(Order.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    setattr(db_order, 'totalAmount', order_data.totalAmount)
    setattr(db_order, 'Id', order_data.Id)
    setattr(db_order, 'status', order_data.status)
    if order_data.paidVia is not None:
        db_paidVia = database.query(Payment).filter(Payment.id == order_data.paidVia).first()
        if not db_paidVia:
            raise HTTPException(status_code=400, detail="Payment not found")
        setattr(db_order, 'paidVia_id', order_data.paidVia)
    if order_data.contains is not None:
        # Clear all existing relationships (set foreign key to NULL)
        database.query(OrderItem).filter(OrderItem.order_id == db_order.id).update(
            {OrderItem.order_id: None}, synchronize_session=False
        )

        # Set new relationships if list is not empty
        if order_data.contains:
            # Validate that all IDs exist
            for orderitem_id in order_data.contains:
                db_orderitem = database.query(OrderItem).filter(OrderItem.id == orderitem_id).first()
                if not db_orderitem:
                    raise HTTPException(status_code=400, detail=f"OrderItem with id {orderitem_id} not found")

            # Update the related entities with the new foreign key
            database.query(OrderItem).filter(OrderItem.id.in_(order_data.contains)).update(
                {OrderItem.order_id: db_order.id}, synchronize_session=False
            )
    database.commit()
    database.refresh(db_order)

    contains_ids = database.query(OrderItem.id).filter(OrderItem.order_id == db_order.id).all()
    response_data = {
        "order": db_order,
        "contains_ids": [x[0] for x in contains_ids]    }
    return response_data


@app.delete("/order/{order_id}/", response_model=None, tags=["Order"])
async def delete_order(order_id: int, database: Session = Depends(get_db)):
    db_order = database.query(Order).filter(Order.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    database.delete(db_order)
    database.commit()
    return db_order


@app.get("/order/{order_id}/contains/", response_model=None, tags=["Order Relationships"])
async def get_contains_of_order(order_id: int, database: Session = Depends(get_db)):
    """Get all OrderItem entities related to this Order through contains"""
    db_order = database.query(Order).filter(Order.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    contains_list = database.query(OrderItem).filter(OrderItem.order_id == order_id).all()

    return {
        "order_id": order_id,
        "contains_count": len(contains_list),
        "contains": contains_list
    }



############################################
#   Order Method Endpoints
############################################




@app.post("/order/methods/updateStatus/", response_model=None, tags=["Order Methods"])
async def order_updateStatus(
    database: Session = Depends(get_db)
):
    """
    Execute the updateStatus class method on Order.
    This method operates on all Order entities or performs class-level operations.
    """
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output


        # Method body not defined
        result = None

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Handle result serialization
        if hasattr(result, '__iter__') and not isinstance(result, (str, dict)):
            # It's a list of entities
            result_data = []
            for item in result:
                if hasattr(item, '__dict__'):
                    item_dict = {k: v for k, v in item.__dict__.items() if not k.startswith('_')}
                    result_data.append(item_dict)
                else:
                    result_data.append(str(item))
            result = result_data
        elif hasattr(result, '__dict__'):
            result = {k: v for k, v in result.__dict__.items() if not k.startswith('_')}

        return {
            "class": "Order",
            "method": "updateStatus",
            "status": "executed",
            "result": result,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")






@app.post("/order/methods/generateInvoice/", response_model=None, tags=["Order Methods"])
async def order_generateInvoice(
    database: Session = Depends(get_db)
):
    """
    Execute the generateInvoice class method on Order.
    This method operates on all Order entities or performs class-level operations.
    """
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output


        # Method body not defined
        result = None

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Handle result serialization
        if hasattr(result, '__iter__') and not isinstance(result, (str, dict)):
            # It's a list of entities
            result_data = []
            for item in result:
                if hasattr(item, '__dict__'):
                    item_dict = {k: v for k, v in item.__dict__.items() if not k.startswith('_')}
                    result_data.append(item_dict)
                else:
                    result_data.append(str(item))
            result = result_data
        elif hasattr(result, '__dict__'):
            result = {k: v for k, v in result.__dict__.items() if not k.startswith('_')}

        return {
            "class": "Order",
            "method": "generateInvoice",
            "status": "executed",
            "result": result,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")






@app.post("/order/methods/calculateTotal/", response_model=None, tags=["Order Methods"])
async def order_calculateTotal(
    database: Session = Depends(get_db)
):
    """
    Execute the calculateTotal class method on Order.
    This method operates on all Order entities or performs class-level operations.
    """
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output


        # Method body not defined
        result = None

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Handle result serialization
        if hasattr(result, '__iter__') and not isinstance(result, (str, dict)):
            # It's a list of entities
            result_data = []
            for item in result:
                if hasattr(item, '__dict__'):
                    item_dict = {k: v for k, v in item.__dict__.items() if not k.startswith('_')}
                    result_data.append(item_dict)
                else:
                    result_data.append(str(item))
            result = result_data
        elif hasattr(result, '__dict__'):
            result = {k: v for k, v in result.__dict__.items() if not k.startswith('_')}

        return {
            "class": "Order",
            "method": "calculateTotal",
            "status": "executed",
            "result": result,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")




############################################
#
#   User functions
#
############################################

@app.get("/user/", response_model=None, tags=["User"])
def get_all_user(detailed: bool = False, database: Session = Depends(get_db)) -> list:
    from sqlalchemy.orm import joinedload

    return database.query(User).all()


@app.get("/user/count/", response_model=None, tags=["User"])
def get_count_user(database: Session = Depends(get_db)) -> dict:
    """Get the total count of User entities"""
    count = database.query(User).count()
    return {"count": count}


@app.get("/user/paginated/", response_model=None, tags=["User"])
def get_paginated_user(skip: int = 0, limit: int = 100, detailed: bool = False, database: Session = Depends(get_db)) -> dict:
    """Get paginated list of User entities"""
    total = database.query(User).count()
    user_list = database.query(User).offset(skip).limit(limit).all()
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": user_list
    }


@app.get("/user/search/", response_model=None, tags=["User"])
def search_user(
    database: Session = Depends(get_db)
) -> list:
    """Search User entities by attributes"""
    query = database.query(User)


    results = query.all()
    return results


@app.get("/user/{user_id}/", response_model=None, tags=["User"])
async def get_user(user_id: int, database: Session = Depends(get_db)) -> User:
    db_user = database.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    response_data = {
        "user": db_user,
}
    return response_data



@app.post("/user/", response_model=None, tags=["User"])
async def create_user(user_data: UserCreate, database: Session = Depends(get_db)) -> User:


    db_user = User(
        name=user_data.name,        createdAt=user_data.createdAt,        id=user_data.id,        surname=user_data.surname        )

    database.add(db_user)
    database.commit()
    database.refresh(db_user)




    return db_user


@app.post("/user/bulk/", response_model=None, tags=["User"])
async def bulk_create_user(items: list[UserCreate], database: Session = Depends(get_db)) -> dict:
    """Create multiple User entities at once"""
    created_items = []
    errors = []

    for idx, item_data in enumerate(items):
        try:
            # Basic validation for each item

            db_user = User(
                name=item_data.name,                createdAt=item_data.createdAt,                id=item_data.id,                surname=item_data.surname            )
            database.add(db_user)
            database.flush()  # Get ID without committing
            created_items.append(db_user.id)
        except Exception as e:
            errors.append({"index": idx, "error": str(e)})

    if errors:
        database.rollback()
        raise HTTPException(status_code=400, detail={"message": "Bulk creation failed", "errors": errors})

    database.commit()
    return {
        "created_count": len(created_items),
        "created_ids": created_items,
        "message": f"Successfully created {len(created_items)} User entities"
    }


@app.delete("/user/bulk/", response_model=None, tags=["User"])
async def bulk_delete_user(ids: list[int], database: Session = Depends(get_db)) -> dict:
    """Delete multiple User entities at once"""
    deleted_count = 0
    not_found = []

    for item_id in ids:
        db_user = database.query(User).filter(User.id == item_id).first()
        if db_user:
            database.delete(db_user)
            deleted_count += 1
        else:
            not_found.append(item_id)

    database.commit()

    return {
        "deleted_count": deleted_count,
        "not_found": not_found,
        "message": f"Successfully deleted {deleted_count} User entities"
    }

@app.put("/user/{user_id}/", response_model=None, tags=["User"])
async def update_user(user_id: int, user_data: UserCreate, database: Session = Depends(get_db)) -> User:
    db_user = database.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    setattr(db_user, 'name', user_data.name)
    setattr(db_user, 'createdAt', user_data.createdAt)
    setattr(db_user, 'id', user_data.id)
    setattr(db_user, 'surname', user_data.surname)
    database.commit()
    database.refresh(db_user)

    return db_user


@app.delete("/user/{user_id}/", response_model=None, tags=["User"])
async def delete_user(user_id: int, database: Session = Depends(get_db)):
    db_user = database.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    database.delete(db_user)
    database.commit()
    return db_user




############################################
#   User Method Endpoints
############################################




@app.post("/user/methods/register/", response_model=None, tags=["User Methods"])
async def user_register(
    database: Session = Depends(get_db)
):
    """
    Execute the register class method on User.
    This method operates on all User entities or performs class-level operations.
    """
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output


        # Method body not defined
        result = None

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Handle result serialization
        if hasattr(result, '__iter__') and not isinstance(result, (str, dict)):
            # It's a list of entities
            result_data = []
            for item in result:
                if hasattr(item, '__dict__'):
                    item_dict = {k: v for k, v in item.__dict__.items() if not k.startswith('_')}
                    result_data.append(item_dict)
                else:
                    result_data.append(str(item))
            result = result_data
        elif hasattr(result, '__dict__'):
            result = {k: v for k, v in result.__dict__.items() if not k.startswith('_')}

        return {
            "class": "User",
            "method": "register",
            "status": "executed",
            "result": result,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")






@app.post("/user/methods/login/", response_model=None, tags=["User Methods"])
async def user_login(
    database: Session = Depends(get_db)
):
    """
    Execute the login class method on User.
    This method operates on all User entities or performs class-level operations.
    """
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output


        # Method body not defined
        result = None

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Handle result serialization
        if hasattr(result, '__iter__') and not isinstance(result, (str, dict)):
            # It's a list of entities
            result_data = []
            for item in result:
                if hasattr(item, '__dict__'):
                    item_dict = {k: v for k, v in item.__dict__.items() if not k.startswith('_')}
                    result_data.append(item_dict)
                else:
                    result_data.append(str(item))
            result = result_data
        elif hasattr(result, '__dict__'):
            result = {k: v for k, v in result.__dict__.items() if not k.startswith('_')}

        return {
            "class": "User",
            "method": "login",
            "status": "executed",
            "result": result,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")




############################################
#
#   Customer functions
#
############################################

@app.get("/customer/", response_model=None, tags=["Customer"])
def get_all_customer(detailed: bool = False, database: Session = Depends(get_db)) -> list:
    from sqlalchemy.orm import joinedload

    # Use detailed=true to get entities with eagerly loaded relationships (for tables with lookup columns)
    if detailed:
        # Eagerly load all relationships to avoid N+1 queries
        query = database.query(Customer)
        query = query.options(joinedload(Customer.owns))
        customer_list = query.all()

        # Serialize with relationships included
        result = []
        for customer_item in customer_list:
            item_dict = customer_item.__dict__.copy()
            item_dict.pop('_sa_instance_state', None)

            # Add many-to-one relationships (foreign keys for lookup columns)
            if customer_item.owns:
                related_obj = customer_item.owns
                related_dict = related_obj.__dict__.copy()
                related_dict.pop('_sa_instance_state', None)
                item_dict['owns'] = related_dict
            else:
                item_dict['owns'] = None

            # Add many-to-many and one-to-many relationship objects (full details)
            address_list = database.query(Address).filter(Address.customer_3_id == customer_item.id).all()
            item_dict['has'] = []
            for address_obj in address_list:
                address_dict = address_obj.__dict__.copy()
                address_dict.pop('_sa_instance_state', None)
                item_dict['has'].append(address_dict)
            order_list = database.query(Order).filter(Order.customer_1_id == customer_item.id).all()
            item_dict['places'] = []
            for order_obj in order_list:
                order_dict = order_obj.__dict__.copy()
                order_dict.pop('_sa_instance_state', None)
                item_dict['places'].append(order_dict)
            review_list = database.query(Review).filter(Review.customer_2_id == customer_item.id).all()
            item_dict['writes'] = []
            for review_obj in review_list:
                review_dict = review_obj.__dict__.copy()
                review_dict.pop('_sa_instance_state', None)
                item_dict['writes'].append(review_dict)

            result.append(item_dict)
        return result
    else:
        # Default: return flat entities (faster for charts/widgets without lookup columns)
        return database.query(Customer).all()


@app.get("/customer/count/", response_model=None, tags=["Customer"])
def get_count_customer(database: Session = Depends(get_db)) -> dict:
    """Get the total count of Customer entities"""
    count = database.query(Customer).count()
    return {"count": count}


@app.get("/customer/paginated/", response_model=None, tags=["Customer"])
def get_paginated_customer(skip: int = 0, limit: int = 100, detailed: bool = False, database: Session = Depends(get_db)) -> dict:
    """Get paginated list of Customer entities"""
    total = database.query(Customer).count()
    customer_list = database.query(Customer).offset(skip).limit(limit).all()
    # By default, return flat entities (for charts/widgets)
    # Use detailed=true to get entities with relationships
    if not detailed:
        return {
            "total": total,
            "skip": skip,
            "limit": limit,
            "data": customer_list
        }

    result = []
    for customer_item in customer_list:
        has_ids = database.query(Address.id).filter(Address.customer_3_id == customer_item.id).all()
        places_ids = database.query(Order.id).filter(Order.customer_1_id == customer_item.id).all()
        writes_ids = database.query(Review.id).filter(Review.customer_2_id == customer_item.id).all()
        item_data = {
            "customer": customer_item,
            "has_ids": [x[0] for x in has_ids],            "places_ids": [x[0] for x in places_ids],            "writes_ids": [x[0] for x in writes_ids]        }
        result.append(item_data)
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": result
    }


@app.get("/customer/search/", response_model=None, tags=["Customer"])
def search_customer(
    database: Session = Depends(get_db)
) -> list:
    """Search Customer entities by attributes"""
    query = database.query(Customer)


    results = query.all()
    return results


@app.get("/customer/{customer_id}/", response_model=None, tags=["Customer"])
async def get_customer(customer_id: int, database: Session = Depends(get_db)) -> Customer:
    db_customer = database.query(Customer).filter(Customer.id == customer_id).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")

    has_ids = database.query(Address.id).filter(Address.customer_3_id == db_customer.id).all()
    places_ids = database.query(Order.id).filter(Order.customer_1_id == db_customer.id).all()
    writes_ids = database.query(Review.id).filter(Review.customer_2_id == db_customer.id).all()
    response_data = {
        "customer": db_customer,
        "has_ids": [x[0] for x in has_ids],        "places_ids": [x[0] for x in places_ids],        "writes_ids": [x[0] for x in writes_ids]}
    return response_data



@app.post("/customer/", response_model=None, tags=["Customer"])
async def create_customer(customer_data: CustomerCreate, database: Session = Depends(get_db)) -> Customer:


    db_customer = Customer(
        name=customer_data.name,        createdAt=customer_data.createdAt,        id=customer_data.id,        surname=customer_data.surname,        Id=customer_data.Id        )

    database.add(db_customer)
    database.commit()
    database.refresh(db_customer)

    if customer_data.has:
        # Validate that all Address IDs exist
        for address_id in customer_data.has:
            db_address = database.query(Address).filter(Address.id == address_id).first()
            if not db_address:
                raise HTTPException(status_code=400, detail=f"Address with id {address_id} not found")

        # Update the related entities with the new foreign key
        database.query(Address).filter(Address.id.in_(customer_data.has)).update(
            {Address.customer_3_id: db_customer.id}, synchronize_session=False
        )
        database.commit()
    if customer_data.places:
        # Validate that all Order IDs exist
        for order_id in customer_data.places:
            db_order = database.query(Order).filter(Order.id == order_id).first()
            if not db_order:
                raise HTTPException(status_code=400, detail=f"Order with id {order_id} not found")

        # Update the related entities with the new foreign key
        database.query(Order).filter(Order.id.in_(customer_data.places)).update(
            {Order.customer_1_id: db_customer.id}, synchronize_session=False
        )
        database.commit()
    if customer_data.writes:
        # Validate that all Review IDs exist
        for review_id in customer_data.writes:
            db_review = database.query(Review).filter(Review.id == review_id).first()
            if not db_review:
                raise HTTPException(status_code=400, detail=f"Review with id {review_id} not found")

        # Update the related entities with the new foreign key
        database.query(Review).filter(Review.id.in_(customer_data.writes)).update(
            {Review.customer_2_id: db_customer.id}, synchronize_session=False
        )
        database.commit()



    has_ids = database.query(Address.id).filter(Address.customer_3_id == db_customer.id).all()
    places_ids = database.query(Order.id).filter(Order.customer_1_id == db_customer.id).all()
    writes_ids = database.query(Review.id).filter(Review.customer_2_id == db_customer.id).all()
    response_data = {
        "customer": db_customer,
        "has_ids": [x[0] for x in has_ids],        "places_ids": [x[0] for x in places_ids],        "writes_ids": [x[0] for x in writes_ids]    }
    return response_data


@app.post("/customer/bulk/", response_model=None, tags=["Customer"])
async def bulk_create_customer(items: list[CustomerCreate], database: Session = Depends(get_db)) -> dict:
    """Create multiple Customer entities at once"""
    created_items = []
    errors = []

    for idx, item_data in enumerate(items):
        try:
            # Basic validation for each item

            db_customer = Customer(
                name=item_data.name,                createdAt=item_data.createdAt,                id=item_data.id,                surname=item_data.surname,                Id=item_data.Id            )
            database.add(db_customer)
            database.flush()  # Get ID without committing
            created_items.append(db_customer.id)
        except Exception as e:
            errors.append({"index": idx, "error": str(e)})

    if errors:
        database.rollback()
        raise HTTPException(status_code=400, detail={"message": "Bulk creation failed", "errors": errors})

    database.commit()
    return {
        "created_count": len(created_items),
        "created_ids": created_items,
        "message": f"Successfully created {len(created_items)} Customer entities"
    }


@app.delete("/customer/bulk/", response_model=None, tags=["Customer"])
async def bulk_delete_customer(ids: list[int], database: Session = Depends(get_db)) -> dict:
    """Delete multiple Customer entities at once"""
    deleted_count = 0
    not_found = []

    for item_id in ids:
        db_customer = database.query(Customer).filter(Customer.id == item_id).first()
        if db_customer:
            database.delete(db_customer)
            deleted_count += 1
        else:
            not_found.append(item_id)

    database.commit()

    return {
        "deleted_count": deleted_count,
        "not_found": not_found,
        "message": f"Successfully deleted {deleted_count} Customer entities"
    }

@app.put("/customer/{customer_id}/", response_model=None, tags=["Customer"])
async def update_customer(customer_id: int, customer_data: CustomerCreate, database: Session = Depends(get_db)) -> Customer:
    db_customer = database.query(Customer).filter(Customer.id == customer_id).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")

    setattr(db_customer, 'Id', customer_data.Id)
    if customer_data.has is not None:
        # Clear all existing relationships (set foreign key to NULL)
        database.query(Address).filter(Address.customer_3_id == db_customer.id).update(
            {Address.customer_3_id: None}, synchronize_session=False
        )

        # Set new relationships if list is not empty
        if customer_data.has:
            # Validate that all IDs exist
            for address_id in customer_data.has:
                db_address = database.query(Address).filter(Address.id == address_id).first()
                if not db_address:
                    raise HTTPException(status_code=400, detail=f"Address with id {address_id} not found")

            # Update the related entities with the new foreign key
            database.query(Address).filter(Address.id.in_(customer_data.has)).update(
                {Address.customer_3_id: db_customer.id}, synchronize_session=False
            )
    if customer_data.places is not None:
        # Clear all existing relationships (set foreign key to NULL)
        database.query(Order).filter(Order.customer_1_id == db_customer.id).update(
            {Order.customer_1_id: None}, synchronize_session=False
        )

        # Set new relationships if list is not empty
        if customer_data.places:
            # Validate that all IDs exist
            for order_id in customer_data.places:
                db_order = database.query(Order).filter(Order.id == order_id).first()
                if not db_order:
                    raise HTTPException(status_code=400, detail=f"Order with id {order_id} not found")

            # Update the related entities with the new foreign key
            database.query(Order).filter(Order.id.in_(customer_data.places)).update(
                {Order.customer_1_id: db_customer.id}, synchronize_session=False
            )
    if customer_data.writes is not None:
        # Clear all existing relationships (set foreign key to NULL)
        database.query(Review).filter(Review.customer_2_id == db_customer.id).update(
            {Review.customer_2_id: None}, synchronize_session=False
        )

        # Set new relationships if list is not empty
        if customer_data.writes:
            # Validate that all IDs exist
            for review_id in customer_data.writes:
                db_review = database.query(Review).filter(Review.id == review_id).first()
                if not db_review:
                    raise HTTPException(status_code=400, detail=f"Review with id {review_id} not found")

            # Update the related entities with the new foreign key
            database.query(Review).filter(Review.id.in_(customer_data.writes)).update(
                {Review.customer_2_id: db_customer.id}, synchronize_session=False
            )
    database.commit()
    database.refresh(db_customer)

    has_ids = database.query(Address.id).filter(Address.customer_3_id == db_customer.id).all()
    places_ids = database.query(Order.id).filter(Order.customer_1_id == db_customer.id).all()
    writes_ids = database.query(Review.id).filter(Review.customer_2_id == db_customer.id).all()
    response_data = {
        "customer": db_customer,
        "has_ids": [x[0] for x in has_ids],        "places_ids": [x[0] for x in places_ids],        "writes_ids": [x[0] for x in writes_ids]    }
    return response_data


@app.delete("/customer/{customer_id}/", response_model=None, tags=["Customer"])
async def delete_customer(customer_id: int, database: Session = Depends(get_db)):
    db_customer = database.query(Customer).filter(Customer.id == customer_id).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    database.delete(db_customer)
    database.commit()
    return db_customer


@app.get("/customer/{customer_id}/has/", response_model=None, tags=["Customer Relationships"])
async def get_has_of_customer(customer_id: int, database: Session = Depends(get_db)):
    """Get all Address entities related to this Customer through has"""
    db_customer = database.query(Customer).filter(Customer.id == customer_id).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")

    has_list = database.query(Address).filter(Address.customer_3_id == customer_id).all()

    return {
        "customer_id": customer_id,
        "has_count": len(has_list),
        "has": has_list
    }

@app.get("/customer/{customer_id}/places/", response_model=None, tags=["Customer Relationships"])
async def get_places_of_customer(customer_id: int, database: Session = Depends(get_db)):
    """Get all Order entities related to this Customer through places"""
    db_customer = database.query(Customer).filter(Customer.id == customer_id).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")

    places_list = database.query(Order).filter(Order.customer_1_id == customer_id).all()

    return {
        "customer_id": customer_id,
        "places_count": len(places_list),
        "places": places_list
    }

@app.get("/customer/{customer_id}/writes/", response_model=None, tags=["Customer Relationships"])
async def get_writes_of_customer(customer_id: int, database: Session = Depends(get_db)):
    """Get all Review entities related to this Customer through writes"""
    db_customer = database.query(Customer).filter(Customer.id == customer_id).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")

    writes_list = database.query(Review).filter(Review.customer_2_id == customer_id).all()

    return {
        "customer_id": customer_id,
        "writes_count": len(writes_list),
        "writes": writes_list
    }



############################################
#   Customer Method Endpoints
############################################




@app.post("/customer/methods/writeReview/", response_model=None, tags=["Customer Methods"])
async def customer_writeReview(
    database: Session = Depends(get_db)
):
    """
    Execute the writeReview class method on Customer.
    This method operates on all Customer entities or performs class-level operations.
    """
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output


        # Method body not defined
        result = None

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Handle result serialization
        if hasattr(result, '__iter__') and not isinstance(result, (str, dict)):
            # It's a list of entities
            result_data = []
            for item in result:
                if hasattr(item, '__dict__'):
                    item_dict = {k: v for k, v in item.__dict__.items() if not k.startswith('_')}
                    result_data.append(item_dict)
                else:
                    result_data.append(str(item))
            result = result_data
        elif hasattr(result, '__dict__'):
            result = {k: v for k, v in result.__dict__.items() if not k.startswith('_')}

        return {
            "class": "Customer",
            "method": "writeReview",
            "status": "executed",
            "result": result,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")






@app.post("/customer/methods/placeOrder/", response_model=None, tags=["Customer Methods"])
async def customer_placeOrder(
    database: Session = Depends(get_db)
):
    """
    Execute the placeOrder class method on Customer.
    This method operates on all Customer entities or performs class-level operations.
    """
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output


        # Method body not defined
        result = None

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Handle result serialization
        if hasattr(result, '__iter__') and not isinstance(result, (str, dict)):
            # It's a list of entities
            result_data = []
            for item in result:
                if hasattr(item, '__dict__'):
                    item_dict = {k: v for k, v in item.__dict__.items() if not k.startswith('_')}
                    result_data.append(item_dict)
                else:
                    result_data.append(str(item))
            result = result_data
        elif hasattr(result, '__dict__'):
            result = {k: v for k, v in result.__dict__.items() if not k.startswith('_')}

        return {
            "class": "Customer",
            "method": "placeOrder",
            "status": "executed",
            "result": result,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")






@app.post("/customer/methods/addToCart/", response_model=None, tags=["Customer Methods"])
async def customer_addToCart(
    database: Session = Depends(get_db)
):
    """
    Execute the addToCart class method on Customer.
    This method operates on all Customer entities or performs class-level operations.
    """
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output


        # Method body not defined
        result = None

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Handle result serialization
        if hasattr(result, '__iter__') and not isinstance(result, (str, dict)):
            # It's a list of entities
            result_data = []
            for item in result:
                if hasattr(item, '__dict__'):
                    item_dict = {k: v for k, v in item.__dict__.items() if not k.startswith('_')}
                    result_data.append(item_dict)
                else:
                    result_data.append(str(item))
            result = result_data
        elif hasattr(result, '__dict__'):
            result = {k: v for k, v in result.__dict__.items() if not k.startswith('_')}

        return {
            "class": "Customer",
            "method": "addToCart",
            "status": "executed",
            "result": result,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")




############################################
#
#   Admin functions
#
############################################

@app.get("/admin/", response_model=None, tags=["Admin"])
def get_all_admin(detailed: bool = False, database: Session = Depends(get_db)) -> list:
    from sqlalchemy.orm import joinedload

    return database.query(Admin).all()


@app.get("/admin/count/", response_model=None, tags=["Admin"])
def get_count_admin(database: Session = Depends(get_db)) -> dict:
    """Get the total count of Admin entities"""
    count = database.query(Admin).count()
    return {"count": count}


@app.get("/admin/paginated/", response_model=None, tags=["Admin"])
def get_paginated_admin(skip: int = 0, limit: int = 100, detailed: bool = False, database: Session = Depends(get_db)) -> dict:
    """Get paginated list of Admin entities"""
    total = database.query(Admin).count()
    admin_list = database.query(Admin).offset(skip).limit(limit).all()
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": admin_list
    }


@app.get("/admin/search/", response_model=None, tags=["Admin"])
def search_admin(
    database: Session = Depends(get_db)
) -> list:
    """Search Admin entities by attributes"""
    query = database.query(Admin)


    results = query.all()
    return results


@app.get("/admin/{admin_id}/", response_model=None, tags=["Admin"])
async def get_admin(admin_id: int, database: Session = Depends(get_db)) -> Admin:
    db_admin = database.query(Admin).filter(Admin.id == admin_id).first()
    if db_admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")

    response_data = {
        "admin": db_admin,
}
    return response_data



@app.post("/admin/", response_model=None, tags=["Admin"])
async def create_admin(admin_data: AdminCreate, database: Session = Depends(get_db)) -> Admin:


    db_admin = Admin(
        name=admin_data.name,        createdAt=admin_data.createdAt,        id=admin_data.id,        surname=admin_data.surname,        role=admin_data.role        )

    database.add(db_admin)
    database.commit()
    database.refresh(db_admin)




    return db_admin


@app.post("/admin/bulk/", response_model=None, tags=["Admin"])
async def bulk_create_admin(items: list[AdminCreate], database: Session = Depends(get_db)) -> dict:
    """Create multiple Admin entities at once"""
    created_items = []
    errors = []

    for idx, item_data in enumerate(items):
        try:
            # Basic validation for each item

            db_admin = Admin(
                name=item_data.name,                createdAt=item_data.createdAt,                id=item_data.id,                surname=item_data.surname,                role=item_data.role            )
            database.add(db_admin)
            database.flush()  # Get ID without committing
            created_items.append(db_admin.id)
        except Exception as e:
            errors.append({"index": idx, "error": str(e)})

    if errors:
        database.rollback()
        raise HTTPException(status_code=400, detail={"message": "Bulk creation failed", "errors": errors})

    database.commit()
    return {
        "created_count": len(created_items),
        "created_ids": created_items,
        "message": f"Successfully created {len(created_items)} Admin entities"
    }


@app.delete("/admin/bulk/", response_model=None, tags=["Admin"])
async def bulk_delete_admin(ids: list[int], database: Session = Depends(get_db)) -> dict:
    """Delete multiple Admin entities at once"""
    deleted_count = 0
    not_found = []

    for item_id in ids:
        db_admin = database.query(Admin).filter(Admin.id == item_id).first()
        if db_admin:
            database.delete(db_admin)
            deleted_count += 1
        else:
            not_found.append(item_id)

    database.commit()

    return {
        "deleted_count": deleted_count,
        "not_found": not_found,
        "message": f"Successfully deleted {deleted_count} Admin entities"
    }

@app.put("/admin/{admin_id}/", response_model=None, tags=["Admin"])
async def update_admin(admin_id: int, admin_data: AdminCreate, database: Session = Depends(get_db)) -> Admin:
    db_admin = database.query(Admin).filter(Admin.id == admin_id).first()
    if db_admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")

    setattr(db_admin, 'role', admin_data.role)
    database.commit()
    database.refresh(db_admin)

    return db_admin


@app.delete("/admin/{admin_id}/", response_model=None, tags=["Admin"])
async def delete_admin(admin_id: int, database: Session = Depends(get_db)):
    db_admin = database.query(Admin).filter(Admin.id == admin_id).first()
    if db_admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")
    database.delete(db_admin)
    database.commit()
    return db_admin




############################################
#   Admin Method Endpoints
############################################




@app.post("/admin/methods/manageOrders/", response_model=None, tags=["Admin Methods"])
async def admin_manageOrders(
    database: Session = Depends(get_db)
):
    """
    Execute the manageOrders class method on Admin.
    This method operates on all Admin entities or performs class-level operations.
    """
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output


        # Method body not defined
        result = None

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Handle result serialization
        if hasattr(result, '__iter__') and not isinstance(result, (str, dict)):
            # It's a list of entities
            result_data = []
            for item in result:
                if hasattr(item, '__dict__'):
                    item_dict = {k: v for k, v in item.__dict__.items() if not k.startswith('_')}
                    result_data.append(item_dict)
                else:
                    result_data.append(str(item))
            result = result_data
        elif hasattr(result, '__dict__'):
            result = {k: v for k, v in result.__dict__.items() if not k.startswith('_')}

        return {
            "class": "Admin",
            "method": "manageOrders",
            "status": "executed",
            "result": result,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")






@app.post("/admin/methods/manageProducts/", response_model=None, tags=["Admin Methods"])
async def admin_manageProducts(
    database: Session = Depends(get_db)
):
    """
    Execute the manageProducts class method on Admin.
    This method operates on all Admin entities or performs class-level operations.
    """
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output


        # Method body not defined
        result = None

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Handle result serialization
        if hasattr(result, '__iter__') and not isinstance(result, (str, dict)):
            # It's a list of entities
            result_data = []
            for item in result:
                if hasattr(item, '__dict__'):
                    item_dict = {k: v for k, v in item.__dict__.items() if not k.startswith('_')}
                    result_data.append(item_dict)
                else:
                    result_data.append(str(item))
            result = result_data
        elif hasattr(result, '__dict__'):
            result = {k: v for k, v in result.__dict__.items() if not k.startswith('_')}

        return {
            "class": "Admin",
            "method": "manageProducts",
            "status": "executed",
            "result": result,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")






############################################
# Maintaining the server
############################################
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



