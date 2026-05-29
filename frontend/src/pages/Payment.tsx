import React from "react";
import { TableBlock } from "../components/runtime/TableBlock";
import { MethodButton } from "../components/MethodButton";

const Payment: React.FC = () => {
  return (
    <div id="page-payment-8">
    <div id="i6mgnq" style={{"height": "100vh", "fontFamily": "Arial, sans-serif", "display": "flex", "--chart-color-palette": "default"}}>
      <nav id="ie1uut" style={{"width": "250px", "padding": "20px", "display": "flex", "overflowY": "auto", "background": "linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", "color": "white", "--chart-color-palette": "default", "flexDirection": "column"}}>
        <h2 id="ixu48h" style={{"fontSize": "24px", "fontWeight": "bold", "marginTop": "0", "marginBottom": "30px", "--chart-color-palette": "default"}}>{"BESSER"}</h2>
        <div id="iy8dqf" style={{"display": "flex", "--chart-color-palette": "default", "flexDirection": "column", "flex": "1"}}>
          <a id="ilod4i" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/user">{"User"}</a>
          <a id="iaolfd" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/customer">{"Customer"}</a>
          <a id="ico7vf" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/admin">{"Admin"}</a>
          <a id="ijifx9" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/order">{"Order"}</a>
          <a id="i9kpcv" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/cart">{"Cart"}</a>
          <a id="ipqifc" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/review">{"Review"}</a>
          <a id="ivgeik" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/address">{"Address"}</a>
          <a id="itqmgw" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/orderitem">{"OrderItem"}</a>
          <a id="i114v5" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "rgba(255,255,255,0.2)", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/payment">{"Payment"}</a>
          <a id="i42brj" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/cartitem">{"CartItem"}</a>
          <a id="is9g7k" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/album">{"Album"}</a>
          <a id="ix5o9l" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/artist">{"Artist"}</a>
          <a id="ioa5de" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/track">{"Track"}</a>
        </div>
        <p id="ik50x5" style={{"fontSize": "11px", "paddingTop": "20px", "marginTop": "auto", "textAlign": "center", "opacity": "0.8", "borderTop": "1px solid rgba(255,255,255,0.2)", "--chart-color-palette": "default"}}>{"© 2026 BESSER. All rights reserved."}</p>
      </nav>
      <main id="iygzb4" style={{"padding": "40px", "overflowY": "auto", "background": "#f5f5f5", "--chart-color-palette": "default", "flex": "1"}}>
        <h1 id="i1n35o" style={{"fontSize": "32px", "marginTop": "0", "marginBottom": "10px", "color": "#333", "--chart-color-palette": "default"}}>{"Payment"}</h1>
        <p id="ivwlpx" style={{"marginBottom": "30px", "color": "#666", "--chart-color-palette": "default"}}>{"Manage Payment data"}</p>
        <TableBlock id="table-payment-8" styles={{"width": "100%", "minHeight": "400px", "--chart-color-palette": "default"}} title="Payment List" options={{"showHeader": true, "stripedRows": false, "showPagination": true, "rowsPerPage": 5, "actionButtons": true, "columns": [{"label": "Id", "column_type": "field", "field": "Id", "type": "int", "required": true}, {"label": "Method", "column_type": "field", "field": "method", "type": "str", "required": true}, {"label": "Amount", "column_type": "field", "field": "amount", "type": "float", "required": true}], "formColumns": [{"column_type": "field", "field": "Id", "label": "Id", "type": "int", "required": true, "defaultValue": null}, {"column_type": "field", "field": "method", "label": "method", "type": "str", "required": true, "defaultValue": null}, {"column_type": "field", "field": "amount", "label": "amount", "type": "float", "required": true, "defaultValue": null}, {"column_type": "lookup", "path": "order_1", "field": "order_1", "lookup_field": "Id", "entity": "Order", "type": "str", "required": true}]}} dataBinding={{"entity": "Payment", "endpoint": "/payment/"}} />
        <div id="iejlyv" style={{"marginTop": "20px", "display": "flex", "--chart-color-palette": "default", "flexWrap": "wrap", "gap": "10px"}}>
          <MethodButton id="i63g33" className="action-button-component" style={{"padding": "6px 14px", "fontSize": "13px", "fontWeight": "600", "textDecoration": "none", "letterSpacing": "0.01em", "display": "flex", "cursor": "pointer", "transition": "background 0.2s", "background": "linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", "color": "#fff", "borderRadius": "4px", "border": "none", "boxShadow": "0 1px 4px rgba(37,99,235,0.10)", "--chart-color-palette": "default", "alignItems": "center"}} endpoint="/payment/{payment_id}/methods/validate/" label="+ validate" isInstanceMethod={true} instanceSourceTableId="table-payment-8" />
        </div>
      </main>
    </div>    </div>
  );
};

export default Payment;
