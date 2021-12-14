lines = []
with open('inputs/day14.txt') as f:
    lines = f.readlines()

polymerTemplate = ''
rules = {}
for line in lines:
    if len(polymerTemplate) == 0:
        buff = list(line.strip())
        for b in buff:
            polymerTemplate += b
    elif line.strip() != '':
        l = list(line.strip())
        rules[l[0]+l[1]] = l[6]

matchesFound = True
limit = 0
while matchesFound and limit < 10:
    matchesFound = False
    polymerTemplateList = list(polymerTemplate)
    i = len(polymerTemplate)-2
    while i >= 0:
        key = polymerTemplate[i] + polymerTemplate[i+1]
        if key in rules:
            matchesFound = True
            polymerTemplateList.insert(i+1, rules[key])
        i -= 1
    polymerTemplate = ''
    for p in polymerTemplateList:
        polymerTemplate += p
    limit += 1
    print(polymerTemplate)

sums = {}
for p in list(polymerTemplate):
    if p not in sums:
        sums[p] = 1
    else:
        sums[p] += 1

leastCommon = -1
mostCommon = 0
for s in sums.values():
    if s > mostCommon:
        mostCommon = s
    if s < leastCommon or leastCommon == -1:
        leastCommon = s

print(mostCommon-leastCommon)
