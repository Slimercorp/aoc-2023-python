import re, sys

with open("input.txt", 'r') as file:
    input = file.read()
paragraphs = input.split("\n\n")
pattern = r"(\d+)"

seeds_line = paragraphs[0]
matches = re.finditer(pattern, seeds_line)
seeds = list()
for match in matches:
    seeds.append(int(match.group(1)))

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


def get_map_value(map, breakpoint):
    for map_line in map:
        map_start_value = map_line[0]
        breakpoint_start_value = map_line[1]
        length = map_line[2]
        if breakpoint_start_value <= breakpoint <= breakpoint_start_value + length:
            return map_start_value + (breakpoint - breakpoint_start_value)
    return breakpoint

min_location = sys.maxsize
for seed in seeds:
    soil = get_map_value(soils, seed)
    fertilizer = get_map_value(fertilizers, soil)
    water = get_map_value(waters, fertilizer)
    light = get_map_value(lights, water)
    temperature = get_map_value(temperatures, light)
    humidity = get_map_value(humidities, temperature)
    location = get_map_value(locations, humidity)
    if location < min_location:
        min_location = location

print(min_location)