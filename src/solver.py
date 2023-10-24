import copy
from parser import parser
from game import game
from state import State
from rules import Rules
from move import Move
from node import Node
from heuristics import Heuristics
from collections import deque


class Play:
    def __init__(self):
        self.consideredStates = 0
        self.generatedStates = 0
        self.previousMoves = []  # list of previous moves
        self.puzzle = None  # puzzle data
        self.startState = None  # start state of the puzzle
        self.goalState = None  # goal state of the puzzle

    # loading the puzzle and validating it
    def loadPuzzle(self):
        isValid = False

        # requiring the puzzle to be valid before moving on
        while isValid is False:
            filename = input("Enter the filename: ")

            # parsing the json file containing the puzzle data
            json_parser = parser(filename)  # using the parser class
            parsed_puzzle = json_parser.parse()

            self.puzzle = game(parsed_puzzle)  # using the game class

            print("\nLoading puzzle...")

            # validating the puzzle using the game class methods
            if self.puzzle.validate() is True:
                print("\nThis is a valid puzzle!\n")
                isValid = True
            else:
                print("\nOOPS! This is not a valid puzzle...\n")
                isValid = False

        # printing the puzzle data for the user
        print("puzzle size: ", self.puzzle.n, " by ", self.puzzle.n, "\n\nstart s: \n", self.puzzle.start,
              "\n\ngoal s: \n", self.puzzle.goal, "\n")

    # loading the start state and the goal state of the puzzle using the state class
    def loadState(self):
        self.startState = State(self.puzzle.n, self.puzzle.start)
        self.startState.move = "start"
        self.goalState = State(self.puzzle.n, self.puzzle.goal)

    # determining the rules applicable to the given state
    @staticmethod
    def getMoves(s):
        stateRules = Rules(s)
        ruleList = []

        if stateRules.left() is True:
            ruleList.append("left")
            # self.previousMoves.append(self.executeMoves("left"))
        if stateRules.right() is True:
            ruleList.append("right")
            # self.previousMoves.append(self.executeMoves("right"))
        if stateRules.up() is True:
            ruleList.append("up")
            # self.previousMoves.append(self.executeMoves("up"))
        if stateRules.down() is True:
            ruleList.append("down")
            # self.previousMoves.append(self.executeMoves("down"))

        return ruleList

        # print(s.ruleList, "\n")

    # executing the appropriate moves on the current state based on the rules determined by the getMoves method
    @staticmethod
    def executeMoves(rule, s):
        newState = copy.deepcopy(s)

        if rule == "left":
            return Move(newState).moveLeft()
        if rule == "right":
            return Move(newState).moveRight()
        if rule == "up":
            return Move(newState).moveUp()
        if rule == "down":
            return Move(newState).moveDown()

    # solve using backtracking driver method
    def solveUsingBacktracking(self):
        self.consideredStates = 0
        self.generatedStates = 0
        self.previousMoves.clear()
        self.previousMoves.append(self.startState)
        return self.backtrackingAlgorithm(30)  # setting the depth bound to 30

    # solve using iterative backtracking driver method
    def solveUsingIterativeBacktracking(self):
        self.consideredStates = 0
        self.generatedStates = 0
        self.previousMoves.clear()
        self.previousMoves.append(self.startState)

        bound = 1
        while bound < 30 and not self.backtrackingAlgorithm(bound):
            self.previousMoves.clear()
            self.previousMoves.append(self.startState)
            bound += 1

        if bound == 30:
            return False
        else:
            return True

    # backtracking algorithm used by the two driver functions above
    def backtrackingAlgorithm(self, depthBound):
        # checking that the depth bound has not been passed
        if len(self.previousMoves) > depthBound:
            # print("\nLength of previous moves: ", len(self.previousMoves), depthBound)
            return False

        # checking if the goal state has been found
        if self.previousMoves[-1].singleListRep == self.goalState.singleListRep:
            return True

        else:
            # expanding the last state
            lastState = copy.deepcopy(self.previousMoves[-1])
            lastState.ruleList = self.getMoves(lastState)
            # print("\n", lastState.ruleList, "\n")

            for rule in lastState.ruleList:
                self.consideredStates += 1
                # generating the applicable rules to this state
                newState = State(lastState.dimension, self.executeMoves(rule, lastState))
                newState.move = rule

                # print(newState.state, newState.singleListRep)
                # adding the generated states to the previous moves list if they have not yet been discovered
                if not next((True for x in self.previousMoves if x.singleListRep == newState.singleListRep), False):
                    # print("\nState is new, appending...\n")
                    self.generatedStates += 1
                    self.previousMoves.append(newState)
                    # print(newState.state, "\n")
                    # print(self.previousMoves)

                    # recursively calling the algorithm
                    if self.backtrackingAlgorithm(depthBound):
                        return True

                    # backtracking
                    else:
                        # print("\nbacktracking...")
                        self.previousMoves = copy.deepcopy(self.previousMoves[:-1])

            # if nothing else works, the algorithm has failed to find a solution
            return False

    def graphSearchAlgorithm(self):
        self.consideredStates = 0
        self.generatedStates = 0
        self.previousMoves.clear()
        self.previousMoves.append(self.startState)

        # creating the first node for the start state of the puzzle
        n = Node(self.startState, None, None, None)

        # initializing the closedNodes and openNodes lists
        closedNodes = set([])
        openNodes = deque([])

        # appending the start state node to the openNodes list
        openNodes.append(n)

        # looping as long as there are nodes in the openNodes list
        while len(openNodes) != 0:
            # getting the first node in the list of openNodes
            current = openNodes.popleft()
            # print("Open nodes: ", len(openNodes), "\n")
            # moving the node from the open List to the closed List
            closedNodes.add(current)
            # print("Closed nodes: ", len(closedNodes), "\n")
            # setting the game state to the node we just popped off from the openNodes list
            gameState = copy.deepcopy(current.data)
            # print(gameState.state, "\n")
            # checking if we found the goal state
            if current.data.singleListRep == self.goalState.singleListRep:
                reverse = []
                # creating a list of the solution path
                while current.data.singleListRep != n.data.singleListRep:
                    reverse.append(current)
                    # print("Len reverse: ", len(closedNodes), "\n")
                    current = current.parent
                    # print("New current node: ", current.data.state, "\n")
                while len(reverse) != 0:
                    self.previousMoves.append(reverse.pop().data)
                # print("Previous moves: ", len(self.previousMoves), "\n")
                return True
            else:
                # generating applicable rules
                gameState.ruleList = self.getMoves(gameState)
                # print(gameState.ruleList, "\n")

                # executing moves based on the applicable rules found
                for rule in gameState.ruleList:
                    self.consideredStates += 1
                    tempState = State(gameState.dimension, self.executeMoves(rule, gameState))
                    tempState.move = rule
                    tempNode = Node(tempState, None, None, None)
                    if (next((True for x in closedNodes if x.data.singleListRep == tempNode.data.singleListRep), False)) \
                            and (next((True for y in openNodes if y.data.singleListRep == tempNode.data.singleListRep), False)):
                        # print("State already exists... moving on to next state")
                        continue
                        # adding the new state to the list if it is a state that has yet to be discovered
                    else:
                        # print("Appending new state... \n")
                        # print(tempNode.data.state, "\n")
                        self.generatedStates += 1
                        tempNode.parent = current
                        openNodes.append(tempNode)

        # if nothing else works, the algorithm has failed to find a solution
        return False

    # modified / extended version of the graph search algorithm
    def AstarAlgorithm(self):
        # heu = Heuristics(self.startState, self.goalState)
        # print(heu.misplacedTiles)
        # print(heu.manhattanDistance)

        self.consideredStates = 0
        self.generatedStates = 0
        self.previousMoves.clear()
        self.previousMoves.append(self.startState)

        # creating the first node for the start state of the puzzle
        n = Node(self.startState, None, 0, Heuristics(self.startState, self.goalState).cost)

        # initializing the closed nodes list and priority queue list
        closedNodes = set([])
        pQueue = deque([n])

        # looping as long as there are nodes in the openNodes list
        while len(pQueue) != 0:
            # sorting the priority queue
            sorted(pQueue)
            # print(pQueue)

            # popping the highest priority node
            current = pQueue.popleft()
            # print(current.data.state)
            # print("Open nodes: ", len(pQueue), "\n")

            # adding the node to the closed nodes list
            closedNodes.add(current)
            # print("Closed nodes: ", len(closedNodes), "\n")

            # setting the node as the current game state node
            gameState = copy.deepcopy(current.data)
            # print(gameState.state, "\n")

            # checking if we found the goal
            if current.data.singleListRep == self.goalState.singleListRep:
                reverse = []

                # tracing the solution path
                while current.data.singleListRep != n.data.singleListRep:
                    reverse.append(current)
                    # print("Len reverse: ", len(closedNodes), "\n")
                    current = current.parent
                    # print("New current node: ", current.data.state, "\n")
                while len(reverse) != 0:
                    self.previousMoves.append(reverse.pop().data)
                # print("Previous moves: ", len(self.previousMoves), "\n")
                return True

            # if we haven't found the goal, continue expanding
            else:
                # generating the rules applicable to the current game state
                gameState.ruleList = self.getMoves(gameState)
                # print(gameState.ruleList, "\n")

                # executing the moves based on the generated applicable moves
                for rule in gameState.ruleList:
                    self.consideredStates += 1
                    tempState = State(gameState.dimension, self.executeMoves(rule, gameState))
                    tempState.move = rule
                    tempNode = Node(tempState, None, None, None)
                    if (next((True for x in closedNodes if x.data.singleListRep == tempNode.data.singleListRep), False)) \
                            or (next((True for y in pQueue if y.data.singleListRep == tempNode.data.singleListRep), False)):
                        # print("State already exists... moving on to next state")
                        continue
                        # if the state is new / has not been found already we add it to the priority queue list
                    else:
                        # print("Appending new state... \n")
                        # print(tempNode.data.state, "\n")
                        self.generatedStates += 1
                        tempNode.parent = current
                        tempNode.depth = current.depth + 1
                        tempNode.cost = Heuristics(tempNode.data, self.goalState).cost
                        pQueue.append(tempNode)

        return False




















