id = int(input())
row = id // 4
col = id % 4
if row % 2 == 1:
    col = 3 - col
print(row, col)