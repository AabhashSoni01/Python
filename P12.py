import math
a = int(input())
results = []  
for n in range(a):
    x, y = map(int, input().split())
    gcd = math.gcd(x, y)
    lcm = (x * y) // gcd
    results.append([gcd, lcm])  
for g, l in results:
    print(g, l)