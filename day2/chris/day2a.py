#Template
horizontal = 0
vertical = 0
acc = 0

array = []
lineArray = []
for line in open('input.txt'):
  line = line.strip()
  for element in range(0,len(line)):
    lengthLine = len(line)
    firstLetter = line[0]
    var = line[lengthLine-1]
    distance = int(var)
    if (firstLetter == 'f'):
      horizontal = horizontal + distance
      break;
    if (firstLetter == 'd'):
      vertical = vertical - distance
      break;
    if (firstLetter == 'u'):
      vertical = vertical + distance
      break;
print(horizontal)
print(vertical)
print('the answer is ', horizontal*vertical)