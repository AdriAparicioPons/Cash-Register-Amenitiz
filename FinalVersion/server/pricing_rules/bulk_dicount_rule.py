from .base_rule import PricingRule

class BulkDiscountRule(PricingRule):
    def __init__(self, product_code:str, min_qty: int, discounted_price: float):
        self.product_code = product_code
        self.min_qty = min_qty
        self.discounted_price = discounted_price

    def apply( self, items: dict, products: dict) -> float:
        if self.product_code in items:
            count = items[self.product_code]
            price = self.discounted_price if count >= self.min_qty else products[self.product_code].price
            return count * price
        return 0