left = []
right = []
with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

for line in lines:
    l, r = map(int, line.split('   '))
    left.append(l)
    right.append(r)

total = 0
for x in range(len(left)):
    total = total + left[x] * right.count(left[x])

print(total)