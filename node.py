class Node:
    def __init__(self, data, parent, depth, cost):
        self.data = data  # the state of the node
        self.parent = parent  # the parent node of the current node
        self.depth = depth  # the depth of the node
        self.cost = cost  # the cost of the node

    def __lt__(self, other):
        # comparison of two nodes
        return self.cost < other.cost






