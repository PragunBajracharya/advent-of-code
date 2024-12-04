import re

muls = []
sum = 0
with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"

dont = False
do = True

for line in lines:
    matches = re.finditer(pattern, line)

    for match in matches:
        print(match.group())
        if match.group() == "do()":
            dont = False
            do = True
        if match.group() == "don't()":
            dont = True
            do = False
        if match.group().startswith('mul') and do:
            l, r = map(int, match.group().replace("mul", "").replace("(", "").replace(")", "").split(","))
            sum += (l * r)

print(sum)
