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
    duration: timedelta
    title: str
    truckNumber: int
    Id: int
    album_1: int  # N:1 Relationship (mandatory)


class ArtistCreate(BaseModel):
    Id: int
    bio: str
    name: str
    country: str
    album: int  # N:1 Relationship (mandatory)


class AlbumCreate(BaseModel):
    format: str
    stockQuantity: int
    price: float
    artist: str
    releaseYear: date
    Id: int
    title: str
    orderitem: int  # 1:1 Relationship (mandatory)
    createdBy: Optional[List[int]] = None  # 1:N Relationship
    contains: Optional[List[int]] = None  # 1:N Relationship


class CartItemCreate(BaseModel):
    unintPrice: float
    quantity: int
    cart: int  # N:1 Relationship (mandatory)


class PaymentCreate(BaseModel):
    Id: int
    method: str
    amount: float
    order_1: int  # 1:1 Relationship (mandatory)


class OrderItemCreate(BaseModel):
    quantity: int
    unintPrice: str
    refersTo: int  # 1:1 Relationship (mandatory)
    order: int  # N:1 Relationship (mandatory)


class AddressCreate(BaseModel):
    street: str
    city: float
    zip_code: str
    Id: int
    customer_3: int  # N:1 Relationship (mandatory)
    order_2: int  # 1:1 Relationship (mandatory)


class ReviewCreate(BaseModel):
    rating: str
    Id: int
    comment: str
    customer_2: int  # N:1 Relationship (mandatory)


class CartCreate(BaseModel):
    Id: int
    cartitem: Optional[List[int]] = None  # 1:N Relationship


class OrderCreate(BaseModel):
    totalAmount: float
    Id: int
    status: str
    contains: Optional[List[int]] = None  # 1:N Relationship
    paidVia: int  # 1:1 Relationship (mandatory)
    shipsTo: int  # 1:1 Relationship (mandatory)


class UserCreate(BaseModel):
    name: str
    createdAt: date
    id: int
    surname: str


class CustomerCreate(UserCreate):
    Id: str
    owns: Optional[int] = None  # 1:1 Relationship (optional)
    has: Optional[List[int]] = None  # 1:N Relationship
    places: Optional[List[int]] = None  # 1:N Relationship
    writes: Optional[List[int]] = None  # 1:N Relationship


class AdminCreate(UserCreate):
    role: str


