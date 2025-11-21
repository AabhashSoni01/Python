def reverse_num(x):
    return int(str(x)[::-1])

n = int(input())
answers = []

for x in range(n):
    a, b = input().split()
    a = reverse_num(a)
    b = reverse_num(b)
    s = a + b
    answers.append(reverse_num(s))

for ans in answers:
    print(ans)