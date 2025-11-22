s = input().strip()
n = int(input().strip())
numbers = list(map(int, input().strip().split()))
for x in numbers:
    print(s * x)