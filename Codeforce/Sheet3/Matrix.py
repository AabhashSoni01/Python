n = int(input())
matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

primary = secondary = 0

for i in range(n):
    primary += matrix[i][i]
    secondary += matrix[i][n - i - 1]

print(abs(primary - secondary))