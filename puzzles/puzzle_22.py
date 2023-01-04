import re

def read_file(file):
    
    board = {}
    instructions = []
    
    with open(file) as f:
        lines = f.read().splitlines()
    
    for y, line in enumerate(lines):
        if line == r'\n':
            break
        
        read_line(board, line, y + 1)
    
    instructions = read_instructions(lines[-1])
    
    return board, instructions


SPACE = '.'
WALL = '#'
 
def read_line(board, line, y):
    
    for x, char in enumerate(line):
        if char == SPACE or char == WALL:
            board[(x + 1, y)] = char 
    
    return board


RIGHT = 'R'
LEFT = 'L'

def read_instructions(line):
    
    tokens = re.split(r'(R|L)', line)
    
    instructions = []
    
    for token in tokens:
        if token == RIGHT or token == LEFT:
            instructions.append(token)
            continue
        
        instructions.append(int(token))
    
    return instructions

POSITION = 'position'
DIRECTION = 'direction'
DIR_RIGHT = 'dir_right'
DIR_LEFT = 'dir_left'
DIR_UP = 'dir_up'
DIR_DOWN = 'dir_down'
VEC_RIGHT = (1, 0)
VEC_LEFT = (-1, 0)
VEC_UP = (0, -1)
VEC_DOWN = (0, 1)

def get_starting_state(board):
    
    state = {}
    
    state[DIRECTION] = DIR_RIGHT
    
    start_x = min([x for x, y in board if y == 1 and board[(x, y)] == SPACE])
    
    state[POSITION] = (start_x, 1)
    
    return state


def get_state(position, direction):
    
    state = {}
    
    state[DIRECTION] = direction
    state[POSITION] = position
    
    return state


def get_direction_value(direction):
    
    if direction == DIR_RIGHT:
        return 0
    
    if direction == DIR_DOWN:
        return 1
    
    if direction == DIR_LEFT:
        return 2
    
    if direction == DIR_UP:
        return 3


FACTOR_Y = 1000
FACTOR_X = 4

def get_password(state):
    
    position = state[POSITION]
    direction = state[DIRECTION]
    
    x, y = position
    direction_value = get_direction_value(direction)
    
    password = FACTOR_X * x + FACTOR_Y * y + direction_value
    
    return password


def apply_rotation(rotation, direction):
    
    if rotation == RIGHT:
        if direction == DIR_RIGHT:
            return DIR_DOWN
        
        if direction == DIR_DOWN:
            return DIR_LEFT
        
        if direction == DIR_LEFT:
            return DIR_UP
        
        if direction == DIR_UP:
            return DIR_RIGHT
    
    if rotation == LEFT:
        if direction == DIR_RIGHT:
            return DIR_UP
        
        if direction == DIR_UP:
            return DIR_LEFT
        
        if direction == DIR_LEFT:
            return DIR_DOWN
        
        if direction == DIR_DOWN:
            return DIR_RIGHT


def get_vector(direction):
    
    if direction == DIR_RIGHT:
        return VEC_RIGHT
    
    if direction == DIR_LEFT:
        return VEC_LEFT
    
    if direction == DIR_UP:
        return VEC_UP
    
    if direction == DIR_DOWN:
        return VEC_DOWN


def add_vector(position, vector):
    
    x, y = position
    v_x, v_y = vector
    
    return (x + v_x, y + v_y)


def move(board, state, steps):
    
    position = state[POSITION]
    direction = state[DIRECTION]
    vector = get_vector(direction)
    
    for i in range(steps):
        next_position = add_vector(position, vector)
        
        if not next_position in board:
            next_position = opposite(board, position, direction)
            
            if board[next_position] == WALL:
                next_position = position
                break
            
            if board[next_position] == SPACE:
                position = next_position
                continue
    
        if board[next_position] == SPACE:
            position = next_position
            continue
        
        if board[next_position] == WALL:
            next_position = position
            break
        
    state[POSITION] = next_position
    
    return state


def rotate(state, rotation):
    direction = state[DIRECTION]
    
    new_direction = apply_rotation(rotation, direction)
    
    state[DIRECTION] = new_direction
    
    return state


def process_instruction(board, state, instruction):
    if instruction in [RIGHT, LEFT]:
        state = rotate(state, instruction)
    
    if isinstance(instruction, int):
        state = move(board, state, instruction)
    
    return state


def opposite(board, position, direction):
    
    if direction == DIR_RIGHT:
        opp_direction = DIR_LEFT
    
    if direction == DIR_LEFT:
        opp_direction = DIR_RIGHT
    
    if direction == DIR_UP:
        opp_direction = DIR_DOWN
    
    if direction == DIR_DOWN:
        opp_direction = DIR_UP
    
    vector = get_vector(opp_direction)
    
    can_move = True
    
    while can_move:
        
        next_position = add_vector(position, vector)
        
        if not next_position in board:
            return position
        
        position = next_position


def get_side_table(sides):
    
    side_table = {}
    
    for side in sides:
        
        side_table = process_side(side_table, side[0], side[1], side[2], side[3], side[4], side[5])
    
    return side_table


def process_side(side_table, direction_a, direction_b, point_a_1, point_a_2, point_b_1, point_b_2):
    
    a_1_x, a_1_y = point_a_1
    a_2_x, a_2_y = point_a_2
    
    b_1_x, b_1_y = point_b_1
    b_2_x, b_2_y = point_b_2
    
    a_x_len = (a_2_x - a_1_x)
    a_y_len = (a_2_y - a_1_y)
    
    b_x_len = (b_2_x - b_1_x)
    b_y_len = (b_2_y - b_1_y)
    
    direction_a_rev = apply_rotation(RIGHT, apply_rotation(RIGHT, direction_a))
    direction_b_rev = apply_rotation(RIGHT, apply_rotation(RIGHT, direction_b))
    
    for i in range(50):
        
        a_x = a_1_x + a_x_len // 49 * i
        a_y = a_1_y + a_y_len // 49 * i
        
        b_x = b_1_x + b_x_len // 49 * i
        b_y = b_1_y + b_y_len // 49 * i
        
        side_table[( (a_x, a_y), direction_a )] = ( (b_x, b_y), direction_b )
        side_table[( (b_x, b_y), direction_b_rev )] = ( (a_x, a_y), direction_a_rev )
    
    return side_table


def move_2(board, state, steps, side_table):
    
    position = state[POSITION]
    direction = state[DIRECTION]
    
    for i in range(steps):
        vector = get_vector(direction)
        
        next_position = add_vector(position, vector)
        next_direction = direction
        
        if not next_position in board:
            next_position, next_direction = side_table[(position, direction)]
            
            if board[next_position] == WALL:
                next_position = position
                next_direction = direction
                break
            
            if board[next_position] == SPACE:
                position = next_position
                direction = next_direction
                continue
    
        if board[next_position] == SPACE:
            position = next_position
            direction = next_direction
            continue
        
        if board[next_position] == WALL:
            next_position = position
            next_direction = direction
            break
        
    state[POSITION] = next_position
    state[DIRECTION] = next_direction
    
    return state


def process_instruction_2(board, state, instruction, side_table):
    if instruction in [RIGHT, LEFT]:
        state = rotate(state, instruction)
    
    if isinstance(instruction, int):
        state = move_2(board, state, instruction, side_table)
    
    return state















