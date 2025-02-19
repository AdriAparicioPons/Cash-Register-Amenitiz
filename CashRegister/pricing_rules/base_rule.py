from abc import ABC, abstractmethod

class BaseRule(ABC):
    """Abstract base class for pricing rules"""
    
    def __init__(self, product_code):
        self.product_code = product_code

    @abstractmethod
    def apply(self, items, prices):
        """Applies the pricing rule to the basket"""
        pass