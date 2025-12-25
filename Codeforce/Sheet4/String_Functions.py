n, q = map(int, input().split())
s = list(input().strip())

for _ in range(q):
    line = input().split()
    cmd = line[0]

    if cmd == "pop_back":
        s.pop()
    elif cmd == "front":
        print(s[0])
    elif cmd == "back":
        print(s[-1])
    elif cmd == "push_back":
        s.append(line[1])
    elif cmd == "print":
        print(s[int(line[1]) - 1])
    else:
        l_in = int(line[1])
        r_in = int(line[2])
        
        start = min(l_in, r_in) - 1
        end = max(l_in, r_in)
        
        if cmd == "substr":
            print("".join(s[start:end]))
        else:
            sub = s[start:end]
            if cmd == "sort":
                sub.sort()
            elif cmd == "reverse":
                sub.reverse()
            
            s[start:end] = sub