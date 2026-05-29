import enum
from typing import List as List_, Optional as Optional_
from sqlalchemy import (
    create_engine, Column as Column_, ForeignKey as ForeignKey_, Table as Table_, 
    Text as Text_, Boolean as Boolean_, String as String_, Date as Date_, 
    Time as Time_, DateTime as DateTime_, Float as Float_, Integer as Integer_, Enum
)
from sqlalchemy.orm import (
    column_property, DeclarativeBase, Mapped as Mapped_, mapped_column, relationship
)
from datetime import datetime as dt_datetime, time as dt_time, date as dt_date

class Base(DeclarativeBase):
    pass



# Tables definition for many-to-many relationships

# Tables definition
class Order(Base):
    __tablename__ = "order"
    id: Mapped_[int] = mapped_column(primary_key=True)
    Id: Mapped_[int] = mapped_column(Integer_)
    status: Mapped_[str] = mapped_column(String_(100))
    totalAmount: Mapped_[float] = mapped_column(Float_)
    paidVia_id: Mapped_[int] = mapped_column(ForeignKey_("payment.id"), unique=True)
    customer_1_id: Mapped_[int] = mapped_column(ForeignKey_("customer.id"))

class User(Base):
    __tablename__ = "user"
    id: Mapped_[int] = mapped_column(Integer_, primary_key=True)
    name: Mapped_[str] = mapped_column(String_(100))
    surname: Mapped_[str] = mapped_column(String_(100))
    createdAt: Mapped_[dt_date] = mapped_column(Date_)
    type_spec: Mapped_[str] = mapped_column(String_(50))
    __mapper_args__ = {
        "polymorphic_identity": "user",
        "polymorphic_on": "type_spec",
    }

class Admin(User):
    __tablename__ = "admin"
    id: Mapped_[int] = mapped_column(ForeignKey_("user.id"), primary_key=True)
    role: Mapped_[str] = mapped_column(String_(100))
    __mapper_args__ = {
        "polymorphic_identity": "admin",
    }

class Customer(User):
    __tablename__ = "customer"
    id: Mapped_[int] = mapped_column(ForeignKey_("user.id"), primary_key=True)
    Id: Mapped_[str] = mapped_column(String_(100))
    __mapper_args__ = {
        "polymorphic_identity": "customer",
    }

class Track(Base):
    __tablename__ = "track"
    id: Mapped_[int] = mapped_column(primary_key=True)
    Id: Mapped_[int] = mapped_column(Integer_)
    title: Mapped_[str] = mapped_column(String_(100))
    duration: Mapped_[timedelta] = mapped_column()
    truckNumber: Mapped_[int] = mapped_column(Integer_)
    album_1_id: Mapped_[int] = mapped_column(ForeignKey_("album.id"))

class Artist(Base):
    __tablename__ = "artist"
    id: Mapped_[int] = mapped_column(primary_key=True)
    Id: Mapped_[int] = mapped_column(Integer_)
    name: Mapped_[str] = mapped_column(String_(100))
    bio: Mapped_[str] = mapped_column(String_(100))
    country: Mapped_[str] = mapped_column(String_(100))
    album_id: Mapped_[int] = mapped_column(ForeignKey_("album.id"))

class Album(Base):
    __tablename__ = "album"
    id: Mapped_[int] = mapped_column(primary_key=True)
    Id: Mapped_[int] = mapped_column(Integer_)
    title: Mapped_[str] = mapped_column(String_(100))
    artist: Mapped_[str] = mapped_column(String_(100))
    releaseYear: Mapped_[dt_date] = mapped_column(Date_)
    price: Mapped_[float] = mapped_column(Float_)
    stockQuantity: Mapped_[int] = mapped_column(Integer_)
    format: Mapped_[str] = mapped_column(String_(100))
    orderitem_id: Mapped_[int] = mapped_column(ForeignKey_("orderitem.id"), unique=True)

class CartItem(Base):
    __tablename__ = "cartitem"
    id: Mapped_[int] = mapped_column(primary_key=True)
    quantity: Mapped_[int] = mapped_column(Integer_)
    unintPrice: Mapped_[float] = mapped_column(Float_)
    cart_id: Mapped_[int] = mapped_column(ForeignKey_("cart.id"))

class Payment(Base):
    __tablename__ = "payment"
    id: Mapped_[int] = mapped_column(primary_key=True)
    Id: Mapped_[int] = mapped_column(Integer_)
    method: Mapped_[str] = mapped_column(String_(100))
    amount: Mapped_[float] = mapped_column(Float_)

class OrderItem(Base):
    __tablename__ = "orderitem"
    id: Mapped_[int] = mapped_column(primary_key=True)
    quantity: Mapped_[int] = mapped_column(Integer_)
    unintPrice: Mapped_[str] = mapped_column(String_(100))
    order_id: Mapped_[int] = mapped_column(ForeignKey_("order.id"))

class Address(Base):
    __tablename__ = "address"
    id: Mapped_[int] = mapped_column(primary_key=True)
    street: Mapped_[str] = mapped_column(String_(100))
    city: Mapped_[float] = mapped_column(Float_)
    zip_code: Mapped_[str] = mapped_column(String_(100))
    Id: Mapped_[int] = mapped_column(Integer_)
    customer_3_id: Mapped_[int] = mapped_column(ForeignKey_("customer.id"))
    order_2_id: Mapped_[int] = mapped_column(ForeignKey_("order.id"), unique=True)

class Review(Base):
    __tablename__ = "review"
    id: Mapped_[int] = mapped_column(primary_key=True)
    Id: Mapped_[int] = mapped_column(Integer_)
    rating: Mapped_[str] = mapped_column(String_(100))
    comment: Mapped_[str] = mapped_column(String_(100))
    customer_2_id: Mapped_[int] = mapped_column(ForeignKey_("customer.id"))

class Cart(Base):
    __tablename__ = "cart"
    id: Mapped_[int] = mapped_column(primary_key=True)
    Id: Mapped_[int] = mapped_column(Integer_)
    customer_id: Mapped_[int] = mapped_column(ForeignKey_("customer.id"), unique=True)


#--- Relationships of the order table
Order.contains: Mapped_[List_["OrderItem"]] = relationship("OrderItem", back_populates="order", foreign_keys=[OrderItem.order_id])
Order.paidVia: Mapped_["Payment"] = relationship("Payment", back_populates="order_1", foreign_keys=[Order.paidVia_id])
Order.customer_1: Mapped_["Customer"] = relationship("Customer", back_populates="places", foreign_keys=[Order.customer_1_id])
Order.shipsTo: Mapped_["Address"] = relationship("Address", back_populates="order_2", foreign_keys=[Address.order_2_id])

#--- Relationships of the customer table
Customer.writes: Mapped_[List_["Review"]] = relationship("Review", back_populates="customer_2", foreign_keys=[Review.customer_2_id])
Customer.has: Mapped_[List_["Address"]] = relationship("Address", back_populates="customer_3", foreign_keys=[Address.customer_3_id])
Customer.places: Mapped_[List_["Order"]] = relationship("Order", back_populates="customer_1", foreign_keys=[Order.customer_1_id])
Customer.owns: Mapped_["Cart"] = relationship("Cart", back_populates="customer", foreign_keys=[Cart.customer_id])

#--- Relationships of the track table
Track.album_1: Mapped_["Album"] = relationship("Album", back_populates="contains", foreign_keys=[Track.album_1_id])

#--- Relationships of the artist table
Artist.album: Mapped_["Album"] = relationship("Album", back_populates="createdBy", foreign_keys=[Artist.album_id])

#--- Relationships of the album table
Album.orderitem: Mapped_["OrderItem"] = relationship("OrderItem", back_populates="refersTo", foreign_keys=[Album.orderitem_id])
Album.createdBy: Mapped_[List_["Artist"]] = relationship("Artist", back_populates="album", foreign_keys=[Artist.album_id])
Album.contains: Mapped_[List_["Track"]] = relationship("Track", back_populates="album_1", foreign_keys=[Track.album_1_id])

#--- Relationships of the cartitem table
CartItem.cart: Mapped_["Cart"] = relationship("Cart", back_populates="cartitem", foreign_keys=[CartItem.cart_id])

#--- Relationships of the payment table
Payment.order_1: Mapped_["Order"] = relationship("Order", back_populates="paidVia", foreign_keys=[Order.paidVia_id])

#--- Relationships of the orderitem table
OrderItem.refersTo: Mapped_["Album"] = relationship("Album", back_populates="orderitem", foreign_keys=[Album.orderitem_id])
OrderItem.order: Mapped_["Order"] = relationship("Order", back_populates="contains", foreign_keys=[OrderItem.order_id])

#--- Relationships of the address table
Address.customer_3: Mapped_["Customer"] = relationship("Customer", back_populates="has", foreign_keys=[Address.customer_3_id])
Address.order_2: Mapped_["Order"] = relationship("Order", back_populates="shipsTo", foreign_keys=[Address.order_2_id])

#--- Relationships of the review table
Review.customer_2: Mapped_["Customer"] = relationship("Customer", back_populates="writes", foreign_keys=[Review.customer_2_id])

#--- Relationships of the cart table
Cart.customer: Mapped_["Customer"] = relationship("Customer", back_populates="owns", foreign_keys=[Cart.customer_id])
Cart.cartitem: Mapped_[List_["CartItem"]] = relationship("CartItem", back_populates="cart", foreign_keys=[CartItem.cart_id])

# Database connection
DATABASE_URL = "sqlite:///Library.db"  # SQLite connection
engine = create_engine(DATABASE_URL, echo=True)

# Create tables in the database
Base.metadata.create_all(engine, checkfirst=True)