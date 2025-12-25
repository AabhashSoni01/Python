import sys

s = input()
target = "hello"
idx = 0

for char in s:
    if char == target[idx]:
        idx += 1
        if idx == 5:
            print("YES")
            sys.exit()

print("NO")