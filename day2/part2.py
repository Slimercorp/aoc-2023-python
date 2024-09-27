import re

patterns = (r"\b(\d+)\s+red\b", r"\b(\d+)\s+green\b", r"\b(\d+)\s+blue\b")
with open("input.txt", 'r') as file:
    lines = file.readlines()
summ = 0
for i in range(len(lines)):
    max_values = [1, 1, 1]
    line = lines[i]
    rounds = line.split(";")
    for round in rounds:
        for j in range(len(max_values)):
            pattern = patterns[j]
            match = re.search(pattern, round)
            if match and int(match.group(1)) > max_values[j]:
                max_values[j] = int(match.group(1))
    summ += (max_values[0] * max_values[1] * max_values[2])
print(summ)