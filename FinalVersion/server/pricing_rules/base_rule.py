from abc import ABC, abstractmethod

class PricingRule(ABC):
    @abstractmethod
    def apply(self, items: dict, products: dict)-> float:
        pass