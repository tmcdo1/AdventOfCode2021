lines = []
with open('inputs/day10.txt') as f:
    lines = f.readlines()

grid = []
i = 0
for line in lines:
    grid.append(list(line.strip()))
    i += 1

sumRisk = 0
for y in range(0, len(grid)):
    for x in range(0, len(grid[y])):
        lowPoint = True
        if y < len(grid)-1 and int(grid[y][x]) >= int(grid[y+1][x]):
            lowPoint = False
        if y > 0 and int(grid[y][x]) >= int(grid[y-1][x]):
            lowPoint = False
        if x < len(grid[y])-1 and int(grid[y][x]) >= int(grid[y][x+1]):
            lowPoint = False
        if x > 0 and int(grid[y][x]) >= int(grid[y][x-1]):
            lowPoint = False
        if lowPoint:
            sumRisk += int(grid[y][x]) + 1

print(sumRisk)