with open("input.txt", 'r') as file:
    lines = [line.rstrip('\n') for line in file.readlines()]
digits = list()
replacements = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
for line in lines:
    original_line = line
    i = 3
    while i <= len(line):
        str_temp = line[0:i]
        for key, value in replacements.items():
            if key in str_temp:
                str_temp = str_temp.replace(key, value)
                line = str_temp + line[i:]
                i = 2
                break
        i += 1

    digit_str = ''.join(filter(lambda x: x.isdigit(), line))
    if len(digit_str) == 1:
        digit_str = digit_str * 2
    elif len(digit_str) > 1:
        digit_str = digit_str[0] + digit_str[-1]

    if digit_str.isdigit():
        digits.append(int(digit_str))

print(sum(digits))