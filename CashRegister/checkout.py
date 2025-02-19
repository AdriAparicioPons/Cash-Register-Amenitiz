from decimal import Decimal
class Checkout:
    """Checkout system that applies pricing rules dynamically."""
    
    def __init__(self, pricing_rules):
        self.pricing_rules = pricing_rules  # Dictionary of pricing rules
        self.items = {}  # Tracks scanned items
        self.prices = {}  # Stores individual item prices

    def scan(self, product_code):
        """Adds a product to the basket."""
        if product_code not in self.items:
            self.items[product_code] = 0
        self.items[product_code] += 1

    def remove(self, product_code):
        """Removes a product from the basket."""
        if product_code in self.items:
            if self.items[product_code] > 1:
                self.items[product_code] -= 1
            else:
                del self.items[product_code]

    def apply_pricing_rules(self, products):
        """Applies pricing rules to adjust product prices dynamically."""
        self.prices = {code: Decimal(products[code]["price"]) for code in self.items}

        for rule in self.pricing_rules.values():
            if rule.product_code in self.items:
                rule.apply(self.items, self.prices)

    def total(self, products):
        """Calculates the total price after applying pricing rules."""
        self.apply_pricing_rules(products)
        total_price = sum(Decimal(self.prices[code]) * self.items[code] for code in self.items)
        return total_price.quantize(Decimal('0.01'))  # Round to 2 decimal places
