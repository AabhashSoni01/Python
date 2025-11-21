amount = int(input())
denom = int(input())

n100 = n50 = n20 = n10 = n5 = n2 = n1 = 0

match denom:
    case 100:
        n100 = amount // 100
        amount %= 100
    case 50:
        n50 = amount // 50
        amount %= 50
    case 20:
        n20 = amount // 20
        amount %= 20
    case 10:
        n10 = amount // 10
        amount %= 10
    case 5:
        n5 = amount // 5
        amount %= 5
    case 2:
        n2 = amount // 2
        amount %= 2
    case 1:
        n1 = amount
        amount = 0

if denom > 50:
    n50 = amount // 50
    amount %= 50
if denom > 20:
    n20 = amount // 20
    amount %= 20
if denom > 10:
    n10 = amount // 10
    amount %= 10
if denom > 5:
    n5 = amount // 5
    amount %= 5
if denom > 2:
    n2 = amount // 2
    amount %= 2
if denom > 1:
    n1 = amount

print(f"50 rupees note: {n50}")
print(f"20 rupees note: {n20}")
print(f"10 rupees note: {n10}")
print(f"5 rupees note: {n5}")
print(f"2 rupees note: {n2}")
print(f"1 rupees note: {n1}")
