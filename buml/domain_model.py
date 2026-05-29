####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata, MethodImplementationType
)

# Classes
User = Class(name="User")
Customer = Class(name="Customer")
Admin = Class(name="Admin")
Order = Class(name="Order")
Cart = Class(name="Cart")
Review = Class(name="Review")
Address = Class(name="Address")
OrderItem = Class(name="OrderItem")
Payment = Class(name="Payment")
CartItem = Class(name="CartItem")
Album = Class(name="Album")
Artist = Class(name="Artist")
Track = Class(name="Track")

# User class attributes and methods
User_id: Property = Property(name="id", type=IntegerType)
User_name: Property = Property(name="name", type=StringType)
User_surname: Property = Property(name="surname", type=StringType)
User_createdAt: Property = Property(name="createdAt", type=DateType)
User_m_register: Method = Method(name="register", parameters={}, implementation_type=MethodImplementationType.NONE)
User_m_login: Method = Method(name="login", parameters={}, implementation_type=MethodImplementationType.NONE)
User.attributes={User_createdAt, User_id, User_name, User_surname}
User.methods={User_m_login, User_m_register}

# Customer class attributes and methods
Customer_Id: Property = Property(name="Id", type=StringType)
Customer_m_placeOrder: Method = Method(name="placeOrder", parameters={}, implementation_type=MethodImplementationType.NONE)
Customer_m_addToCart: Method = Method(name="addToCart", parameters={}, type=StringType, implementation_type=MethodImplementationType.NONE)
Customer_m_writeReview: Method = Method(name="writeReview", parameters={}, implementation_type=MethodImplementationType.NONE)
Customer.attributes={Customer_Id}
Customer.methods={Customer_m_addToCart, Customer_m_placeOrder, Customer_m_writeReview}

# Admin class attributes and methods
Admin_role: Property = Property(name="role", type=StringType)
Admin_m_manageProducts: Method = Method(name="manageProducts", parameters={}, implementation_type=MethodImplementationType.NONE)
Admin_m_manageOrders: Method = Method(name="manageOrders", parameters={}, implementation_type=MethodImplementationType.NONE)
Admin.attributes={Admin_role}
Admin.methods={Admin_m_manageOrders, Admin_m_manageProducts}

# Order class attributes and methods
Order_Id: Property = Property(name="Id", type=IntegerType)
Order_status: Property = Property(name="status", type=StringType)
Order_totalAmount: Property = Property(name="totalAmount", type=FloatType)
Order_m_calculateTotal: Method = Method(name="calculateTotal", parameters={}, implementation_type=MethodImplementationType.NONE)
Order_m_updateStatus: Method = Method(name="updateStatus", parameters={}, implementation_type=MethodImplementationType.NONE)
Order_m_generateInvoice: Method = Method(name="generateInvoice", parameters={}, implementation_type=MethodImplementationType.NONE)
Order.attributes={Order_Id, Order_status, Order_totalAmount}
Order.methods={Order_m_calculateTotal, Order_m_generateInvoice, Order_m_updateStatus}

# Cart class attributes and methods
Cart_Id: Property = Property(name="Id", type=IntegerType)
Cart_m_addItem: Method = Method(name="addItem", parameters={}, implementation_type=MethodImplementationType.NONE)
Cart_m_removeItem: Method = Method(name="removeItem", parameters={}, implementation_type=MethodImplementationType.NONE)
Cart_m_clear: Method = Method(name="clear", parameters={}, implementation_type=MethodImplementationType.NONE)
Cart_m_getTotal: Method = Method(name="getTotal", parameters={}, implementation_type=MethodImplementationType.NONE)
Cart.attributes={Cart_Id}
Cart.methods={Cart_m_addItem, Cart_m_clear, Cart_m_getTotal, Cart_m_removeItem}

# Review class attributes and methods
Review_Id: Property = Property(name="Id", type=IntegerType)
Review_rating: Property = Property(name="rating", type=StringType)
Review_comment: Property = Property(name="comment", type=StringType)
Review_m_isVerified: Method = Method(name="isVerified", parameters={}, implementation_type=MethodImplementationType.NONE)
Review.attributes={Review_Id, Review_comment, Review_rating}
Review.methods={Review_m_isVerified}

# Address class attributes and methods
Address_Id: Property = Property(name="Id", type=IntegerType)
Address_street: Property = Property(name="street", type=StringType)
Address_city: Property = Property(name="city", type=FloatType)
Address_zip_code: Property = Property(name="zip_code", type=StringType)
Address_m_validate: Method = Method(name="validate", parameters={}, implementation_type=MethodImplementationType.NONE)
Address.attributes={Address_Id, Address_city, Address_street, Address_zip_code}
Address.methods={Address_m_validate}

# OrderItem class attributes and methods
OrderItem_quantity: Property = Property(name="quantity", type=IntegerType)
OrderItem_unintPrice: Property = Property(name="unintPrice", type=StringType)
OrderItem_m_getSubtotal: Method = Method(name="getSubtotal", parameters={}, implementation_type=MethodImplementationType.NONE)
OrderItem.attributes={OrderItem_quantity, OrderItem_unintPrice}
OrderItem.methods={OrderItem_m_getSubtotal}

# Payment class attributes and methods
Payment_Id: Property = Property(name="Id", type=IntegerType)
Payment_method: Property = Property(name="method", type=StringType)
Payment_amount: Property = Property(name="amount", type=FloatType)
Payment_m_validate: Method = Method(name="validate", parameters={}, implementation_type=MethodImplementationType.NONE)
Payment.attributes={Payment_Id, Payment_amount, Payment_method}
Payment.methods={Payment_m_validate}

# CartItem class attributes and methods
CartItem_quantity: Property = Property(name="quantity", type=IntegerType)
CartItem_unintPrice: Property = Property(name="unintPrice", type=FloatType)
CartItem_m_getSubtotal: Method = Method(name="getSubtotal", parameters={}, implementation_type=MethodImplementationType.NONE)
CartItem.attributes={CartItem_quantity, CartItem_unintPrice}
CartItem.methods={CartItem_m_getSubtotal}

# Album class attributes and methods
Album_Id: Property = Property(name="Id", type=IntegerType)
Album_title: Property = Property(name="title", type=StringType)
Album_artist: Property = Property(name="artist", type=StringType)
Album_releaseYear: Property = Property(name="releaseYear", type=DateType)
Album_price: Property = Property(name="price", type=FloatType)
Album_stockQuantity: Property = Property(name="stockQuantity", type=IntegerType)
Album_format: Property = Property(name="format", type=StringType)
Album_m_isAvailable: Method = Method(name="isAvailable", parameters={}, implementation_type=MethodImplementationType.NONE)
Album_m_updateStock: Method = Method(name="updateStock", parameters={}, implementation_type=MethodImplementationType.NONE)
Album.attributes={Album_Id, Album_artist, Album_format, Album_price, Album_releaseYear, Album_stockQuantity, Album_title}
Album.methods={Album_m_isAvailable, Album_m_updateStock}

# Artist class attributes and methods
Artist_Id: Property = Property(name="Id", type=IntegerType)
Artist_name: Property = Property(name="name", type=StringType)
Artist_bio: Property = Property(name="bio", type=StringType)
Artist_country: Property = Property(name="country", type=StringType)
Artist_m_getDiscography: Method = Method(name="getDiscography", parameters={}, implementation_type=MethodImplementationType.NONE)
Artist.attributes={Artist_Id, Artist_bio, Artist_country, Artist_name}
Artist.methods={Artist_m_getDiscography}

# Track class attributes and methods
Track_Id: Property = Property(name="Id", type=IntegerType)
Track_title: Property = Property(name="title", type=StringType)
Track_duration: Property = Property(name="duration", type=TimeDeltaType)
Track_truckNumber: Property = Property(name="truckNumber", type=IntegerType)
Track_m_getOverallDuration: Method = Method(name="getOverallDuration", parameters={}, implementation_type=MethodImplementationType.NONE)
Track.attributes={Track_Id, Track_duration, Track_title, Track_truckNumber}
Track.methods={Track_m_getOverallDuration}

# Relationships
Customer_Cart: BinaryAssociation = BinaryAssociation(
    name="Customer_Cart",
    ends={
        Property(name="customer", type=Customer, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="owns", type=Cart, multiplicity=Multiplicity(0, 1))
    }
)
places: BinaryAssociation = BinaryAssociation(
    name="places",
    ends={
        Property(name="customer_1", type=Customer, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="places", type=Order, multiplicity=Multiplicity(0, 9999))
    }
)
writes: BinaryAssociation = BinaryAssociation(
    name="writes",
    ends={
        Property(name="customer_2", type=Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="writes", type=Review, multiplicity=Multiplicity(0, 9999))
    }
)
CartItem_Cart: BinaryAssociation = BinaryAssociation(
    name="CartItem_Cart",
    ends={
        Property(name="cartitem", type=CartItem, multiplicity=Multiplicity(0, 9999)),
        Property(name="cart", type=Cart, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
OrderItem_Order: BinaryAssociation = BinaryAssociation(
    name="OrderItem_Order",
    ends={
        Property(name="contains", type=OrderItem, multiplicity=Multiplicity(1, 9999)),
        Property(name="order", type=Order, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Payment_Order: BinaryAssociation = BinaryAssociation(
    name="Payment_Order",
    ends={
        Property(name="paidVia", type=Payment, multiplicity=Multiplicity(1, 1)),
        Property(name="order_1", type=Order, multiplicity=Multiplicity(1, 1))
    }
)
Order_Address: BinaryAssociation = BinaryAssociation(
    name="Order_Address",
    ends={
        Property(name="order_2", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="shipsTo", type=Address, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Address: BinaryAssociation = BinaryAssociation(
    name="Customer_Address",
    ends={
        Property(name="customer_3", type=Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="has", type=Address, multiplicity=Multiplicity(0, 9999))
    }
)
createdBy: BinaryAssociation = BinaryAssociation(
    name="createdBy",
    ends={
        Property(name="album", type=Album, multiplicity=Multiplicity(1, 1)),
        Property(name="createdBy", type=Artist, multiplicity=Multiplicity(1, 9999))
    }
)
contains: BinaryAssociation = BinaryAssociation(
    name="contains",
    ends={
        Property(name="album_1", type=Album, multiplicity=Multiplicity(1, 1)),
        Property(name="contains", type=Track, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
refersTo: BinaryAssociation = BinaryAssociation(
    name="refersTo",
    ends={
        Property(name="orderitem", type=OrderItem, multiplicity=Multiplicity(1, 1)),
        Property(name="refersTo", type=Album, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_Customer_User = Generalization(general=User, specific=Customer)
gen_Admin_User = Generalization(general=User, specific=Admin)

# Domain Model
domain_model = DomainModel(
    name="Library",
    types={User, Customer, Admin, Order, Cart, Review, Address, OrderItem, Payment, CartItem, Album, Artist, Track},
    associations={Customer_Cart, places, writes, CartItem_Cart, OrderItem_Order, Payment_Order, Order_Address, Customer_Address, createdBy, contains, refersTo},
    generalizations={gen_Customer_User, gen_Admin_User},
    metadata=None
)
