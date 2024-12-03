import re

result = 0
for line in open('day3/data.txt'):
    list_found = re.findall(r'mul\(\d+,\d+\)', line)
    for item in list_found:
        a, b = map(int, re.findall(r'\d+', item))
        result += a * b

print("answer:", result)
