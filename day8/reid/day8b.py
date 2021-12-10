lines = []
with open('inputs/day8.txt') as f:
    lines = f.readlines()

sumOutputs = 0
for line in lines:
    row = line.strip().split(" ")
    afterDelimiter = False
    outputValueString = ""
    one = ""
    four = ""
    seven = ""
    eight = ""
    for code in row:
        if code == "|":
            afterDelimiter = True
        elif afterDelimiter == False:
            if len(code) == 2:
                one = code
            elif len(code) == 3:
                seven = code
            elif len(code) == 4:
                four = code
            elif len(code) == 7:
                eight = code

    # keyMap['2'] = top +           topRight + mid + bot + botLeft
    # keyMap['3'] = top +           topRight + mid + bot +           botRight
    # keyMap['5'] = top + topLeft +            mid + bot +           botRight

    # keyMap['0'] = top + topLeft + topRight +       bot + botLeft + botRight
    # keyMap['6'] = top + topLeft +            mid + bot + botLeft + botRight
    # keyMap['9'] = top + topLeft + topRight + mid + bot +           botRight

    midAndTopLeftChars = "" 
    for l in range(0, len(four)):
        if one.find(four[l]) == -1:
            midAndTopLeftChars = midAndTopLeftChars + four[l]
    
    # print(one)
    # print(four)
    # print(seven)
    # print(eight)

    afterDelimiter = False
    for code in row:
        if code == "|":
            afterDelimiter = True
        elif afterDelimiter:
            if len(code) == 2:
                outputValueString += "1"
            elif len(code) == 3:
                outputValueString += "7"
            elif len(code) == 4:
                outputValueString += "4"
            elif len(code) == 7:
                outputValueString += "8"
            elif len(code) == 5:
                if code.find(one[0]) != -1 and code.find(one[1]) != -1:
                    outputValueString += "3"
                elif code.find(midAndTopLeftChars[0]) != -1 and code.find(midAndTopLeftChars[1]) != -1:
                    outputValueString += "5"
                else:
                    outputValueString += "2"
            elif len(code) == 6:
                if not (code.find(one[0]) != -1 and code.find(one[1]) != -1):
                    outputValueString += "6"
                elif code.find(four[0]) != -1 and code.find(four[1]) != -1 and code.find(four[2]) != -1 and code.find(four[3]) != -1:
                    outputValueString += "9"
                else:
                    outputValueString += "0"
    sumOutputs += int(outputValueString)
    print("CODE: " + code + " " + outputValueString)
            
                
print(sumOutputs)