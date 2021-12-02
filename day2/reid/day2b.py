lines = []
with open('inputs/day2.txt') as f:
    lines = f.readlines()

x = 0
y = 0
aim = 0
direction = ""
units = 0
count = 0
for line in lines:
    line = line.split()
    direction = line[0]
    units = int(line[1])
    if (direction == "forward"):
        x += units
        y += units*aim
    elif (direction == "up"):
        aim -= units
    elif (direction == "down"):
        aim += units
    else:
        print("error")
    count += 1
    
answer = x*y
print(answer)