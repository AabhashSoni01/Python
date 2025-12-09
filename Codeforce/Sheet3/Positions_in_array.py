n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    if arr[i] <= 10:
        print("A[" + str(i) + "]", "=", arr[i])