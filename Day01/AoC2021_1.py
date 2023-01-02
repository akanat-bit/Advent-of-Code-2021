#importing the os module
import os

#to get the current working directory
directory = os.getcwd()

print(directory)

#os.chdir("/Users/isseitanaka/Documents/Python Practice/Advent-of-Code-2021")

with open("AoC2021_1.txt", 'r') as f:
    lines = f.readlines()

line_list = []
for line in lines:
    line_list.append(line.strip())

int_list = [int(s) for s in line_list]

print(int_list)  # Output: [1, 2, 3, 4, 5]

def sum_triplets(numbers):
    result = []
    for i in range(0, len(numbers)-2, 1):
        triplet = numbers[i:i+3]
        result.append(sum(triplet))
    return result


triplet_list= sum_triplets(int_list)
print(triplet_list)

#Count number of increases
counter = 0

for i in range(1, len(triplet_list)):
    if triplet_list[i] > triplet_list[i - 1]:
        counter += 1

print(counter)
