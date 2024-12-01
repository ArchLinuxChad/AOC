#!/usr/bin/env python

with open("input.txt", "r") as f:
    file = f.read()

file = file.split("\n")

left = []
right = []

for i in file:
    x = i.split(" ")
    if x[0] == "":
        break
    else:
        left.append(x[0])
        right.append(x[3])

total = 0
for i in left:
    count = 0
    for j in right:
        if i == j:
            count += 1
    x = int(i) * count
    total += x
print(total)





