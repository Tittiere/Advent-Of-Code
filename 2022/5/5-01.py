import os
# this is required because of a bug on my windows pc sry
# (it sets current working directory to file directory)
os.chdir(os.path.dirname(os.path.realpath(__file__)))

def make_move(move, array):
    move = [e for e in move.split(' ') if e.isdigit()]
    quantity = int(move[0])
    startPos = int(move[1])-1
    endPos = int(move[2])-1
    for i in range(quantity):
        array[endPos].append(array[startPos][-1])
        array[startPos].pop(-1)
    return array

# get content of strategy file
with open("instructions.txt", 'r') as file:
    content = file.read()

# split the content by row
instructions = content.split("\n")

# split the data from the instructions file into
# piles and moves
piles = []
moves = []

# the first few rows are the piles order, until an empty row is
# read. Then it's the moves.
pilesEnd = False
for el in instructions:
    if el == '':
        pilesEnd = True
    elif pilesEnd:
        moves.append(el)
    else:
        piles.append(el)

# now let's rearrange the piles into lists of elements
arr = [e for e in piles[-1].split(' ') if e != '']
# remove last el of piles
piles.pop(-1)
truePiles = []
for i in range(0, len(arr)):
    aus = []
    for j in range(len(piles), 0, -1):
        temp = [e for e in piles[j-1].split(' ')]
        space = False
        toPop = []
        e = 0
        while len(temp) != len(arr):
            if temp[e] == '':
                for k in range(3):
                    temp.pop(e)
            e += 1
        if(temp[i] != ''):
            aus.append(temp[i])
    truePiles.append(aus)


for move in moves:
    truePiles = make_move(move, truePiles)
for e in truePiles:
    print(f"{e[-1][1]}", end='')
# print(moves)