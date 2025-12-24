from collections import Counter
s = input()
counts = Counter(s)

alpha = "abcdefghijklmnopqrstuvwxyz"
for char in alpha:
    if counts[char] > 0:
        print(f"{char} : {counts[char]}")