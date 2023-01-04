import copy
import itertools

ROCK_START_X = 3
ROCK_START_Y = 4

POINTS = 'points'
BOTTOM = 'bottom'
TOP = 'top'
LEFT = 'left'
RIGHT = 'right'
CUSP = 'cusp'
ID = 'id'

ROCK_1 = {POINTS: [(0, 0), (1, 0), (2, 0), (3, 0)],
          BOTTOM: [(0, 0), (1, 0), (2, 0), (3, 0)],
          TOP: [(0, 0), (1, 0), (2, 0), (3, 0)],
          LEFT: [(0, 0)],
          RIGHT: [(3, 0)],
          CUSP: (0, 0),
          ID: 1}

ROCK_2 = {POINTS: [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
          BOTTOM: [(1, 0), (0, 1), (2, 1)],
          TOP: [(1, 2), (0, 1), (2, 1)],
          LEFT: [(1, 0), (0, 1), (1, 2)],
          RIGHT: [(1, 0), (2, 1), (1, 2)],
          CUSP: (1, 2),
          ID: 2}

ROCK_3 = {POINTS: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
          BOTTOM: [(0, 0), (1, 0), (2, 0)],
          TOP: [(0, 0), (0, 1), (2, 2)],
          LEFT: [(0, 0), (2, 1), (2, 2)],
          RIGHT: [(2, 0), (2, 1), (2, 2)],
          CUSP: (2, 2),
          ID: 3}

ROCK_4 = {POINTS: [(0, 0), (0, 1), (0, 2), (0, 3)],
          BOTTOM: [(0, 0)],
          TOP: [(0, 3)],
          LEFT: [(0, 0), (0, 1), (0, 2), (0, 3)],
          RIGHT: [(0, 0), (0, 1), (0, 2), (0, 3)],
          CUSP: (0, 3),
          ID: 4}

ROCK_5 = {POINTS: [(0, 0), (0, 1), (1, 0), (1, 1)],
          BOTTOM: [(0, 0), (1, 0)],
          TOP: [(0, 1), (1, 1)],
          LEFT: [(0, 0), (0, 1)],
          RIGHT: [(1, 0), (1, 1)],
          CUSP: (0, 1),
          ID: 5}

ROCKS = [ROCK_1, ROCK_2, ROCK_3, ROCK_4, ROCK_5]


def add_coords(p, v):
    p_x, p_y = p
    v_x, v_y = v
    
    return (p_x + v_x, p_y + v_y)


WALL = 0
ROCK = 1
VOID = 2

SPACE = 'space'
STATE = 'state'

ROCK_HEIGHT = 'rock_height'
WALL_HEIGHT = 'wall_height'

WALL_LEFT = 0
WALL_RIGHT = 8
WALL_FLOOR = 0

def get_new_tunnel():
    
    tunnel = {}
    
    tunnel[STATE] = {}
    
    tunnel[STATE][ROCK_HEIGHT] = WALL_FLOOR
    tunnel[STATE][WALL_HEIGHT] = WALL_FLOOR
    
    tunnel[SPACE] = {}
    
    for x in range(WALL_LEFT, WALL_RIGHT + 1):
        add_to_tunnel(tunnel, (x, WALL_FLOOR), WALL)
    
    update_tunnel(tunnel)
    
    return tunnel


def add_to_tunnel(tunnel, p, item):
    
    tunnel[SPACE][p] = item

MIN_WALL_FREE = 7

def update_tunnel(tunnel):
    
    h = tunnel[STATE][ROCK_HEIGHT]
    
    for y in range(h + 1, h + MIN_WALL_FREE + 1):
        add_to_tunnel(tunnel, (WALL_LEFT, y), WALL)
        add_to_tunnel(tunnel, (WALL_RIGHT, y), WALL)
        
        for x in range(WALL_LEFT + 1, WALL_RIGHT):
            
            add_to_tunnel(tunnel, (x, y), VOID)
    
    tunnel[STATE][WALL_HEIGHT] = h + MIN_WALL_FREE


def get_tunnel_rock_height(tunnel):
    
    rock_height = tunnel[STATE][ROCK_HEIGHT]
    
    return rock_height


def next_rock_coords(tunnel):
    
    rh = tunnel[STATE][ROCK_HEIGHT]
    
    y = rh + ROCK_START_Y
    x = ROCK_START_X
    
    return (x, y)


def set_rock(coord, rock, tunnel):
    
    for p in rock[POINTS]:
        point_rock = add_coords(coord, p)
        add_to_tunnel(tunnel, point_rock, ROCK)
    
    cusp = add_coords(coord, rock[CUSP])
    
    cusp_height = cusp[1]
    
    tunnel_height = tunnel[STATE][ROCK_HEIGHT]
    
    tunnel[STATE][ROCK_HEIGHT] = max(cusp_height, tunnel_height)
    
    update_tunnel(tunnel)


# Rock movement

def wind_generator(string):
    
    for char in itertools.cycle(string):
        
        yield char

def wind_generator_2(string):
    
    for i in itertools.cycle(range(0, len(string))):
        
        yield i, string[i]


def rock_generator(rocks):
    
    for rock in itertools.cycle(rocks):
        
        yield rock


RIGHT_VECTOR = (1, 0)
LEFT_VECTOR = (-1, 0)
DOWN_VECTOR = (0, -1)

LEFT_WIND = '<'
RIGHT_WIND = '>'

def move_rock_wind(rock_coord, rock, tunnel, wind):
    
    if wind == LEFT_WIND:
        move, coord = move_rock_left(rock_coord, rock, tunnel)
        return move, coord
    
    if wind == RIGHT_WIND:
        move, coord = move_rock_right(rock_coord, rock, tunnel)
        return move, coord


def move_rock_right(rock_coord, rock, tunnel):
    
    right_coord = add_coords(rock_coord, RIGHT_VECTOR)
    
    right_points = [add_coords(right_coord, p) for p in rock[RIGHT]]
    
    tunnel_points = [tunnel[SPACE][p] for p in right_points]
    
    right_free = all([p == VOID for p in tunnel_points])
    
    if right_free:
        return True, right_coord
    
    return False, rock_coord


def move_rock_left(rock_coord, rock, tunnel):
    
    left_coord = add_coords(rock_coord, LEFT_VECTOR)
    
    left_points = [add_coords(left_coord, p) for p in rock[LEFT]]
    
    tunnel_points = [tunnel[SPACE][p] for p in left_points]
    
    left_free = all([p == VOID for p in tunnel_points])
    
    if left_free:
        return True, left_coord
    
    return False, rock_coord


def move_rock_down(rock_coord, rock, tunnel):
    
    down_coord = add_coords(rock_coord, DOWN_VECTOR)
    
    down_points = [add_coords(down_coord, p) for p in rock[BOTTOM]]
    
    tunnel_points = [tunnel[SPACE][p] for p in down_points]
    
    down_free = all([p == VOID for p in tunnel_points])
    
    if down_free:
        return True, down_coord
    
    return False, rock_coord
    

# Log and monitoring functions


def print_tunnel(tunnel, rows):
    
    wh = tunnel[STATE][WALL_HEIGHT]
    
    for y in reversed(range(wh + 1 - rows, wh + 1)):
        
        line = ''
        
        for x in range(WALL_LEFT, WALL_RIGHT + 1):
            line += get_item_chr(tunnel[SPACE][(x, y)])
        
        print(line)
            

WALL_CHR = '$'
ROCK_CHR = '#'
VOID_CHR = '.'

def get_item_chr(item):
    
    if item == WALL:
        return WALL_CHR
    
    if item == ROCK:
        return ROCK_CHR
    
    if item == VOID:
        return VOID_CHR


# Cycle detection algorithm

CYCLE_FAIL = 0
CYCLE_SUCCESS = 1

def detect_cycle(seq):
    
    seq_len = len(seq)
    
    for index_1 in range(seq_len):
    
        for index_2 in range(index_1 + 1, seq_len):
            
            if seq[index_1] == seq[index_2]:
                cycle_len = (index_2 - index_1)
                
                if check_cycle(seq, index_1, cycle_len):
                    return CYCLE_SUCCESS, (index_1, cycle_len)
    
    return CYCLE_FAIL, None


def check_cycle(seq, index, cycle_len):
    
    seq_len = len(seq)
    
    for i in range(index, index + cycle_len):
        
        if (i + cycle_len * 2) >= seq_len:
            return False
        
        if seq[i] != seq[i + cycle_len] or seq[i] != seq[i + 2 * cycle_len]:
            
            return False

    return True




















