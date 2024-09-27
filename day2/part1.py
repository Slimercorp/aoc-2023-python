import re

max_values = (12, 13, 14)
patterns = (r"\b(\d+)\s+red\b", r"\b(\d+)\s+green\b", r"\b(\d+)\s+blue\b")
with open("input.txt", 'r') as file:
    lines = file.readlines()
summ = 0
for i in range(len(lines)):
    line = lines[i]
    rounds = line.split(";")
    flag = False
    for round in rounds:
        if flag:
            break
        for j in range(len(max_values)):
            pattern = patterns[j]
            match = re.search(pattern, round)
            if match and int(match.group(1)) > max_values[j]:
                flag = True
                break
    if not flag:
        summ += (i + 1)
print(summ)