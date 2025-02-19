import unittest
from checkout import Checkout
from pricing_rules.bogof_rule import BOGOFRule
from pricing_rules.bulk_dicount_rule import BulkDiscountRule
from pricing_rules.price_drop_rule import PriceDropRule

class TestCheckout(unittest.TestCase):
    def setUp(self):
        """Set up a new checkout instance with pricing rules and products."""
        self.products = {
            "GR1": {"name": "Green Tea", "price": 3.11},
            "SR1": {"name": "Strawberries", "price": 5.00},
            "CF1": {"name": "Coffee", "price": 11.23}
        }
        self.rules = {
            "GR1": BOGOFRule("GR1"),
            "SR1": BulkDiscountRule("SR1", min_qty=3, discounted_price=4.50),
            "CF1": PriceDropRule("CF1", min_qty=3, discount_factor=0.6667)
        }
        self.checkout = Checkout(self.rules)

    def test_bogof_rule(self):
        """Test Buy One Get One Free for Green Tea."""
        self.checkout.scan("GR1")
        self.checkout.scan("GR1")
        total = self.checkout.total(self.products)
        self.assertEqual(total, 3.11)

    def test_bulk_discount_rule(self):
        """Test bulk discount for Strawberries."""
        self.checkout.scan("SR1")
        self.checkout.scan("SR1")
        self.checkout.scan("GR1")
        self.checkout.scan("SR1")
        total = self.checkout.total(self.products)
        self.assertEqual(total, 16.61)

    def test_price_drop_rule(self):
        """Test price drop for Coffee when buying 3 or more."""
        self.checkout.scan("GR1")
        self.checkout.scan("CF1")
        self.checkout.scan("SR1")
        self.checkout.scan("CF1")
        self.checkout.scan("CF1")
        total = self.checkout.total(self.products)
        self.assertEqual(total, 30.57)

    def test_empty_basket(self):
        """Test total price when no items are scanned."""
        total = self.checkout.total(self.products)
        self.assertEqual(total, 0.00)

if __name__ == "__main__":
    unittest.main()