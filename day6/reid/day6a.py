lines = []
with open('inputs/day6.txt') as f:
    lines = f.readlines()

inp = lines[0].strip().split(",")
state = []
for s in inp:
    state.append(int(s))

for day in range():
    fishIdx = 0
    fishCount = len(state)
    while fishIdx < fishCount:
        if state[fishIdx] > 0:
            state[fishIdx] -= 1
        else:
            state[fishIdx] = 6
            state.append(8)
        fishIdx += 1

print(len(state))
