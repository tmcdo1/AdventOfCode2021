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

with open('inputs/day16.txt') as f:
    lines = f.readlines()

versionSum = 0
binaryMessage = ""
for l in lines[0].strip():
    binaryMessage += hexToBinaryConverter[l]

def decode(startIdx):
    idx = startIdx
    versionSum = int(binaryMessage[idx:idx+3],2)
    idx += 3
    type = int(binaryMessage[idx:idx+3],2)
    idx += 3
    if type == 4:
        while True:
            idx += 5
            if binaryMessage[idx-5] == '0':
                break
    else:
        if binaryMessage[idx] == '0':
            subpacketsLen = int(binaryMessage[idx+1:idx+16],2)
            endIdx = idx + 16 + subpacketsLen
            idx += 16
            while idx < endIdx:
                idx,v = decode(idx)
                versionSum += v
        else:
            subpacketsCount = int(binaryMessage[idx+1:idx+12],2)
            idx += 12
            for x in range(subpacketsCount):
                idx,v = decode(idx)
                versionSum += v
    return idx,versionSum

print(decode(0)[1])