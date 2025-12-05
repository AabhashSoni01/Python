n = int(input())
for _ in range(n):
    a, b = list(map(int, input().split()))
    
    x = min(a, b)
    y = max(a, b)
    
    sum = (x + y) * (y - x + 1) // 2
    print(sum)