n = int(input())

for _ in range(n):
    s, t = input().split()
    max_len = max(len(s), len(t))
    result = []

    for i in range(max_len):
        if i < len(s):
            result.append(s[i])
        if i < len(t):
            result.append(t[i])
    
    print("".join(result))