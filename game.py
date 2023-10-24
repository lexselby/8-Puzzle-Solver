import numpy as np


class game:
    def __init__(self, puzzle):
        self.n = puzzle['n']  # puzzle dimension
        self.start = np.array(puzzle['start'])  # puzzle start state
        self.goal = np.array(puzzle['goal'])  # puzzle goal state

    @staticmethod
    def nxn(arr):
        # finding the puzzle size
        x = 0
        y = 0
        puzzleSize = arr.shape
        x = puzzleSize[0]
        y = puzzleSize[1]

        # validating that the puzzle is of n by n form
        if x != y:
            return False
        else:
            return True

    def puzzleNumbers(self):
        # validating that the puzzle has all the correct numbers (0 through n-1)
        for i in range((self.n * self.n) - 1):
            if i not in self.start:
                return False
            if i not in self.goal:
                return False
            else:
                return True

    def validate(self):
        # checking that the start state isn't equal to the goal state
        if self.n <= 0 or self.start is None or self.goal is None:
            return False
        # checking that the size of the puzzle is of n by n form
        elif self.nxn(self.start) is False or self.nxn(self.goal) is False:
            return False
        # checking that the start state and goal state are of the same size
        elif self.nxn(self.start) != self.nxn(self.goal):
            return False
        # checking that all the correct numbers are in the start and goal state
        elif not self.puzzleNumbers():
            return False
        # if all validation tests pass, return true
        else:
            return True


