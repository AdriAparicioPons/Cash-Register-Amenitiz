from pricing_rules import PricingRules

class Checkout:
    def __init__(self, pricing_rules):
        self.pricing_rules = pricing_rules
        self.items = []

    def scan(self, item_code):
        """Add an item to the basket"""
        self.items.append(item_code)

    def total(self):
        """Calculate total price with applied rules"""
        return self.pricing_rules.calculate_total(self.items)
