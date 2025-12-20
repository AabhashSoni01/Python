n = int(int(input()))
arr = list(map(int, input().split()))

arr_set = set(arr)
count = 0

for i in arr:
    if (i + 1) in arr_set:
        count += 1

print(count)