s = input()

s = s.replace('!', ' ')
s = s.replace('.', ' ')
s = s.replace('?', ' ')
s = s.replace(',', ' ')

words = s.split()
print(len(words))