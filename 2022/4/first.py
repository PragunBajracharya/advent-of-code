with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

count = 0

for x in lines:
    firstElfLow = int(x.split(',')[0].split('-')[0])
    firstElfHigh = int(x.split(',')[0].split('-')[1])
    secondElfLow = int(x.split(',')[1].split('-')[0])
    secondElfHigh = int(x.split(',')[1].split('-')[1])
    if firstElfHigh >= secondElfHigh and firstElfLow <= secondElfLow:
        count = count + 1
    elif firstElfHigh <= secondElfHigh and firstElfLow >= secondElfLow:
        count = count + 1

print(count)
