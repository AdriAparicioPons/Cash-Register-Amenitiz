# Checkout System

## Overview
This project implements a checkout system with special pricing rules.

## Installation
1. Clone the repository: https://github.com/AdriAparicioPons/Cash-Register-Amenitiz.git

2. Install dependencies (if needed).

## Usage

cd Version1

```python
from checkout import Checkout
from pricing_rules import PricingRules

rules = PricingRules()
checkout = Checkout(rules)

checkout.scan("GR1")
checkout.scan("GR1")

print(checkout.total())  # Expected Output: 3.11
