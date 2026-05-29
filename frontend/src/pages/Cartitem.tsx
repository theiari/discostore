import React from "react";
import { TableBlock } from "../components/runtime/TableBlock";
import { MethodButton } from "../components/MethodButton";

const Cartitem: React.FC = () => {
  return (
    <div id="page-cartitem-9">
    <div id="ioi4wa" style={{"height": "100vh", "fontFamily": "Arial, sans-serif", "display": "flex", "--chart-color-palette": "default"}}>
      <nav id="ii1i6s" style={{"width": "250px", "padding": "20px", "display": "flex", "overflowY": "auto", "background": "linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", "color": "white", "--chart-color-palette": "default", "flexDirection": "column"}}>
        <h2 id="isnxfj" style={{"fontSize": "24px", "fontWeight": "bold", "marginTop": "0", "marginBottom": "30px", "--chart-color-palette": "default"}}>{"BESSER"}</h2>
        <div id="i7yk1s" style={{"display": "flex", "--chart-color-palette": "default", "flexDirection": "column", "flex": "1"}}>
          <a id="i6o5sw" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/user">{"User"}</a>
          <a id="il1a8e" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/customer">{"Customer"}</a>
          <a id="ixjtjg" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/admin">{"Admin"}</a>
          <a id="i4o7we" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/order">{"Order"}</a>
          <a id="irsxjq" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/cart">{"Cart"}</a>
          <a id="ixnx0w" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/review">{"Review"}</a>
          <a id="i1h7gr" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/address">{"Address"}</a>
          <a id="ibppqt" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/orderitem">{"OrderItem"}</a>
          <a id="it0wgl" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/payment">{"Payment"}</a>
          <a id="i84jka" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "rgba(255,255,255,0.2)", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/cartitem">{"CartItem"}</a>
          <a id="iwyq2h" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/album">{"Album"}</a>
          <a id="i07f2m" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/artist">{"Artist"}</a>
          <a id="i1wosi" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/track">{"Track"}</a>
        </div>
        <p id="iac1z8" style={{"fontSize": "11px", "paddingTop": "20px", "marginTop": "auto", "textAlign": "center", "opacity": "0.8", "borderTop": "1px solid rgba(255,255,255,0.2)", "--chart-color-palette": "default"}}>{"© 2026 BESSER. All rights reserved."}</p>
      </nav>
      <main id="i91vvm" style={{"padding": "40px", "overflowY": "auto", "background": "#f5f5f5", "--chart-color-palette": "default", "flex": "1"}}>
        <h1 id="igcy6n" style={{"fontSize": "32px", "marginTop": "0", "marginBottom": "10px", "color": "#333", "--chart-color-palette": "default"}}>{"CartItem"}</h1>
        <p id="ia6usi" style={{"marginBottom": "30px", "color": "#666", "--chart-color-palette": "default"}}>{"Manage CartItem data"}</p>
        <TableBlock id="table-cartitem-9" styles={{"width": "100%", "minHeight": "400px", "--chart-color-palette": "default"}} title="CartItem List" options={{"showHeader": true, "stripedRows": false, "showPagination": true, "rowsPerPage": 5, "actionButtons": true, "columns": [{"label": "Quantity", "column_type": "field", "field": "quantity", "type": "int", "required": true}, {"label": "UnintPrice", "column_type": "field", "field": "unintPrice", "type": "float", "required": true}], "formColumns": [{"column_type": "field", "field": "quantity", "label": "quantity", "type": "int", "required": true, "defaultValue": null}, {"column_type": "field", "field": "unintPrice", "label": "unintPrice", "type": "float", "required": true, "defaultValue": null}, {"column_type": "lookup", "path": "cart", "field": "cart", "lookup_field": "Id", "entity": "Cart", "type": "str", "required": true}]}} dataBinding={{"entity": "CartItem", "endpoint": "/cartitem/"}} />
        <div id="iaatsm" style={{"marginTop": "20px", "display": "flex", "--chart-color-palette": "default", "flexWrap": "wrap", "gap": "10px"}}>
          <MethodButton id="icja42" className="action-button-component" style={{"padding": "6px 14px", "fontSize": "13px", "fontWeight": "600", "textDecoration": "none", "letterSpacing": "0.01em", "display": "flex", "cursor": "pointer", "transition": "background 0.2s", "background": "linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", "color": "#fff", "borderRadius": "4px", "border": "none", "boxShadow": "0 1px 4px rgba(37,99,235,0.10)", "--chart-color-palette": "default", "alignItems": "center"}} endpoint="/cartitem/{cartitem_id}/methods/getSubtotal/" label="+ getSubtotal" isInstanceMethod={true} instanceSourceTableId="table-cartitem-9" />
        </div>
      </main>
    </div>    </div>
  );
};

export default Cartitem;
