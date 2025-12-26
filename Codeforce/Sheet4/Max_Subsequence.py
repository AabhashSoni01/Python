n = int(input())
s = input()
if n == 0:
    print(0)

count = 1
for i in range(1, n):
    if s[i] != s[i-1]:
        count += 1
            
print(count)