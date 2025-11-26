n = int(input())
for _ in range(n):
    x = int(input())
    total_ones = bin(x).count('1')
    ans = (1 << total_ones) - 1
    print(ans)