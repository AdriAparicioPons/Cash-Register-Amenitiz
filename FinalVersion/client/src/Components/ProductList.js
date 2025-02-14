import React from "react";


const ProductList = ({ products, addToCart }) => {
  return (
    <div className="product-container">
      {products.map((product) => (
        <div key={product.code} className="product-card">
          <h3>{product.name}</h3>
          <p>€{product.price.toFixed(2)}</p>
          <button onClick={() => addToCart(product)}>Add to Cart</button>
        </div>
      ))}
    </div>
  );
};

export default ProductList;
