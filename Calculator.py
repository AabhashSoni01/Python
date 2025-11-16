expr = input()

for op in "+-*/":
    if op in expr:
        s = op
        break

a, b = expr.split(s)
a = int(a)
b = int(b)

if s == "+":
    print(a + b)
elif s == "-":
    print(a - b)
elif s == "*":
    print(a * b)
else:
    print(a // b)