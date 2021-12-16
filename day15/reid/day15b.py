def neighbor(node):
    x = node % len(lines); y = int(node / len(lines))
    points = [(y-1,x), (y,x-1), (y,x+1), (y+1,x)]
    return set([node[0] * len(lines) + node[1] for node in points if node[1] >= 0 and node[1] < len(lines) and node[0] >= 0 and node[0] < len(lines)])

with open('inputs/day15.txt') as f:
    originallines = f.readlines()

lines = []
for line in originallines:
    buff = []
    for x in range(5):
        for l in line.strip():
            if int(l)+x > 9:
                buff.append(int(l)+x-9)
            else:
                buff.append(int(l)+x)
    lines.append(buff)
for y in range(1,5):
    for line in lines[0:len(originallines)]:
        buff = []
        for l in line:
            if l+y > 9:
                buff.append(l+y-9)
            else:
                buff.append(l+y)
        lines.append(buff)

grid = []
tentativeTotals = []
for line in lines:
    for l in line:
        grid.append(l)
        tentativeTotals.append(len(lines)*len(lines))
visited = set(range(len(lines) * len(lines)))

currentNode = 0
tentativeTotals[0] = 0
done = False
while not done:
    for n in neighbor(currentNode):
        if tentativeTotals[n] > tentativeTotals[currentNode] + grid[n]:
            tentativeTotals[n] = tentativeTotals[currentNode] + grid[n]
    if len(visited) == 0:
        done = True
    else:
        currentNode = visited.pop()

print(tentativeTotals[len(grid)-1]-grid[len(grid)-1])