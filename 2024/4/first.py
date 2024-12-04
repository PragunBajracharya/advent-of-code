txt = []

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

for line in lines:
    txt.append(list(line))

row = len(txt)
col = len(txt[0])
count = 0


def checkChar(i, j, c):
    if 0 <= i < row and 0 <= j < col:
        return txt[i][j] == c
    return False


for x in range(row):
    for y in range(col):
        if txt[x][y] == 'X':
            # Top
            if checkChar(x - 1, y, 'M') and checkChar(x - 2, y, 'A') and checkChar(x - 3, y, 'S'):
                count += 1

            # Bottom
            if checkChar(x + 1, y, 'M') and checkChar(x + 2, y, 'A') and checkChar(x + 3, y, 'S'):
                count += 1

            # Right
            if checkChar(x, y + 1, 'M') and checkChar(x, y + 2, 'A') and checkChar(x, y + 3, 'S'):
                count += 1

            # Left
            if checkChar(x, y - 1, 'M') and checkChar(x, y - 2, 'A') and checkChar(x, y - 3, 'S'):
                count += 1

            # Top Right
            if checkChar(x - 1, y + 1, 'M') and checkChar(x - 2, y + 2, 'A') and checkChar(x - 3, y + 3, 'S'):
                count += 1

            # Top Left
            if checkChar(x - 1, y - 1, 'M') and checkChar(x - 2, y - 2, 'A') and checkChar(x - 3, y - 3, 'S'):
                count += 1

            # Bottom Right
            if checkChar(x + 1, y + 1, 'M') and checkChar(x + 2, y + 2, 'A') and checkChar(x + 3, y + 3, 'S'):
                count += 1

            # Bottom Left
            if checkChar(x + 1, y - 1, 'M') and checkChar(x + 2, y - 2, 'A') and checkChar(x + 3, y - 3, 'S'):
                count += 1


print(count)
