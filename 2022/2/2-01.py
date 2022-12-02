import os
# this is required because of a bug on my windows pc sry
# (it sets current working directory to file directory)
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# elves
# A = Rock
# B = Paper
# C = Scissors

# me
# X = Rock
# Y = Paper
# Z = Scissors

# get content of strategy file
with open("strategy.txt", 'r') as file:
    content = file.read()

# split them by row
matches = content.split('\n')

# calculate score of a match
def calc_score(elf, me):
    score = 0
    # points for the shape I play
    if me == 'X':
        score += 1
    elif me == 'Y':
        score += 2
    else:
        score += 3
    # points if match ends in a draw
    if (me == 'X' and elf == 'A') or (me == 'Y' and elf == 'B') or (me == 'Z' and elf == 'C'):
        score += 3
    # points if I win
    elif (me == 'X' and elf == 'C') or (me == 'Y' and elf == 'A') or (me == 'Z' and elf == 'B'):
        score += 6
    # no points if i loose
    return score

# calculate the total score for every match
tot = 0
for match in matches:
    # split the match and get elf's move and my move
    match = match.split(' ')
    # sum match's score to total score
    tot += calc_score(match[0], match[1])

# print total score
print(f"Total score: {tot} points")