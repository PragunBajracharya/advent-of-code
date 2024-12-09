index = {}
uniquePos = []

with open('input.txt') as file:
    inputBlock = [list(line.rstrip()) for line in file]

for i, arr in enumerate(inputBlock):
    for j, x in enumerate(arr):
        if x != '.':
            if x not in index:
                index[x] = []
            index[x].append([i, j])

for ant, vals in index.items():
    tempAnt = ant
    for i in range(len(vals)):
        for j in range(i + 1, len(vals)):
            diffRow = vals[j][0] - vals[i][0]
            diffCol = vals[j][1] - vals[i][1]
            newRowA = vals[i][0] - diffRow
            newColA = vals[i][1] - diffCol
            newRowB = vals[j][0] + diffRow
            newColB = vals[j][1] + diffCol
            if 0 <= newRowA < len(inputBlock) and 0 <= newColA < len(inputBlock[0]):
                if [newRowA, newColA] not in uniquePos:
                    inputBlock[newRowA][newColA] = '#'
                    uniquePos.append([newRowA, newColA])
            if 0 <= newRowB < len(inputBlock) and 0 <= newColB < len(inputBlock[0]):
                if [newRowB, newColB] not in uniquePos:
                    uniquePos.append([newRowB, newColB])
                    inputBlock[newRowB][newColB] = '#'


print(len(uniquePos))

