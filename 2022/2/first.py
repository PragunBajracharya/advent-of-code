with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

print(lines)
points = 0
signPoints = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}
for x in lines:
    opp = x.split(' ')[0]
    my = x.split(' ')[1]
    if (opp == 'A' and my == 'X') or (opp == 'B' and my == 'Y') or (opp == 'C' and my == 'Z'):
        points = points + 3 + signPoints[my]
    elif (opp == 'A' and my == 'Y') or (opp == 'B' and my == 'Z') or (opp == 'C' and my == 'X'):
        points = points + 6 + signPoints[my]
    else:
        points = points + signPoints[my]

print(points)
