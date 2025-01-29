N-Queens Problem Solver

This project provides a Python implementation to solve the N-Queens problem. The N-Queens problem is a classic algorithmic puzzle where the goal is to place N queens on an N×N chessboard such that no two queens threaten each other. This means that no two queens can share the same row, column, or diagonal.

chessBoard.py
This is the main Python script that contains the implementation of the N-Queens solver. It includes the following functions:
- **`createChessBoard(n)`**: Creates an N×N chessboard with alternating black and white squares.
- **`printChessBoard(chessBoard, setOfCombo)`**: Prints the chessboard with the queens placed in their respective positions.
- **`possibleLocation(nQueen)`**: Finds and prints all possible solutions for placing N queens on the chessboard without them threatening each other.
The script takes user input for the number of queens and ensures that the input is greater than 3, as the problem is trivial for smaller values.

Out File Sample.txt
This file contains sample output from running the `chessBoard.py` script. It lists all possible solutions for an 8-queens problem, showing the positions of the queens on the chessboard for each solution.

Requirements.txt
This file lists the dependencies required to run the project. Currently, it only requires the `itertools` library, specifically the `permutations` function, which is used to generate all possible arrangements of the queens.

PDF
This document (in Persian) explains the fundamental workings of the algorithm used in the project. It covers:
- How the number of queens is taken as input.
- How possible positions for the queens are calculated.
- How the chessboard is constructed and filled based on the number of queens.
- The conditions under which a solution is considered valid.

## How to Run
1. Ensure you have Python installed on your system.
2. Clone this repository or download the files.
3. Navigate to the directory containing the files.
4. Run the `chessBoard.py` script using Python:  python chessBoard.py
5. Enter the number of queens when prompted. The script will output all possible solutions to the console.
