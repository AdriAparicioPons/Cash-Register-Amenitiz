from .base_rule import PricingRule

class BOGOFRule(PricingRule):
    def __init__(self, product_code: str):
        self.product_code = product_code

    def apply(self, items: dict, products:dict) -> float:
        if self.product_code in items:
            count = items[self.product_code]
            price = products[self.product_code].price
            return (count // 2+ count % 2)* price
        return 0