lines = []
with open('inputs/day10.txt') as f:
    lines = f.readlines()

sumPoints = 0
for line in lines:
    stack = []
    for c in list(line.strip()):
        if c == "(":
            stack.append(")")
        elif c == "[":
            stack.append("]")
        elif c == "{":
            stack.append("}")
        elif c == "<":
            stack.append(">")
        else:
            if c != stack.pop():
                if c == ")":
                    sumPoints += 3
                elif c == "]":
                    sumPoints += 57
                elif c == "}":
                    sumPoints += 1197
                elif c == ">":
                    sumPoints += 25137

print(sumPoints)