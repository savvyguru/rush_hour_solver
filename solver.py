from collections import defaultdict
from copy import copy, deepcopy

# example input, red car is 00
# ......
# 12233.
# 1.045.
# 66045.
# .7775.
# ......

def parse_input(input_file):
    board = []
    file_reader = open(input_file,"r")
    for line in file_reader.readlines():
        board.append(list(line[:len(line)-1]))
    return board

# output -> cars_positions : dictionary
def get_car_positions(board):
    car_positions = defaultdict(list)
    for i in range(len(board)):
        for j in range(len(board[0])- 1):
                if board[i][j] != ".":
                    car_positions[str(board[i][j])].append([i,j])
    return car_positions

# output -> is_solved : boolean
def is_solved(board):
    for i in range(len(board)):
        if board[i][2] != "." and board[i][2] != "0":
            return False
        elif board[i][2] == "0":
            return True

# output -> next_board_states : list of 2d array
def get_possible_moves(board,car):
    next_board_states = []
    row = car[0][0]
    car_type = board[int(car[0][0])][int(car[0][1])]
    isHorizontal = True
    coordinates = []
    car_length = len(car)

    for pos in car:
        if pos[0] != row:
            isHorizontal = False

    if isHorizontal:
        for pos in car:
            coordinates.append(pos[1])
    else:
        for pos in car:
            coordinates.append(pos[0])

    if isHorizontal:
        car_row = car[0][0]
        for col in range(min(coordinates)-1,-1,-1):
            next_board_state = deepcopy(board)
            if board[car_row][col]==".":
                next_board_state[car_row][col]=car_type
                next_board_state[car_row][col+car_length]="."
                next_board_states.append(next_board_state)
            else:
                break

        for col in range(max(coordinates)+1,len(board[0])):
            next_board_state = deepcopy(board)
            if board[car_row][col]==".":
                next_board_state[car_row][col]=car_type
                next_board_state[car_row][col-car_length]="."
                next_board_states.append(next_board_state)
            else:
                break

    else:
        car_col = car[0][1]
        for row in range(min(coordinates)-1,-1,-1):
            next_board_state = deepcopy(board)
            if board[row][car_col]==".":
                next_board_state[row][car_col]=car_type
                next_board_state[row+car_length][car_col]="."
                next_board_states.append(next_board_state)
            else:
                break

        for row in range(max(coordinates)+1,len(board)):
            next_board_state = deepcopy(board)
            if board[row][car_col]==".":
                next_board_state[row][car_col]=car_type
                next_board_state[row-car_length][car_col]="."
                next_board_states.append(next_board_state)
            else:
                break

    return next_board_states

def backtrack(board,visited_boards):
    if is_solved(board):
        return "SOLVED"
    else:
        next_board_states = []
        car_positions = get_car_positions(board)
        for car in car_positions.values():
            possible_next_board_state = get_possible_moves(board,car)

            next_board_states += [item for item in possible_next_board_state if item not in visited_boards]

        if next_board_states == []:
            return "NO SOLUTION"
        for state in next_board_states:
            new_visited_boards = deepcopy(visited_boards) + [state]
            return backtrack(state,new_visited_boards)

# input -> board state : 2d array
# output -> solvable : boolean
def solver():
    ################### IDEA #####################
    # BFS for car in board, try all possible moves
    # check winning state
    # return false unsolvable 
    ##############################################

    visited_boards = []
    board = parse_input("input.txt")
    car_positions = get_car_positions(board)
    
    print(backtrack(board,visited_boards))


if __name__ == "__main__":
    solver()