lines = []
with open('inputs/day5.txt') as f:
    lines = f.readlines()

strippedLines = []
for line in lines:
    strippedLines.append(line.strip())

grid = []
for y in range(1000):
    row = []
    for r in range(1000):
        row.append(0)
    grid.append(row)

total = 0
for line in strippedLines:
    coordinates = line.split(" -> ")
    buff = coordinates[0].split(",")
    x1 = int(buff[0])
    y1 = int(buff[1])
    buff = coordinates[1].split(",")
    x2 = int(buff[0])
    y2 = int(buff[1])
    if x1 == x2:
        if y2 > y1:
            for y in range(y2-y1+1):
                grid[x1][y+y1] += 1
                if grid[x1][y+y1] == 2:
                    total += 1
        elif y1 > y2:
            for y in range(y1-y2+1):
                grid[x1][y+y2] += 1
                if grid[x1][y+y2] == 2:
                    total += 1
    elif y1 == y2:
        if x2 > x1:
            for x in range(x2-x1+1):
                grid[x+x1][y1] += 1
                if grid[x+x1][y1] == 2:
                    total += 1
        elif x1 > x2:
            for x in range(x1-x2+1):
                grid[x+x2][y1] += 1
                if grid[x+x2][y1] == 2:
                    total += 1

print(total)