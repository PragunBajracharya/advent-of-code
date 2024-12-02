with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

currentDir = ''
currentDirSize = 0
path = ''
dirSizes = {}

for x in lines:
    commandSplit = x.split(' ')
    if commandSplit[0] == '$' and commandSplit[1] == 'cd' and commandSplit[2] != '..':
        if path == '':
            path = commandSplit[2]
        else:
            path = path + '++' + commandSplit[2]
        dirSizes[commandSplit[2]] = 0
        currentDir = commandSplit[2]
    elif commandSplit[0] == '$' and commandSplit[1] == 'cd' and commandSplit[2] == '..':
        pathSplit = path.split('++')
        del pathSplit[-1]
        path = '++'.join(pathSplit)
    elif commandSplit[0] != '$' and commandSplit[0] != 'dir':
        # dirSizes[currentDir]['size'] = int(commandSplit[0])
        pathSplit = path.split('++')
        for y in pathSplit:
            # print(commandSplit[0])
            dirSizes[y] = dirSizes[y] + int(commandSplit[0])
            print(y, dirSizes[y])
        # print(pathSplit)
        # print(dirSizes)
        # break
    # print(path)

# print(dirSizes)
totalSize = 0
for x, v in dirSizes.items():
    if int(v) < 100000:
        totalSize = totalSize + v

print(totalSize)
