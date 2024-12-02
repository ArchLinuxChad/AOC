#!/usr/bin/env python

with open("input.bak", "r") as f:
    puzzle = f.read()

puzzle = puzzle.split("\n")

DESC = False
run = True
count = 0
for i in puzzle:
    if i == "":
        break
    i = i.split(" ")
    i = [int(x) for x in i]
    print(i)
    x = i[0] - i[1]
    if x < 0:
        DES = True
    elif x > 0:
        DES = False
    elif x == 0:
        correct = False
        run = False

    if run:
        itr = len(i) - 1
        for j in range(0, itr):
            diff = i[j] - i[j+1]
            if diff < 0 and DES == False:
                correct = False
                break
            elif diff > 0 and DES == True:
                correct = False
                break
            diff = abs(diff)
            if diff >= 1 and diff <= 3:
                correct = True
            else:
                correct = False
                break
    print(correct)
    if correct:
        count += 1

print(count)
