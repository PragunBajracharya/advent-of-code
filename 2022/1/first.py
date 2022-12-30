foodCarried = []
sumOfCalories = []
temp = []
with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

print(lines)
for x in lines:
    if x == '':
        foodCarried.append(temp)
        temp = []
        continue
    x = int(x)
    temp.append(x)
print(foodCarried)
for x in foodCarried:
    sumOfCalories.append(sum(x))

print(max(sumOfCalories))
