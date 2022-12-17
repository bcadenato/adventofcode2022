import math
import logging

SANDHOLE_COORD = (500, 0)

ITEM_ROCK = '#'
ITEM_AIR = '.'
ITEM_SAND = 'o'

def read_lines(file):
    with open(file) as f:
        lines = f.read().splitlines()
    
    return lines


def read_cave(lines):
    cave = {}
    
    add_sandhole(cave)
    
    for wall_str in lines:
        read_wall(cave, wall_str)
    
    fill_cave(cave)
    
    return cave


def read_coord(coord):
    coord_x, coord_y = coord.split(sep=',')
    
    row = int(coord_y)
    col = int(coord_x)
    
    return (row, col)


def from_coord(coord):
    coord_x, coord_y = coord
    
    row = coord_y
    col = coord_x
    
    return (row, col)

def read_wall(cave, wall_str):
    tokens = wall_str.split()
    
    tokens = [read_coord(token) for token in tokens if token != '->']
    
    tokens_len = len(tokens)
    
    for i in range(0, tokens_len - 1):
        add_wall(cave, tokens[i], tokens[i+1])
    
    return cave


def add_wall(cave, start, end):
    start_row, start_col = start
    end_row, end_col = end
    
    min_row = min(start_row, end_row)
    max_row = max(start_row, end_row)
    min_col = min(start_col, end_col)
    max_col = max(start_col, end_col)
    
    logging.debug(f'Adding a wall from {start} to {end}:')
    
    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            logging.debug(f'\tAdding # to {(row, col)}')
            cave[(row, col)] = ITEM_ROCK
    
    return cave

def add_floor(cave, height, coord=SANDHOLE_COORD):
    sandhole_row, sandhole_col = from_coord(coord)
    
    floor_start = (sandhole_row + height, sandhole_col - height - 1)
    floor_end = (sandhole_row + height, sandhole_col + height + 1)
    
    add_wall(cave, floor_start, floor_end)
    
    return cave
    

def add_sandhole(cave, coord=SANDHOLE_COORD):
    (row, col) = coord[1], coord[0]
    
    logging.debug(f'Adding a sandhole in {(row, col)}')
    cave[(row, col)] = '+'
    
    return cave

 
def get_dims(cave):
    min_row, max_row = math.inf, -math.inf
    min_col, max_col = math.inf, -math.inf
    
    for key in cave.keys():
        row, col = key
        
        min_row = min(min_row, row)
        max_row = max(max_row, row)
        
        min_col = min(min_col, col)
        max_col = max(max_col, col)
    
    logging.debug(f'Cave dims are {(min_row, min_col, max_row, max_col)}')
    
    return (min_row, min_col, max_row, max_col)


def fill_cave(cave):
    (min_row, min_col, max_row, max_col) = get_dims(cave)
    
    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            if not (row, col) in cave:
                cave[(row, col)] = ITEM_AIR
    
    return cave


def cave_to_str(cave):
    (min_row, min_col, max_row, max_col) = get_dims(cave)
    
    cave_str = []
    
    for row in range(min_row, max_row + 1):
        
        cave_line = ''
        
        for col in range(min_col, max_col+ 1):
            cave_line += cave[(row, col)]
        
        cave_str.append(cave_line)
    
    return cave_str


def print_cave(cave):
    cave_str = cave_to_str(cave)
    
    for line in cave_str:
        print(line)


# Simulate sand dynamics

STATUS_VOID = -1
STATUS_SETTLED = 0
STATUS_MOVE = 1
STATUS_BLOCKED = 2

def next_position(cave, start):
    
    row, col = start
    
    down_position = (row + 1, col)
    
    if down_position in cave.keys():
        down_item = cave[down_position]
    else:
        return (STATUS_VOID, down_position)
    
    if down_item == ITEM_ROCK:
        pass
    elif down_item == ITEM_AIR:
        return (STATUS_MOVE, down_position)
    elif down_item == ITEM_SAND:
        pass
    else:
        logging.warning(f'Trying position {down_position} and found something strange {down_item}')
    
    left_position = (row + 1, col -1)
    
    if left_position in cave.keys():
        left_item = cave[left_position]
    else:
        return (STATUS_VOID, left_position)
    
    if left_item == ITEM_ROCK:
        pass
    elif left_item == ITEM_AIR:
        return (STATUS_MOVE, left_position)
    elif left_item == ITEM_SAND:
        pass
    else:
        logging.warning(f'Trying position {left_position} and found something strange {left_item}')
    
    right_position = (row + 1, col + 1)
    
    if right_position in cave.keys():
        right_item = cave[right_position]
    else:
        return (STATUS_VOID, right_position)
    
    if right_item == ITEM_ROCK:
        return (STATUS_SETTLED, start)
    elif right_item == ITEM_AIR:
        return (STATUS_MOVE, right_position)
    if right_item == ITEM_SAND:
        return (STATUS_SETTLED, start)
    else:    
        logging.warning(f'Trying position {right_position} and found something strange {right_item}')


def drop_sand(cave, start):
    
    start_item = cave[start]
    
    if start_item == ITEM_SAND:
        return STATUS_BLOCKED
    
    move_position = start
    
    while True:
        move = next_position(cave, move_position)
    
        move_status, move_position = move
        
        if move_status == STATUS_SETTLED:
            cave[move_position] = ITEM_SAND
            return STATUS_SETTLED
        
        if move_status == STATUS_VOID:
            return STATUS_VOID
        
        if move_status == STATUS_MOVE:
            continue















