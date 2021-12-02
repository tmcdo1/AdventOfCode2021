#Template
p1 = None
p2 = None
acc = 0
array = []
for line in open('input.txt'):
  line = line.strip()
  currentVal = int(line)
  array.append(currentVal)
p1 = array[0]
p2 = array[1]

for i in range(0,len(array)-3):
  p1=array[i]+array[i+1]+array[i+2]
  p2=array[i+1]+array[i+2]+array[i+3]
  if(p2 > p1):
    acc = acc + 1
print(acc)
