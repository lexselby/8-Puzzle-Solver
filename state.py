class State:
    def __init__(self, dimension, startState):
        self.dimension = dimension  # puzzle dimension
        self.state = startState  # puzzle state
        self.zeroRow = 0  # row that the zero tile is located
        self.zeroColumn = 0  # column that the zero tile is located
        self.move = None  # what move was made to get to this state
        self.ruleList = []  # list of possible moves that can be made after from this state
        self.singleListRep = []  # condensing the state into a single list for comparison purposes
        self.findZero()  # finding the zero tiles position upon state object initialization
        self.generateSingleListRep()  # generating the single list representation of the state upon initialization

    def findZero(self):
        # finding the location of the zero tile
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.state[i][j] == 0:
                    self.zeroRow = i
                    self.zeroColumn = j

        # print("\nBlank Column: ", self.zeroColumn + 1, "\nBlank Row: ", self.zeroRow + 1)

    def generateSingleListRep(self):
        # generating the single list representation of the state from the current list of lists representation
        for sublist in self.state:
            for i in sublist:  # iterating through the values in each sublist of the list containing the state
                self.singleListRep.append(i)  # appending to the singleListRep list variable



