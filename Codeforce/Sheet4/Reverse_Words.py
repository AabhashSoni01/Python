s = input()
words = s.split()
reversed_words = [word[::-1] for word in words]
print(*reversed_words)