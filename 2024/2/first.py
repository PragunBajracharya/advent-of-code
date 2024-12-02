reports = []
totalSafe = 0;
with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

for line in lines:
    unsafe = False
    r = list(map(int, line.split(' ')))
    if not (r == sorted(r) or r == sorted(r, reverse=True)):
        print(r)
        continue
    for x in range(1, len(r)):
        diff = abs(r[x] - r[x - 1])
        if not diff in [1, 2, 3]:
            unsafe = True
            break
    if not unsafe:
        totalSafe += 1

print(totalSafe)
