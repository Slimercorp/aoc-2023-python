with open("input.txt", 'r') as file:
    lines = file.readlines()
digits = list()
for line in lines:
    digit_str = ''.join(filter(lambda x: x.isdigit(), line))
    if len(digit_str) == 1:
        digit_str = digit_str * 2
    elif len(digit_str) > 1:
        digit_str = digit_str[0] + digit_str[-1]

    if digit_str.isdigit():
        digits.append(int(digit_str))

print(sum(digits))