n, m = map(int, input().split())

matrix = []
for i in range(n):
    r = list(map(int, input().split()))
    matrix.append(r)

x = int(input())
found = False

for r in matrix:
    if x in r:
        found = True
        break

if found:
    print("will not take number")
else:
    print("will take number")