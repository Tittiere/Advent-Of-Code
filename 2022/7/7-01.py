# solution
import os
# this is required because of a bug on my windows pc sry
# (it sets current working directory to file directory)
os.chdir(os.path.dirname(os.path.realpath(__file__)))

def sort_by_item(arr, index=0, order='d'):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if order == 'd':
                if arr[i][index] < arr[j][index]:
                    aus = arr[i]
                    arr[i] = arr[j]
                    arr[j] = aus
            elif order == 'a':
                if arr[i][index] > arr[j][index]:
                    aus = arr[i]
                    arr[i] = arr[j]
                    arr[j] = aus
    return arr

# get content of strategy file
with open("terminal.txt", 'r') as file:
    content = file.read()

# split the content by row
output = content.split('\n')

dirs = []
dir = []
for i in range(len(output)):
    if output[i].startswith("$ cd") and (len(dir) == 0 or dir[-1] == "$ cd .."):
        dir.append(output[i])
    elif not output[i].startswith("$ cd") and not output[i].startswith("$ ls"):
        dir.append(output[i])
    elif output[i].startswith("$ ls"):
        pass
    else:
        dirs.append(dir)
        dir = []
        dir.append(output[i])
dirs.append(dir)

# for e in dirs: print(e)

dirvalue = []
level = 0
names = []
for i in range(len(dirs)):
    tot = 0
    for e in dirs[i]:
        if e[0].isdigit():
            tot += int(e.split(' ')[0])
        elif e.startswith("$ cd"):
            name = e.split("$ cd ")[1]
            if name == '..':
                level -= 1
            elif name != '/':
                names.append(name)
                level += 1
            parent = None
            for k in range(len(dirvalue)):
                if dirvalue[k][1] == level-1:
                    parent = dirvalue[k][0]

    l = [name, level, tot, parent]
    dirvalue.append(l)

dirvalue = sort_by_item(dirvalue, 1)
# print()
# for e in dirvalue: print(e)

for i in range(len(dirvalue)):
    for j in range(len(dirvalue)):
        if dirvalue[i][3] == dirvalue[j][0]:
            dirvalue[j][2] += dirvalue[i][2]
            break

print()
for e in dirvalue: print(e)

# print(f"tot = {tot}")

tot = 0
for e in dirvalue:
    if e[2] < 100000:
        tot += e[2]

print(tot)