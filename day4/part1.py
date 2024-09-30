import re

with open("input.txt", 'r') as file:
    cards = list([line.rstrip('\n') for line in file.readlines()])
summ = 0
for card in cards:
    numbers = card.split(":")[1]
    win_numbers = numbers.split("|")[0]
    my_numbers = numbers.split("|")[1]
    pattern = r"(\d+)"

    matches = re.finditer(pattern, win_numbers)
    win_set = set()
    for match in matches:
        win_set.add(int(match.group(1)))

    matches = re.finditer(pattern, my_numbers)
    my_set = set()
    for match in matches:
        my_set.add(int(match.group(1)))

    score = 0
    for number in win_set:
        if number in my_set:
            score = 1 if score == 0 else score * 2
    summ += score

print(summ)