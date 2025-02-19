from .base_rule import BaseRule

class BulkDiscountRule(BaseRule):
    """Bulk discount when buying a minimum quantity of an item"""
    def __init__(self, product_code, min_qty, discounted_price):
        super().__init__(product_code)
        self.min_qty = min_qty
        self.discounted_price = discounted_price

    def apply(self, items, prices):
        if items.get(self.product_code, 0) >= self.min_qty:
            prices[self.product_code] = self.discounted_price