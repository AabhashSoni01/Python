n = int(input())
nums = list(map(int, input().split()))

max_div = 0

for x in nums:
    count = 0
    while x > 0 and x % 2 == 0:
        count += 1
        x //= 2

    if count > max_div:
        max_div = count

print(max_div)