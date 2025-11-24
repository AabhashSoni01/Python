while True:
    n, m = map(int, input().split())
    if n <= 0 or m <= 0:
        break
    x = min(n, m)
    y = max(n, m)
    num = list(range(x, y + 1))
    total = sum(num)
    print(*num, f"sum ={total}")