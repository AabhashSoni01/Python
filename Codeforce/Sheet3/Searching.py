n = int(input())
arr = list(map(int, input().split()))
x = int(input())

matched = False

for i in range(n):
    if arr[i] == x:
        print(i)
        matched = True
        break

if not matched:
    print("-1")