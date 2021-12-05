lines = []
with open('inputs/day4.txt') as f:
    lines = f.readlines()

choices = lines[0].strip().split(',')

board = []
allBoards = []
rowCount = 0
for line in lines[2:]:
    if rowCount < 5:
        board.append(list(line.strip().split()))
    if rowCount == 5:
        allBoards.append(board)
        board = []
        rowCount = 0
    else:
        rowCount += 1

b = 0
winningNum = 0
for choice in choices:
    while len(allBoards) >= 1 and b < len(allBoards) and winningNum == 0:
        winner = False
        for x in range(5):
            for y in range(5):
                if allBoards[b][x][y] == choice:
                    allBoards[b][x][y] = "X"
        for x in range(5):
            good = True
            for y in range(5):
                if allBoards[b][x][y] != "X":
                    good = False
            if good:
                winner = True
        for y in range(5):
            good = True
            for x in range(5):
                if allBoards[b][x][y] != "X":
                    good = False
            if good:
                winner = True
        if winner:
            if len(allBoards) > 1:
                allBoards.pop(b)
            else:
                winningNum = int(choice)
        else:
            b += 1
    b = 0

nonWinnerSum = 0
for x in range(5):
    for y in range(5):
        if allBoards[0][x][y] != "X":
            nonWinnerSum += int(allBoards[0][x][y])

print(winningNum*nonWinnerSum)