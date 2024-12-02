reports = []
totalSafe = 0;
with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def safeChecker(arr):
    if len(arr) != len(set(arr)):
        return False
    if arr != sorted(arr) and arr != sorted(arr, reverse=True):
        return False
    for y in range(1, len(arr)):
        diff = abs(arr[y] - arr[y - 1])
        if diff > 3:
            return False
    return True


for line in lines:
    r = list(map(int, line.split(' ')))
    l = len(r)
    if (l - len(set(r))) > 1:
        continue
    safe = safeChecker(r)
    if not safe:
        for x in range(l):
            t = r.copy()
            t.pop(x)
            safe = safeChecker(t)
            if safe:
                break

    if safe:
        totalSafe += 1

print(totalSafe)
