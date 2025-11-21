n = int(input())
if n < 2:
    print("-1")
else:
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)