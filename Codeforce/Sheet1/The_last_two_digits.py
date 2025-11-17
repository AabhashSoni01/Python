a, b, c, d = map(int, input().split())
last_two_digits = (a * b * c * d) % 100
print(f"{last_two_digits:02d}")