n, a, b = map(int, input().split())

total = 0

for i in range(1, n + 1):
    digit_sum = sum(map(int, str(i)))
    if a <= digit_sum <= b:
        total += i

print(total)