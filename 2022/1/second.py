foodCarried = []
sumOfCalories = []
temp = []
with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

for x in lines:
    if x == '':
        foodCarried.append(temp)
        temp = []
        continue
    x = int(x)
    temp.append(x)

for x in foodCarried:
    sumOfCalories.append(sum(x))

print(sorted(sumOfCalories)[-3:])
print(sum(sorted(sumOfCalories)[-3:]))
