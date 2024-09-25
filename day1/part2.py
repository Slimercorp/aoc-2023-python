with open("input.txt", 'r') as file:
    lines = [line.rstrip('\n') for line in file.readlines()]
digits = list()
replacements = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def replace_words_from_right(line):
    i = len(line)
    while i > 0:
        for word, digit in replacements.items():
            if line[i - len(word):i] == word:
                line = line[:i - 1] + digit + line[i:]
                i -= 1
                break
        else:
            i -= 1
    return line


for line in lines:
    original_line = line
    line = replace_words_from_right(line)

    digit_str = ''.join(filter(lambda x: x.isdigit(), line))
    if len(digit_str) == 1:
        digit_str = digit_str * 2
    elif len(digit_str) > 1:
        digit_str = digit_str[0] + digit_str[-1]

    if digit_str.isdigit():
        digits.append(int(digit_str))

print(sum(digits))