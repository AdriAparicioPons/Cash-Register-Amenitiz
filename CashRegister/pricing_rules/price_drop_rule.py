from .base_rule import BaseRule

class PriceDropRule(BaseRule):
    """Price drop when buying a minimum quantity of an item"""
    def __init__(self, product_code, min_qty, discount_factor):
        super().__init__(product_code)
        self.min_qty = min_qty
        self.discount_factor = discount_factor

    def apply(self, items, prices):
        if items.get(self.product_code, 0) >= self.min_qty:
            prices[self.product_code] *= self.discount_factor
