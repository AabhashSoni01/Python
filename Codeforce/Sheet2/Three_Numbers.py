k, s = map(int, input().split())
ans = 0

for x in range(k + 1):

    target_sum = s - x
    
    if target_sum >= 0:
        min_y = max(0, target_sum - k)
        max_y = min(k, target_sum)

        if max_y >= min_y:
            ans += (max_y - min_y + 1)

print(ans)