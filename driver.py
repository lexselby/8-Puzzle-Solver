from solver import Play


def main():
    puzzleSolver = Play()

    # loading the puzzle and its state
    puzzleSolver.loadPuzzle()
    puzzleSolver.loadState()

    # solving the puzzle using backtracking and printing results
    print("Solving using Backtracking\n")
    if puzzleSolver.solveUsingBacktracking():
        print("Solution found in ", len(puzzleSolver.previousMoves) - 1, "\n")
        print("Nodes examined: ", puzzleSolver.consideredStates, "\n")
        for s in puzzleSolver.previousMoves:
            print(s.move, "\n", s.state, "\n")
        print("GOAL!!!\n")
    else:
        print("OOPS... solution not found.")

    # solving the puzzle using iterative backtracking and printing results
    print("Solving using Iterative Backtracking\n")
    if puzzleSolver.solveUsingIterativeBacktracking():
        print("Solution found in ", len(puzzleSolver.previousMoves) - 1, "\n")
        print("Nodes examined: ", puzzleSolver.consideredStates, "\n")
        for s in puzzleSolver.previousMoves:
            print(s.move, "\n", s.state, "\n")
        print("GOAL!!!\n")
    else:
        print("OOPS... solution not found.")

    # solving the puzzle using a graph search algorithm and printing results
    if puzzleSolver.graphSearchAlgorithm():
        print("Solution found in ", len(puzzleSolver.previousMoves) - 1, "\n")
        print("Nodes examined: ", puzzleSolver.consideredStates, "\n")
        print("Generated states: ", puzzleSolver.generatedStates, "\n")
        for s in puzzleSolver.previousMoves:
            print(s.move, "\n", s.state, "\n")
        print("GOAL!!!\n")
    else:
        print("OOPS... solution not found.")

    # solving the puzzle using the A* algorithm and printing results
    if puzzleSolver.AstarAlgorithm():
        print("Solution found in ", len(puzzleSolver.previousMoves) - 1, "\n")
        print("Nodes examined: ", puzzleSolver.consideredStates, "\n")
        print("Generated states: ", puzzleSolver.generatedStates, "\n")
        for s in puzzleSolver.previousMoves:
            print(s.move, "\n", s.state, "\n")
        print("GOAL!!!\n")
    else:
        print("OOPS... solution not found.")


if __name__ == '__main__':
    main()
