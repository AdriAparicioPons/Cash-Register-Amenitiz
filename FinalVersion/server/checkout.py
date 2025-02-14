from models.product import Product

class Checkout:
    def __init__(self, pricing_rules):
        self.pricing_rules = pricing_rules
        self.items = {}

       #Product Definition

        self.products = {
             "GR1": Product("GR1", "Green Tea", 3.11),
            "SR1": Product("SR1", "Strawberries", 5.00),
            "CF1": Product("CF1", "Coffee", 11.23),
        }
    
    def scan(self, item_code):
        #Add item to basket
        if item_code in self.products:
            self.items[item_code] = self.items.get(item_code,0)+1
    
    def total(self):
        #Calculate total w/ pricing rules
        total = 0
        for rule in self.pricing_rules:
            total += rule.apply(self.items, self.products)
        return round(total, 2)