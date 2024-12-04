import re

muls = []
sum = 0
with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

pattern = r"mul\(\d+,\d+\)"

for line in lines:
    match = re.findall(pattern, line)
    muls += match

for mul in muls:
    l, r = map(int, mul.replace("mul", "").replace("(", "").replace(")", "").split(","))
    sum += (l * r)

print(sum)
# 191183308
