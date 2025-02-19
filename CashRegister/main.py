from flask import Flask, request, jsonify
import json
from checkout import Checkout
from pricing_rules.bogof_rule import BOGOFRule
from pricing_rules.bulk_dicount_rule import BulkDiscountRule
from pricing_rules.price_drop_rule import PriceDropRule


def load_products(filename="products.json"):
    """Load products from a JSON file."""
    with open(filename, "r") as file:
        data = json.load(file)
    return {product["code"]: product for product in data["products"]}

def load_pricing_rules(filename="pricing_rules.json"):
    """Load pricing rules from a JSON file."""
    with open(filename, "r") as file:
        data = json.load(file)
    
    rules = {}
    for rule in data["rules"]:
        if rule["type"] == "BOGOF":
            rules[rule["product_code"]] = BOGOFRule(rule["product_code"])
        elif rule["type"] == "BulkDiscount":
            rules[rule["product_code"]] = BulkDiscountRule(rule["product_code"], rule["min_qty"], rule["discounted_price"])
        elif rule["type"] == "PriceDrop":
            rules[rule["product_code"]] = PriceDropRule(rule["product_code"], rule["min_qty"], rule["discount_factor"])
    
    return rules

def main():
    """Main function to run the checkout system."""
    products = load_products()
    pricing_rules = load_pricing_rules()
    checkout = Checkout(pricing_rules)

    print("Welcome to the Checkout System!")
    print("Available products:")
    for code, product in products.items():
        print(f"{code}: {product['name']} - €{product['price']}")

    print("\nType 'pay' to finalize payment, 'new' to start a new order, 'remove <item code>' to remove item from the basket or 'exit' to quit.")

    while True:
        item = input("\nScan item (or type 'pay', 'new', 'exit'): ").strip().upper()

        if item == "EXIT":
            print("Exiting... Goodbye!")
            break
        elif item == "PAY":
            total = checkout.total(products)
            print(f"Total amount due: €{total:.2f}")
            print("Payment successful! Thank you for shopping.")
            checkout = Checkout(pricing_rules)  # Reset checkout for a new order
        elif item == "NEW":
            print("Starting a new order...")
            checkout = Checkout(pricing_rules) # Reset checkout
        elif item.startswith("REMOVE"):
            _, product_code = item.split()
            if product_code in products:
                checkout.remove(product_code)
                print(f"Removed {products[product_code]['name']} from cart.")
        elif item in products:
            checkout.scan(item)
            print(f"Added {products[item]['name']} to cart.")
        else:
            print("Invalid product code. Please try again.")

if __name__ == "__main__":
    main()