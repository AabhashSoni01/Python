n = int(input())
for i in range(n):
    a, b = map(int, input().split())

    x = min(a, b)
    y = max(a, b)

    sum = 0

    for num in range(x + 1, y):
        if num % 2 != 0:
           sum += num

    print(sum)