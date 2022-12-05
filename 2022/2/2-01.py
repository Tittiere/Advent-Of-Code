with open("strategy.txt", 'r') as file:
    content = file.read()

matches = content.split('\n')

def calc_score(elf, me):
    score = 0
    if me == 'X':
        score += 1
    elif me == 'Y':
        score += 2
    else:
        score += 3
    if (me == 'X' and elf == 'A') or (me == 'Y' and elf == 'B') or (me == 'Z' and elf == 'C'):
        score += 3
    elif (me == 'X' and elf == 'C') or (me == 'Y' and elf == 'A') or (me == 'Z' and elf == 'B'):
        score += 6
    return score

tot = 0
for match in matches:
    match = match.split(' ')
    tot += calc_score(match[0], match[1])

print(f"Total score: {tot} points")
