a, b = map(int, input().split())
if abs(a - b) <= 1 and a + b >= 1:
   print("YES")
else:
    print("NO")