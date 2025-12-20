n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1
result = []

while left <= right:
    result.append(arr[left])
    if left != right:
        result.append(arr[right])
    left += 1
    right -= 1

print(*result)