n = int(input())
nums = []

for i in range(n):
    nums.append(input().strip())

for j in nums:
    print(*j[::-1])