n = int(input())
for _ in range(n):
    nums = input().split()
    x = int(nums[0])
    y = int(nums[1])

    max_sum = x * (x + 1) // 2
    if y > max_sum:
        print("-1")
        continue

    result = []
    current = x

    while y > 0:
        if y < current:
            result.append(y)
            break

        result.append(current)
        y -= current
        current -= 1

    print(*result)