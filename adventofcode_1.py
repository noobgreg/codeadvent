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

pattern = r'\b(?:one|two|three|four|five|six|seven|eight|nine)\b'
all_written_numbers = []

with open('input.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break

        num = re.findall(pattern, line, flags=re.IGNORECASE)
        print(line)
        print(num)

        # if len(num) < 2:
            # str = num[0] + num[0]
        # else:
            # str = num[0] + num[len(num)-1]

        all_written_numbers.append(str)


print('end')
