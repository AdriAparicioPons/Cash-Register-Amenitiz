# 🛒 Checkout System

A simple checkout system implementing pricing rules using OOP and SOLID principles.

## 🚀 Features
- **Buy One Get One Free (BOGOF)**: Green Tea
- **Bulk Discount**: Strawberries price drops to €4.50 when buying 3+
- **Price Drop**: Coffee price drops by 2/3 when buying 3+
- **Modular Pricing Rules**: Easily add new pricing rules via JSON files
- **JSON-based Products & Rules**: Easily configurable
- **Test Coverage**: Includes unit tests using `unittest`

## 📂 Project Structure

checkout_system/
│── pricing_rules/
│   │── base_rule.py
│   │── bogof_rule.py
│   │── bulk_discount_rule.py
│   │── price_drop_rule.py
│── products.json
│── pricing_rules.json
│── checkout.py
│── main.py


## 🛠️ Setup & Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/AdriAparicioPons/Cash-Register-Amenitiz.git
cd CashRegister
```

### 2️⃣ Install Dependencies


Ensure you have Python installed. Then, install any required libraries:
```sh
pip install -r requirements.txt
```


### 3️⃣ Run the Checkout System
```sh
 python main.py
 ```


 ### 4️⃣ Run Tests
```sh
 python -m unittest test_checkout.py
```


 ### 📜 Example Usage
```sh
 Welcome to the Checkout System!
Available products:
GR1: Green Tea - €3.11
SR1: Strawberries - €5.00
CF1: Coffee - €11.23

Type 'pay' to finalize payment, 'new' to start a new order, 'remove <item code>' to remove item from the basket or 'exit' to quit.

Scan item (or type 'pay', 'new', 'exit'): GR1
Added Green Tea to cart.

Scan item: GR1
Added Green Tea to cart.

Scan item: PAY
Total amount due: €3.11
Payment successful! Thank you for shopping.
```
