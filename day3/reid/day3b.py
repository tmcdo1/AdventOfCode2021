lines = []
with open('inputs/day3.txt') as f:
    lines = f.readlines()

leastCommonSubset = []
mostCommonSubset = []
for line in lines:
    leastCommonSubset.append(line.strip())
    mostCommonSubset.append(line.strip())

bitIdx = 0
bitLength = len(leastCommonSubset)
leastFound = False
mostFound = False
while bitIdx < bitLength and (not leastFound or not mostFound):
    if not leastFound:
        zeroes = []
        ones = []
        for num in leastCommonSubset:
            if num[bitIdx] == '0':
                zeroes.append(num)
            else:
                ones.append(num)
        if len(zeroes) <= len(ones):
            leastCommonSubset = zeroes
            if len(zeroes) == 1:
                leastFound = True
        else:
            leastCommonSubset = ones
            if len(ones) == 1:
                leastFound = True
    if not mostFound:
        zeroes = []
        ones = []
        for num in mostCommonSubset:
            if num[bitIdx] == '0':
                zeroes.append(num)
            else:
                ones.append(num)
        if len(zeroes) > len(ones):
            mostCommonSubset = zeroes
            if len(zeroes) == 1:
                mostFound = True
        else:
            mostCommonSubset = ones
            if len(ones) == 1:
                mostFound = True
    bitIdx += 1

answer = int(leastCommonSubset[0],2)*int(mostCommonSubset[0],2)
print(answer)