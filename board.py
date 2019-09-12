import random
import numpy as np


class Board:
    def __init__(self, n):
        self.n_queen = n
        self.map = [[0 for j in range(n)] for i in range(n)]
        self.fit = n * (n-1) // 2

    def set_queens(self):
        for i in range(self.n_queen):
            j = random.randint(0, self.n_queen - 1)
            self.map[i][j] = 1

    def fitness(self):
        for i in range(self.n_queen):       # go through row,
            for j in range(self.n_queen):   # go through column,
                if self.map[i][j] == 1:     # to find 1
                    for k in range(1, self.n_queen - i):    # go through the rows below current row.
                        if self.map[i + k][j] == 1:         # check the column below
                            self.fit -= 1
                        if j - k >= 0 and self.map[i + k][j - k] == 1:      # check left diagonal
                            self.fit -= 1
                        if j + k < self.n_queen and self.map[i + k][j + k] == 1:    # check right diagonal
                            self.fit -= 1

    def show(self):
        print(np.matrix(self.map))
        print("Fitness: ",  self.fit)


if __name__ == '__main__':
    test = Board(5)
    test.set_queens()
    test.fitness()
    test.show()

