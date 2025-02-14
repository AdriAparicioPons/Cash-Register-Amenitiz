const API_URL = "http://127.0.0.1:8080";
export async function fetchProducts() {
  return [
    { code: "GR1", name: "Green Tea", price: 3.11 },
    { code: "SR1", name: "Strawberries", price: 5.0 },
    { code: "CF1", name: "Coffee", price: 11.23 },
  ];
}

export async function calculateTotal(cart) {
  const response = await fetch(`${API_URL}/calculate-total`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ cart }),
  });
  return response.json();
}
