eye, mouth, body = map(int, input().split())
x = min(eye, body)
if x <= mouth:
    print(x)
else:
    print(min(body, (eye + mouth) // 2))