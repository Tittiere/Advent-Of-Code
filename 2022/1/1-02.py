# solution 205805
import os
# this is required because of a bug on my windows pc sry
# (it sets current working directory to file directory)
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# read elves' inventory and save it in content
with open("elves_inv.txt", 'r') as file:
    content = file.read()

# split the content on every \n
content = content.split("\n")
# append '' to content as a terminator of the last elf's inventory
content.append('')
elves = []
calories = 0
# sum calories until next inventory starts
for el in content:
    if el != '':
        calories += int(el)
    else:
        elves.append(calories)
        calories = 0

three_fattest_elves = []
# find the three elves with the most calories by popping the elf from the list
tot = 0
for i in range(3):
    # find the elf with the most calories
    most_calories = max(elves)
    tot += most_calories
    # find his number in the list
    number = elves.index(most_calories)
    # delete the elf with the most calories
    elves.pop(number)
    print(f"The n{i+1} elf with the most calories is elf #{number+1} with {most_calories} cals")
print(f"Their cals combined are {tot}cals")