pageOrderRules = []
updates = []
inputUpdate = False
inCorrectOrderUpdates = []
totalSum = 0

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

for line in lines:
    if line == "":
        inputUpdate = True
        continue
    if not inputUpdate:
        pageOrderRules.append(list(map(int, line.split("|"))))
        continue
    updates.append(list(map(int, line.split(","))))

for update in updates:
    inCorrect = False
    for x in range(len(update)):
        for y in range(x + 1, len(update)):
            if [update[y], update[x]] in pageOrderRules:
                inCorrect = True
                break
        if inCorrect:
            break
    if inCorrect:
        inCorrectOrderUpdates.append(update)

for index, update in enumerate(inCorrectOrderUpdates):
    length = len(update)
    for x in range(length):
        min_index = x
        for y in range(x + 1, length):
            if [update[y], update[min_index]] in pageOrderRules:
                min_index = y
        inCorrectOrderUpdates[index][x], inCorrectOrderUpdates[index][min_index] = inCorrectOrderUpdates[index][min_index], inCorrectOrderUpdates[index][x]

for update in inCorrectOrderUpdates:
    length = len(update)
    totalSum += update[length // 2]

print(totalSum)
