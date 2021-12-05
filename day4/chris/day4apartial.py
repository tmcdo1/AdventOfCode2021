#Template
answers = []
board_rows = []
total_row = []
row_of_rows = []
single_column = []
total_column = []
column_of_columns = []
rows = 2
columns = 2
pos = 0
for line in open('input.txt'):
  line = line.strip()

  # Grab the answers
  if "," in line:
    answers = line.split(",")
    # Parse the answers at the end
    for i in range(0, len(answers)):
      answers[i] = int(answers[i])
    print(answers)

  # skip the empty lines
  elif line == '':
    continue

  else:
    board_rows = line.split(" ")
    for i in range(0, len(board_rows)):
      board_rows[i] = int(board_rows[i])
    if(pos < rows):
      for element in board_rows:
        total_row.append(element)
      pos = pos + 1
    if(pos == rows):
      total_row.append("a")
      row_of_rows.append(total_row)
      total_row = []
      pos = 0
for answer in answers:
  for bingo_board in row_of_rows:
    if(answer in bingo_board):
      bingo_board[len(bingo_board)-1] = bingo_board[len(bingo_board)-1] + 'a'
    if('aaa' in bingo_board):
      print('winner!')
print(row_of_rows)
