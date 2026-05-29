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
class OrderCreate(BaseModel):
    status: str
    Id: int
    totalAmount: float
    shipsTo: int  # 1:1 Relationship (mandatory)
    contains: Optional[List[int]] = None  # 1:N Relationship
    paidVia: int  # 1:1 Relationship (mandatory)


class UserCreate(BaseModel):
    id: int
    surname: str
    name: str
    createdAt: date


class AdminCreate(UserCreate):
    role: str


class CustomerCreate(UserCreate):
    Id: str
    owns: Optional[int] = None  # 1:1 Relationship (optional)
    writes: Optional[List[int]] = None  # 1:N Relationship
    has: Optional[List[int]] = None  # 1:N Relationship
    places: Optional[List[int]] = None  # 1:N Relationship


class TrackCreate(BaseModel):
    Id: int
    duration: timedelta
    title: str
    truckNumber: int
    album_1: int  # N:1 Relationship (mandatory)


class ArtistCreate(BaseModel):
    country: str
    Id: int
    name: str
    bio: str
    album: int  # N:1 Relationship (mandatory)


class AlbumCreate(BaseModel):
    Id: int
    releaseYear: date
    format: str
    title: str
    price: float
    artist: str
    stockQuantity: int
    contains: Optional[List[int]] = None  # 1:N Relationship
    orderitem: int  # 1:1 Relationship (mandatory)
    createdBy: Optional[List[int]] = None  # 1:N Relationship


class CartItemCreate(BaseModel):
    unintPrice: float
    quantity: int
    cart: int  # N:1 Relationship (mandatory)


class PaymentCreate(BaseModel):
    Id: int
    amount: float
    method: str
    order_1: int  # 1:1 Relationship (mandatory)


class OrderItemCreate(BaseModel):
    unintPrice: str
    quantity: int
    order: int  # N:1 Relationship (mandatory)
    refersTo: int  # 1:1 Relationship (mandatory)


class AddressCreate(BaseModel):
    street: str
    city: float
    zip_code: str
    Id: int
    order_2: int  # 1:1 Relationship (mandatory)
    customer_3: int  # N:1 Relationship (mandatory)


class ReviewCreate(BaseModel):
    rating: str
    comment: str
    Id: int
    customer_2: int  # N:1 Relationship (mandatory)


class CartCreate(BaseModel):
    Id: int
    cartitem: Optional[List[int]] = None  # 1:N Relationship


