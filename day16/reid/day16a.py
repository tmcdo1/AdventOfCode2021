with open('inputs/day16TEST.txt') as f:
    lines = f.readlines()

hexToBinaryConverter = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

binaryMessage = ""
for l in lines[0].strip():
    binaryMessage += hexToBinaryConverter[l]

binIdx = 0
version = 0; type = 0
versionSum = 0
while binIdx < len(binaryMessage):
    if version == 0 and type == 0:
        # pre-process packet
        version = int(binaryMessage[binIdx:binIdx+3],2)
        versionSum += version
        binIdx += 3
        type = int(binaryMessage[binIdx:binIdx+3],2)
        binIdx += 3
        if type == 4:
            # literal packet
            literal = int(binaryMessage[binIdx+1:binIdx+5]+binaryMessage[binIdx+6:binIdx+10]+binaryMessage[binIdx+11:binIdx+15],2)
            binIdx += 18
            version = 0; type = 0
        else:
            # operator packet
            if int(binaryMessage[binIdx+1:binIdx+5]) == 0:
                length = 15
            else:
                length = 10
            binIdx += 1

            # do some processing

            version = 0; type = 0



print(versionSum)
