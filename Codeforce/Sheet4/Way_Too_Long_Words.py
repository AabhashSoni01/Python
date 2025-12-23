t = int(input())

for _ in range(t):
    s = input()
    if len(s) > 10:
        middle_count = len(s) - 2
        print(f"{s[0]}{middle_count}{s[-1]}")
    else:
        print(s)