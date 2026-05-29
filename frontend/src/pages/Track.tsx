import React from "react";
import { TableBlock } from "../components/runtime/TableBlock";
import { MethodButton } from "../components/MethodButton";

const Track: React.FC = () => {
  return (
    <div id="page-track-12">
    <div id="iyfdrz" style={{"height": "100vh", "fontFamily": "Arial, sans-serif", "display": "flex", "--chart-color-palette": "default"}}>
      <nav id="iodmpl" style={{"width": "250px", "padding": "20px", "display": "flex", "overflowY": "auto", "background": "linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", "color": "white", "--chart-color-palette": "default", "flexDirection": "column"}}>
        <h2 id="imyuke" style={{"fontSize": "24px", "fontWeight": "bold", "marginTop": "0", "marginBottom": "30px", "--chart-color-palette": "default"}}>{"BESSER"}</h2>
        <div id="i0ie7w" style={{"display": "flex", "--chart-color-palette": "default", "flexDirection": "column", "flex": "1"}}>
          <a id="iw88g7" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/user">{"User"}</a>
          <a id="i4gif7" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/customer">{"Customer"}</a>
          <a id="iumtpg" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/admin">{"Admin"}</a>
          <a id="i5qf8p" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/order">{"Order"}</a>
          <a id="isnfjf" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/cart">{"Cart"}</a>
          <a id="ix6snj" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/review">{"Review"}</a>
          <a id="ipzubz" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/address">{"Address"}</a>
          <a id="iyoeuh" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/orderitem">{"OrderItem"}</a>
          <a id="i7ux5q" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/payment">{"Payment"}</a>
          <a id="iqasqb" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/cartitem">{"CartItem"}</a>
          <a id="iag24a" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/album">{"Album"}</a>
          <a id="i52ww5" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/artist">{"Artist"}</a>
          <a id="i1u9hy" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "rgba(255,255,255,0.2)", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/track">{"Track"}</a>
        </div>
        <p id="iai105" style={{"fontSize": "11px", "paddingTop": "20px", "marginTop": "auto", "textAlign": "center", "opacity": "0.8", "borderTop": "1px solid rgba(255,255,255,0.2)", "--chart-color-palette": "default"}}>{"© 2026 BESSER. All rights reserved."}</p>
      </nav>
      <main id="iirkws" style={{"padding": "40px", "overflowY": "auto", "background": "#f5f5f5", "--chart-color-palette": "default", "flex": "1"}}>
        <h1 id="iifekk" style={{"fontSize": "32px", "marginTop": "0", "marginBottom": "10px", "color": "#333", "--chart-color-palette": "default"}}>{"Track"}</h1>
        <p id="i64rzh" style={{"marginBottom": "30px", "color": "#666", "--chart-color-palette": "default"}}>{"Manage Track data"}</p>
        <TableBlock id="table-track-12" styles={{"width": "100%", "minHeight": "400px", "--chart-color-palette": "default"}} title="Track List" options={{"showHeader": true, "stripedRows": false, "showPagination": true, "rowsPerPage": 5, "actionButtons": true, "columns": [{"label": "Id", "column_type": "field", "field": "Id", "type": "int", "required": true}, {"label": "Title", "column_type": "field", "field": "title", "type": "str", "required": true}, {"label": "Duration", "column_type": "field", "field": "duration", "type": "timedelta", "required": true}, {"label": "TruckNumber", "column_type": "field", "field": "truckNumber", "type": "int", "required": true}], "formColumns": [{"column_type": "field", "field": "Id", "label": "Id", "type": "int", "required": true, "defaultValue": null}, {"column_type": "field", "field": "title", "label": "title", "type": "str", "required": true, "defaultValue": null}, {"column_type": "field", "field": "duration", "label": "duration", "type": "timedelta", "required": true, "defaultValue": null}, {"column_type": "field", "field": "truckNumber", "label": "truckNumber", "type": "int", "required": true, "defaultValue": null}, {"column_type": "lookup", "path": "album_1", "field": "album_1", "lookup_field": "Id", "entity": "Album", "type": "str", "required": true}]}} dataBinding={{"entity": "Track", "endpoint": "/track/"}} />
        <div id="i1qwlh" style={{"marginTop": "20px", "display": "flex", "--chart-color-palette": "default", "flexWrap": "wrap", "gap": "10px"}}>
          <MethodButton id="izwidt" className="action-button-component" style={{"padding": "6px 14px", "fontSize": "13px", "fontWeight": "600", "textDecoration": "none", "letterSpacing": "0.01em", "display": "flex", "cursor": "pointer", "transition": "background 0.2s", "background": "linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", "color": "#fff", "borderRadius": "4px", "border": "none", "boxShadow": "0 1px 4px rgba(37,99,235,0.10)", "--chart-color-palette": "default", "alignItems": "center"}} endpoint="/track/{track_id}/methods/getOverallDuration/" label="+ getOverallDuration" isInstanceMethod={true} instanceSourceTableId="table-track-12" />
        </div>
      </main>
    </div>    </div>
  );
};

export default Track;
