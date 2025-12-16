n, m = map(int, input().split())
arr = list(map(int, input().split()))

# frequency list of size m + 1 initialized to 0, like [0,0,0,0] suppose m = 3 
count = [0] * (m + 1)

# using the number itself as the address (index) for where to store its count
for i in arr:
    count[i] += 1

for j in range(1, m + 1):
    print(count[j])