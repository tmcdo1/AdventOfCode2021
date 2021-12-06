from collections import defaultdict

lines = []
with open('input.txt') as f:
    lines = f.readlines()

starting_fish = lines[0].strip().split(",")
all_fish = []
starting_int = []

for fish in starting_fish:
  starting_int.append(int(fish))

total_fish = {
  0: 0,
  1: 0,
  2: 0,
  3: 0,
  4: 0,
  5: 0,
  6: 0,
  7: 0,
  8: 0
}

# Get the starting fish in there
for fish in starting_int:
  total_fish[fish] += 1

for day in range(0,256):
  day_fish = defaultdict(int)
  for school_fish_day, num_fish in total_fish.items():
    if school_fish_day == 0:
      day_fish[8] += num_fish
      day_fish[6] += num_fish
    else:
      day_fish[school_fish_day-1]+= num_fish
  total_fish = day_fish

acc = 0
for days, final_fish in total_fish.items():
  acc += final_fish
print(acc)

  