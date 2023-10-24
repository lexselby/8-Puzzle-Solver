class Heuristics:
    def __init__(self, s1, s2):
        self.s1 = s1  # start state
        self.s2 = s2  # goal state
        self.misplacedTiles = 0
        self.manhattanDistance = 0
        self.findMisplacedTiles()  # find the number of misplaced tiles on initialization
        self.findManhattanDistance()  # find the manhattan distance on initialization
        self.cost = self.misplacedTiles + self.manhattanDistance  # determine the total cost on initialization

    def findMisplacedTiles(self):
        # counting the number of misplaced tiles
        for i in range(self.s1.dimension):
            for j in range(self.s2.dimension):
                if self.s1.state[i][j] != self.s2.state[i][j]:
                    self.misplacedTiles += 1

    def findManhattanDistance(self):
        # finding the manhattan distance
        sumDistances = 0
        mDist = [0] * (self.s1.dimension * self.s1.dimension)
        # print(mDist)

        for i in range(self.s1.dimension):
            for j in range(self.s1.dimension):
                if self.s1.state[i][j] != self.s2.state[i][j]:
                    # print("check")
                    for x in range(self.s1.dimension):
                        for y in range(self.s1.dimension):
                            if self.s2.state[x][y] == self.s1.state[i][j]:
                                current = self.s2.state[x][y]
                                mDist[current] = abs(i - x) + abs(j - y)  # manhattan distance formula
                                # print(mDist[current])
        for d in mDist:
            sumDistances += d
        self.manhattanDistance = sumDistances
        # print(sumDistances)

