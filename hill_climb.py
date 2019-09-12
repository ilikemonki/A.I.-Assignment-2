# Meng Cha
# CECS 451 A.I.
# 9/12/2019

import random
import numpy as np

from board import Board


# Hill Climb Algorithm

class Hill_Climb:
    def __init__(self, n):
        self.step = 0
        self.conflicts = [[0 for j in range(n)] for i in range(n)]  # array to record number of conflicts at the spot
        self.pos = [0 for i in range(n)]    # n_queen's column position
        self.fit = n * (n - 1) // 2
        self.maxFit = self.fit
        self.new_board = list(map(list, home.map))   # copy board
        self.countColumn = 0
        self.countRow = 0
        self.movedSpot = [home.n_queen for i in range(n)]  # record the moved spot
        # Get queen position
        for i in range(n):
            for j in range(n):
                if home.map[i][j] == 1:
                    self.pos[i] = j

    # Checks all positions and get the number of conflicts
    def heuristic(self):
        self.conflicts = [[0 for j in range(home.n_queen)] for i in range(home.n_queen)]

        # Checks bottom rows for conflict for all possible spots
        for i in range(home.n_queen):   # Row
            for j in range(home.n_queen):   # Column
                for k in range(1, home.n_queen - i):    # go through the rows below current row.
                    if self.new_board[i + k][j] == 1:         # check the column below
                        self.conflicts[i][j] += 1
                    if j - k >= 0 and self.new_board[i + k][j - k] == 1:      # check bottom left diagonal
                        self.conflicts[i][j] += 1
                    if j + k < home.n_queen and self.new_board[i + k][j + k] == 1:    # check bottom right diagonal
                        self.conflicts[i][j] += 1
        # Checks top rows for conflict for all possible spots
        for i in range(1, home.n_queen):    # Start at row 1 and down
            for j in range(home.n_queen):   # Column
                for k in range(1, i + 1):    # go through the rows above current row.
                    if self.new_board[i - k][j] == 1:         # check the column above
                        self.conflicts[i][j] += 1
                    if j - k >= 0 and self.new_board[i - k][j - k] == 1:      # check top left diagonal
                        self.conflicts[i][j] += 1
                    if j + k < home.n_queen and self.new_board[i - k][j + k] == 1:    # check top right diagonal
                        self.conflicts[i][j] += 1
        # print(np.matrix(self.conflicts), "conflict")

    # Move the Queens around
    def steps(self):
        hc.heuristic()
        hc.fitness()
        for c in range(home.n_queen):   # run it n times
            for i in range(home.n_queen):   # row
                for j in range(home.n_queen):   # column
                    if self.conflicts[i][j] == 0:       # Looks for zero conflict to move to
                        if self.movedSpot[i] < home.n_queen:    # If Q was already moved to this spot, break
                            break
                        if j != self.pos[i]:    # If the zero conflict is not on the Q, move to that spot
                            self.movedSpot[i] = j   # Record the spot where Q moved to
                            for k in range(home.n_queen):   # clear the row
                                self.new_board[i][k] = 0
                            self.new_board[i][j] = 1    # Move Q to new spot
                        if j == self.pos[i]:
                            break
                        break
                hc.heuristic()
            hc.fitness()
            if self.fit == self.maxFit:     # When solved, stop and print the new board
                hc.countSteps()
                print("The number of required steps:", self.step)
                print(np.matrix(self.new_board))
                break
        if self.fit != self.maxFit:     # If all else fails, redo
            hc.redo()

    # If steps function fails, force move the Queen and try again
    def redo(self):
        self.movedSpot = [home.n_queen for i in range(home.n_queen)]
        self.new_board = list(map(list, home.map))   # copy board
        self.new_board[self.countRow][self.pos[self.countRow]] = 0
        self.new_board[self.countRow][self.countColumn] = 1     # Force move Queen
        # print(np.matrix(self.new_board))
        if self.countColumn < home.n_queen - 1:     # Do all columns in that row
            self.countColumn += 1
            hc.steps()
        else:   # if not solved yet, go to the next row
            self.countColumn = 0
            self.countRow += 1
            hc.redo()

    # Count the number of required steps to solve the problem.
    def countSteps(self):
        for i in range(home.n_queen):       # go through row
            for j in range(home.n_queen):   # go through column
                if self.new_board[i][j] != 1 and home.map[i][j] == 1:
                    self.step += 1
                    break

    # Check for conflicts
    def fitness(self):
        self.fit = self.maxFit
        for i in range(home.n_queen):       # go through row,
            for j in range(home.n_queen):   # go through column,
                if self.new_board[i][j] == 1:     # to find 1
                    for k in range(1, home.n_queen - i):    # go through the rows below current row.
                        if self.new_board[i + k][j] == 1:         # check the column below
                            self.fit -= 1
                        if j - k >= 0 and self.new_board[i + k][j - k] == 1:      # check left diagonal
                            self.fit -= 1
                        if j + k < home.n_queen and self.new_board[i + k][j + k] == 1:    # check right diagonal
                            self.fit -= 1
        # print("Fitness: ", self.fit)

if __name__ == '__main__':
    home = Board(5)
    home.set_queens()
    home.fitness()
    home.show()
    hc = Hill_Climb(home.n_queen)
    hc.steps()

