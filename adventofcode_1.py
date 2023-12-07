import re

# read in as text file
# check line for line
# extract only numbers form string and save first and last number
# if only one digit found use it as first and last digit
all_numbers = []

with open('input.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break

        num = re.findall(r'\d', line)

        if len(num) < 2:
            solution = num[0] + num[0]
        else:
            solution = num[0] + num[len(num)-1]

        all_numbers.append(int(solution))
        # print(line)

# print(sum(all_numbers))

# pattern = r'\b(?:one|two|three|four|five|six|seven|eight|nine)\b'
pattern = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))')
digit_mapping = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

all_written_numbers = []

with open('input.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break

        num = pattern.findall(line)
        converted_digits = [str(digit_mapping[string]) if string in digit_mapping else string for string in num]
        print(line)
        print(num)
        print(converted_digits)

        if len(converted_digits) < 2:
            result = converted_digits[0] + converted_digits[0]
        else:
            result = converted_digits[0] + converted_digits[len(converted_digits)-1]

        all_written_numbers.append(result)

#print(sum(all_written_numbers))
print(sum(map(int, all_written_numbers)))
print('end')
