class Move:
    def __init__(self, newState):
        self.newState = newState  # state to be manipulated

    def moveLeft(self):
        # moving the zero left
        tempVal = self.newState.state[self.newState.zeroRow + 0][self.newState.zeroColumn - 1]
        self.newState.state[self.newState.zeroRow + 0][self.newState.zeroColumn - 1] = 0
        self.newState.state[self.newState.zeroRow][self.newState.zeroColumn] = tempVal
        self.newState.zeroRow = self.newState.zeroRow + 0
        self.newState.zeroColumn = self.newState.zeroColumn - 1

        # print(tempVal)

        return self.newState.state

    def moveRight(self):
        # moving the zero right
        tempVal = self.newState.state[self.newState.zeroRow + 0][self.newState.zeroColumn + 1]
        self.newState.state[self.newState.zeroRow + 0][self.newState.zeroColumn + 1] = 0
        self.newState.state[self.newState.zeroRow][self.newState.zeroColumn] = tempVal
        self.newState.zeroRow = self.newState.zeroRow + 0
        self.newState.zeroColumn = self.newState.zeroColumn + 1

        # print(tempVal)

        return self.newState.state

    def moveUp(self):
        # moving the zero up
        tempVal = self.newState.state[self.newState.zeroRow - 1][self.newState.zeroColumn + 0]
        self.newState.state[self.newState.zeroRow - 1][self.newState.zeroColumn + 0] = 0
        self.newState.state[self.newState.zeroRow][self.newState.zeroColumn] = tempVal
        self.newState.zeroRow = self.newState.zeroRow - 1
        self.newState.zeroColumn = self.newState.zeroColumn + 0

        # print(tempVal)

        return self.newState.state

    def moveDown(self):
        # moving the zero down
        tempVal = self.newState.state[self.newState.zeroRow + 1][self.newState.zeroColumn + 0]
        self.newState.state[self.newState.zeroRow + 1][self.newState.zeroColumn + 0] = 0
        self.newState.state[self.newState.zeroRow][self.newState.zeroColumn] = tempVal
        self.newState.zeroRow = self.newState.zeroRow + 1
        self.newState.zeroColumn = self.newState.zeroColumn + 0

        # print(tempVal)

        return self.newState.state



