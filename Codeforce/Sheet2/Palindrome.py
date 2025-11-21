a = int(input())
is_palindrome = True
n = str(a)
for i in range(len(n) // 2):
    if n[i] != n[len(n) - 1 - i]:
        is_palindrome = False
        break
if is_palindrome:
    print(n)
    print("YES")
else:
    print(int(n[::-1]))
    print("NO")