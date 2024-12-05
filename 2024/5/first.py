pageOrderRules = []
updates = []
inputUpdate = False
correctOrderUpdates = []
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
    correct = True
    for x in range(len(update)):
        for y in range(x + 1, len(update)):
            if [update[y], update[x]] in pageOrderRules:
                correct = False
                break
        if not correct:
            break
    if correct:
        correctOrderUpdates.append(update)

for update in correctOrderUpdates:
    length = len(update)
    totalSum += update[length // 2]

print(totalSum)
