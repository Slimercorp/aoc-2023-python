import re

with open("input.txt", 'r') as file:
    cards = list([line.rstrip('\n') for line in file.readlines()])
games = dict()
gameNo = 0
for card in cards:
    gameNo += 1
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

    summ = 0
    for number in win_set:
        if number in my_set:
            summ += 1
    games[gameNo] = summ

my_cards = list(range(1,gameNo+1,1))
n_cards = gameNo
while (True):
    new_cards = list()
    for card in my_cards:
        new_cards_count = games[card]
        for i in range(1, new_cards_count + 1, 1):
            new_cards_no = card + i
            if new_cards_no <= gameNo:
                new_cards.append(new_cards_no)
                n_cards += 1
    if len(my_cards) == 0:
        break
    else:
        my_cards = new_cards

print(n_cards)
