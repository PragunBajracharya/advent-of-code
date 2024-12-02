with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

dataStream = lines[0]
marker = []
counter = 0

for x in dataStream:
    marker.append(x)
    counter = counter + 1
    if len(marker) == 14:
        if len(set(marker)) == 14:
            break
        marker = marker[1:]

print(''.join(marker))
print(counter)
