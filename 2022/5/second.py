with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

# [P]     [L]         [T]
# [L]     [M] [G]     [G]     [S]
# [M]     [Q] [W]     [H] [R] [G]
# [N]     [F] [M]     [D] [V] [R] [N]
# [W]     [G] [Q] [P] [J] [F] [M] [C]
# [V] [H] [B] [F] [H] [M] [B] [H] [B]
# [B] [Q] [D] [T] [T] [B] [N] [L] [D]
# [H] [M] [N] [Z] [M] [C] [M] [P] [P]
#  1   2   3   4   5   6   7   8   9

stack = [
    ['H', 'B', 'V', 'W', 'N', 'M', 'L', 'P'],
    ['M', 'Q', 'P'],
    ['N', 'D', 'B', 'G', 'F', 'Q', 'M', 'L'],
    ['Z', 'T', 'F', 'Q', 'M', 'W', 'G'],
    ['M', 'T', 'H', 'P'],
    ['C', 'B', 'M', 'J', 'D', 'H', 'G', 'T'],
    ['M', 'N', 'B', 'F', 'V', 'R'],
    ['P', 'L', 'H', 'M', 'R', 'G', 'S'],
    ['P', 'D', 'B', 'C', 'N']
]

for x in lines:
    fromStack = int(x.split(' ')[3]) - 1
    toStack = int(x.split(' ')[5]) - 1
    toMove = int(x.split(' ')[1])
    fromStackLen = len(stack[fromStack])
    remaining = fromStackLen - toMove
    newFrom = stack[fromStack][:remaining]
    stack[toStack] = stack[toStack] + stack[fromStack][remaining:]
    stack[fromStack] = newFrom

allTop = ''

for x in stack:
    allTop = allTop + x[-1]

print(allTop)
