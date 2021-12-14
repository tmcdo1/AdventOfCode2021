lines = []
with open('inputs/day13TEST.txt') as f:
    lines = f.readlines()

paper = []
instructions = False
maxX = 0
maxY = 0
for line in lines:
    l = line.strip().split()
    if len(l) == 0:
        instructions = True
    elif not instructions:
        if l[0] > maxX:
            maxX = l[0]
        if l[1] > maxY:
            maxY = l[1]

for y in range(maxY):
    row = []
    for x in range(maxX):
        row.append('.')
    paper.append(row)

instructions = False
for line in lines:
    l = line.strip().split()
    if len(l) == 0:
        instructions = True
    elif not instructions:
        paper[l[0]][l[1]] = '#'
    else:
        direction = l[2].split('=')[0]
        value = l[2].split('=')[1]
        if direction == 'x':
            # fold right to left by value

        else:
            # fold bottom to top by value
            

count = 0
for y in paper:
    for x in paper[y]:
        if paper[y][x] == '#':
            count +=1

print(count)