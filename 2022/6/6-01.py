# solution 1647
import os
# this is required because of a bug on my windows pc sry
# (it sets current working directory to file directory)
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# get content of strategy file
with open("signal.txt", 'r') as file:
    content = file.read()

# check 4 consecutive chars to see if they are all unique
def find_unique(signal):
    for i in range(0, len(signal)-4):
        temp = []
        # append the next 4 chars to temp
        for j in range(0, 4):
            temp.append(signal[i+j])
        # set(temp) returns a list with duplicates removed. If it's lenght it's equal to the original one
        if(len(set(temp)) == len(temp)):
            # then we return the index of the final char of the list
            return i+4

# print the index returned by the function
print(find_unique(content))