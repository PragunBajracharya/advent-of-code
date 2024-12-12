from itertools import product

equations = []
validTargets = []


def evaluateExpression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
    return result


with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

for line in lines:
    target, numbers = line.split(":")
    target = int(target.strip())
    numbers = list(map(int, numbers.strip().split()))
    equations.append((target, numbers))

for target, numbers in equations:
    num_operators = len(numbers) - 1
    for ops in product(['+', '*'], repeat=num_operators):
        if evaluateExpression(numbers, ops) == target:
            validTargets.append(target)
            break

print(sum(validTargets))
