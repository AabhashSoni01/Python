n = int(input())
a, b = 0, 1
result = []

for i in range(1, n + 1):
    if i == 1:
        result.append(a)
    elif i == 2:
        result.append(b)
    else:
        c = a + b
        result.append(c)
        a, b = b, c

print(*result)