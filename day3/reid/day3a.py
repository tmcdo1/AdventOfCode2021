lines = []
with open('inputs/day3.txt') as f:
    lines = f.readlines()

bitTally = []
first = True
for line in lines:
    idx = 0
    for bit in list(line.strip()):
        if first:
            bitTally.append(int(bit))
        else:
            bitTally[idx] += int(bit)
        idx += 1
    if first:
        first = False

gamma = ""
epsilon = ""
for bit in bitTally:
    if (bit > len(lines)/2):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
        
answer = int(gamma,2)*int(epsilon,2)
print(answer)