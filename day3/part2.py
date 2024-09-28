import re

with open("input.txt", 'r') as file:
    map = list([line.rstrip('\n') for line in file.readlines()])
max_rows = len(map)
max_columns = len(map[0])
map_extra = [[0]*max_columns for _ in range(max_rows)]
map_pair = [[0]*max_columns for _ in range(max_rows)]
pair_number = 1
def mark_around_symbol(x, y, map, map_extra, map_pair, pair_number):
    counterByRow = 0
    last_row = -1
    left_side_covered = False
    right_side_covered = False
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i<0 or i>=max_rows or j<0 or j>=max_columns:
                continue
            elif map[i][j].isdigit():
                map_extra[i][j] = 1
                if last_row == -1 or last_row != i:
                    last_row = i
                    counterByRow += 1
                if i == x and j < y and not left_side_covered:
                    left_side_covered = True
                if i == x and j > y and not right_side_covered:
                    right_side_covered = True
    two_digits_on_the_top = (x-1) >= 0 and map[x-1][y] == "." and (y-1) >=0 and map[x-1][y-1].isdigit() and (y+1) < max_columns and map[x-1][y + 1].isdigit()
    two_digits_on_the_bottom = (x+1) < max_rows and map[x+1][y] == "." and (y-1) >=0 and map[x+1][y-1].isdigit() and (y+1) < max_columns and map[x+1][y + 1].isdigit()
    if counterByRow == 2 or (left_side_covered and right_side_covered) or two_digits_on_the_top or two_digits_on_the_bottom:
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i < 0 or i >= max_rows or j < 0 or j >= max_columns:
                    continue
                elif map_extra[i][j] == 1:
                    map_extra[i][j] = 2
                    map_pair[i][j] = pair_number
        pair_number += 1
    return pair_number

for i in range(max_rows):
    for j in range(max_columns):
        if map[i][j] == "*":
            pair_number = mark_around_symbol(i,j,map,map_extra, map_pair, pair_number)

def mark_around_good_digit(x, y, map, map_extra, map_pair):
    pair_number = map_pair[x][y]
    for i in range(y, -1, -1):
        if map[x][i].isdigit():
            map_extra[x][i] = 2
            map_pair[x][i] = pair_number
        else:
            break
    for i in range(y, max_columns):
        if map[x][i].isdigit():
            map_extra[x][i] = 2
            map_pair[x][i] = pair_number
        else:
            break

for i in range(max_rows):
    for j in range(max_columns):
        if map_extra[i][j] == 2:
            mark_around_good_digit(i,j,map,map_extra, map_pair)

for i in range(max_rows):
    for j in range(max_columns):
        if map_extra[i][j] != 2:
            map[i] = map[i][:j] + '.' + map[i][j+1:]

def get_pair_number(map, map_pair, pair_number):
    number = ""
    for i in range(max_rows):
        if (len(number) != 0):
            break
        for j in range(max_columns):
            if (map_pair[i][j] == pair_number):
                number += map[i][j]
                map_pair[i][j] = 0
            elif (len(number) != 0):
                break
    if (len(number) != 0):
        return int(number)
    else:
        return -1
summ = 0
for pair in range(1, pair_number):
    number1 = get_pair_number(map, map_pair, pair)
    number2 = get_pair_number(map, map_pair, pair)
    if (number1 == -1 or number2 == -1):
        print("something wrong")
    else:
        summ += number1 * number2

print(summ)