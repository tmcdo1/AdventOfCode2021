lines = []
with open('inputs/day14.txt') as f:
    lines = f.readlines()

rules = {}
first = True
for line in lines:
    if first:
        buff = line.strip()
        first = False
    elif line.strip() != '':
        l = list(line.strip())
        rules[l[0]+l[1]] = l[6]

phrase = dict.fromkeys(rules, 0)
for i in range(len(buff)-1):
    phrase[buff[i:i+2]] += 1

for gen in range(40):
    nextPhrase = dict.fromkeys(phrase, 0)
    for key in phrase:
        nextPhrase[key[0]+rules[key]] += phrase[key]
        nextPhrase[rules[key]+key[1]] += phrase[key]
    phrase = nextPhrase

elements = dict.fromkeys(rules.values(),0)
for key in phrase:
    elements[key[0]] += phrase[key]
    elements[key[0]] += phrase[key]

for key in elements:
    if elements[key] % 2 == 1:
        elements[key] = (elements[key] // 2) + 1
    else:
        elements[key] = (elements[key] // 2)


maxi = elements[max(elements, key=elements.get)]
mini = elements[min(elements, key=elements.get)]
print(maxi-mini+1)
        
        