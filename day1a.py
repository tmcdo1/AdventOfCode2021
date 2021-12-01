lines = []
with open('inputs/day1a.txt') as f:
    lines = f.readlines()

first = True
increaseCount = 0
prev = 0
for line in lines:
    if first:
        first = False
    else:
        if (int(line) > int(prev)):
            increaseCount += 1
    prev = line

print(f'increase count: {increaseCount}')
