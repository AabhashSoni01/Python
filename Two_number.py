a, b = map(int, input().split())

floor_val = a // b
ceil_val = -(a // -b)
round_val = (a + b // 2) // b

print(f"floor {a} / {b} = {floor_val}")
print(f"ceil {a} / {b} = {ceil_val}")
print(f"round {a} / {b} = {round_val}")
