t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    length = 0

    for i in range(n):
        if i > 0 and arr[i] > arr[i - 1]:
            length += 1
        else:
            length = 1
        count += length

    print(count)