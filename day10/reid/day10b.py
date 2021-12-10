lines = []
with open('inputs/day10.txt') as f:
    lines = f.readlines()

scores = []
sumPoints = 0
for line in lines:
    stack = []
    ignore = False
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
                ignore = True
    if not ignore:
        subtotal = 0
        while len(stack) > 0:
            c = stack.pop()
            subtotal = subtotal * 5
            if c == ")":
                subtotal += 1
            elif c == "]":
                subtotal += 2
            elif c == "}":
                subtotal += 3
            elif c == ">":
                subtotal += 4
        scores.append(subtotal)

scores.sort()
print(scores[int((len(scores)-1) / 2)])