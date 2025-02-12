import unittest
from checkout import Checkout
from pricing_rules import PricingRules

class TestCheckout(unittest.TestCase):
    def setUp(self):
        self.rules = PricingRules()
        self.checkout = Checkout(self.rules)

    def test_green_tea_bogo(self):
        self.checkout.scan("GR1")
        self.checkout.scan("GR1")
        self.assertEqual(self.checkout.total(), 3.11)  # BOGO applies

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
