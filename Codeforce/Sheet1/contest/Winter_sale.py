x, p = map(float, input().split())
original_price = p / (1 - x / 100)
print(f"{original_price:.2f}")