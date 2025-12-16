n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

j = 0

for i in range(n):
    if j < m and a[i] == b[j]:
        j += 1       
    if j == m:
        break

if j == m:
    print("YES")
else:
    print("NO")