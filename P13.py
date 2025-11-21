n = int(input())
move = [] 
i = 1
while n > 0:
    r = min(i, n)
    n -= r
    move.append(["Ramesh", r])
    if n == 0:
        break
    s = min(2 * i, n)
    n -= s
    move.append(["Suresh", s])
    if n == 0:
        break
    i += 1
win = move[-1][0]
print(win)