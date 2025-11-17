l1, r1, l2, r2 = map(int, input().split())
x = max(l1, l2)
y = min(r1, r2)
if x > y:
    print(-1)
else:
    print(x, y)