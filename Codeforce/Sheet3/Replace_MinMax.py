n = int(input())
nums = list(map(int, input().split()))
low = min(nums)
high = max(nums)

low_id = nums.index(low)
high_id = nums.index(high)

nums[low_id], nums[high_id] = nums[high_id], nums[low_id]

print(*nums)