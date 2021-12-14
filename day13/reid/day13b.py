lines = []
with open('inputs/day13.txt') as f:
    lines = f.readlines()

paper = []
instructions = False
maxX = 0
maxY = 0
for line in lines:
    if line.strip() == '':
        instructions = True
    elif not instructions:
        l = line.strip().split(',')
        if int(l[0]) > maxX:
            maxX = int(l[0])
        if int(l[1]) > maxY:
            maxY = int(l[1])

for y in range(maxY+1):
    row = []
    for x in range(maxX+1):
        row.append('.')
    paper.append(row)

instructions = False
for line in lines:
    if line.strip() == '':
        instructions = True
    elif not instructions:
        l = line.strip().split(',')
        paper[int(l[1])][int(l[0])] = '#'
    else:
        l = line.strip().split()
        direction = l[2].split('=')[0]
        value = int(l[2].split('=')[1])
        if direction == 'x':
            # fold right to left by value
            idx = value+1
            while idx < maxX+1:
                y = 0
                while y < maxY+1:
                    if paper[y][idx] == '#':
                        reflectedIdx = (value-1)-(idx-value-1)
                        if reflectedIdx >=0: 
                            paper[y][reflectedIdx] = '#'
                    y+=1
                idx+=1
            maxX = value-1
        else:
            # fold bottom to top by value
            idx = value+1
            while idx < maxY+1:
                x = 0
                while x < maxX+1:
                    if paper[idx][x] == '#':
                        reflectedIdx = (value-1)-(idx-value-1)
                        if reflectedIdx >=0: 
                            paper[reflectedIdx][x] = '#'
                    x+=1
                idx+=1
            maxY = value-1

for y in paper[0:maxY+1]:
    s = ''
    for x in y[0:maxX+1]:
        s = s + x
    print(s)