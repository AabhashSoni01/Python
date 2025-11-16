n = input()
firstDigit = n[0]
if firstDigit.isdigit():
    if int(firstDigit) % 2 == 0:
        print("EVEN")
    else:
        print("ODD")