import React from "react";


const Cart = ({ cart, total, removeFromCart }) => {
  return (
    <div className="cart-container">
      <h2>Shopping Cart</h2>
      {cart.length === 0 ? (
        <p>Your cart is empty.</p>
      ) : (
        <>
          <ul>
            {cart.map((item, index) => (
              <li key={index}>
                {item.name}
                <button onClick={() => removeFromCart(item.code)}>Remove</button>
              </li>
            ))}
          </ul>
          <p className="total-price">Total: €{total}</p>
        </>
      )}
    </div>
  );
};

export default Cart;
