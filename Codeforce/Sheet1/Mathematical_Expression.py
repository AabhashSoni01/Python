a, s, b, q, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if s == '+':
    if q == '=':
        if a + b == c:
            print("Yes")
        else:
            print(a + b)
elif s == '-':
    if q == '=':
        if a - b == c:
            print("Yes")
        else:
            print(a - b)
elif s == '*':
    if q == '=':
        if a * b == c:
            print("Yes")
        else:
            print(a * b)