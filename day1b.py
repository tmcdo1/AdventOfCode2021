lines = []
with open('inputs/day1.txt') as f:
    lines = f.readlines()

increaseCount = 0
prevThree = int(lines[0]) + int(lines[1]) + int(lines[2])
choppingBlock = int(lines[0])
onDeckChoppingBlock = int(lines[1])
inTheHoleChoppingBlock = int(lines[2])
for line in lines[3:]:
    currThree = onDeckChoppingBlock + inTheHoleChoppingBlock + int(line)
    if (currThree > prevThree):
        increaseCount += 1
    prevThree = currThree
    choppingBlock = onDeckChoppingBlock
    onDeckChoppingBlock = inTheHoleChoppingBlock
    inTheHoleChoppingBlock = int(line)

print(f'increase count: {increaseCount}')
