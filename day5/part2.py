import re, sys

with open("input.txt", 'r') as file:
    input = file.read()
paragraphs = input.split("\n\n")
pattern = r"(\d+)"

seeds_line = paragraphs[0]
matches = re.finditer(pattern, seeds_line)
seeds = list()
counter = 0
seeds_line = list()
for match in matches:
    counter += 1
    value = int(match.group(1))
    if counter == 1:
        seeds_line.append(value)
    else:
        seeds_line.append(value)
        seeds.append(seeds_line)
        seeds_line = list()
        counter = 0

def parse_line(line, pattern):
    matches = re.finditer(pattern, line)
    items = list()
    item = list()
    counter = 0
    for match in matches:
        counter += 1
        item.append(int(match.group(1)))
        if counter == 3:
            items.append(item)
            counter = 0
            item = list()
    return items

soils = parse_line(paragraphs[1], pattern)
fertilizers = parse_line(paragraphs[2], pattern)
waters = parse_line(paragraphs[3], pattern)
lights = parse_line(paragraphs[4], pattern)
temperatures = parse_line(paragraphs[5], pattern)
humidities = parse_line(paragraphs[6], pattern)
locations = parse_line(paragraphs[7], pattern)


def get_breakpoint_value(map, map_value):
    for map_line in map:
        map_start_value = map_line[0]
        breakpoint_start_value = map_line[1]
        length = map_line[2]
        if map_start_value <= map_value <= map_start_value + length:
            return breakpoint_start_value + (map_value - map_start_value)
    return map_value

min_location = 0
for location in range(0, 9622623):
    humidity = get_breakpoint_value(locations, location)
    temperature = get_breakpoint_value(humidities, humidity)
    light = get_breakpoint_value(temperatures, temperature)
    water = get_breakpoint_value(lights, light)
    fertilizer = get_breakpoint_value(waters, water)
    soil = get_breakpoint_value(fertilizers, fertilizer)
    seed = get_breakpoint_value(soils, soil)
    for seed_line in seeds:
        start_value = seed_line[0]
        length = seed_line[1]
        if start_value <= seed <= start_value + length:
            min_location = location
            break

    if min_location != 0:
        break

print(min_location)