with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

winPoints = 0
signPoints = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

winSign = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
}

lossSign = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y',
}

drawSign = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}

for x in lines:
    opp = x.split(' ')[0]
    my = x.split(' ')[1]
    if my == 'Y':
        winPoints = winPoints + 3 + signPoints[drawSign[opp]]
    elif my == 'Z':
        winPoints = winPoints + 6 + signPoints[winSign[opp]]
    else:
        winPoints = winPoints + signPoints[lossSign[opp]]

print(winPoints)
