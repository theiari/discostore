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


###############
#  GUI MODEL  #
###############

from besser.BUML.metamodel.gui import (
    GUIModel, Module, Screen,
    ViewComponent, ViewContainer,
    Button, ButtonType, ButtonActionType,
    Text, Image, Link, InputField, InputFieldType,
    Form, Menu, MenuItem, DataList,
    DataSource, DataSourceElement, EmbeddedContent,
    Styling, Size, Position, Color, Layout, LayoutType,
    UnitSize, PositionType, Alignment
)
from besser.BUML.metamodel.gui.dashboard import (
    LineChart, BarChart, PieChart, RadarChart, RadialBarChart, Table, AgentComponent,
    Column, FieldColumn, LookupColumn, ExpressionColumn, MetricCard, Series
)
from besser.BUML.metamodel.gui.events_actions import (
    Event, EventType, Transition, Create, Read, Update, Delete, Parameter
)
from besser.BUML.metamodel.gui.binding import DataBinding

# Module: GUI_Module

# Screen: wrapper
wrapper = Screen(name="wrapper", description="User", view_elements=set(), is_main_page=True, route_path="/user", screen_size="Medium")
wrapper.component_id = "page-user-0"
i0oo6 = Text(
    name="i0oo6",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="i0oo6",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "i0oo6"}
)
iruqu = Link(
    name="iruqu",
    description="Link element",
    label="User",
    url="/user",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iruqu",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/user", "id": "iruqu"}
)
iow5i = Link(
    name="iow5i",
    description="Link element",
    label="Customer",
    url="/customer",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iow5i",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/customer", "id": "iow5i"}
)
i91yl = Link(
    name="i91yl",
    description="Link element",
    label="Admin",
    url="/admin",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i91yl",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/admin", "id": "i91yl"}
)
imxgw = Link(
    name="imxgw",
    description="Link element",
    label="Order",
    url="/order",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="imxgw",
    tag_name="a",
    display_order=3,
    custom_attributes={"href": "/order", "id": "imxgw"}
)
iwzfp = Link(
    name="iwzfp",
    description="Link element",
    label="Cart",
    url="/cart",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iwzfp",
    tag_name="a",
    display_order=4,
    custom_attributes={"href": "/cart", "id": "iwzfp"}
)
irui5 = Link(
    name="irui5",
    description="Link element",
    label="Review",
    url="/review",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="irui5",
    tag_name="a",
    display_order=5,
    custom_attributes={"href": "/review", "id": "irui5"}
)
i05l9 = Link(
    name="i05l9",
    description="Link element",
    label="Address",
    url="/address",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i05l9",
    tag_name="a",
    display_order=6,
    custom_attributes={"href": "/address", "id": "i05l9"}
)
ifyzo = Link(
    name="ifyzo",
    description="Link element",
    label="OrderItem",
    url="/orderitem",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ifyzo",
    tag_name="a",
    display_order=7,
    custom_attributes={"href": "/orderitem", "id": "ifyzo"}
)
iad4d = Link(
    name="iad4d",
    description="Link element",
    label="Payment",
    url="/payment",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iad4d",
    tag_name="a",
    display_order=8,
    custom_attributes={"href": "/payment", "id": "iad4d"}
)
ihbg7 = Link(
    name="ihbg7",
    description="Link element",
    label="CartItem",
    url="/cartitem",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ihbg7",
    tag_name="a",
    display_order=9,
    custom_attributes={"href": "/cartitem", "id": "ihbg7"}
)
ihv2k = Link(
    name="ihv2k",
    description="Link element",
    label="Album",
    url="/album",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ihv2k",
    tag_name="a",
    display_order=10,
    custom_attributes={"href": "/album", "id": "ihv2k"}
)
itoxl = Link(
    name="itoxl",
    description="Link element",
    label="Artist",
    url="/artist",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="itoxl",
    tag_name="a",
    display_order=11,
    custom_attributes={"href": "/artist", "id": "itoxl"}
)
ic2c7 = Link(
    name="ic2c7",
    description="Link element",
    label="Track",
    url="/track",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ic2c7",
    tag_name="a",
    display_order=12,
    custom_attributes={"href": "/track", "id": "ic2c7"}
)
i8v6m = ViewContainer(
    name="i8v6m",
    description=" component",
    view_elements={iruqu, iow5i, i91yl, imxgw, iwzfp, irui5, i05l9, ifyzo, iad4d, ihbg7, ihv2k, itoxl, ic2c7},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="i8v6m",
    display_order=1,
    custom_attributes={"id": "i8v6m"}
)
i8v6m_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
i8v6m.layout = i8v6m_layout
ix6gj = Text(
    name="ix6gj",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="ix6gj",
    display_order=2,
    custom_attributes={"id": "ix6gj"}
)
io2qk = ViewContainer(
    name="io2qk",
    description="nav container",
    view_elements={i0oo6, i8v6m, ix6gj},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="io2qk",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "io2qk"}
)
io2qk_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
io2qk.layout = io2qk_layout
iysot = Text(
    name="iysot",
    content="User",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="iysot",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "iysot"}
)
iqeof = Text(
    name="iqeof",
    content="Manage User data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="iqeof",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "iqeof"}
)
table_user_0_col_0 = FieldColumn(label="Id", field=User_id)
table_user_0_col_1 = FieldColumn(label="Name", field=User_name)
table_user_0_col_2 = FieldColumn(label="Surname", field=User_surname)
table_user_0_col_3 = FieldColumn(label="CreatedAt", field=User_createdAt)
table_user_0 = Table(
    name="table_user_0",
    title="User List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_user_0_col_0, table_user_0_col_1, table_user_0_col_2, table_user_0_col_3],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-user-0",
    display_order=2,
    css_classes=["has-data-binding"],
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "User List", "data-source": "class_oho5ergc3_mjikkmod", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'id', 'label': 'Id', 'columnType': 'field', '_expanded': False}, {'field': 'name', 'label': 'Name', 'columnType': 'field', '_expanded': False}, {'field': 'surname', 'label': 'Surname', 'columnType': 'field', '_expanded': False}, {'field': 'createdAt', 'label': 'CreatedAt', 'columnType': 'field', '_expanded': False}], "id": "table-user-0", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_user_0_binding_domain = None
if domain_model_ref is not None:
    table_user_0_binding_domain = domain_model_ref.get_class_by_name("User")
if table_user_0_binding_domain:
    table_user_0_binding = DataBinding(domain_concept=table_user_0_binding_domain, name="UserDataBinding")
else:
    # Domain class 'User' not resolved; data binding skipped.
    table_user_0_binding = None
if table_user_0_binding:
    table_user_0.data_binding = table_user_0_binding
id1ut = Button(
    name="id1ut",
    description="Button component",
    label="register",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=User_m_register,
    instance_source="table-user-0",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="id1ut",
    tag_name="button",
    display_order=0,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "register", "data-action-type": "run-method", "data-method": "f5c26f48-81e4-4528-87f4-67316aa32c2f", "data-instance-source": "table-user-0", "id": "id1ut", "method-class": "User", "endpoint": "/user/{user_id}/methods/register/", "is-instance-method": "true", "instance-source": "table-user-0"}
)
i279d = Button(
    name="i279d",
    description="Button component",
    label="login",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=User_m_login,
    instance_source="table-user-0",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="i279d",
    tag_name="button",
    display_order=1,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "login", "data-action-type": "run-method", "data-method": "373ad14d-2889-4789-bc14-84cac03c2df5", "data-instance-source": "table-user-0", "id": "i279d", "method-class": "User", "endpoint": "/user/{user_id}/methods/login/", "is-instance-method": "true", "instance-source": "table-user-0"}
)
ivnek = ViewContainer(
    name="ivnek",
    description=" component",
    view_elements={id1ut, i279d},
    styling=Styling(size=Size(margin_top="20px"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")),
    component_id="ivnek",
    display_order=3,
    custom_attributes={"id": "ivnek"}
)
ivnek_layout = Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")
ivnek.layout = ivnek_layout
ijeow = ViewContainer(
    name="ijeow",
    description="main container",
    view_elements={iysot, iqeof, table_user_0, ivnek},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="ijeow",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "ijeow"}
)
ijeow_layout = Layout(flex="1")
ijeow.layout = ijeow_layout
i8twp = ViewContainer(
    name="i8twp",
    description=" component",
    view_elements={io2qk, ijeow},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="i8twp",
    display_order=0,
    custom_attributes={"id": "i8twp"}
)
i8twp_layout = Layout(layout_type=LayoutType.FLEX)
i8twp.layout = i8twp_layout
wrapper.view_elements = {i8twp}


# Screen: wrapper_10
wrapper_10 = Screen(name="wrapper_10", description="CartItem", view_elements=set(), route_path="/cartitem", screen_size="Medium")
wrapper_10.component_id = "page-cartitem-9"
isnxfj = Text(
    name="isnxfj",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="isnxfj",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "isnxfj"}
)
i6o5sw = Link(
    name="i6o5sw",
    description="Link element",
    label="User",
    url="/user",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i6o5sw",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/user", "id": "i6o5sw"}
)
il1a8e = Link(
    name="il1a8e",
    description="Link element",
    label="Customer",
    url="/customer",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="il1a8e",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/customer", "id": "il1a8e"}
)
ixjtjg = Link(
    name="ixjtjg",
    description="Link element",
    label="Admin",
    url="/admin",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ixjtjg",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/admin", "id": "ixjtjg"}
)
i4o7we = Link(
    name="i4o7we",
    description="Link element",
    label="Order",
    url="/order",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i4o7we",
    tag_name="a",
    display_order=3,
    custom_attributes={"href": "/order", "id": "i4o7we"}
)
irsxjq = Link(
    name="irsxjq",
    description="Link element",
    label="Cart",
    url="/cart",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="irsxjq",
    tag_name="a",
    display_order=4,
    custom_attributes={"href": "/cart", "id": "irsxjq"}
)
ixnx0w = Link(
    name="ixnx0w",
    description="Link element",
    label="Review",
    url="/review",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ixnx0w",
    tag_name="a",
    display_order=5,
    custom_attributes={"href": "/review", "id": "ixnx0w"}
)
i1h7gr = Link(
    name="i1h7gr",
    description="Link element",
    label="Address",
    url="/address",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i1h7gr",
    tag_name="a",
    display_order=6,
    custom_attributes={"href": "/address", "id": "i1h7gr"}
)
ibppqt = Link(
    name="ibppqt",
    description="Link element",
    label="OrderItem",
    url="/orderitem",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ibppqt",
    tag_name="a",
    display_order=7,
    custom_attributes={"href": "/orderitem", "id": "ibppqt"}
)
it0wgl = Link(
    name="it0wgl",
    description="Link element",
    label="Payment",
    url="/payment",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="it0wgl",
    tag_name="a",
    display_order=8,
    custom_attributes={"href": "/payment", "id": "it0wgl"}
)
i84jka = Link(
    name="i84jka",
    description="Link element",
    label="CartItem",
    url="/cartitem",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i84jka",
    tag_name="a",
    display_order=9,
    custom_attributes={"href": "/cartitem", "id": "i84jka"}
)
iwyq2h = Link(
    name="iwyq2h",
    description="Link element",
    label="Album",
    url="/album",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iwyq2h",
    tag_name="a",
    display_order=10,
    custom_attributes={"href": "/album", "id": "iwyq2h"}
)
i07f2m = Link(
    name="i07f2m",
    description="Link element",
    label="Artist",
    url="/artist",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i07f2m",
    tag_name="a",
    display_order=11,
    custom_attributes={"href": "/artist", "id": "i07f2m"}
)
i1wosi = Link(
    name="i1wosi",
    description="Link element",
    label="Track",
    url="/track",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i1wosi",
    tag_name="a",
    display_order=12,
    custom_attributes={"href": "/track", "id": "i1wosi"}
)
i7yk1s = ViewContainer(
    name="i7yk1s",
    description=" component",
    view_elements={i6o5sw, il1a8e, ixjtjg, i4o7we, irsxjq, ixnx0w, i1h7gr, ibppqt, it0wgl, i84jka, iwyq2h, i07f2m, i1wosi},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="i7yk1s",
    display_order=1,
    custom_attributes={"id": "i7yk1s"}
)
i7yk1s_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
i7yk1s.layout = i7yk1s_layout
iac1z8 = Text(
    name="iac1z8",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="iac1z8",
    display_order=2,
    custom_attributes={"id": "iac1z8"}
)
ii1i6s = ViewContainer(
    name="ii1i6s",
    description="nav container",
    view_elements={isnxfj, i7yk1s, iac1z8},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="ii1i6s",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "ii1i6s"}
)
ii1i6s_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
ii1i6s.layout = ii1i6s_layout
igcy6n = Text(
    name="igcy6n",
    content="CartItem",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="igcy6n",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "igcy6n"}
)
ia6usi = Text(
    name="ia6usi",
    content="Manage CartItem data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="ia6usi",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "ia6usi"}
)
table_cartitem_9_col_0 = FieldColumn(label="Quantity", field=CartItem_quantity)
table_cartitem_9_col_1 = FieldColumn(label="UnintPrice", field=CartItem_unintPrice)
table_cartitem_9 = Table(
    name="table_cartitem_9",
    title="CartItem List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_cartitem_9_col_0, table_cartitem_9_col_1],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-cartitem-9",
    display_order=2,
    css_classes=["has-data-binding"],
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "CartItem List", "data-source": "8581908a-9d9b-4f13-acee-981d568b389e", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'quantity', 'label': 'Quantity', 'columnType': 'field', '_expanded': False}, {'field': 'unintPrice', 'label': 'UnintPrice', 'columnType': 'field', '_expanded': False}, {'field': 'Cart', 'label': 'Cart', 'columnType': 'lookup', 'lookupEntity': '89f3febf-3264-4c26-9b93-cec260faf4c6', 'lookupField': 'Id', '_expanded': False}], "id": "table-cartitem-9", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_cartitem_9_binding_domain = None
if domain_model_ref is not None:
    table_cartitem_9_binding_domain = domain_model_ref.get_class_by_name("CartItem")
if table_cartitem_9_binding_domain:
    table_cartitem_9_binding = DataBinding(domain_concept=table_cartitem_9_binding_domain, name="CartItemDataBinding")
else:
    # Domain class 'CartItem' not resolved; data binding skipped.
    table_cartitem_9_binding = None
if table_cartitem_9_binding:
    table_cartitem_9.data_binding = table_cartitem_9_binding
icja42 = Button(
    name="icja42",
    description="Button component",
    label="+ getSubtotal",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=CartItem_m_getSubtotal,
    instance_source="table-cartitem-9",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="icja42",
    tag_name="button",
    display_order=0,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "+ getSubtotal", "data-action-type": "run-method", "data-method": "fd745f71-7317-48ad-87a2-5333247a8546", "data-instance-source": "table-cartitem-9", "id": "icja42", "method-class": "CartItem", "endpoint": "/cartitem/{cartitem_id}/methods/getSubtotal/", "is-instance-method": "true", "instance-source": "table-cartitem-9"}
)
iaatsm = ViewContainer(
    name="iaatsm",
    description=" component",
    view_elements={icja42},
    styling=Styling(size=Size(margin_top="20px"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")),
    component_id="iaatsm",
    display_order=3,
    custom_attributes={"id": "iaatsm"}
)
iaatsm_layout = Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")
iaatsm.layout = iaatsm_layout
i91vvm = ViewContainer(
    name="i91vvm",
    description="main container",
    view_elements={igcy6n, ia6usi, table_cartitem_9, iaatsm},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="i91vvm",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "i91vvm"}
)
i91vvm_layout = Layout(flex="1")
i91vvm.layout = i91vvm_layout
ioi4wa = ViewContainer(
    name="ioi4wa",
    description=" component",
    view_elements={ii1i6s, i91vvm},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="ioi4wa",
    display_order=0,
    custom_attributes={"id": "ioi4wa"}
)
ioi4wa_layout = Layout(layout_type=LayoutType.FLEX)
ioi4wa.layout = ioi4wa_layout
wrapper_10.view_elements = {ioi4wa}


# Screen: wrapper_11
wrapper_11 = Screen(name="wrapper_11", description="Album", view_elements=set(), route_path="/album", screen_size="Medium")
wrapper_11.component_id = "page-album-10"
ijniak = Text(
    name="ijniak",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="ijniak",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "ijniak"}
)
i4e9ej = Link(
    name="i4e9ej",
    description="Link element",
    label="User",
    url="/user",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i4e9ej",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/user", "id": "i4e9ej"}
)
i83u6u = Link(
    name="i83u6u",
    description="Link element",
    label="Customer",
    url="/customer",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i83u6u",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/customer", "id": "i83u6u"}
)
iv27zj = Link(
    name="iv27zj",
    description="Link element",
    label="Admin",
    url="/admin",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iv27zj",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/admin", "id": "iv27zj"}
)
ib2lkg = Link(
    name="ib2lkg",
    description="Link element",
    label="Order",
    url="/order",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ib2lkg",
    tag_name="a",
    display_order=3,
    custom_attributes={"href": "/order", "id": "ib2lkg"}
)
ii2jek = Link(
    name="ii2jek",
    description="Link element",
    label="Cart",
    url="/cart",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ii2jek",
    tag_name="a",
    display_order=4,
    custom_attributes={"href": "/cart", "id": "ii2jek"}
)
ir8btl = Link(
    name="ir8btl",
    description="Link element",
    label="Review",
    url="/review",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ir8btl",
    tag_name="a",
    display_order=5,
    custom_attributes={"href": "/review", "id": "ir8btl"}
)
iv1u55 = Link(
    name="iv1u55",
    description="Link element",
    label="Address",
    url="/address",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iv1u55",
    tag_name="a",
    display_order=6,
    custom_attributes={"href": "/address", "id": "iv1u55"}
)
idwd8p = Link(
    name="idwd8p",
    description="Link element",
    label="OrderItem",
    url="/orderitem",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="idwd8p",
    tag_name="a",
    display_order=7,
    custom_attributes={"href": "/orderitem", "id": "idwd8p"}
)
ibnl8f = Link(
    name="ibnl8f",
    description="Link element",
    label="Payment",
    url="/payment",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ibnl8f",
    tag_name="a",
    display_order=8,
    custom_attributes={"href": "/payment", "id": "ibnl8f"}
)
im8feh = Link(
    name="im8feh",
    description="Link element",
    label="CartItem",
    url="/cartitem",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="im8feh",
    tag_name="a",
    display_order=9,
    custom_attributes={"href": "/cartitem", "id": "im8feh"}
)
ijpq8f = Link(
    name="ijpq8f",
    description="Link element",
    label="Album",
    url="/album",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ijpq8f",
    tag_name="a",
    display_order=10,
    custom_attributes={"href": "/album", "id": "ijpq8f"}
)
i1756r = Link(
    name="i1756r",
    description="Link element",
    label="Artist",
    url="/artist",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i1756r",
    tag_name="a",
    display_order=11,
    custom_attributes={"href": "/artist", "id": "i1756r"}
)
iryyuk = Link(
    name="iryyuk",
    description="Link element",
    label="Track",
    url="/track",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iryyuk",
    tag_name="a",
    display_order=12,
    custom_attributes={"href": "/track", "id": "iryyuk"}
)
iify4w = ViewContainer(
    name="iify4w",
    description=" component",
    view_elements={i4e9ej, i83u6u, iv27zj, ib2lkg, ii2jek, ir8btl, iv1u55, idwd8p, ibnl8f, im8feh, ijpq8f, i1756r, iryyuk},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="iify4w",
    display_order=1,
    custom_attributes={"id": "iify4w"}
)
iify4w_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
iify4w.layout = iify4w_layout
i18y8h = Text(
    name="i18y8h",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="i18y8h",
    display_order=2,
    custom_attributes={"id": "i18y8h"}
)
iqogjn = ViewContainer(
    name="iqogjn",
    description="nav container",
    view_elements={ijniak, iify4w, i18y8h},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="iqogjn",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "iqogjn"}
)
iqogjn_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
iqogjn.layout = iqogjn_layout
i90p49 = Text(
    name="i90p49",
    content="Album",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="i90p49",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "i90p49"}
)
ippbjq = Text(
    name="ippbjq",
    content="Manage Album data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="ippbjq",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "ippbjq"}
)
table_album_10_col_0 = FieldColumn(label="Id", field=Album_Id)
table_album_10_col_1 = FieldColumn(label="Title", field=Album_title)
table_album_10_col_2 = FieldColumn(label="Artist", field=Album_artist)
table_album_10_col_3 = FieldColumn(label="ReleaseYear", field=Album_releaseYear)
table_album_10_col_4 = FieldColumn(label="Price", field=Album_price)
table_album_10_col_5 = FieldColumn(label="StockQuantity", field=Album_stockQuantity)
table_album_10_col_6 = FieldColumn(label="Format", field=Album_format)
table_album_10_col_7_path = next(end for assoc in domain_model.associations for end in assoc.ends if end.name == "createdBy")
table_album_10_col_7 = LookupColumn(label="CreatedBy", path=table_album_10_col_7_path, field=Artist_Id)
table_album_10_col_8_path = next(end for assoc in domain_model.associations for end in assoc.ends if end.name == "contains")
table_album_10_col_8 = LookupColumn(label="Contains", path=table_album_10_col_8_path, field=Track_Id)
table_album_10 = Table(
    name="table_album_10",
    title="Album List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_album_10_col_0, table_album_10_col_1, table_album_10_col_2, table_album_10_col_3, table_album_10_col_4, table_album_10_col_5, table_album_10_col_6, table_album_10_col_7, table_album_10_col_8],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-album-10",
    display_order=2,
    css_classes=["has-data-binding"],
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Album List", "data-source": "8ced71dd-9fd8-4eb8-8308-dd72e95597c0", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'Id', 'label': 'Id', 'columnType': 'field', '_expanded': False}, {'field': 'title', 'label': 'Title', 'columnType': 'field', '_expanded': False}, {'field': 'artist', 'label': 'Artist', 'columnType': 'field', '_expanded': False}, {'field': 'releaseYear', 'label': 'ReleaseYear', 'columnType': 'field', '_expanded': False}, {'field': 'price', 'label': 'Price', 'columnType': 'field', '_expanded': False}, {'field': 'stockQuantity', 'label': 'StockQuantity', 'columnType': 'field', '_expanded': False}, {'field': 'format', 'label': 'Format', 'columnType': 'field', '_expanded': False}, {'field': 'createdBy', 'label': 'CreatedBy', 'columnType': 'lookup', 'lookupEntity': '17cd967c-a02e-4bdb-8412-d4bd48d4b2a8', 'lookupField': 'Id', '_expanded': False}, {'field': 'contains', 'label': 'Contains', 'columnType': 'lookup', 'lookupEntity': '73cc7b41-4975-41ae-85e0-75445e403e8a', 'lookupField': 'Id', '_expanded': False}, {'field': 'OrderItem', 'label': 'OrderItem', 'columnType': 'lookup', 'lookupEntity': 'c2efb871-77f2-4f8f-a4d9-4402f11e68ee', 'lookupField': 'quantity', '_expanded': False}], "id": "table-album-10", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_album_10_binding_domain = None
if domain_model_ref is not None:
    table_album_10_binding_domain = domain_model_ref.get_class_by_name("Album")
if table_album_10_binding_domain:
    table_album_10_binding = DataBinding(domain_concept=table_album_10_binding_domain, name="AlbumDataBinding")
else:
    # Domain class 'Album' not resolved; data binding skipped.
    table_album_10_binding = None
if table_album_10_binding:
    table_album_10.data_binding = table_album_10_binding
ijjffi = Button(
    name="ijjffi",
    description="Button component",
    label="+ isAvailable",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=Album_m_isAvailable,
    instance_source="table-album-10",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="ijjffi",
    tag_name="button",
    display_order=0,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "+ isAvailable", "data-action-type": "run-method", "data-method": "cd53a502-a6cc-4cdd-acda-7f7ba5a646b2", "data-instance-source": "table-album-10", "id": "ijjffi", "method-class": "Album", "endpoint": "/album/{album_id}/methods/isAvailable/", "is-instance-method": "true", "instance-source": "table-album-10"}
)
i6a1mj = Button(
    name="i6a1mj",
    description="Button component",
    label="updateStock",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=Album_m_updateStock,
    instance_source="table-album-10",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="i6a1mj",
    tag_name="button",
    display_order=1,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "updateStock", "data-action-type": "run-method", "data-method": "e61a9460-b6b6-4045-b137-730a95439071", "data-instance-source": "table-album-10", "id": "i6a1mj", "method-class": "Album", "endpoint": "/album/{album_id}/methods/updateStock/", "is-instance-method": "true", "instance-source": "table-album-10"}
)
ivbw8s = ViewContainer(
    name="ivbw8s",
    description=" component",
    view_elements={ijjffi, i6a1mj},
    styling=Styling(size=Size(margin_top="20px"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")),
    component_id="ivbw8s",
    display_order=3,
    custom_attributes={"id": "ivbw8s"}
)
ivbw8s_layout = Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")
ivbw8s.layout = ivbw8s_layout
ixxlaf = ViewContainer(
    name="ixxlaf",
    description="main container",
    view_elements={i90p49, ippbjq, table_album_10, ivbw8s},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="ixxlaf",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "ixxlaf"}
)
ixxlaf_layout = Layout(flex="1")
ixxlaf.layout = ixxlaf_layout
i0ha4a = ViewContainer(
    name="i0ha4a",
    description=" component",
    view_elements={iqogjn, ixxlaf},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="i0ha4a",
    display_order=0,
    custom_attributes={"id": "i0ha4a"}
)
i0ha4a_layout = Layout(layout_type=LayoutType.FLEX)
i0ha4a.layout = i0ha4a_layout
wrapper_11.view_elements = {i0ha4a}


# Screen: wrapper_12
wrapper_12 = Screen(name="wrapper_12", description="Artist", view_elements=set(), route_path="/artist", screen_size="Medium")
wrapper_12.component_id = "page-artist-11"
iyj3wj = Text(
    name="iyj3wj",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="iyj3wj",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "iyj3wj"}
)
iktci2 = Link(
    name="iktci2",
    description="Link element",
    label="User",
    url="/user",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iktci2",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/user", "id": "iktci2"}
)
ixfktv = Link(
    name="ixfktv",
    description="Link element",
    label="Customer",
    url="/customer",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ixfktv",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/customer", "id": "ixfktv"}
)
i6xwhp = Link(
    name="i6xwhp",
    description="Link element",
    label="Admin",
    url="/admin",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i6xwhp",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/admin", "id": "i6xwhp"}
)
ijtq1o = Link(
    name="ijtq1o",
    description="Link element",
    label="Order",
    url="/order",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ijtq1o",
    tag_name="a",
    display_order=3,
    custom_attributes={"href": "/order", "id": "ijtq1o"}
)
iop7bl = Link(
    name="iop7bl",
    description="Link element",
    label="Cart",
    url="/cart",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iop7bl",
    tag_name="a",
    display_order=4,
    custom_attributes={"href": "/cart", "id": "iop7bl"}
)
iqip06 = Link(
    name="iqip06",
    description="Link element",
    label="Review",
    url="/review",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iqip06",
    tag_name="a",
    display_order=5,
    custom_attributes={"href": "/review", "id": "iqip06"}
)
irwclk = Link(
    name="irwclk",
    description="Link element",
    label="Address",
    url="/address",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="irwclk",
    tag_name="a",
    display_order=6,
    custom_attributes={"href": "/address", "id": "irwclk"}
)
iy0nzh = Link(
    name="iy0nzh",
    description="Link element",
    label="OrderItem",
    url="/orderitem",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iy0nzh",
    tag_name="a",
    display_order=7,
    custom_attributes={"href": "/orderitem", "id": "iy0nzh"}
)
ilpsuj = Link(
    name="ilpsuj",
    description="Link element",
    label="Payment",
    url="/payment",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ilpsuj",
    tag_name="a",
    display_order=8,
    custom_attributes={"href": "/payment", "id": "ilpsuj"}
)
iq80i4 = Link(
    name="iq80i4",
    description="Link element",
    label="CartItem",
    url="/cartitem",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iq80i4",
    tag_name="a",
    display_order=9,
    custom_attributes={"href": "/cartitem", "id": "iq80i4"}
)
iu3jef = Link(
    name="iu3jef",
    description="Link element",
    label="Album",
    url="/album",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iu3jef",
    tag_name="a",
    display_order=10,
    custom_attributes={"href": "/album", "id": "iu3jef"}
)
is0rie = Link(
    name="is0rie",
    description="Link element",
    label="Artist",
    url="/artist",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="is0rie",
    tag_name="a",
    display_order=11,
    custom_attributes={"href": "/artist", "id": "is0rie"}
)
it8god = Link(
    name="it8god",
    description="Link element",
    label="Track",
    url="/track",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="it8god",
    tag_name="a",
    display_order=12,
    custom_attributes={"href": "/track", "id": "it8god"}
)
i4nj2u = ViewContainer(
    name="i4nj2u",
    description=" component",
    view_elements={iktci2, ixfktv, i6xwhp, ijtq1o, iop7bl, iqip06, irwclk, iy0nzh, ilpsuj, iq80i4, iu3jef, is0rie, it8god},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="i4nj2u",
    display_order=1,
    custom_attributes={"id": "i4nj2u"}
)
i4nj2u_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
i4nj2u.layout = i4nj2u_layout
iia1zi = Text(
    name="iia1zi",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="iia1zi",
    display_order=2,
    custom_attributes={"id": "iia1zi"}
)
ijb25b = ViewContainer(
    name="ijb25b",
    description="nav container",
    view_elements={iyj3wj, i4nj2u, iia1zi},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="ijb25b",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "ijb25b"}
)
ijb25b_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
ijb25b.layout = ijb25b_layout
ixjgzi = Text(
    name="ixjgzi",
    content="Artist",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="ixjgzi",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "ixjgzi"}
)
ig7p6r = Text(
    name="ig7p6r",
    content="Manage Artist data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="ig7p6r",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "ig7p6r"}
)
table_artist_11_col_0 = FieldColumn(label="Id", field=Artist_Id)
table_artist_11_col_1 = FieldColumn(label="Name", field=Artist_name)
table_artist_11_col_2 = FieldColumn(label="Bio", field=Artist_bio)
table_artist_11_col_3 = FieldColumn(label="Country", field=Artist_country)
table_artist_11 = Table(
    name="table_artist_11",
    title="Artist List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_artist_11_col_0, table_artist_11_col_1, table_artist_11_col_2, table_artist_11_col_3],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-artist-11",
    display_order=2,
    css_classes=["has-data-binding"],
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Artist List", "data-source": "17cd967c-a02e-4bdb-8412-d4bd48d4b2a8", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'Id', 'label': 'Id', 'columnType': 'field', '_expanded': False}, {'field': 'name', 'label': 'Name', 'columnType': 'field', '_expanded': False}, {'field': 'bio', 'label': 'Bio', 'columnType': 'field', '_expanded': False}, {'field': 'country', 'label': 'Country', 'columnType': 'field', '_expanded': False}, {'field': 'Album', 'label': 'Album', 'columnType': 'lookup', 'lookupEntity': '8ced71dd-9fd8-4eb8-8308-dd72e95597c0', 'lookupField': 'Id', '_expanded': False}], "id": "table-artist-11", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_artist_11_binding_domain = None
if domain_model_ref is not None:
    table_artist_11_binding_domain = domain_model_ref.get_class_by_name("Artist")
if table_artist_11_binding_domain:
    table_artist_11_binding = DataBinding(domain_concept=table_artist_11_binding_domain, name="ArtistDataBinding")
else:
    # Domain class 'Artist' not resolved; data binding skipped.
    table_artist_11_binding = None
if table_artist_11_binding:
    table_artist_11.data_binding = table_artist_11_binding
i88hec = Button(
    name="i88hec",
    description="Button component",
    label="+ getDiscography",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=Artist_m_getDiscography,
    instance_source="table-artist-11",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="i88hec",
    tag_name="button",
    display_order=0,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "+ getDiscography", "data-action-type": "run-method", "data-method": "8bfc9e03-2a64-48ac-82cb-7264f615066e", "data-instance-source": "table-artist-11", "id": "i88hec", "method-class": "Artist", "endpoint": "/artist/{artist_id}/methods/getDiscography/", "is-instance-method": "true", "instance-source": "table-artist-11"}
)
ismdoa = ViewContainer(
    name="ismdoa",
    description=" component",
    view_elements={i88hec},
    styling=Styling(size=Size(margin_top="20px"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")),
    component_id="ismdoa",
    display_order=3,
    custom_attributes={"id": "ismdoa"}
)
ismdoa_layout = Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")
ismdoa.layout = ismdoa_layout
itto0y = ViewContainer(
    name="itto0y",
    description="main container",
    view_elements={ixjgzi, ig7p6r, table_artist_11, ismdoa},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="itto0y",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "itto0y"}
)
itto0y_layout = Layout(flex="1")
itto0y.layout = itto0y_layout
igm12v = ViewContainer(
    name="igm12v",
    description=" component",
    view_elements={ijb25b, itto0y},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="igm12v",
    display_order=0,
    custom_attributes={"id": "igm12v"}
)
igm12v_layout = Layout(layout_type=LayoutType.FLEX)
igm12v.layout = igm12v_layout
wrapper_12.view_elements = {igm12v}


# Screen: wrapper_13
wrapper_13 = Screen(name="wrapper_13", description="Track", view_elements=set(), route_path="/track", screen_size="Medium")
wrapper_13.component_id = "page-track-12"
imyuke = Text(
    name="imyuke",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="imyuke",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "imyuke"}
)
iw88g7 = Link(
    name="iw88g7",
    description="Link element",
    label="User",
    url="/user",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iw88g7",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/user", "id": "iw88g7"}
)
i4gif7 = Link(
    name="i4gif7",
    description="Link element",
    label="Customer",
    url="/customer",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i4gif7",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/customer", "id": "i4gif7"}
)
iumtpg = Link(
    name="iumtpg",
    description="Link element",
    label="Admin",
    url="/admin",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iumtpg",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/admin", "id": "iumtpg"}
)
i5qf8p = Link(
    name="i5qf8p",
    description="Link element",
    label="Order",
    url="/order",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i5qf8p",
    tag_name="a",
    display_order=3,
    custom_attributes={"href": "/order", "id": "i5qf8p"}
)
isnfjf = Link(
    name="isnfjf",
    description="Link element",
    label="Cart",
    url="/cart",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="isnfjf",
    tag_name="a",
    display_order=4,
    custom_attributes={"href": "/cart", "id": "isnfjf"}
)
ix6snj = Link(
    name="ix6snj",
    description="Link element",
    label="Review",
    url="/review",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ix6snj",
    tag_name="a",
    display_order=5,
    custom_attributes={"href": "/review", "id": "ix6snj"}
)
ipzubz = Link(
    name="ipzubz",
    description="Link element",
    label="Address",
    url="/address",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ipzubz",
    tag_name="a",
    display_order=6,
    custom_attributes={"href": "/address", "id": "ipzubz"}
)
iyoeuh = Link(
    name="iyoeuh",
    description="Link element",
    label="OrderItem",
    url="/orderitem",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iyoeuh",
    tag_name="a",
    display_order=7,
    custom_attributes={"href": "/orderitem", "id": "iyoeuh"}
)
i7ux5q = Link(
    name="i7ux5q",
    description="Link element",
    label="Payment",
    url="/payment",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i7ux5q",
    tag_name="a",
    display_order=8,
    custom_attributes={"href": "/payment", "id": "i7ux5q"}
)
iqasqb = Link(
    name="iqasqb",
    description="Link element",
    label="CartItem",
    url="/cartitem",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iqasqb",
    tag_name="a",
    display_order=9,
    custom_attributes={"href": "/cartitem", "id": "iqasqb"}
)
iag24a = Link(
    name="iag24a",
    description="Link element",
    label="Album",
    url="/album",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iag24a",
    tag_name="a",
    display_order=10,
    custom_attributes={"href": "/album", "id": "iag24a"}
)
i52ww5 = Link(
    name="i52ww5",
    description="Link element",
    label="Artist",
    url="/artist",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i52ww5",
    tag_name="a",
    display_order=11,
    custom_attributes={"href": "/artist", "id": "i52ww5"}
)
i1u9hy = Link(
    name="i1u9hy",
    description="Link element",
    label="Track",
    url="/track",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i1u9hy",
    tag_name="a",
    display_order=12,
    custom_attributes={"href": "/track", "id": "i1u9hy"}
)
i0ie7w = ViewContainer(
    name="i0ie7w",
    description=" component",
    view_elements={iw88g7, i4gif7, iumtpg, i5qf8p, isnfjf, ix6snj, ipzubz, iyoeuh, i7ux5q, iqasqb, iag24a, i52ww5, i1u9hy},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="i0ie7w",
    display_order=1,
    custom_attributes={"id": "i0ie7w"}
)
i0ie7w_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
i0ie7w.layout = i0ie7w_layout
iai105 = Text(
    name="iai105",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="iai105",
    display_order=2,
    custom_attributes={"id": "iai105"}
)
iodmpl = ViewContainer(
    name="iodmpl",
    description="nav container",
    view_elements={imyuke, i0ie7w, iai105},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="iodmpl",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "iodmpl"}
)
iodmpl_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
iodmpl.layout = iodmpl_layout
iifekk = Text(
    name="iifekk",
    content="Track",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="iifekk",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "iifekk"}
)
i64rzh = Text(
    name="i64rzh",
    content="Manage Track data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="i64rzh",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "i64rzh"}
)
table_track_12_col_0 = FieldColumn(label="Id", field=Track_Id)
table_track_12_col_1 = FieldColumn(label="Title", field=Track_title)
table_track_12_col_2 = FieldColumn(label="Duration", field=Track_duration)
table_track_12_col_3 = FieldColumn(label="TruckNumber", field=Track_truckNumber)
table_track_12 = Table(
    name="table_track_12",
    title="Track List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_track_12_col_0, table_track_12_col_1, table_track_12_col_2, table_track_12_col_3],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-track-12",
    display_order=2,
    css_classes=["has-data-binding"],
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Track List", "data-source": "73cc7b41-4975-41ae-85e0-75445e403e8a", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'Id', 'label': 'Id', 'columnType': 'field', '_expanded': False}, {'field': 'title', 'label': 'Title', 'columnType': 'field', '_expanded': False}, {'field': 'duration', 'label': 'Duration', 'columnType': 'field', '_expanded': False}, {'field': 'truckNumber', 'label': 'TruckNumber', 'columnType': 'field', '_expanded': False}, {'field': 'Album', 'label': 'Album', 'columnType': 'lookup', 'lookupEntity': '8ced71dd-9fd8-4eb8-8308-dd72e95597c0', 'lookupField': 'Id', '_expanded': False}], "id": "table-track-12", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_track_12_binding_domain = None
if domain_model_ref is not None:
    table_track_12_binding_domain = domain_model_ref.get_class_by_name("Track")
if table_track_12_binding_domain:
    table_track_12_binding = DataBinding(domain_concept=table_track_12_binding_domain, name="TrackDataBinding")
else:
    # Domain class 'Track' not resolved; data binding skipped.
    table_track_12_binding = None
if table_track_12_binding:
    table_track_12.data_binding = table_track_12_binding
izwidt = Button(
    name="izwidt",
    description="Button component",
    label="+ getOverallDuration",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=Track_m_getOverallDuration,
    instance_source="table-track-12",
    is_instance_method=True,
    confirmation_message="Are you sure?",
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="izwidt",
    tag_name="button",
    display_order=0,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "+ getOverallDuration", "data-action-type": "run-method", "data-method": "d74bc694-5252-47d2-9ee4-ea61f9993030", "data-instance-source": "table-track-12", "id": "izwidt", "data-confirmation": "false", "data-confirmation-message": "Are you sure?", "button-label": "+ getOverallDuration", "method-name": "getOverallDuration", "method-class": "Track", "endpoint": "/track/{track_id}/methods/getOverallDuration/", "is-instance-method": "true", "instance-source": "table-track-12"}
)
i1qwlh = ViewContainer(
    name="i1qwlh",
    description=" component",
    view_elements={izwidt},
    styling=Styling(size=Size(margin_top="20px"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")),
    component_id="i1qwlh",
    display_order=3,
    custom_attributes={"id": "i1qwlh"}
)
i1qwlh_layout = Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")
i1qwlh.layout = i1qwlh_layout
iirkws = ViewContainer(
    name="iirkws",
    description="main container",
    view_elements={iifekk, i64rzh, table_track_12, i1qwlh},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="iirkws",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "iirkws"}
)
iirkws_layout = Layout(flex="1")
iirkws.layout = iirkws_layout
iyfdrz = ViewContainer(
    name="iyfdrz",
    description=" component",
    view_elements={iodmpl, iirkws},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="iyfdrz",
    display_order=0,
    custom_attributes={"id": "iyfdrz"}
)
iyfdrz_layout = Layout(layout_type=LayoutType.FLEX)
iyfdrz.layout = iyfdrz_layout
wrapper_13.view_elements = {iyfdrz}


# Screen: wrapper_2
wrapper_2 = Screen(name="wrapper_2", description="Customer", view_elements=set(), route_path="/customer", screen_size="Medium")
wrapper_2.component_id = "page-customer-1"
i395s = Text(
    name="i395s",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="i395s",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "i395s"}
)
isu1h = Link(
    name="isu1h",
    description="Link element",
    label="User",
    url="/user",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="isu1h",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/user", "id": "isu1h"}
)
if61u = Link(
    name="if61u",
    description="Link element",
    label="Customer",
    url="/customer",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="if61u",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/customer", "id": "if61u"}
)
i3xpy = Link(
    name="i3xpy",
    description="Link element",
    label="Admin",
    url="/admin",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i3xpy",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/admin", "id": "i3xpy"}
)
ie546x = Link(
    name="ie546x",
    description="Link element",
    label="Order",
    url="/order",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ie546x",
    tag_name="a",
    display_order=3,
    custom_attributes={"href": "/order", "id": "ie546x"}
)
icdzys = Link(
    name="icdzys",
    description="Link element",
    label="Cart",
    url="/cart",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="icdzys",
    tag_name="a",
    display_order=4,
    custom_attributes={"href": "/cart", "id": "icdzys"}
)
i3fmxb = Link(
    name="i3fmxb",
    description="Link element",
    label="Review",
    url="/review",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i3fmxb",
    tag_name="a",
    display_order=5,
    custom_attributes={"href": "/review", "id": "i3fmxb"}
)
ifno7s = Link(
    name="ifno7s",
    description="Link element",
    label="Address",
    url="/address",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ifno7s",
    tag_name="a",
    display_order=6,
    custom_attributes={"href": "/address", "id": "ifno7s"}
)
ifknpi = Link(
    name="ifknpi",
    description="Link element",
    label="OrderItem",
    url="/orderitem",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ifknpi",
    tag_name="a",
    display_order=7,
    custom_attributes={"href": "/orderitem", "id": "ifknpi"}
)
i5a2bk = Link(
    name="i5a2bk",
    description="Link element",
    label="Payment",
    url="/payment",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i5a2bk",
    tag_name="a",
    display_order=8,
    custom_attributes={"href": "/payment", "id": "i5a2bk"}
)
i1ie6h = Link(
    name="i1ie6h",
    description="Link element",
    label="CartItem",
    url="/cartitem",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i1ie6h",
    tag_name="a",
    display_order=9,
    custom_attributes={"href": "/cartitem", "id": "i1ie6h"}
)
ieamvp = Link(
    name="ieamvp",
    description="Link element",
    label="Album",
    url="/album",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ieamvp",
    tag_name="a",
    display_order=10,
    custom_attributes={"href": "/album", "id": "ieamvp"}
)
iyr9n7 = Link(
    name="iyr9n7",
    description="Link element",
    label="Artist",
    url="/artist",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iyr9n7",
    tag_name="a",
    display_order=11,
    custom_attributes={"href": "/artist", "id": "iyr9n7"}
)
ilux57 = Link(
    name="ilux57",
    description="Link element",
    label="Track",
    url="/track",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ilux57",
    tag_name="a",
    display_order=12,
    custom_attributes={"href": "/track", "id": "ilux57"}
)
iee39 = ViewContainer(
    name="iee39",
    description=" component",
    view_elements={isu1h, if61u, i3xpy, ie546x, icdzys, i3fmxb, ifno7s, ifknpi, i5a2bk, i1ie6h, ieamvp, iyr9n7, ilux57},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="iee39",
    display_order=1,
    custom_attributes={"id": "iee39"}
)
iee39_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
iee39.layout = iee39_layout
i3xyhi = Text(
    name="i3xyhi",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="i3xyhi",
    display_order=2,
    custom_attributes={"id": "i3xyhi"}
)
i27au = ViewContainer(
    name="i27au",
    description="nav container",
    view_elements={i395s, iee39, i3xyhi},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="i27au",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "i27au"}
)
i27au_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
i27au.layout = i27au_layout
is6nrm = Text(
    name="is6nrm",
    content="Customer",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="is6nrm",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "is6nrm"}
)
iiaeq2 = Text(
    name="iiaeq2",
    content="Manage Customer data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="iiaeq2",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "iiaeq2"}
)
table_customer_1_col_0 = FieldColumn(label="Id", field=Customer_Id)
table_customer_1_col_1 = FieldColumn(label="Id", field=Customer_id)
table_customer_1_col_2 = FieldColumn(label="Name", field=Customer_name)
table_customer_1_col_3 = FieldColumn(label="Surname", field=Customer_surname)
table_customer_1_col_4 = FieldColumn(label="CreatedAt", field=Customer_createdAt)
table_customer_1_col_5_path = next(end for assoc in domain_model.associations for end in assoc.ends if end.name == "owns")
table_customer_1_col_5 = LookupColumn(label="Owns", path=table_customer_1_col_5_path, field=Cart_Id)
table_customer_1_col_6_path = next(end for assoc in domain_model.associations for end in assoc.ends if end.name == "places")
table_customer_1_col_6 = LookupColumn(label="Places", path=table_customer_1_col_6_path, field=Order_Id)
table_customer_1_col_7_path = next(end for assoc in domain_model.associations for end in assoc.ends if end.name == "writes")
table_customer_1_col_7 = LookupColumn(label="Writes", path=table_customer_1_col_7_path, field=Review_Id)
table_customer_1_col_8_path = next(end for assoc in domain_model.associations for end in assoc.ends if end.name == "has")
table_customer_1_col_8 = LookupColumn(label="Has", path=table_customer_1_col_8_path, field=Address_Id)
table_customer_1 = Table(
    name="table_customer_1",
    title="Customer List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_customer_1_col_0, table_customer_1_col_1, table_customer_1_col_2, table_customer_1_col_3, table_customer_1_col_4, table_customer_1_col_5, table_customer_1_col_6, table_customer_1_col_7, table_customer_1_col_8],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-customer-1",
    display_order=2,
    css_classes=["has-data-binding"],
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Customer List", "data-source": "class_06blhjj3h_mjikkmod", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'Id', 'label': 'Id', 'columnType': 'field', '_expanded': False}, {'field': 'id', 'label': 'Id', 'columnType': 'field', '_expanded': False}, {'field': 'name', 'label': 'Name', 'columnType': 'field', '_expanded': False}, {'field': 'surname', 'label': 'Surname', 'columnType': 'field', '_expanded': False}, {'field': 'createdAt', 'label': 'CreatedAt', 'columnType': 'field', '_expanded': False}, {'field': 'owns', 'label': 'Owns', 'columnType': 'lookup', 'lookupEntity': '89f3febf-3264-4c26-9b93-cec260faf4c6', 'lookupField': 'Id', '_expanded': False}, {'field': 'places', 'label': 'Places', 'columnType': 'lookup', 'lookupEntity': 'ddb8e355-2f38-44ae-b1fe-ad4b089643ef', 'lookupField': 'Id', '_expanded': False}, {'field': 'writes', 'label': 'Writes', 'columnType': 'lookup', 'lookupEntity': 'a197039c-66f1-43b2-8407-48476b434c9f', 'lookupField': 'Id', '_expanded': False}, {'field': 'has', 'label': 'Has', 'columnType': 'lookup', 'lookupEntity': 'f5c614e2-8480-4d43-9921-4d64b23cc339', 'lookupField': 'Id', '_expanded': False}], "id": "table-customer-1", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_customer_1_binding_domain = None
if domain_model_ref is not None:
    table_customer_1_binding_domain = domain_model_ref.get_class_by_name("Customer")
if table_customer_1_binding_domain:
    table_customer_1_binding = DataBinding(domain_concept=table_customer_1_binding_domain, name="CustomerDataBinding")
else:
    # Domain class 'Customer' not resolved; data binding skipped.
    table_customer_1_binding = None
if table_customer_1_binding:
    table_customer_1.data_binding = table_customer_1_binding
i3u89a = Button(
    name="i3u89a",
    description="Button component",
    label="placeOrder",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=Customer_m_placeOrder,
    instance_source="table-customer-1",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="i3u89a",
    tag_name="button",
    display_order=0,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "placeOrder", "data-action-type": "run-method", "data-method": "7cdf2141-5269-489f-9e5c-1a170229ec72", "data-instance-source": "table-customer-1", "id": "i3u89a", "method-class": "Customer", "endpoint": "/customer/{customer_id}/methods/placeOrder/", "is-instance-method": "true", "instance-source": "table-customer-1"}
)
ixdotf = Button(
    name="ixdotf",
    description="Button component",
    label="+ addToCart",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=Customer_m_addToCart,
    instance_source="table-customer-1",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="ixdotf",
    tag_name="button",
    display_order=1,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "+ addToCart", "data-action-type": "run-method", "data-method": "b71b4137-14d0-4a9c-ad27-ce8a21de185c", "data-instance-source": "table-customer-1", "id": "ixdotf", "method-class": "Customer", "endpoint": "/customer/{customer_id}/methods/addToCart/", "is-instance-method": "true", "instance-source": "table-customer-1"}
)
iihr0u = Button(
    name="iihr0u",
    description="Button component",
    label="writeReview",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=Customer_m_writeReview,
    instance_source="table-customer-1",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="iihr0u",
    tag_name="button",
    display_order=2,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "writeReview", "data-action-type": "run-method", "data-method": "5c5a9806-7d79-4c9d-8f6e-65a8b0680a62", "data-instance-source": "table-customer-1", "id": "iihr0u", "method-class": "Customer", "endpoint": "/customer/{customer_id}/methods/writeReview/", "is-instance-method": "true", "instance-source": "table-customer-1"}
)
ikxc61 = ViewContainer(
    name="ikxc61",
    description=" component",
    view_elements={i3u89a, ixdotf, iihr0u},
    styling=Styling(size=Size(margin_top="20px"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")),
    component_id="ikxc61",
    display_order=3,
    custom_attributes={"id": "ikxc61"}
)
ikxc61_layout = Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")
ikxc61.layout = ikxc61_layout
i2qqag = ViewContainer(
    name="i2qqag",
    description="main container",
    view_elements={is6nrm, iiaeq2, table_customer_1, ikxc61},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="i2qqag",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "i2qqag"}
)
i2qqag_layout = Layout(flex="1")
i2qqag.layout = i2qqag_layout
i8ruv = ViewContainer(
    name="i8ruv",
    description=" component",
    view_elements={i27au, i2qqag},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="i8ruv",
    display_order=0,
    custom_attributes={"id": "i8ruv"}
)
i8ruv_layout = Layout(layout_type=LayoutType.FLEX)
i8ruv.layout = i8ruv_layout
wrapper_2.view_elements = {i8ruv}


# Screen: wrapper_3
wrapper_3 = Screen(name="wrapper_3", description="Admin", view_elements=set(), route_path="/admin", screen_size="Medium")
wrapper_3.component_id = "page-admin-2"
iu9rgn = Text(
    name="iu9rgn",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="iu9rgn",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "iu9rgn"}
)
im9fii = Link(
    name="im9fii",
    description="Link element",
    label="User",
    url="/user",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="im9fii",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/user", "id": "im9fii"}
)
ilozhs = Link(
    name="ilozhs",
    description="Link element",
    label="Customer",
    url="/customer",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ilozhs",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/customer", "id": "ilozhs"}
)
idz3zr = Link(
    name="idz3zr",
    description="Link element",
    label="Admin",
    url="/admin",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="idz3zr",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/admin", "id": "idz3zr"}
)
iih60i = Link(
    name="iih60i",
    description="Link element",
    label="Order",
    url="/order",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iih60i",
    tag_name="a",
    display_order=3,
    custom_attributes={"href": "/order", "id": "iih60i"}
)
irgg45 = Link(
    name="irgg45",
    description="Link element",
    label="Cart",
    url="/cart",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="irgg45",
    tag_name="a",
    display_order=4,
    custom_attributes={"href": "/cart", "id": "irgg45"}
)
iaeka9 = Link(
    name="iaeka9",
    description="Link element",
    label="Review",
    url="/review",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iaeka9",
    tag_name="a",
    display_order=5,
    custom_attributes={"href": "/review", "id": "iaeka9"}
)
imz7th = Link(
    name="imz7th",
    description="Link element",
    label="Address",
    url="/address",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="imz7th",
    tag_name="a",
    display_order=6,
    custom_attributes={"href": "/address", "id": "imz7th"}
)
i8nmgy = Link(
    name="i8nmgy",
    description="Link element",
    label="OrderItem",
    url="/orderitem",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i8nmgy",
    tag_name="a",
    display_order=7,
    custom_attributes={"href": "/orderitem", "id": "i8nmgy"}
)
izeslv = Link(
    name="izeslv",
    description="Link element",
    label="Payment",
    url="/payment",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="izeslv",
    tag_name="a",
    display_order=8,
    custom_attributes={"href": "/payment", "id": "izeslv"}
)
iqrc0j = Link(
    name="iqrc0j",
    description="Link element",
    label="CartItem",
    url="/cartitem",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iqrc0j",
    tag_name="a",
    display_order=9,
    custom_attributes={"href": "/cartitem", "id": "iqrc0j"}
)
i37a35 = Link(
    name="i37a35",
    description="Link element",
    label="Album",
    url="/album",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i37a35",
    tag_name="a",
    display_order=10,
    custom_attributes={"href": "/album", "id": "i37a35"}
)
is1o5z = Link(
    name="is1o5z",
    description="Link element",
    label="Artist",
    url="/artist",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="is1o5z",
    tag_name="a",
    display_order=11,
    custom_attributes={"href": "/artist", "id": "is1o5z"}
)
i9jpsm = Link(
    name="i9jpsm",
    description="Link element",
    label="Track",
    url="/track",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i9jpsm",
    tag_name="a",
    display_order=12,
    custom_attributes={"href": "/track", "id": "i9jpsm"}
)
idvsh1 = ViewContainer(
    name="idvsh1",
    description=" component",
    view_elements={im9fii, ilozhs, idz3zr, iih60i, irgg45, iaeka9, imz7th, i8nmgy, izeslv, iqrc0j, i37a35, is1o5z, i9jpsm},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="idvsh1",
    display_order=1,
    custom_attributes={"id": "idvsh1"}
)
idvsh1_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
idvsh1.layout = idvsh1_layout
irks67 = Text(
    name="irks67",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="irks67",
    display_order=2,
    custom_attributes={"id": "irks67"}
)
i1m5j9 = ViewContainer(
    name="i1m5j9",
    description="nav container",
    view_elements={iu9rgn, idvsh1, irks67},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="i1m5j9",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "i1m5j9"}
)
i1m5j9_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
i1m5j9.layout = i1m5j9_layout
i42nal = Text(
    name="i42nal",
    content="Admin",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="i42nal",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "i42nal"}
)
iql1mj = Text(
    name="iql1mj",
    content="Manage Admin data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="iql1mj",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "iql1mj"}
)
table_admin_2_col_0 = FieldColumn(label="Role", field=Admin_role)
table_admin_2_col_1 = FieldColumn(label="Id", field=Admin_id)
table_admin_2_col_2 = FieldColumn(label="Name", field=Admin_name)
table_admin_2_col_3 = FieldColumn(label="Surname", field=Admin_surname)
table_admin_2_col_4 = FieldColumn(label="CreatedAt", field=Admin_createdAt)
table_admin_2 = Table(
    name="table_admin_2",
    title="Admin List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_admin_2_col_0, table_admin_2_col_1, table_admin_2_col_2, table_admin_2_col_3, table_admin_2_col_4],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-admin-2",
    display_order=2,
    css_classes=["has-data-binding"],
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Admin List", "data-source": "class_d3f0di6lb_mjikkmoe", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'role', 'label': 'Role', 'columnType': 'field', '_expanded': False}, {'field': 'id', 'label': 'Id', 'columnType': 'field', '_expanded': False}, {'field': 'name', 'label': 'Name', 'columnType': 'field', '_expanded': False}, {'field': 'surname', 'label': 'Surname', 'columnType': 'field', '_expanded': False}, {'field': 'createdAt', 'label': 'CreatedAt', 'columnType': 'field', '_expanded': False}], "id": "table-admin-2", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_admin_2_binding_domain = None
if domain_model_ref is not None:
    table_admin_2_binding_domain = domain_model_ref.get_class_by_name("Admin")
if table_admin_2_binding_domain:
    table_admin_2_binding = DataBinding(domain_concept=table_admin_2_binding_domain, name="AdminDataBinding")
else:
    # Domain class 'Admin' not resolved; data binding skipped.
    table_admin_2_binding = None
if table_admin_2_binding:
    table_admin_2.data_binding = table_admin_2_binding
i826xh = Button(
    name="i826xh",
    description="Button component",
    label="manageProducts",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=Admin_m_manageProducts,
    instance_source="table-admin-2",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="i826xh",
    tag_name="button",
    display_order=0,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "manageProducts", "data-action-type": "run-method", "data-method": "909446e1-da4c-4a43-983c-b777280ccb9c", "data-instance-source": "table-admin-2", "id": "i826xh", "method-class": "Admin", "endpoint": "/admin/{admin_id}/methods/manageProducts/", "is-instance-method": "true", "instance-source": "table-admin-2"}
)
ifnd5a = Button(
    name="ifnd5a",
    description="Button component",
    label="manageOrders",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=Admin_m_manageOrders,
    instance_source="table-admin-2",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="ifnd5a",
    tag_name="button",
    display_order=1,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "manageOrders", "data-action-type": "run-method", "data-method": "ec7671d3-5162-47b6-b248-91d24ac1b952", "data-instance-source": "table-admin-2", "id": "ifnd5a", "method-class": "Admin", "endpoint": "/admin/{admin_id}/methods/manageOrders/", "is-instance-method": "true", "instance-source": "table-admin-2"}
)
ieeiva = ViewContainer(
    name="ieeiva",
    description=" component",
    view_elements={i826xh, ifnd5a},
    styling=Styling(size=Size(margin_top="20px"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")),
    component_id="ieeiva",
    display_order=3,
    custom_attributes={"id": "ieeiva"}
)
ieeiva_layout = Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")
ieeiva.layout = ieeiva_layout
i20l0k = ViewContainer(
    name="i20l0k",
    description="main container",
    view_elements={i42nal, iql1mj, table_admin_2, ieeiva},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="i20l0k",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "i20l0k"}
)
i20l0k_layout = Layout(flex="1")
i20l0k.layout = i20l0k_layout
iofqcj = ViewContainer(
    name="iofqcj",
    description=" component",
    view_elements={i1m5j9, i20l0k},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="iofqcj",
    display_order=0,
    custom_attributes={"id": "iofqcj"}
)
iofqcj_layout = Layout(layout_type=LayoutType.FLEX)
iofqcj.layout = iofqcj_layout
wrapper_3.view_elements = {iofqcj}


# Screen: wrapper_4
wrapper_4 = Screen(name="wrapper_4", description="Order", view_elements=set(), route_path="/order", screen_size="Medium")
wrapper_4.component_id = "page-order-3"
ir4cnh = Text(
    name="ir4cnh",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="ir4cnh",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "ir4cnh"}
)
izwgxs = Link(
    name="izwgxs",
    description="Link element",
    label="User",
    url="/user",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="izwgxs",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/user", "id": "izwgxs"}
)
iad9vh = Link(
    name="iad9vh",
    description="Link element",
    label="Customer",
    url="/customer",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iad9vh",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/customer", "id": "iad9vh"}
)
ixcnuk = Link(
    name="ixcnuk",
    description="Link element",
    label="Admin",
    url="/admin",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ixcnuk",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/admin", "id": "ixcnuk"}
)
igqxou = Link(
    name="igqxou",
    description="Link element",
    label="Order",
    url="/order",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="igqxou",
    tag_name="a",
    display_order=3,
    custom_attributes={"href": "/order", "id": "igqxou"}
)
iup7ob = Link(
    name="iup7ob",
    description="Link element",
    label="Cart",
    url="/cart",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iup7ob",
    tag_name="a",
    display_order=4,
    custom_attributes={"href": "/cart", "id": "iup7ob"}
)
i43kaf = Link(
    name="i43kaf",
    description="Link element",
    label="Review",
    url="/review",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i43kaf",
    tag_name="a",
    display_order=5,
    custom_attributes={"href": "/review", "id": "i43kaf"}
)
ixm3ta = Link(
    name="ixm3ta",
    description="Link element",
    label="Address",
    url="/address",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ixm3ta",
    tag_name="a",
    display_order=6,
    custom_attributes={"href": "/address", "id": "ixm3ta"}
)
ih4kiz = Link(
    name="ih4kiz",
    description="Link element",
    label="OrderItem",
    url="/orderitem",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ih4kiz",
    tag_name="a",
    display_order=7,
    custom_attributes={"href": "/orderitem", "id": "ih4kiz"}
)
i500ps = Link(
    name="i500ps",
    description="Link element",
    label="Payment",
    url="/payment",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i500ps",
    tag_name="a",
    display_order=8,
    custom_attributes={"href": "/payment", "id": "i500ps"}
)
ivamil = Link(
    name="ivamil",
    description="Link element",
    label="CartItem",
    url="/cartitem",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ivamil",
    tag_name="a",
    display_order=9,
    custom_attributes={"href": "/cartitem", "id": "ivamil"}
)
ij3zcg = Link(
    name="ij3zcg",
    description="Link element",
    label="Album",
    url="/album",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ij3zcg",
    tag_name="a",
    display_order=10,
    custom_attributes={"href": "/album", "id": "ij3zcg"}
)
ipknvl = Link(
    name="ipknvl",
    description="Link element",
    label="Artist",
    url="/artist",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ipknvl",
    tag_name="a",
    display_order=11,
    custom_attributes={"href": "/artist", "id": "ipknvl"}
)
iwnulk = Link(
    name="iwnulk",
    description="Link element",
    label="Track",
    url="/track",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iwnulk",
    tag_name="a",
    display_order=12,
    custom_attributes={"href": "/track", "id": "iwnulk"}
)
i9tx5g = ViewContainer(
    name="i9tx5g",
    description=" component",
    view_elements={izwgxs, iad9vh, ixcnuk, igqxou, iup7ob, i43kaf, ixm3ta, ih4kiz, i500ps, ivamil, ij3zcg, ipknvl, iwnulk},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="i9tx5g",
    display_order=1,
    custom_attributes={"id": "i9tx5g"}
)
i9tx5g_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
i9tx5g.layout = i9tx5g_layout
i2ammv = Text(
    name="i2ammv",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="i2ammv",
    display_order=2,
    custom_attributes={"id": "i2ammv"}
)
imhqqo = ViewContainer(
    name="imhqqo",
    description="nav container",
    view_elements={ir4cnh, i9tx5g, i2ammv},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="imhqqo",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "imhqqo"}
)
imhqqo_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
imhqqo.layout = imhqqo_layout
ij2ood = Text(
    name="ij2ood",
    content="Order",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="ij2ood",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "ij2ood"}
)
itmxvk = Text(
    name="itmxvk",
    content="Manage Order data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="itmxvk",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "itmxvk"}
)
table_order_3_col_0 = FieldColumn(label="Id", field=Order_Id)
table_order_3_col_1 = FieldColumn(label="Status", field=Order_status)
table_order_3_col_2 = FieldColumn(label="TotalAmount", field=Order_totalAmount)
table_order_3_col_3_path = next(end for assoc in domain_model.associations for end in assoc.ends if end.name == "contains")
table_order_3_col_3 = LookupColumn(label="Contains", path=table_order_3_col_3_path, field=OrderItem_quantity)
table_order_3_col_4_path = next(end for assoc in domain_model.associations for end in assoc.ends if end.name == "paidVia")
table_order_3_col_4 = LookupColumn(label="PaidVia", path=table_order_3_col_4_path, field=Payment_Id)
table_order_3_col_5_path = next(end for assoc in domain_model.associations for end in assoc.ends if end.name == "shipsTo")
table_order_3_col_5 = LookupColumn(label="ShipsTo", path=table_order_3_col_5_path, field=Address_Id)
table_order_3 = Table(
    name="table_order_3",
    title="Order List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_order_3_col_0, table_order_3_col_1, table_order_3_col_2, table_order_3_col_3, table_order_3_col_4, table_order_3_col_5],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-order-3",
    display_order=2,
    css_classes=["has-data-binding"],
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Order List", "data-source": "ddb8e355-2f38-44ae-b1fe-ad4b089643ef", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'Id', 'label': 'Id', 'columnType': 'field', '_expanded': False}, {'field': 'status', 'label': 'Status', 'columnType': 'field', '_expanded': False}, {'field': 'totalAmount', 'label': 'TotalAmount', 'columnType': 'field', '_expanded': False}, {'field': 'contains', 'label': 'Contains', 'columnType': 'lookup', 'lookupEntity': 'c2efb871-77f2-4f8f-a4d9-4402f11e68ee', 'lookupField': 'quantity', '_expanded': False}, {'field': 'paidVia', 'label': 'PaidVia', 'columnType': 'lookup', 'lookupEntity': '03eeb196-3a08-4420-8f1f-192c5abaebe0', 'lookupField': 'Id', '_expanded': False}, {'field': 'shipsTo', 'label': 'ShipsTo', 'columnType': 'lookup', 'lookupEntity': 'f5c614e2-8480-4d43-9921-4d64b23cc339', 'lookupField': 'Id', '_expanded': False}], "id": "table-order-3", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_order_3_binding_domain = None
if domain_model_ref is not None:
    table_order_3_binding_domain = domain_model_ref.get_class_by_name("Order")
if table_order_3_binding_domain:
    table_order_3_binding = DataBinding(domain_concept=table_order_3_binding_domain, name="OrderDataBinding")
else:
    # Domain class 'Order' not resolved; data binding skipped.
    table_order_3_binding = None
if table_order_3_binding:
    table_order_3.data_binding = table_order_3_binding
ibg7ww = Button(
    name="ibg7ww",
    description="Button component",
    label="+ calculateTotal",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=Order_m_calculateTotal,
    instance_source="table-order-3",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="ibg7ww",
    tag_name="button",
    display_order=0,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "+ calculateTotal", "data-action-type": "run-method", "data-method": "7db75d5d-2bf9-45ed-9123-e3dd20fcaaba", "data-instance-source": "table-order-3", "id": "ibg7ww", "method-class": "Order", "endpoint": "/order/{order_id}/methods/calculateTotal/", "is-instance-method": "true", "instance-source": "table-order-3"}
)
io05ab = Button(
    name="io05ab",
    description="Button component",
    label="+ updateStatus",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=Order_m_updateStatus,
    instance_source="table-order-3",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="io05ab",
    tag_name="button",
    display_order=1,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "+ updateStatus", "data-action-type": "run-method", "data-method": "3eca0a7d-2d7c-4bad-8262-b507369653f3", "data-instance-source": "table-order-3", "id": "io05ab", "method-class": "Order", "endpoint": "/order/{order_id}/methods/updateStatus/", "is-instance-method": "true", "instance-source": "table-order-3"}
)
imtp95 = Button(
    name="imtp95",
    description="Button component",
    label="+ generateInvoice",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=Order_m_generateInvoice,
    instance_source="table-order-3",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="imtp95",
    tag_name="button",
    display_order=2,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "+ generateInvoice", "data-action-type": "run-method", "data-method": "3290f503-39de-4c92-a950-a57f58c2e06f", "data-instance-source": "table-order-3", "id": "imtp95", "method-class": "Order", "endpoint": "/order/{order_id}/methods/generateInvoice/", "is-instance-method": "true", "instance-source": "table-order-3"}
)
ih2lqg = ViewContainer(
    name="ih2lqg",
    description=" component",
    view_elements={ibg7ww, io05ab, imtp95},
    styling=Styling(size=Size(margin_top="20px"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")),
    component_id="ih2lqg",
    display_order=3,
    custom_attributes={"id": "ih2lqg"}
)
ih2lqg_layout = Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")
ih2lqg.layout = ih2lqg_layout
ilxj8d = ViewContainer(
    name="ilxj8d",
    description="main container",
    view_elements={ij2ood, itmxvk, table_order_3, ih2lqg},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="ilxj8d",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "ilxj8d"}
)
ilxj8d_layout = Layout(flex="1")
ilxj8d.layout = ilxj8d_layout
i51svg = ViewContainer(
    name="i51svg",
    description=" component",
    view_elements={imhqqo, ilxj8d},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="i51svg",
    display_order=0,
    custom_attributes={"id": "i51svg"}
)
i51svg_layout = Layout(layout_type=LayoutType.FLEX)
i51svg.layout = i51svg_layout
wrapper_4.view_elements = {i51svg}


# Screen: wrapper_5
wrapper_5 = Screen(name="wrapper_5", description="Cart", view_elements=set(), route_path="/cart", screen_size="Medium")
wrapper_5.component_id = "page-cart-4"
iuq9u4 = Text(
    name="iuq9u4",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="iuq9u4",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "iuq9u4"}
)
iuro2b = Link(
    name="iuro2b",
    description="Link element",
    label="User",
    url="/user",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iuro2b",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/user", "id": "iuro2b"}
)
isifb8 = Link(
    name="isifb8",
    description="Link element",
    label="Customer",
    url="/customer",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="isifb8",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/customer", "id": "isifb8"}
)
i9rmda = Link(
    name="i9rmda",
    description="Link element",
    label="Admin",
    url="/admin",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i9rmda",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/admin", "id": "i9rmda"}
)
i0wxyi = Link(
    name="i0wxyi",
    description="Link element",
    label="Order",
    url="/order",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i0wxyi",
    tag_name="a",
    display_order=3,
    custom_attributes={"href": "/order", "id": "i0wxyi"}
)
ifuzsz = Link(
    name="ifuzsz",
    description="Link element",
    label="Cart",
    url="/cart",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ifuzsz",
    tag_name="a",
    display_order=4,
    custom_attributes={"href": "/cart", "id": "ifuzsz"}
)
i6dutk = Link(
    name="i6dutk",
    description="Link element",
    label="Review",
    url="/review",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i6dutk",
    tag_name="a",
    display_order=5,
    custom_attributes={"href": "/review", "id": "i6dutk"}
)
i8kxzi = Link(
    name="i8kxzi",
    description="Link element",
    label="Address",
    url="/address",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i8kxzi",
    tag_name="a",
    display_order=6,
    custom_attributes={"href": "/address", "id": "i8kxzi"}
)
i6xaf2 = Link(
    name="i6xaf2",
    description="Link element",
    label="OrderItem",
    url="/orderitem",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i6xaf2",
    tag_name="a",
    display_order=7,
    custom_attributes={"href": "/orderitem", "id": "i6xaf2"}
)
ioo73y = Link(
    name="ioo73y",
    description="Link element",
    label="Payment",
    url="/payment",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ioo73y",
    tag_name="a",
    display_order=8,
    custom_attributes={"href": "/payment", "id": "ioo73y"}
)
idkxpp = Link(
    name="idkxpp",
    description="Link element",
    label="CartItem",
    url="/cartitem",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="idkxpp",
    tag_name="a",
    display_order=9,
    custom_attributes={"href": "/cartitem", "id": "idkxpp"}
)
iu5qvw = Link(
    name="iu5qvw",
    description="Link element",
    label="Album",
    url="/album",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iu5qvw",
    tag_name="a",
    display_order=10,
    custom_attributes={"href": "/album", "id": "iu5qvw"}
)
iuwor6 = Link(
    name="iuwor6",
    description="Link element",
    label="Artist",
    url="/artist",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iuwor6",
    tag_name="a",
    display_order=11,
    custom_attributes={"href": "/artist", "id": "iuwor6"}
)
igv2ao = Link(
    name="igv2ao",
    description="Link element",
    label="Track",
    url="/track",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="igv2ao",
    tag_name="a",
    display_order=12,
    custom_attributes={"href": "/track", "id": "igv2ao"}
)
iqr16l = ViewContainer(
    name="iqr16l",
    description=" component",
    view_elements={iuro2b, isifb8, i9rmda, i0wxyi, ifuzsz, i6dutk, i8kxzi, i6xaf2, ioo73y, idkxpp, iu5qvw, iuwor6, igv2ao},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="iqr16l",
    display_order=1,
    custom_attributes={"id": "iqr16l"}
)
iqr16l_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
iqr16l.layout = iqr16l_layout
imx4kg = Text(
    name="imx4kg",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="imx4kg",
    display_order=2,
    custom_attributes={"id": "imx4kg"}
)
i4v11d = ViewContainer(
    name="i4v11d",
    description="nav container",
    view_elements={iuq9u4, iqr16l, imx4kg},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="i4v11d",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "i4v11d"}
)
i4v11d_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
i4v11d.layout = i4v11d_layout
iv6ao9 = Text(
    name="iv6ao9",
    content="Cart",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="iv6ao9",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "iv6ao9"}
)
iwbdoj = Text(
    name="iwbdoj",
    content="Manage Cart data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="iwbdoj",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "iwbdoj"}
)
table_cart_4_col_0 = FieldColumn(label="Id", field=Cart_Id)
table_cart_4 = Table(
    name="table_cart_4",
    title="Cart List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_cart_4_col_0],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-cart-4",
    display_order=2,
    css_classes=["has-data-binding"],
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Cart List", "data-source": "89f3febf-3264-4c26-9b93-cec260faf4c6", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'Id', 'label': 'Id', 'columnType': 'field', '_expanded': False}, {'field': 'CartItem', 'label': 'CartItem', 'columnType': 'lookup', 'lookupEntity': '8581908a-9d9b-4f13-acee-981d568b389e', 'lookupField': 'quantity', '_expanded': False}], "id": "table-cart-4", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_cart_4_binding_domain = None
if domain_model_ref is not None:
    table_cart_4_binding_domain = domain_model_ref.get_class_by_name("Cart")
if table_cart_4_binding_domain:
    table_cart_4_binding = DataBinding(domain_concept=table_cart_4_binding_domain, name="CartDataBinding")
else:
    # Domain class 'Cart' not resolved; data binding skipped.
    table_cart_4_binding = None
if table_cart_4_binding:
    table_cart_4.data_binding = table_cart_4_binding
i5zx6f = Button(
    name="i5zx6f",
    description="Button component",
    label="+ addItem",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=Cart_m_addItem,
    instance_source="table-cart-4",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="i5zx6f",
    tag_name="button",
    display_order=0,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "+ addItem", "data-action-type": "run-method", "data-method": "5cbb649f-81c6-40ba-a1c0-73f2c82000f7", "data-instance-source": "table-cart-4", "id": "i5zx6f", "method-class": "Cart", "endpoint": "/cart/{cart_id}/methods/addItem/", "is-instance-method": "true", "instance-source": "table-cart-4"}
)
icjfi5 = Button(
    name="icjfi5",
    description="Button component",
    label="+ removeItem",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=Cart_m_removeItem,
    instance_source="table-cart-4",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="icjfi5",
    tag_name="button",
    display_order=1,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "+ removeItem", "data-action-type": "run-method", "data-method": "95090796-1ab5-43a7-886e-26de53873ed8", "data-instance-source": "table-cart-4", "id": "icjfi5", "method-class": "Cart", "endpoint": "/cart/{cart_id}/methods/removeItem/", "is-instance-method": "true", "instance-source": "table-cart-4"}
)
ijnd7g = Button(
    name="ijnd7g",
    description="Button component",
    label="+ clear",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=Cart_m_clear,
    instance_source="table-cart-4",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="ijnd7g",
    tag_name="button",
    display_order=2,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "+ clear", "data-action-type": "run-method", "data-method": "5cec9a5e-9705-4baa-8d18-25f78af4574d", "data-instance-source": "table-cart-4", "id": "ijnd7g", "method-class": "Cart", "endpoint": "/cart/{cart_id}/methods/clear/", "is-instance-method": "true", "instance-source": "table-cart-4"}
)
ia8r8g = Button(
    name="ia8r8g",
    description="Button component",
    label="getTotal",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=Cart_m_getTotal,
    instance_source="table-cart-4",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="ia8r8g",
    tag_name="button",
    display_order=3,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "getTotal", "data-action-type": "run-method", "data-method": "6ccc7713-7676-4b39-9535-ad0538546a14", "data-instance-source": "table-cart-4", "id": "ia8r8g", "method-class": "Cart", "endpoint": "/cart/{cart_id}/methods/getTotal/", "is-instance-method": "true", "instance-source": "table-cart-4"}
)
icsuft = ViewContainer(
    name="icsuft",
    description=" component",
    view_elements={i5zx6f, icjfi5, ijnd7g, ia8r8g},
    styling=Styling(size=Size(margin_top="20px"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")),
    component_id="icsuft",
    display_order=3,
    custom_attributes={"id": "icsuft"}
)
icsuft_layout = Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")
icsuft.layout = icsuft_layout
iv5moe = ViewContainer(
    name="iv5moe",
    description="main container",
    view_elements={iv6ao9, iwbdoj, table_cart_4, icsuft},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="iv5moe",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "iv5moe"}
)
iv5moe_layout = Layout(flex="1")
iv5moe.layout = iv5moe_layout
igqu2l = ViewContainer(
    name="igqu2l",
    description=" component",
    view_elements={i4v11d, iv5moe},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="igqu2l",
    display_order=0,
    custom_attributes={"id": "igqu2l"}
)
igqu2l_layout = Layout(layout_type=LayoutType.FLEX)
igqu2l.layout = igqu2l_layout
wrapper_5.view_elements = {igqu2l}


# Screen: wrapper_6
wrapper_6 = Screen(name="wrapper_6", description="Review", view_elements=set(), route_path="/review", screen_size="Medium")
wrapper_6.component_id = "page-review-5"
ir0w61 = Text(
    name="ir0w61",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="ir0w61",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "ir0w61"}
)
i7lcjj = Link(
    name="i7lcjj",
    description="Link element",
    label="User",
    url="/user",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i7lcjj",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/user", "id": "i7lcjj"}
)
im3zev = Link(
    name="im3zev",
    description="Link element",
    label="Customer",
    url="/customer",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="im3zev",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/customer", "id": "im3zev"}
)
iqmf9l = Link(
    name="iqmf9l",
    description="Link element",
    label="Admin",
    url="/admin",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iqmf9l",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/admin", "id": "iqmf9l"}
)
ihmmr1 = Link(
    name="ihmmr1",
    description="Link element",
    label="Order",
    url="/order",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ihmmr1",
    tag_name="a",
    display_order=3,
    custom_attributes={"href": "/order", "id": "ihmmr1"}
)
izn0le = Link(
    name="izn0le",
    description="Link element",
    label="Cart",
    url="/cart",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="izn0le",
    tag_name="a",
    display_order=4,
    custom_attributes={"href": "/cart", "id": "izn0le"}
)
iycvm7 = Link(
    name="iycvm7",
    description="Link element",
    label="Review",
    url="/review",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iycvm7",
    tag_name="a",
    display_order=5,
    custom_attributes={"href": "/review", "id": "iycvm7"}
)
ip0px9 = Link(
    name="ip0px9",
    description="Link element",
    label="Address",
    url="/address",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ip0px9",
    tag_name="a",
    display_order=6,
    custom_attributes={"href": "/address", "id": "ip0px9"}
)
ir7rg8 = Link(
    name="ir7rg8",
    description="Link element",
    label="OrderItem",
    url="/orderitem",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ir7rg8",
    tag_name="a",
    display_order=7,
    custom_attributes={"href": "/orderitem", "id": "ir7rg8"}
)
inhr8o = Link(
    name="inhr8o",
    description="Link element",
    label="Payment",
    url="/payment",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="inhr8o",
    tag_name="a",
    display_order=8,
    custom_attributes={"href": "/payment", "id": "inhr8o"}
)
iahub8 = Link(
    name="iahub8",
    description="Link element",
    label="CartItem",
    url="/cartitem",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iahub8",
    tag_name="a",
    display_order=9,
    custom_attributes={"href": "/cartitem", "id": "iahub8"}
)
i5zhr1 = Link(
    name="i5zhr1",
    description="Link element",
    label="Album",
    url="/album",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i5zhr1",
    tag_name="a",
    display_order=10,
    custom_attributes={"href": "/album", "id": "i5zhr1"}
)
iej7o4 = Link(
    name="iej7o4",
    description="Link element",
    label="Artist",
    url="/artist",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iej7o4",
    tag_name="a",
    display_order=11,
    custom_attributes={"href": "/artist", "id": "iej7o4"}
)
ip0m1t = Link(
    name="ip0m1t",
    description="Link element",
    label="Track",
    url="/track",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ip0m1t",
    tag_name="a",
    display_order=12,
    custom_attributes={"href": "/track", "id": "ip0m1t"}
)
iy1daf = ViewContainer(
    name="iy1daf",
    description=" component",
    view_elements={i7lcjj, im3zev, iqmf9l, ihmmr1, izn0le, iycvm7, ip0px9, ir7rg8, inhr8o, iahub8, i5zhr1, iej7o4, ip0m1t},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="iy1daf",
    display_order=1,
    custom_attributes={"id": "iy1daf"}
)
iy1daf_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
iy1daf.layout = iy1daf_layout
icrdmi = Text(
    name="icrdmi",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="icrdmi",
    display_order=2,
    custom_attributes={"id": "icrdmi"}
)
i0pulc = ViewContainer(
    name="i0pulc",
    description="nav container",
    view_elements={ir0w61, iy1daf, icrdmi},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="i0pulc",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "i0pulc"}
)
i0pulc_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
i0pulc.layout = i0pulc_layout
iapm7j = Text(
    name="iapm7j",
    content="Review",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="iapm7j",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "iapm7j"}
)
icgqjn = Text(
    name="icgqjn",
    content="Manage Review data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="icgqjn",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "icgqjn"}
)
table_review_5_col_0 = FieldColumn(label="Id", field=Review_Id)
table_review_5_col_1 = FieldColumn(label="Rating", field=Review_rating)
table_review_5_col_2 = FieldColumn(label="Comment", field=Review_comment)
table_review_5 = Table(
    name="table_review_5",
    title="Review List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_review_5_col_0, table_review_5_col_1, table_review_5_col_2],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-review-5",
    display_order=2,
    css_classes=["has-data-binding"],
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Review List", "data-source": "a197039c-66f1-43b2-8407-48476b434c9f", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'Id', 'label': 'Id', 'columnType': 'field', '_expanded': False}, {'field': 'rating', 'label': 'Rating', 'columnType': 'field', '_expanded': False}, {'field': 'comment', 'label': 'Comment', 'columnType': 'field', '_expanded': False}, {'field': 'Customer', 'label': 'Customer', 'columnType': 'lookup', 'lookupEntity': 'class_06blhjj3h_mjikkmod', 'lookupField': 'Id', '_expanded': False}], "id": "table-review-5", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_review_5_binding_domain = None
if domain_model_ref is not None:
    table_review_5_binding_domain = domain_model_ref.get_class_by_name("Review")
if table_review_5_binding_domain:
    table_review_5_binding = DataBinding(domain_concept=table_review_5_binding_domain, name="ReviewDataBinding")
else:
    # Domain class 'Review' not resolved; data binding skipped.
    table_review_5_binding = None
if table_review_5_binding:
    table_review_5.data_binding = table_review_5_binding
iekoph = Button(
    name="iekoph",
    description="Button component",
    label="+ isVerified",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=Review_m_isVerified,
    instance_source="table-review-5",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="iekoph",
    tag_name="button",
    display_order=0,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "+ isVerified", "data-action-type": "run-method", "data-method": "7f280d34-89f5-498f-9f5a-8b2f831ec162", "data-instance-source": "table-review-5", "id": "iekoph", "method-class": "Review", "endpoint": "/review/{review_id}/methods/isVerified/", "is-instance-method": "true", "instance-source": "table-review-5"}
)
ie0n8y = ViewContainer(
    name="ie0n8y",
    description=" component",
    view_elements={iekoph},
    styling=Styling(size=Size(margin_top="20px"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")),
    component_id="ie0n8y",
    display_order=3,
    custom_attributes={"id": "ie0n8y"}
)
ie0n8y_layout = Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")
ie0n8y.layout = ie0n8y_layout
ih6r6a = ViewContainer(
    name="ih6r6a",
    description="main container",
    view_elements={iapm7j, icgqjn, table_review_5, ie0n8y},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="ih6r6a",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "ih6r6a"}
)
ih6r6a_layout = Layout(flex="1")
ih6r6a.layout = ih6r6a_layout
iwm3dt = ViewContainer(
    name="iwm3dt",
    description=" component",
    view_elements={i0pulc, ih6r6a},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="iwm3dt",
    display_order=0,
    custom_attributes={"id": "iwm3dt"}
)
iwm3dt_layout = Layout(layout_type=LayoutType.FLEX)
iwm3dt.layout = iwm3dt_layout
wrapper_6.view_elements = {iwm3dt}


# Screen: wrapper_7
wrapper_7 = Screen(name="wrapper_7", description="Address", view_elements=set(), route_path="/address", screen_size="Medium")
wrapper_7.component_id = "page-address-6"
im1m17 = Text(
    name="im1m17",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="im1m17",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "im1m17"}
)
i9q8a4 = Link(
    name="i9q8a4",
    description="Link element",
    label="User",
    url="/user",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i9q8a4",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/user", "id": "i9q8a4"}
)
imrin2 = Link(
    name="imrin2",
    description="Link element",
    label="Customer",
    url="/customer",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="imrin2",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/customer", "id": "imrin2"}
)
i4r0cs = Link(
    name="i4r0cs",
    description="Link element",
    label="Admin",
    url="/admin",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i4r0cs",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/admin", "id": "i4r0cs"}
)
i7vgcj = Link(
    name="i7vgcj",
    description="Link element",
    label="Order",
    url="/order",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i7vgcj",
    tag_name="a",
    display_order=3,
    custom_attributes={"href": "/order", "id": "i7vgcj"}
)
iw8xmk = Link(
    name="iw8xmk",
    description="Link element",
    label="Cart",
    url="/cart",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iw8xmk",
    tag_name="a",
    display_order=4,
    custom_attributes={"href": "/cart", "id": "iw8xmk"}
)
ilkt0r = Link(
    name="ilkt0r",
    description="Link element",
    label="Review",
    url="/review",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ilkt0r",
    tag_name="a",
    display_order=5,
    custom_attributes={"href": "/review", "id": "ilkt0r"}
)
ih7wtm = Link(
    name="ih7wtm",
    description="Link element",
    label="Address",
    url="/address",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ih7wtm",
    tag_name="a",
    display_order=6,
    custom_attributes={"href": "/address", "id": "ih7wtm"}
)
i17ah9 = Link(
    name="i17ah9",
    description="Link element",
    label="OrderItem",
    url="/orderitem",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i17ah9",
    tag_name="a",
    display_order=7,
    custom_attributes={"href": "/orderitem", "id": "i17ah9"}
)
iia9n6 = Link(
    name="iia9n6",
    description="Link element",
    label="Payment",
    url="/payment",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iia9n6",
    tag_name="a",
    display_order=8,
    custom_attributes={"href": "/payment", "id": "iia9n6"}
)
i3qleb = Link(
    name="i3qleb",
    description="Link element",
    label="CartItem",
    url="/cartitem",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i3qleb",
    tag_name="a",
    display_order=9,
    custom_attributes={"href": "/cartitem", "id": "i3qleb"}
)
i8toka = Link(
    name="i8toka",
    description="Link element",
    label="Album",
    url="/album",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i8toka",
    tag_name="a",
    display_order=10,
    custom_attributes={"href": "/album", "id": "i8toka"}
)
izbwwh = Link(
    name="izbwwh",
    description="Link element",
    label="Artist",
    url="/artist",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="izbwwh",
    tag_name="a",
    display_order=11,
    custom_attributes={"href": "/artist", "id": "izbwwh"}
)
i8ddnn = Link(
    name="i8ddnn",
    description="Link element",
    label="Track",
    url="/track",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i8ddnn",
    tag_name="a",
    display_order=12,
    custom_attributes={"href": "/track", "id": "i8ddnn"}
)
iatzo6 = ViewContainer(
    name="iatzo6",
    description=" component",
    view_elements={i9q8a4, imrin2, i4r0cs, i7vgcj, iw8xmk, ilkt0r, ih7wtm, i17ah9, iia9n6, i3qleb, i8toka, izbwwh, i8ddnn},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="iatzo6",
    display_order=1,
    custom_attributes={"id": "iatzo6"}
)
iatzo6_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
iatzo6.layout = iatzo6_layout
itp08q = Text(
    name="itp08q",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="itp08q",
    display_order=2,
    custom_attributes={"id": "itp08q"}
)
iyx47b = ViewContainer(
    name="iyx47b",
    description="nav container",
    view_elements={im1m17, iatzo6, itp08q},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="iyx47b",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "iyx47b"}
)
iyx47b_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
iyx47b.layout = iyx47b_layout
i7590a = Text(
    name="i7590a",
    content="Address",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="i7590a",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "i7590a"}
)
ia2vjg = Text(
    name="ia2vjg",
    content="Manage Address data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="ia2vjg",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "ia2vjg"}
)
table_address_6_col_0 = FieldColumn(label="Id", field=Address_Id)
table_address_6_col_1 = FieldColumn(label="Street", field=Address_street)
table_address_6_col_2 = FieldColumn(label="City", field=Address_city)
table_address_6_col_3 = FieldColumn(label="Zip Code", field=Address_zip_code)
table_address_6 = Table(
    name="table_address_6",
    title="Address List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_address_6_col_0, table_address_6_col_1, table_address_6_col_2, table_address_6_col_3],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-address-6",
    display_order=2,
    css_classes=["has-data-binding"],
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Address List", "data-source": "f5c614e2-8480-4d43-9921-4d64b23cc339", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'Id', 'label': 'Id', 'columnType': 'field', '_expanded': False}, {'field': 'street', 'label': 'Street', 'columnType': 'field', '_expanded': False}, {'field': 'city', 'label': 'City', 'columnType': 'field', '_expanded': False}, {'field': 'zip_code', 'label': 'Zip Code', 'columnType': 'field', '_expanded': False}, {'field': 'Order', 'label': 'Order', 'columnType': 'lookup', 'lookupEntity': 'ddb8e355-2f38-44ae-b1fe-ad4b089643ef', 'lookupField': 'Id', '_expanded': False}, {'field': 'Customer', 'label': 'Customer', 'columnType': 'lookup', 'lookupEntity': 'class_06blhjj3h_mjikkmod', 'lookupField': 'Id', '_expanded': False}], "id": "table-address-6", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_address_6_binding_domain = None
if domain_model_ref is not None:
    table_address_6_binding_domain = domain_model_ref.get_class_by_name("Address")
if table_address_6_binding_domain:
    table_address_6_binding = DataBinding(domain_concept=table_address_6_binding_domain, name="AddressDataBinding")
else:
    # Domain class 'Address' not resolved; data binding skipped.
    table_address_6_binding = None
if table_address_6_binding:
    table_address_6.data_binding = table_address_6_binding
ix8he1 = Button(
    name="ix8he1",
    description="Button component",
    label="+ validate",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=Address_m_validate,
    instance_source="table-address-6",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="ix8he1",
    tag_name="button",
    display_order=0,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "+ validate", "data-action-type": "run-method", "data-method": "15bfcbe7-933e-4808-80f1-1393433b0a85", "data-instance-source": "table-address-6", "id": "ix8he1", "method-class": "Address", "endpoint": "/address/{address_id}/methods/validate/", "is-instance-method": "true", "instance-source": "table-address-6"}
)
ih0vri = ViewContainer(
    name="ih0vri",
    description=" component",
    view_elements={ix8he1},
    styling=Styling(size=Size(margin_top="20px"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")),
    component_id="ih0vri",
    display_order=3,
    custom_attributes={"id": "ih0vri"}
)
ih0vri_layout = Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")
ih0vri.layout = ih0vri_layout
ia6u9w = ViewContainer(
    name="ia6u9w",
    description="main container",
    view_elements={i7590a, ia2vjg, table_address_6, ih0vri},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="ia6u9w",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "ia6u9w"}
)
ia6u9w_layout = Layout(flex="1")
ia6u9w.layout = ia6u9w_layout
i56j7g = ViewContainer(
    name="i56j7g",
    description=" component",
    view_elements={iyx47b, ia6u9w},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="i56j7g",
    display_order=0,
    custom_attributes={"id": "i56j7g"}
)
i56j7g_layout = Layout(layout_type=LayoutType.FLEX)
i56j7g.layout = i56j7g_layout
wrapper_7.view_elements = {i56j7g}


# Screen: wrapper_8
wrapper_8 = Screen(name="wrapper_8", description="OrderItem", view_elements=set(), route_path="/orderitem", screen_size="Medium")
wrapper_8.component_id = "page-orderitem-7"
i8vcr2 = Text(
    name="i8vcr2",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="i8vcr2",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "i8vcr2"}
)
ioyc3f = Link(
    name="ioyc3f",
    description="Link element",
    label="User",
    url="/user",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ioyc3f",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/user", "id": "ioyc3f"}
)
iyxzau = Link(
    name="iyxzau",
    description="Link element",
    label="Customer",
    url="/customer",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iyxzau",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/customer", "id": "iyxzau"}
)
ims8ew = Link(
    name="ims8ew",
    description="Link element",
    label="Admin",
    url="/admin",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ims8ew",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/admin", "id": "ims8ew"}
)
ix5ksh = Link(
    name="ix5ksh",
    description="Link element",
    label="Order",
    url="/order",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ix5ksh",
    tag_name="a",
    display_order=3,
    custom_attributes={"href": "/order", "id": "ix5ksh"}
)
iv6l0z = Link(
    name="iv6l0z",
    description="Link element",
    label="Cart",
    url="/cart",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iv6l0z",
    tag_name="a",
    display_order=4,
    custom_attributes={"href": "/cart", "id": "iv6l0z"}
)
im97w5 = Link(
    name="im97w5",
    description="Link element",
    label="Review",
    url="/review",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="im97w5",
    tag_name="a",
    display_order=5,
    custom_attributes={"href": "/review", "id": "im97w5"}
)
ijbp23 = Link(
    name="ijbp23",
    description="Link element",
    label="Address",
    url="/address",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ijbp23",
    tag_name="a",
    display_order=6,
    custom_attributes={"href": "/address", "id": "ijbp23"}
)
ikvker = Link(
    name="ikvker",
    description="Link element",
    label="OrderItem",
    url="/orderitem",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ikvker",
    tag_name="a",
    display_order=7,
    custom_attributes={"href": "/orderitem", "id": "ikvker"}
)
igfsif = Link(
    name="igfsif",
    description="Link element",
    label="Payment",
    url="/payment",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="igfsif",
    tag_name="a",
    display_order=8,
    custom_attributes={"href": "/payment", "id": "igfsif"}
)
ivlc9p = Link(
    name="ivlc9p",
    description="Link element",
    label="CartItem",
    url="/cartitem",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ivlc9p",
    tag_name="a",
    display_order=9,
    custom_attributes={"href": "/cartitem", "id": "ivlc9p"}
)
i6wajk = Link(
    name="i6wajk",
    description="Link element",
    label="Album",
    url="/album",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i6wajk",
    tag_name="a",
    display_order=10,
    custom_attributes={"href": "/album", "id": "i6wajk"}
)
iumwao = Link(
    name="iumwao",
    description="Link element",
    label="Artist",
    url="/artist",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iumwao",
    tag_name="a",
    display_order=11,
    custom_attributes={"href": "/artist", "id": "iumwao"}
)
i2qf02 = Link(
    name="i2qf02",
    description="Link element",
    label="Track",
    url="/track",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i2qf02",
    tag_name="a",
    display_order=12,
    custom_attributes={"href": "/track", "id": "i2qf02"}
)
ib7j3w = ViewContainer(
    name="ib7j3w",
    description=" component",
    view_elements={ioyc3f, iyxzau, ims8ew, ix5ksh, iv6l0z, im97w5, ijbp23, ikvker, igfsif, ivlc9p, i6wajk, iumwao, i2qf02},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="ib7j3w",
    display_order=1,
    custom_attributes={"id": "ib7j3w"}
)
ib7j3w_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
ib7j3w.layout = ib7j3w_layout
idauem = Text(
    name="idauem",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="idauem",
    display_order=2,
    custom_attributes={"id": "idauem"}
)
ic1rd5 = ViewContainer(
    name="ic1rd5",
    description="nav container",
    view_elements={i8vcr2, ib7j3w, idauem},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="ic1rd5",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "ic1rd5"}
)
ic1rd5_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
ic1rd5.layout = ic1rd5_layout
ii00jh = Text(
    name="ii00jh",
    content="OrderItem",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="ii00jh",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "ii00jh"}
)
i2xfv8 = Text(
    name="i2xfv8",
    content="Manage OrderItem data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="i2xfv8",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "i2xfv8"}
)
table_orderitem_7_col_0 = FieldColumn(label="Quantity", field=OrderItem_quantity)
table_orderitem_7_col_1 = FieldColumn(label="UnintPrice", field=OrderItem_unintPrice)
table_orderitem_7_col_2_path = next(end for assoc in domain_model.associations for end in assoc.ends if end.name == "refersTo")
table_orderitem_7_col_2 = LookupColumn(label="RefersTo", path=table_orderitem_7_col_2_path, field=Album_Id)
table_orderitem_7 = Table(
    name="table_orderitem_7",
    title="OrderItem List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_orderitem_7_col_0, table_orderitem_7_col_1, table_orderitem_7_col_2],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-orderitem-7",
    display_order=2,
    css_classes=["has-data-binding"],
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "OrderItem List", "data-source": "c2efb871-77f2-4f8f-a4d9-4402f11e68ee", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'quantity', 'label': 'Quantity', 'columnType': 'field', '_expanded': False}, {'field': 'unintPrice', 'label': 'UnintPrice', 'columnType': 'field', '_expanded': False}, {'field': 'Order', 'label': 'Order', 'columnType': 'lookup', 'lookupEntity': 'ddb8e355-2f38-44ae-b1fe-ad4b089643ef', 'lookupField': 'Id', '_expanded': False}, {'field': 'refersTo', 'label': 'RefersTo', 'columnType': 'lookup', 'lookupEntity': '8ced71dd-9fd8-4eb8-8308-dd72e95597c0', 'lookupField': 'Id', '_expanded': False}], "id": "table-orderitem-7", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_orderitem_7_binding_domain = None
if domain_model_ref is not None:
    table_orderitem_7_binding_domain = domain_model_ref.get_class_by_name("OrderItem")
if table_orderitem_7_binding_domain:
    table_orderitem_7_binding = DataBinding(domain_concept=table_orderitem_7_binding_domain, name="OrderItemDataBinding")
else:
    # Domain class 'OrderItem' not resolved; data binding skipped.
    table_orderitem_7_binding = None
if table_orderitem_7_binding:
    table_orderitem_7.data_binding = table_orderitem_7_binding
ipvahe = Button(
    name="ipvahe",
    description="Button component",
    label="+ getSubtotal",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=OrderItem_m_getSubtotal,
    instance_source="table-orderitem-7",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="ipvahe",
    tag_name="button",
    display_order=0,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "+ getSubtotal", "data-action-type": "run-method", "data-method": "1100794b-861b-402c-a57d-4d850d15c1f5", "data-instance-source": "table-orderitem-7", "id": "ipvahe", "method-class": "OrderItem", "endpoint": "/orderitem/{orderitem_id}/methods/getSubtotal/", "is-instance-method": "true", "instance-source": "table-orderitem-7"}
)
imll1f = ViewContainer(
    name="imll1f",
    description=" component",
    view_elements={ipvahe},
    styling=Styling(size=Size(margin_top="20px"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")),
    component_id="imll1f",
    display_order=3,
    custom_attributes={"id": "imll1f"}
)
imll1f_layout = Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")
imll1f.layout = imll1f_layout
io9guq = ViewContainer(
    name="io9guq",
    description="main container",
    view_elements={ii00jh, i2xfv8, table_orderitem_7, imll1f},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="io9guq",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "io9guq"}
)
io9guq_layout = Layout(flex="1")
io9guq.layout = io9guq_layout
iaa7bq = ViewContainer(
    name="iaa7bq",
    description=" component",
    view_elements={ic1rd5, io9guq},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="iaa7bq",
    display_order=0,
    custom_attributes={"id": "iaa7bq"}
)
iaa7bq_layout = Layout(layout_type=LayoutType.FLEX)
iaa7bq.layout = iaa7bq_layout
wrapper_8.view_elements = {iaa7bq}


# Screen: wrapper_9
wrapper_9 = Screen(name="wrapper_9", description="Payment", view_elements=set(), route_path="/payment", screen_size="Medium")
wrapper_9.component_id = "page-payment-8"
ixu48h = Text(
    name="ixu48h",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="ixu48h",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "ixu48h"}
)
ilod4i = Link(
    name="ilod4i",
    description="Link element",
    label="User",
    url="/user",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ilod4i",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/user", "id": "ilod4i"}
)
iaolfd = Link(
    name="iaolfd",
    description="Link element",
    label="Customer",
    url="/customer",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iaolfd",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/customer", "id": "iaolfd"}
)
ico7vf = Link(
    name="ico7vf",
    description="Link element",
    label="Admin",
    url="/admin",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ico7vf",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/admin", "id": "ico7vf"}
)
ijifx9 = Link(
    name="ijifx9",
    description="Link element",
    label="Order",
    url="/order",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ijifx9",
    tag_name="a",
    display_order=3,
    custom_attributes={"href": "/order", "id": "ijifx9"}
)
i9kpcv = Link(
    name="i9kpcv",
    description="Link element",
    label="Cart",
    url="/cart",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i9kpcv",
    tag_name="a",
    display_order=4,
    custom_attributes={"href": "/cart", "id": "i9kpcv"}
)
ipqifc = Link(
    name="ipqifc",
    description="Link element",
    label="Review",
    url="/review",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ipqifc",
    tag_name="a",
    display_order=5,
    custom_attributes={"href": "/review", "id": "ipqifc"}
)
ivgeik = Link(
    name="ivgeik",
    description="Link element",
    label="Address",
    url="/address",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ivgeik",
    tag_name="a",
    display_order=6,
    custom_attributes={"href": "/address", "id": "ivgeik"}
)
itqmgw = Link(
    name="itqmgw",
    description="Link element",
    label="OrderItem",
    url="/orderitem",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="itqmgw",
    tag_name="a",
    display_order=7,
    custom_attributes={"href": "/orderitem", "id": "itqmgw"}
)
i114v5 = Link(
    name="i114v5",
    description="Link element",
    label="Payment",
    url="/payment",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i114v5",
    tag_name="a",
    display_order=8,
    custom_attributes={"href": "/payment", "id": "i114v5"}
)
i42brj = Link(
    name="i42brj",
    description="Link element",
    label="CartItem",
    url="/cartitem",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i42brj",
    tag_name="a",
    display_order=9,
    custom_attributes={"href": "/cartitem", "id": "i42brj"}
)
is9g7k = Link(
    name="is9g7k",
    description="Link element",
    label="Album",
    url="/album",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="is9g7k",
    tag_name="a",
    display_order=10,
    custom_attributes={"href": "/album", "id": "is9g7k"}
)
ix5o9l = Link(
    name="ix5o9l",
    description="Link element",
    label="Artist",
    url="/artist",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ix5o9l",
    tag_name="a",
    display_order=11,
    custom_attributes={"href": "/artist", "id": "ix5o9l"}
)
ioa5de = Link(
    name="ioa5de",
    description="Link element",
    label="Track",
    url="/track",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ioa5de",
    tag_name="a",
    display_order=12,
    custom_attributes={"href": "/track", "id": "ioa5de"}
)
iy8dqf = ViewContainer(
    name="iy8dqf",
    description=" component",
    view_elements={ilod4i, iaolfd, ico7vf, ijifx9, i9kpcv, ipqifc, ivgeik, itqmgw, i114v5, i42brj, is9g7k, ix5o9l, ioa5de},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="iy8dqf",
    display_order=1,
    custom_attributes={"id": "iy8dqf"}
)
iy8dqf_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
iy8dqf.layout = iy8dqf_layout
ik50x5 = Text(
    name="ik50x5",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="ik50x5",
    display_order=2,
    custom_attributes={"id": "ik50x5"}
)
ie1uut = ViewContainer(
    name="ie1uut",
    description="nav container",
    view_elements={ixu48h, iy8dqf, ik50x5},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="ie1uut",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "ie1uut"}
)
ie1uut_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
ie1uut.layout = ie1uut_layout
i1n35o = Text(
    name="i1n35o",
    content="Payment",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="i1n35o",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "i1n35o"}
)
ivwlpx = Text(
    name="ivwlpx",
    content="Manage Payment data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="ivwlpx",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "ivwlpx"}
)
table_payment_8_col_0 = FieldColumn(label="Id", field=Payment_Id)
table_payment_8_col_1 = FieldColumn(label="Method", field=Payment_method)
table_payment_8_col_2 = FieldColumn(label="Amount", field=Payment_amount)
table_payment_8 = Table(
    name="table_payment_8",
    title="Payment List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_payment_8_col_0, table_payment_8_col_1, table_payment_8_col_2],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-payment-8",
    display_order=2,
    css_classes=["has-data-binding"],
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Payment List", "data-source": "03eeb196-3a08-4420-8f1f-192c5abaebe0", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'Id', 'label': 'Id', 'columnType': 'field', '_expanded': False}, {'field': 'method', 'label': 'Method', 'columnType': 'field', '_expanded': False}, {'field': 'amount', 'label': 'Amount', 'columnType': 'field', '_expanded': False}, {'field': 'Order', 'label': 'Order', 'columnType': 'lookup', 'lookupEntity': 'ddb8e355-2f38-44ae-b1fe-ad4b089643ef', 'lookupField': 'Id', '_expanded': False}], "id": "table-payment-8", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_payment_8_binding_domain = None
if domain_model_ref is not None:
    table_payment_8_binding_domain = domain_model_ref.get_class_by_name("Payment")
if table_payment_8_binding_domain:
    table_payment_8_binding = DataBinding(domain_concept=table_payment_8_binding_domain, name="PaymentDataBinding")
else:
    # Domain class 'Payment' not resolved; data binding skipped.
    table_payment_8_binding = None
if table_payment_8_binding:
    table_payment_8.data_binding = table_payment_8_binding
i63g33 = Button(
    name="i63g33",
    description="Button component",
    label="+ validate",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=Payment_m_validate,
    instance_source="table-payment-8",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="i63g33",
    tag_name="button",
    display_order=0,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "+ validate", "data-action-type": "run-method", "data-method": "412ff47e-e4b6-44da-a641-401dc0386e77", "data-instance-source": "table-payment-8", "id": "i63g33", "method-class": "Payment", "endpoint": "/payment/{payment_id}/methods/validate/", "is-instance-method": "true", "instance-source": "table-payment-8"}
)
iejlyv = ViewContainer(
    name="iejlyv",
    description=" component",
    view_elements={i63g33},
    styling=Styling(size=Size(margin_top="20px"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")),
    component_id="iejlyv",
    display_order=3,
    custom_attributes={"id": "iejlyv"}
)
iejlyv_layout = Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")
iejlyv.layout = iejlyv_layout
iygzb4 = ViewContainer(
    name="iygzb4",
    description="main container",
    view_elements={i1n35o, ivwlpx, table_payment_8, iejlyv},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="iygzb4",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "iygzb4"}
)
iygzb4_layout = Layout(flex="1")
iygzb4.layout = iygzb4_layout
i6mgnq = ViewContainer(
    name="i6mgnq",
    description=" component",
    view_elements={ie1uut, iygzb4},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="i6mgnq",
    display_order=0,
    custom_attributes={"id": "i6mgnq"}
)
i6mgnq_layout = Layout(layout_type=LayoutType.FLEX)
i6mgnq.layout = i6mgnq_layout
wrapper_9.view_elements = {i6mgnq}

gui_module = Module(
    name="GUI_Module",
    screens={wrapper, wrapper_10, wrapper_11, wrapper_12, wrapper_13, wrapper_2, wrapper_3, wrapper_4, wrapper_5, wrapper_6, wrapper_7, wrapper_8, wrapper_9}
)

# GUI Model
gui_model = GUIModel(
    name="GUI",
    package="",
    versionCode="1.0",
    versionName="1.0",
    modules={gui_module},
    description="GUI"
)
