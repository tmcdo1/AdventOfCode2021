#Template
from collections import defaultdict

values = []
lowestValue = 1000000000000000
for line in open('input.txt'):
    valueArray = []
    valueArray = line.split(',')
    for element in valueArray:
      values.append(int(element))

for i in range(0, 1500):
  # print(i)
  total_difference = 0
  for element in values:
    difference = abs(element - i)
    for j in range(1,difference+1):
      total_difference+=j
  if(total_difference < lowestValue):
    lowestValue = total_difference
print(lowestValue)

