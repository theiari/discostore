import React from "react";
import { TableBlock } from "../components/runtime/TableBlock";
import { MethodButton } from "../components/MethodButton";

const Artist: React.FC = () => {
  return (
    <div id="page-artist-11">
    <div id="igm12v" style={{"height": "100vh", "fontFamily": "Arial, sans-serif", "display": "flex", "--chart-color-palette": "default"}}>
      <nav id="ijb25b" style={{"width": "250px", "padding": "20px", "display": "flex", "overflowY": "auto", "background": "linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", "color": "white", "--chart-color-palette": "default", "flexDirection": "column"}}>
        <h2 id="iyj3wj" style={{"fontSize": "24px", "fontWeight": "bold", "marginTop": "0", "marginBottom": "30px", "--chart-color-palette": "default"}}>{"BESSER"}</h2>
        <div id="i4nj2u" style={{"display": "flex", "--chart-color-palette": "default", "flexDirection": "column", "flex": "1"}}>
          <a id="iktci2" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/user">{"User"}</a>
          <a id="ixfktv" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/customer">{"Customer"}</a>
          <a id="i6xwhp" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/admin">{"Admin"}</a>
          <a id="ijtq1o" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/order">{"Order"}</a>
          <a id="iop7bl" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/cart">{"Cart"}</a>
          <a id="iqip06" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/review">{"Review"}</a>
          <a id="irwclk" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/address">{"Address"}</a>
          <a id="iy0nzh" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/orderitem">{"OrderItem"}</a>
          <a id="ilpsuj" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/payment">{"Payment"}</a>
          <a id="iq80i4" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/cartitem">{"CartItem"}</a>
          <a id="iu3jef" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/album">{"Album"}</a>
          <a id="is0rie" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "rgba(255,255,255,0.2)", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/artist">{"Artist"}</a>
          <a id="it8god" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/track">{"Track"}</a>
        </div>
        <p id="iia1zi" style={{"fontSize": "11px", "paddingTop": "20px", "marginTop": "auto", "textAlign": "center", "opacity": "0.8", "borderTop": "1px solid rgba(255,255,255,0.2)", "--chart-color-palette": "default"}}>{"© 2026 BESSER. All rights reserved."}</p>
      </nav>
      <main id="itto0y" style={{"padding": "40px", "overflowY": "auto", "background": "#f5f5f5", "--chart-color-palette": "default", "flex": "1"}}>
        <h1 id="ixjgzi" style={{"fontSize": "32px", "marginTop": "0", "marginBottom": "10px", "color": "#333", "--chart-color-palette": "default"}}>{"Artist"}</h1>
        <p id="ig7p6r" style={{"marginBottom": "30px", "color": "#666", "--chart-color-palette": "default"}}>{"Manage Artist data"}</p>
        <TableBlock id="table-artist-11" styles={{"width": "100%", "minHeight": "400px", "--chart-color-palette": "default"}} title="Artist List" options={{"showHeader": true, "stripedRows": false, "showPagination": true, "rowsPerPage": 5, "actionButtons": true, "columns": [{"label": "Id", "column_type": "field", "field": "Id", "type": "int", "required": true}, {"label": "Name", "column_type": "field", "field": "name", "type": "str", "required": true}, {"label": "Bio", "column_type": "field", "field": "bio", "type": "str", "required": true}, {"label": "Country", "column_type": "field", "field": "country", "type": "str", "required": true}], "formColumns": [{"column_type": "field", "field": "Id", "label": "Id", "type": "int", "required": true, "defaultValue": null}, {"column_type": "field", "field": "name", "label": "name", "type": "str", "required": true, "defaultValue": null}, {"column_type": "field", "field": "bio", "label": "bio", "type": "str", "required": true, "defaultValue": null}, {"column_type": "field", "field": "country", "label": "country", "type": "str", "required": true, "defaultValue": null}, {"column_type": "lookup", "path": "album", "field": "album", "lookup_field": "Id", "entity": "Album", "type": "str", "required": true}]}} dataBinding={{"entity": "Artist", "endpoint": "/artist/"}} />
        <div id="ismdoa" style={{"marginTop": "20px", "display": "flex", "--chart-color-palette": "default", "flexWrap": "wrap", "gap": "10px"}}>
          <MethodButton id="i88hec" className="action-button-component" style={{"padding": "6px 14px", "fontSize": "13px", "fontWeight": "600", "textDecoration": "none", "letterSpacing": "0.01em", "display": "flex", "cursor": "pointer", "transition": "background 0.2s", "background": "linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", "color": "#fff", "borderRadius": "4px", "border": "none", "boxShadow": "0 1px 4px rgba(37,99,235,0.10)", "--chart-color-palette": "default", "alignItems": "center"}} endpoint="/artist/{artist_id}/methods/getDiscography/" label="+ getDiscography" isInstanceMethod={true} instanceSourceTableId="table-artist-11" />
        </div>
      </main>
    </div>    </div>
  );
};

export default Artist;
