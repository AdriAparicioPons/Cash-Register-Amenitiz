import unittest
from checkout import Checkout
from pricing_rules.bogof_rule import BOGOFRule
from pricing_rules.bulk_dicount_rule import BulkDiscountRule
from pricing_rules.price_drop_rule import PriceDropRule

class TestCheckout(unittest.TestCase):
    def setUp(self):
        rules = [
            BOGOFRule("GR1"),
            BulkDiscountRule("SR1", 3, 4.50),
            PriceDropRule("CF1", 3, 2/3),
        ]
        self.checkout = Checkout(rules)

    def test_green_tea_bogo(self):
        self.checkout.scan("GR1")
        self.checkout.scan("GR1")
        self.assertEqual(self.checkout.total(), 3.11)

    def test_strawberries_bulk_discount(self):
        self.checkout.scan("SR1")
        self.checkout.scan("SR1")
        self.checkout.scan("GR1")
        self.checkout.scan("SR1")
        self.assertEqual(self.checkout.total(), 16.61)

    def test_coffee_bulk_discount(self):
        self.checkout.scan("GR1")
        self.checkout.scan("CF1")
        self.checkout.scan("SR1")
        self.checkout.scan("CF1")
        self.checkout.scan("CF1")
        self.assertEqual(self.checkout.total(), 30.57)

if __name__ == "__main__":
    unittest.main()