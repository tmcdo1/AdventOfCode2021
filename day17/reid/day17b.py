with open('inputs/day17.txt') as f:
    lines = f.readlines()

points = { "x": [], "y": []}
input = lines[0].strip().split()
xPointsInput = input[2]
yPointsInput = input[3]
for coord in (coord for coord in xPointsInput.strip(",")[2:].split('..')):
    points["x"].append(int(coord))
for coord in (coord for coord in yPointsInput.strip(",")[2:].split('..')):
    points["y"].append(int(coord))

maxY = 0
count = 0
for x in range(1,max(points["x"])*2):
    for y in range(min(points["y"]),max(points["x"])):
        pX = 0; pY = 0
        vX = x; vY = y
        tX = sorted(points["x"])
        tY = sorted(points["y"])
        currMaxY = pY
        done = False
        while not done and (pX < max(tX)+1 and not (vX == 0 and pX < min(tX))) and not (pX > min(tX) and pY < min(tY)):
            pX += vX
            pY += vY
            if vX > 0:
                vX -= 1
            elif vX < 0:
                vX += 1
            vY -= 1
            if pY > currMaxY:
                currMaxY = pY
            if (pX in range(min(tX),max(tX)+1)) and (pY in range(min(tY),max(tY)+1)):
                if currMaxY > maxY:
                    maxY = currMaxY
                count += 1
                done = True
            
print(count)