a = input()
b = input()

print(len(a), len(b))
print(a + b)

new_a = b[0] + a[1:]
new_b = a[0] + b[1:]
print(new_a, new_b)