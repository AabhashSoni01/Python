a, b = map(int, input().split())
lucky_numbers = []
for i in range(a, b + 1):
    str_i = str(i)
    if all(c in '47' for c in str_i):
        lucky_numbers.append(int(str_i))

if not lucky_numbers:
    print(-1)
else:
    print(' '.join(map(str, lucky_numbers)))