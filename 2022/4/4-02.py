import os
# this is required because of a bug on my windows pc sry
# (it sets current working directory to file directory)
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# develop interval in full list of numbers (e.g.: 2-5 => 2, 3, 4, 5)
def develop_numbers(interval):
    numbers = []
    for i in range(int(interval.split('-')[0]), int(interval.split('-')[1])+1):
        numbers.append(i)
    return numbers

# check if interval is fully contained into other
def contained(a, b):
    if any(item in a for item in b) == False:
        return any(item in b for item in a)
    else:
        return any(item in a for item in b)


# get content of strategy file
with open("assignments.txt", 'r') as file:
    content = file.read()

# split the content by row
assignments = content.split("\n")

tot = 0
for row in assignments:
    tot += int(contained(develop_numbers(row.split(',')[0]), develop_numbers(row.split(',')[1])))

print(f"{tot} overlapping")