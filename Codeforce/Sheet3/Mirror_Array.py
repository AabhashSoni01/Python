n, m = map(int, input().split())

for _ in range(n):
    arr = list(map(int, input().split()))
    rev = arr[::-1]
    print(*rev)