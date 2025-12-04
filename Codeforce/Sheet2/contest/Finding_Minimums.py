n, k = map(int, input().split())

nums = list(map(int, input().split()))

arr = []

for i in range(0, n, k):
    grp = nums[i : i + k]
    arr.append(min(grp))

print(*arr)