def last_digit(a, b):
    result = 1
    for x in range(b):
        result = result * a     
    return result % 10
        
n = int(input())
for y in range(n):
    a, b = map(int, input().split())
    print(last_digit(a, b))