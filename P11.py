n = int(input())
arr = []  
for x in range(n):
    SH, SM, EH, EM = map(int, input().split())   
    min = EM - SM
    hour = EH - SH  
    if min < 0:
        min += 60
        hour -= 1 
    arr.append([hour, min])   
for a, b in arr:
    print(a, b)