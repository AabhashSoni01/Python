ch = input()
# after z -> a
if ch == 'z':
    print('a')
    exit()
else:    
    next_ch = chr(ord(ch) + 1)
    print(next_ch)