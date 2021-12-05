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
winner = None
for choice in choices:
    while b < len(allBoards) and winner == None:
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
                winner = b
                winningNum = int(choice)
        for y in range(5):
            good = True
            for x in range(5):
                if allBoards[b][x][y] != "X":
                    good = False
            if good:
                winner = b
                winningNum = int(choice)
        b += 1
    b = 0

nonWinnerSum = 0
for x in range(5):
    for y in range(5):
        if allBoards[winner][x][y] != "X":
            nonWinnerSum += int(allBoards[winner][x][y])

print(winningNum*nonWinnerSum)