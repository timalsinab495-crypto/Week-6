
from discount import final_price, TAX_RATE

print("TAX_RATE imported:", TAX_RATE)
print()

products = [
    ("Laptop", 85000, 10),
    ("Headphones", 4500, 15),
    ("Phone Case", 800, 5),
    ("USB Cable", 600, 0),
]

print("---- Product Prices ----")
for name, price, discount in products:
    final = final_price(price, discount)
    print(name, "| Original: NPR", price, "| Final Price: NPR", round(final, 2))