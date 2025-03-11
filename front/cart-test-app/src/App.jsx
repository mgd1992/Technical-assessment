import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [products, setProducts] = useState([]);
  const [cart, setCart] = useState([]);
  const [total, setTotal] = useState(0);
  const [finalTotal, setFinalTotal] = useState(0);

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/products")
      .then(res => setProducts(res.data))
      .catch(err => console.error("Error obteniendo productos", err));

    fetchCart();
  }, []);

  const fetchCart = () => {
    axios.get("http://127.0.0.1:5000/cart")
      .then(response => {
        setCart(response.data.cart);
        setTotal(response.data.total);
      })
      .catch(error => console.error("Error obteniendo el carrito", error));
  };

  const addToCart = (product) => {
    axios.post("http://127.0.0.1:5000/cart", product)
      .then(response => {
        setCart(response.data.cart);
        setTotal(response.data.total);
      })
      .catch(error => console.error("Error agregando al carrito", error));
  };

  const clearCart = () => {
    axios.post("http://127.0.0.1:5000/cart/clear")
      .then(() => {
        setCart([]);
        setTotal(0);
        setFinalTotal(0);
      })
      .catch(error => console.error("Error vaciando el carrito", error));
  };

  const calculateTotalToPay = () => {
    axios.get("http://127.0.0.1:5000/cart")
      .then(res => {
        setFinalTotal(res.data.total);
      })
      .catch(error => console.error("Error calculando total a pagar", error));
  };

  return (
    <div className="cart">
      <h1>🛒 Online Shop</h1>
      <div className="main-cart">

        <div className="prod">
          <h2>Products</h2>
          <ul>
            {products.map((product) => (
              <li key={product.code}>
                {product.name} - €{product.price}
                <button onClick={() => addToCart(product)}>Add</button>
              </li>
            ))}
          </ul>
        </div>

        <div className="cart-prod">
          <h2>Carrito</h2>
          {cart.length === 0 ? <p>El carrito está vacío</p> : (
            <ul>
              {cart.map((item, index) => (
                <li key={index}>{item.name} - €{item.price}</li>
              ))}
            </ul>
          )}
          <p>Total: ${total}</p>
          <button onClick={clearCart}>Vaciar Carrito</button>
        </div>


      </div>
      <div className="total">
        <button onClick={calculateTotalToPay}>Total a Pagar</button>
        {finalTotal > 0 && (
          <div className="total-pagar">
            <h3>Total a Pagar: ${finalTotal}</h3>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
