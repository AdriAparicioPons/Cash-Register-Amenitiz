from flask import Flask, request, jsonify
from checkout import Checkout
from pricing_rules.bogof_rule import BOGOFRule
from pricing_rules.bulk_dicount_rule import BulkDiscountRule
from pricing_rules.price_drop_rule import PriceDropRule


app = Flask(__name__)

# Rule definition

rules = [
    BOGOFRule("GR1"),
    BulkDiscountRule("SR1", min_qty=3, discounted_price =4.50),
    PriceDropRule("CF1", min_qty=3, discount_rate=2/3),
]

checkout = Checkout(rules)

# Example Scan Items
checkout.scan("GR1")
checkout.scan("CF1")
checkout.scan("SR1")
checkout.scan("CF1")
checkout.scan("CF1")

print(f"Total price: {checkout.total()}€")  # Expected: 30.57€