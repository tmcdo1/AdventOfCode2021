#Template
def removeWhitespace(coordinates):
  temp = []
  for elem in coordinates:
    new_elem = elem.strip()
    temp.append(new_elem)
  return temp



answers = []
coordinates = 0

total_grid = []
num_possibilities = 1000
for i in range(0,num_possibilities):
  # Need to create a new array each time
  listOfZeros = [0] * num_possibilities
  total_grid.append(listOfZeros)

for line in open('input.txt'):
  line = line.strip()
  middle = line.split("->")
  first_coordinates = middle[0].split(',')
  second_coordinates = middle[1].split(',')
  print(line)

  one_coordinates = removeWhitespace(first_coordinates)
  two_coordinates = removeWhitespace(second_coordinates)
  x_coordinates = []
  y_coordinates = []
  x_coordinates.append(int(one_coordinates[0]))
  x_coordinates.append(int(two_coordinates[0]))
  y_coordinates.append(int(one_coordinates[1]))
  y_coordinates.append(int(two_coordinates[1]))

  # Order doesn't matter when you have lines but makes it easier
  x_coordinates.sort()
  y_coordinates.sort()
  x1 = x_coordinates[0]
  x2 = x_coordinates[1]
  y1 = y_coordinates[0]
  y2 = y_coordinates[1]
  points_of_line = []
  each_point = []

  # Same x coordinate ergo vertical line
  if(x1 == x2):
    # Create a list to add
    for y in range(y1, y2+1):
      each_point = [x1, y]
      points_of_line.append(each_point)
    
  # Same y coordinate ergo horizontal line
  elif (y1 == y2):
    # Create a list to add
    for x in range(x1, x2+1):
      each_point = [x,y1]
      points_of_line.append(each_point)

  #Part 2 diagnol lines
  # elif ()

  for coordinate in points_of_line:
    x1_point = coordinate[0]
    y1_point = coordinate[1]
    total_grid[x1_point][y1_point] += 1

print(total_grid)

acc = 0
# Loop through total_grid and find where 2 points overlap
for x_val in total_grid:
  for elem in x_val:
    if(elem >= 2):
      acc +=1
print(acc)
