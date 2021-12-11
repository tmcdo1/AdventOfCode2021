totalFlashes = 0
grid = []
gridStatus = []

def bumpEnergy(y, x):
    global totalFlashes
    global grid
    global gridStatus
    if grid[y][x] < 9 and gridStatus[y][x] == True:
        grid[y][x] += 1
    elif grid[y][x] == 9:
        totalFlashes += 1
        grid[y][x] = 0
        gridStatus[y][x] = False
        if y > 0 and x > 0:
            bumpEnergy(y-1, x-1)
        if y > 0:
            bumpEnergy(y-1, x)
        if y > 0 and x < len(grid[y])-1:
            bumpEnergy(y-1, x+1)
        if x > 0:
            bumpEnergy(y, x-1)
        if x < len(grid[y])-1:
            bumpEnergy(y, x+1)
        if y < len(grid)-1 and x > 0:
            bumpEnergy(y+1, x-1)
        if y < len(grid)-1:
            bumpEnergy(y+1, x)
        if y < len(grid)-1 and x < len(grid[y])-1:
            bumpEnergy(y+1, x+1)

lines = []
with open('inputs/day11.txt') as f:
    lines = f.readlines()

for line in lines:
    arr1 = []
    arr2 = []
    for c in list(line.strip()):
        arr1.append(int(c))
        arr2.append(True)
    grid.append(arr1)
    gridStatus.append(arr2)

step = 0
allFlashed = False
while not allFlashed:
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            gridStatus[y][x] = True
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            bumpEnergy(y, x)
    allFlashed = True
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != 0:
                allFlashed = False
    step += 1

print(step)