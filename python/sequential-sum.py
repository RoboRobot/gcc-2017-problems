import random

import numpy as np

board = [[[0 for gen_x in xrange(5)] for gen_y in xrange(5)] for gen_z in xrange(4)]

def generate():
    for layer in range(0, 4):
        for x in range(0, 5):
            for y in range(0, 5):
                board[layer][x][y] = random.randint(-10, 10)

def find_solution():
    highest_sum_location = None
    highest_sum = -100

    #Start with horizontal searching
    for layer in range(0,4):
        for y in range(0,5):
            #Because there are only 3 possible positions in a array of 5
            for x in range(0, 3):
                sum = board[layer][x][y] + board[layer][x+1][y] + board[layer][x+2][y]
                if sum > highest_sum:
                    highest_sum_location = "(" + str(layer) + "," + str(x) + "," + str(y) + ")" + \
                                           "(" + str(layer) + "," + str(x+1) + "," + str(y) + ")" + \
                                           "(" + str(layer) + "," + str(x+2) + "," + str(y) + ")"
                    highest_sum = sum
                    # print highest_sum_location + " with: " + str(highest_sum)

    #Vertical searching
    for layer in range(0,4):
        for x in range(0,5):
            #Because there are only 3 possible positions in a array of 5
            for y in range(0, 3):
                sum = board[layer][x][y] + board[layer][x][y+1] + board[layer][x][y+2]
                if sum > highest_sum:
                    highest_sum_location = "(" + str(layer) + "," + str(x) + "," + str(y) + ")" + \
                                           "(" + str(layer) + "," + str(x) + "," + str(y+1) + ")" + \
                                           "(" + str(layer) + "," + str(x) + "," + str(y+2) + ")"
                    highest_sum = sum
                    # print highest_sum_location + " with: " + str(highest_sum)

    #Layer-wise searching
    #There are only 2 possible locations with a layer size of 4
    for layer in range(0,2):
        for x in range(0,5):
            for y in range(0,5):
                sum = board[layer][x][y] + board[layer+1][x][y] + board[layer+2][x][y]
                if sum > highest_sum:
                    highest_sum_location = "(" + str(layer) + "," + str(x) + "," + str(y) + ")" + \
                                           "(" + str(layer+1) + "," + str(x) + "," + str(y) + ")" + \
                                           "(" + str(layer+2) + "," + str(x) + "," + str(y) + ")"
                    highest_sum = sum
                    # print highest_sum_location + " with: " + str(highest_sum)

    return highest_sum_location


def print_boards():
    for layer in range(0,4):
        print "Board " + str(layer) + ": "
        print(np.matrix(board[layer]))


if __name__ == '__main__':
    generate()
    print "Solution: " + find_solution()
    print_boards()