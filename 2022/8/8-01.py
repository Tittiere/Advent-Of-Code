import os
# this is required because of a bug on my windows pc sry
# (it sets current working directory to file directory)
os.chdir(os.path.dirname(os.path.realpath(__file__)))

def visible(a, b):
    global trees
    if a == 0 or b == 0:
        return True
    else:
        print(f"a = {a} e b = {b}")
        for i in range(a):
            for j in range(b):
                print(f"{i}, {j} ", end = '')
            print()
        return False

# get content of strategy file
with open("map.txt", 'r') as file:
    content = file.read()

# split the content by row
rows = content.split('\n')

trees = [list(e) for e in rows]

for i in range(len(trees)):
    for j in range(len(trees[0])):
        print(visible(i, j))
        # print(trees[i][j], end='')
    # print()