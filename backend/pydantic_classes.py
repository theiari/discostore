from datetime import datetime, date, time
from typing import Any, List, Optional, Union, Set
from enum import Enum
from pydantic import BaseModel, field_validator


############################################
# Enumerations are defined here
############################################

############################################
# Classes are defined here
############################################
class TrackCreate(BaseModel):
    truckNumber: int
    Id: int
    duration: timedelta
    title: str
    album_1: int  # N:1 Relationship (mandatory)


class ArtistCreate(BaseModel):
    name: str
    Id: int
    country: str
    bio: str
    album: int  # N:1 Relationship (mandatory)


class AlbumCreate(BaseModel):
    title: str
    stockQuantity: int
    format: str
    artist: str
    price: float
    Id: int
    releaseYear: date
    orderitem: int  # 1:1 Relationship (mandatory)
    contains: Optional[List[int]] = None  # 1:N Relationship
    createdBy: Optional[List[int]] = None  # 1:N Relationship


class CartItemCreate(BaseModel):
    quantity: int
    unintPrice: float
    cart: int  # N:1 Relationship (mandatory)


class PaymentCreate(BaseModel):
    method: str
    Id: int
    amount: float
    order_1: int  # 1:1 Relationship (mandatory)


class OrderItemCreate(BaseModel):
    quantity: int
    unintPrice: str
    order: int  # N:1 Relationship (mandatory)
    refersTo: int  # 1:1 Relationship (mandatory)


class AddressCreate(BaseModel):
    zip_code: str
    Id: int
    city: float
    street: str
    customer_3: int  # N:1 Relationship (mandatory)
    order_2: int  # 1:1 Relationship (mandatory)


class ReviewCreate(BaseModel):
    comment: str
    Id: int
    rating: str
    customer_2: int  # N:1 Relationship (mandatory)


class CartCreate(BaseModel):
    Id: int
    cartitem: Optional[List[int]] = None  # 1:N Relationship


class OrderCreate(BaseModel):
    status: str
    totalAmount: float
    Id: int
    contains: Optional[List[int]] = None  # 1:N Relationship
    paidVia: int  # 1:1 Relationship (mandatory)
    shipsTo: int  # 1:1 Relationship (mandatory)


class UserCreate(BaseModel):
    createdAt: date
    surname: str
    name: str
    id: int


class AdminCreate(UserCreate):
    role: str


class CustomerCreate(UserCreate):
    Id: str
    owns: Optional[int] = None  # 1:1 Relationship (optional)
    has: Optional[List[int]] = None  # 1:N Relationship
    places: Optional[List[int]] = None  # 1:N Relationship
    writes: Optional[List[int]] = None  # 1:N Relationship


