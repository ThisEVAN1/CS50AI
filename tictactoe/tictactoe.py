"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_amount = 0
    o_amount = 0

    # Count all the cells in the board
    for row in board:
        for cell in row:
            # Increment the amount of X or O
            if cell == X:
                x_amount += 1
            if cell == O:
                o_amount += 1
    
    # Return X if the amount of X is less than O, else return O 
    return X if x_amount <= o_amount else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    # Get the index and coordinates of the cell
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                possible_actions.add((i, j))

    return possible_actions 


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    clone = copy.deepcopy(board)
    row, column = action
    if clone[row][column] != EMPTY or (row < 0 or row > 2) or (column < 0 or column > 2):
        raise ValueError
    else:
        clone[row][column] = player(board)

    return clone


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check diagonal wins
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O

    # Check vertical and horizontal wins
    for i in range(3):
        if board[0][i] == X and board[1][i] == X and board[2][i] == X:
            return X
        if board[i][0] == X and board[i][1] == X and board[i][2] == X:
            return X
        if board[0][i] == O and board[1][i] == O and board[2][i] == O:
            return O
        if board[i][0] == O and board[i][1] == O and board[i][2] == O:
            return O
        
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if there is a winner
    if winner(board) != None:
        return True
    
    # Check if one of the board isn't filled yet
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
            
    # Return true if it is a tie
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def max_value(board):
    '''
    Returns the largest value
    '''
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    '''
    Returns the smallest value
    '''
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    best_action = None

    if terminal(board):
        return None
    
    if player(board) == X:
        value = -math.inf
        for action in actions(board):
            new_value = min_value(result(board, action))
            if new_value > value:
                value = new_value
                best_action = action
    if player(board) == O:
        value = math.inf
        for action in actions(board):
            new_value = max_value(result(board, action))
            if new_value < value:
                value = new_value
                best_action = action

    return best_action
    

