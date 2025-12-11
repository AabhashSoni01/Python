t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = []

    for i in range(n):
        current_max = arr[i]
            
        for j in range(i, n):
            if arr[j] > current_max:
                current_max = arr[j]
            result.append(current_max)
        
    print(*result)