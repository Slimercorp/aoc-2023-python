import re

with open("input.txt", 'r') as file:
    map = list([line.rstrip('\n') for line in file.readlines()])
max_rows = len(map)
max_columns = len(map[0])
map_extra = [[0]*max_columns for _ in range(max_rows)]
def mark_around_symbol(x, y, map, map_extra):
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i<0 or i>=max_rows or j<0 or j>=max_columns:
                continue
            elif map[i][j].isdigit():
                map_extra[i][j] = 1

for i in range(max_rows):
    for j in range(max_columns):
        if not map[i][j].isdigit() and map[i][j] != ".":
            mark_around_symbol(i,j,map,map_extra)

def mark_around_good_digit(x, y, map, map_extra):
    for i in range(y, -1, -1):
        if map[x][i].isdigit():
            map_extra[x][i] = 1
        else:
            break
    for i in range(y, max_columns):
        if map[x][i].isdigit():
            map_extra[x][i] = 1
        else:
            break

for i in range(max_rows):
    for j in range(max_columns):
        if map_extra[i][j] == 1:
            mark_around_good_digit(i,j,map,map_extra)

for i in range(max_rows):
    for j in range(max_columns):
        if not map_extra[i][j]:
            map[i] = map[i][:j] + '.' + map[i][j+1:]

pattern = r"(\d+)"
summ = 0
for i in range(max_rows):
    string = map[i]
    matches = re.finditer(pattern, string)
    for match in matches:
        summ += int(match.group(1))

print(summ)