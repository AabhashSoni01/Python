n, m = map(int, input().split())

grid = []
for i in range(n):
    grid.append(input())

x, y = map(int, input().split())
x = x - 1
y = y - 1

for i in range(x - 1, x + 2):
    for j in range(y - 1, y + 2):
        
        # Skipping the center cell itself
        if i == x and j == y:
            continue
            
        if 0 <= i < n and 0 <= j < m:
            if grid[i][j] != 'x':
                print("no")
                exit()

print("yes")