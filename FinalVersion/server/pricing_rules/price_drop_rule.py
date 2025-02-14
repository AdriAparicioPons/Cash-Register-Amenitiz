from .base_rule import PricingRule

class PriceDropRule(PricingRule):
    def __init__(self, product_code: str, min_qty: int, discount_rate: float):
        self.product_code = product_code
        self.min_qty = min_qty
        self.discount_rate = discount_rate
    def apply(self, items: dict, products: dict)->float:
        if self.product_code in items:
            count = items[self.product_code]
            price = products[self.product_code].price* self.discount_rate if count >= self.min_qty else products[self.product_code].price
            return count * price
        return 0