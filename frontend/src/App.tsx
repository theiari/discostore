import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import { TableProvider } from "./contexts/TableContext";
import User from "./pages/User";
import Cartitem from "./pages/Cartitem";
import Album from "./pages/Album";
import Artist from "./pages/Artist";
import Track from "./pages/Track";
import Customer from "./pages/Customer";
import Admin from "./pages/Admin";
import Order from "./pages/Order";
import Cart from "./pages/Cart";
import Review from "./pages/Review";
import Address from "./pages/Address";
import Orderitem from "./pages/Orderitem";
import Payment from "./pages/Payment";

function App() {
  return (
    <TableProvider>
      <div className="app-container">
        <main className="app-main">
          <Routes>
            <Route path="/user" element={<User />} />
            <Route path="/cartitem" element={<Cartitem />} />
            <Route path="/album" element={<Album />} />
            <Route path="/artist" element={<Artist />} />
            <Route path="/track" element={<Track />} />
            <Route path="/customer" element={<Customer />} />
            <Route path="/admin" element={<Admin />} />
            <Route path="/order" element={<Order />} />
            <Route path="/cart" element={<Cart />} />
            <Route path="/review" element={<Review />} />
            <Route path="/address" element={<Address />} />
            <Route path="/orderitem" element={<Orderitem />} />
            <Route path="/payment" element={<Payment />} />
            <Route path="/" element={<Navigate to="/user" replace />} />
            <Route path="*" element={<Navigate to="/user" replace />} />
          </Routes>
        </main>
      </div>
    </TableProvider>
  );
}
export default App;
