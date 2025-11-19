a, b, k = map(int, input().split())

x = (a % k == 0)
y = (b % k == 0)

if x and y:
    print("Both")
elif x:
    print("Memo")
elif y:
    print("Momo")
else:
    print("No One")