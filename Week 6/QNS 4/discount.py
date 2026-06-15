

TAX_RATE = 0.13  # 13% VAT - global constant


def apply_discount(price, percent):
    discount_amount = price * percent / 100
    discounted_price = price - discount_amount
    return discounted_price


def apply_tax(price):
    tax_amount = price * TAX_RATE
    final = price + tax_amount
    return final


def final_price(price, discount_pct):
    after_discount = apply_discount(price, discount_pct)
    after_tax = apply_tax(after_discount)
    return after_tax