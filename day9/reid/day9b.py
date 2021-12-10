def recur(grid, y, x, visited):
    print(visited)
    if y < len(grid)-1 and grid[y+1][x] != '9' and str(y+1)+str(x) not in visited:
        visited.append(str(y+1) + str(x))
        recur(grid, y+1, x, visited)
    if y > 0 and grid[y-1][x] != '9' and str(y-1)+str(x) not in visited:
        visited.append(str(y-1) + str(x))
        recur(grid, y-1, x, visited)
    if x < len(grid[y])-1 and grid[y][x+1] != '9' and str(y)+str(x+1) not in visited:
        visited.append(str(y) + str(x+1))
        recur(grid, y, x+1, visited)
    if x > 0 and grid[y][x-1] != '9' and str(y)+str(x-1) not in visited:
        visited.append(str(y) + str(x-1))
        recur(grid, y, x-1, visited)

lines = []
with open('inputs/day9.txt') as f:
    lines = f.readlines()

grid = []
i = 0
for line in lines:
    grid.append(list(line.strip()))
    i += 1

firstBasin = 1
secondBasin = 1
thirdBasin = 1
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
            visited = []
            visited.append(str(y) + str(x))
            recur(grid, y, x, visited)
            if len(visited) > thirdBasin:
                thirdBasin = len(visited)
                if len(visited) > secondBasin:
                    thirdBasin = secondBasin
                    secondBasin = len(visited)
                if len(visited) > firstBasin:
                    secondBasin = firstBasin
                    firstBasin = len(visited)

print(firstBasin*secondBasin*thirdBasin)
