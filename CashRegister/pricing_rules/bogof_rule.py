from .base_rule import BaseRule

class BOGOFRule(BaseRule):
    def apply(self, items, prices):
        count = items.get(self.product_code, 0)
        if count > 1:
            discount_items = count // 2  # Every second item is free
            prices[self.product_code] -= discount_items * prices[self.product_code] / count