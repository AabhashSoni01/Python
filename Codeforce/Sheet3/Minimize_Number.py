n = int(input())
arr = list(map(int, input().split()))
count = 0

while True:
    even = True
    for i in arr:
        if i % 2 != 0:
            even = False
            break
    
    if not even:
        break

    for j in range(n):
        arr[j] //= 2
    count += 1

print(count)