n = int(input())
a = n // 10
b = n % 10

val = False

if b != 0 and a % b == 0:
    val = True
elif a != 0 and b % a == 0:
    val = True

print("YES" if val else "NO")