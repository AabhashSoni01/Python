n = input()

if '.' not in n:
    print("int", n)
else:
    a, b = n.split('.')
    if int(b) == 0:
        print("int", a)
    else:
        print("float", a, "0." + b if b[0] != '0' else b.rstrip('0'))