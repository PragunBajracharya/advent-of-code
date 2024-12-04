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
        if txt[x][y] == 'A':
            if checkChar(x - 1, y - 1, 'M') and checkChar(x - 1, y + 1, 'M') and checkChar(x + 1, y - 1, 'S') and checkChar(x + 1, y + 1, 'S'):
                count += 1
            if checkChar(x - 1, y - 1, 'S') and checkChar(x - 1, y + 1, 'S') and checkChar(x + 1, y - 1, 'M') and checkChar(x + 1, y + 1, 'M'):
                count += 1
            if checkChar(x - 1, y - 1, 'S') and checkChar(x - 1, y + 1, 'M') and checkChar(x + 1, y - 1, 'S') and checkChar(x + 1, y + 1, 'M'):
                count += 1
            if checkChar(x - 1, y - 1, 'M') and checkChar(x - 1, y + 1, 'S') and checkChar(x + 1, y - 1, 'M') and checkChar(x + 1, y + 1, 'S'):
                count += 1


print(count)
