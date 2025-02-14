import React, { useEffect, useState } from "react";
import ProductList from "./Components/ProductList";
import Cart from "./Components/Cart";
import { fetchProducts, calculateTotal } from "./api";


function App() {
  const [products, setProducts] = useState([]);
  const [cart, setCart] = useState([]);
  const [total, setTotal] = useState(0);

  useEffect(() => {
    async function loadProducts() {
      const data = await fetchProducts();
      setProducts(data);
    }
    loadProducts();
  }, []);

  useEffect(() => {
    async function updateTotal() {
      const result = await calculateTotal(cart);
      setTotal(result.total);
    }
    updateTotal();
  }, [cart]);

  const addToCart = (product) => {
    setCart([...cart, product]);
  };

  const removeFromCart = (code) => {
    setCart(cart.filter((item) => item.code !== code));
  };

  return (
    <div className="container">
      <h1>Checkout System</h1>
      <ProductList products={products} addToCart={addToCart} />
      <Cart cart={cart} total={total} removeFromCart={removeFromCart} />
    </div>
  );
}

export default App;
