lines = []
with open('inputs/day1.txt') as f:
    lines = f.readlines()

increaseCount = 0
prev = lines[0]
for line in lines[1:]:
    if (int(line) > int(prev)):
        increaseCount += 1
    prev = line

print(f'increase count: {increaseCount}')
