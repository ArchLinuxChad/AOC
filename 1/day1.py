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

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

bubble_sort(left)
bubble_sort(right)
total = 0

for i in range(0, 1000):
    x = int(left[i])
    y = int(right[i])
    if x > y:
        z = x - y
    elif y > x:
        z = y - x
    elif y == x:
        z = 0
    total += z

print(total)





