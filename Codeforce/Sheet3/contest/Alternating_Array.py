n = int(input())
arr = list(map(int, input().split()))

op = 0

for i in range(n):
        if i % 2 == 0:
            if arr[i] < 0:
                op += 1
        else:
            if arr[i] > 0:
                op += 1

print(min(op, n - op))