left = []
right = []
with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

for line in lines:
    l, r = map(int, line.split('   '))
    left.append(l)
    right.append(r)

left.sort()
right.sort()
print(left)
print(right)

total = 0
for x in range(len(left)):
    total = total + abs(left[x] - right[x])

print(total)
