# solution 2620
import os
# this is required because of a bug on my windows pc sry
# (it sets current working directory to file directory)
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# use ord() function to get ascii value of character, then subtract
# a constant to scale the ascii value to item's priority
def get_priority(char):
    # if char is uppercase (ascii 65 through 90) subtract 38 to scale the priority
    # in the range of 27-52
    if char.isupper():
        return ord(char)-38
    # if it is lowercase (ascii 97 through 122) subtract 96 to scale the priority
    # in the range of 1-26
    else:
        return ord(char)-96

# check if three strings have items in common
def item_in_common(a, b, c):
    # compare every item in a to every item in b
    for i in a:
        for j in b:
            for k in c:
                if i == j and j == k:
                    # since there can be at most one element in common
                    # between the three elves, once I find it i
                    # immediately return it
                    return i
    return False

# get content of strategy file
with open("backpacks.txt", 'r') as file:
    content = file.read()

# split the content by row
backpacks = content.split("\n")

tot = 0
# cycle all the backpacks 3 by 3
for el in range(0, len(backpacks), 3):
    # get backpacks in groups of three
    first = backpacks[el]
    second = backpacks[el+1]
    third = backpacks[el+2]
    tot += get_priority(item_in_common(first, second, third))

print(f"Tot priority is {tot}")