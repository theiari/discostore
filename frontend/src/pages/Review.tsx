import React from "react";
import { TableBlock } from "../components/runtime/TableBlock";
import { MethodButton } from "../components/MethodButton";

const Review: React.FC = () => {
  return (
    <div id="page-review-5">
    <div id="iwm3dt" style={{"height": "100vh", "fontFamily": "Arial, sans-serif", "display": "flex", "--chart-color-palette": "default"}}>
      <nav id="i0pulc" style={{"width": "250px", "padding": "20px", "display": "flex", "overflowY": "auto", "background": "linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", "color": "white", "--chart-color-palette": "default", "flexDirection": "column"}}>
        <h2 id="ir0w61" style={{"fontSize": "24px", "fontWeight": "bold", "marginTop": "0", "marginBottom": "30px", "--chart-color-palette": "default"}}>{"BESSER"}</h2>
        <div id="iy1daf" style={{"display": "flex", "--chart-color-palette": "default", "flexDirection": "column", "flex": "1"}}>
          <a id="i7lcjj" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/user">{"User"}</a>
          <a id="im3zev" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/customer">{"Customer"}</a>
          <a id="iqmf9l" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/admin">{"Admin"}</a>
          <a id="ihmmr1" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/order">{"Order"}</a>
          <a id="izn0le" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/cart">{"Cart"}</a>
          <a id="iycvm7" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "rgba(255,255,255,0.2)", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/review">{"Review"}</a>
          <a id="ip0px9" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/address">{"Address"}</a>
          <a id="ir7rg8" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/orderitem">{"OrderItem"}</a>
          <a id="inhr8o" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/payment">{"Payment"}</a>
          <a id="iahub8" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/cartitem">{"CartItem"}</a>
          <a id="i5zhr1" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/album">{"Album"}</a>
          <a id="iej7o4" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/artist">{"Artist"}</a>
          <a id="ip0m1t" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/track">{"Track"}</a>
        </div>
        <p id="icrdmi" style={{"fontSize": "11px", "paddingTop": "20px", "marginTop": "auto", "textAlign": "center", "opacity": "0.8", "borderTop": "1px solid rgba(255,255,255,0.2)", "--chart-color-palette": "default"}}>{"© 2026 BESSER. All rights reserved."}</p>
      </nav>
      <main id="ih6r6a" style={{"padding": "40px", "overflowY": "auto", "background": "#f5f5f5", "--chart-color-palette": "default", "flex": "1"}}>
        <h1 id="iapm7j" style={{"fontSize": "32px", "marginTop": "0", "marginBottom": "10px", "color": "#333", "--chart-color-palette": "default"}}>{"Review"}</h1>
        <p id="icgqjn" style={{"marginBottom": "30px", "color": "#666", "--chart-color-palette": "default"}}>{"Manage Review data"}</p>
        <TableBlock id="table-review-5" styles={{"width": "100%", "minHeight": "400px", "--chart-color-palette": "default"}} title="Review List" options={{"showHeader": true, "stripedRows": false, "showPagination": true, "rowsPerPage": 5, "actionButtons": true, "columns": [{"label": "Id", "column_type": "field", "field": "Id", "type": "int", "required": true}, {"label": "Rating", "column_type": "field", "field": "rating", "type": "str", "required": true}, {"label": "Comment", "column_type": "field", "field": "comment", "type": "str", "required": true}], "formColumns": [{"column_type": "field", "field": "Id", "label": "Id", "type": "int", "required": true, "defaultValue": null}, {"column_type": "field", "field": "rating", "label": "rating", "type": "str", "required": true, "defaultValue": null}, {"column_type": "field", "field": "comment", "label": "comment", "type": "str", "required": true, "defaultValue": null}, {"column_type": "lookup", "path": "customer_2", "field": "customer_2", "lookup_field": "id", "entity": "Customer", "type": "str", "required": true}]}} dataBinding={{"entity": "Review", "endpoint": "/review/"}} />
        <div id="ie0n8y" style={{"marginTop": "20px", "display": "flex", "--chart-color-palette": "default", "flexWrap": "wrap", "gap": "10px"}}>
          <MethodButton id="iekoph" className="action-button-component" style={{"padding": "6px 14px", "fontSize": "13px", "fontWeight": "600", "textDecoration": "none", "letterSpacing": "0.01em", "display": "flex", "cursor": "pointer", "transition": "background 0.2s", "background": "linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", "color": "#fff", "borderRadius": "4px", "border": "none", "boxShadow": "0 1px 4px rgba(37,99,235,0.10)", "--chart-color-palette": "default", "alignItems": "center"}} endpoint="/review/{review_id}/methods/isVerified/" label="+ isVerified" isInstanceMethod={true} instanceSourceTableId="table-review-5" />
        </div>
      </main>
    </div>    </div>
  );
};

export default Review;
