t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    if n % 2 != 0:
        print(-1)
        continue

    odd_count = 0
    for x in arr:
        if x % 2 != 0:
            odd_count += 1

    target = n // 2
    ans = abs(odd_count - target)

    print(ans)