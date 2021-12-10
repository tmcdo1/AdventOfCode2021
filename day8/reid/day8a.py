lines = []
with open('inputs/day8.txt') as f:
    lines = f.readlines()

count = 0
for line in lines:
    row = line.strip().split(" ")
    afterDelimiter = False
    for code in row:
        if code == "|":
            afterDelimiter = True
        elif afterDelimiter:
            if len(code) == 2:
                count += 1
            elif len(code) == 3:
                count += 1
            elif len(code) == 4:
                count += 1
            elif len(code) == 7:
                count += 1
                
print(count)