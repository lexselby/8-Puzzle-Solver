class Rules:
    def __init__(self, s):
        self.s = s  # state to be evaluated

    def left(self):
        # checking if moving left is a valid rule
        return self.s.zeroColumn != 0

    def right(self):
        # checking if moving right is a valid rule
        return self.s.zeroColumn != self.s.dimension - 1

    def up(self):
        # checking if moving up is a valid rule
        return self.s.zeroRow != 0

    def down(self):
        # checking if moving down is a valid rule
        return self.s.zeroRow != self.s.dimension - 1
