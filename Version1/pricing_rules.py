class PricingRules:
    PRICES = {
        "GR1": 3.11,
        "SR1": 5.00,
        "CF1": 11.23
    }

    def calculate_total(self, items):
        item_counts = {item: items.count(item) for item in set(items)}
        total = 0

        # Apply BOGO for Green Tea (GR1)
        if "GR1" in item_counts:
            total += (item_counts["GR1"] // 2 + item_counts["GR1"] % 2) * self.PRICES["GR1"]

        # Apply Bulk Discount for Strawberries (SR1)
        if "SR1" in item_counts:
            strawberry_price = 4.50 if item_counts["SR1"] >= 3 else self.PRICES["SR1"]
            total += item_counts["SR1"] * strawberry_price

        # Apply Bulk Discount for Coffee (CF1)
        if "CF1" in item_counts:
            coffee_price = self.PRICES["CF1"] * (2/3) if item_counts["CF1"] >= 3 else self.PRICES["CF1"]
            total += item_counts["CF1"] * coffee_price

        return round(total, 2)
