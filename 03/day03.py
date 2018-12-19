#!/usr/bin/python
# Advent of Code 2018, day 3
# https://adventofcode.com/2018/day/3

import sys

FABRIC_SIZE = 1000

class Rectangle:
    def __init__(self, _id, x, y, val):
        self.id = _id
        self.x = x
        self.y = y
        self.val = val
        self.overlap = False

    def __str__(self):
        return "ID: " + str(self._id) + ", x:" + str(self.x) + ", y:" + str(self.y)

# How many square inches of fabric are within two or more claims?
def part1(filename):
    fabric = [[0 for j in range(FABRIC_SIZE)] for i in range(FABRIC_SIZE)]
    count = 0

    # parse input info into array
    f = open(filename, 'r')
    for line in f:
        arr = line.split()
        id = arr[0][1:]
        startX, startY = int(arr[2].split(',')[0]), int(arr[2].split(',')[1][:-1])
        width, height = int(arr[3].split('x')[0]), int(arr[3].split('x')[1])
        # print("Start point is %i, %i and size is %i x %i" % (startX, startY, width, height))

        # increment each point for each fabric covering it
        for i in range(startX, startX + width):
            # print("i: %i, startY: %i, height: %i" % (i, startY, height+1))
            for j in range(startY, startY + height):
                #print("Incrementing point %i, %i" % (i, j))
                fabric[i][j] += 1
                # print("Incrementing fabric[%i][%i] to %i" % (i, j, fabric[i][j]))

    # count the number with more than 2 overlapping claims
    for i in range(FABRIC_SIZE):
        for j in range(FABRIC_SIZE):
            if fabric[i][j] >= 2:
                count += 1

    return count

# TODO - complete
def part2(filename):
    fabric = [[Rectangle(0, 0, 0, 0) for j in range(FABRIC_SIZE)] for i in range(FABRIC_SIZE)]
    count = 0

    # parse input info into array
    f = open(filename, 'r')
    for line in f:
        arr = line.split()
        id = arr[0][1:]
        startX, startY = int(arr[2].split(',')[0]), int(arr[2].split(',')[1][:-1])
        width, height = int(arr[3].split('x')[0]), int(arr[3].split('x')[1])
        # print("Start point is %i, %i and size is %i x %i" % (startX, startY, width, height))

        # increment each point for each fabric covering it
        for i in range(startX, startX + width):
            # print("i: %i, startY: %i, height: %i" % (i, startY, height+1))
            for j in range(startY, startY + height):
                #print("Incrementing point %i, %i" % (i, j))
                rect = fabric[i][j]
                rect.id = id
                rect.x = i
                rect.y = j
                rect.val += 1
                if rect.val > 1:
                    rect.overlap = True

    # Find the rectangle with no overlapping claims
    for i in range(FABRIC_SIZE):
        for j in range(FABRIC_SIZE):
            if fabric[i][j].val == 1 and rect.overlap == False:
                return fabric[i][j].id

    return None


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python day03.py part[1|2] <input_file>\n")
    else:
        if sys.argv[1] == 'part1':
            result1 = part1(sys.argv[2])
            print("Output is " + str(result1))
        elif sys.argv[1] == 'part2':
            result2 = part2(sys.argv[2])
            print("Output is " + str(result2))
        else:
            print("You must choose either 'part1' or 'part2' to run")
