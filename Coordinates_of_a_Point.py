x, y = map(float, input().split())

if x == y == 0:
    print("Origem")
elif x == 0:
    print("Eixo Y")
elif y == 0:
    print("Eixo X")
else:
    print(
        "Q1" if x > 0 and y > 0 else
        "Q2" if x < 0 and y > 0 else
        "Q3" if x < 0 and y < 0 else
        "Q4"
    )
