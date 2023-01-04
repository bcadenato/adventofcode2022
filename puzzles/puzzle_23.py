import itertools
import math

ELF = '#'
GROUND = '.'

POSITION = 'position'
TARGET_POSITION = 'target_position'

ELF_ID = 'elf_id'
TARGET_ELVES = 'target_elves'

def elf_counter():

    for i in itertools.count():
        
        yield i

def read_elves(file):
    
    elves = {}
    counter = elf_counter()
    
    with open(file) as f:
        
        lines = f.read().splitlines()
   
    for y, line in enumerate(lines):
        
        for x, char in enumerate(line):

            if char == ELF:

                elf_id = next(counter)
                elves[elf_id] = {POSITION: (x, y),
                                 ELF_ID: elf_id}

    return elves


NORTH = 'north'
SOUTH = 'south'
WEST = 'west'
EAST = 'east'

VEC_NORTH = (0, -1)
VEC_SOUTH = (0, 1)
VEC_WEST = (-1, 0)
VEC_EAST = (1, 0)

VEC_NORTHWEST = (-1, -1)
VEC_NORTHEAST = (1, -1)
VEC_SOUTHWEST = (-1, 1)
VEC_SOUTHEAST = (1, 1)

NORTH_AREA = [VEC_NORTH, VEC_NORTHWEST, VEC_NORTHEAST]
SOUTH_AREA = [VEC_SOUTH, VEC_SOUTHWEST, VEC_SOUTHEAST]
WEST_AREA = [VEC_WEST, VEC_NORTHWEST, VEC_SOUTHWEST]
EAST_AREA = [VEC_EAST, VEC_NORTHEAST, VEC_SOUTHEAST]

ADJACENT_AREA = [VEC_NORTH,
                 VEC_SOUTH,
                 VEC_WEST,
                 VEC_EAST,
                 VEC_NORTHWEST,
                 VEC_NORTHEAST,
                 VEC_SOUTHWEST,
                 VEC_SOUTHEAST]

DIR_ID = 'dir_id'
DIR_VEC = 'dir_vec'
DIR_AREA = 'dir_area'

NORTH_DIR = {DIR_ID: NORTH,
             DIR_VEC: VEC_NORTH,
             DIR_AREA: NORTH_AREA}
 
SOUTH_DIR = {DIR_ID: SOUTH,
             DIR_VEC: VEC_SOUTH,
             DIR_AREA: SOUTH_AREA}
 
WEST_DIR = {DIR_ID: WEST,
             DIR_VEC: VEC_WEST,
             DIR_AREA: WEST_AREA}
 
EAST_DIR = {DIR_ID: EAST,
             DIR_VEC: VEC_EAST,
             DIR_AREA: EAST_AREA}


def calculate_next_position(elves, directions):

    target = {}

    for elf in elves.values():
        calculate_next_position_elf(elf, elves, directions, target)
    
    return elves, target
 

def is_elf_in_position(elves, position):

    for elf in elves:

        if position == elves[elf][POSITION]:

            return True
    
    return False


def is_elf_alone(elf, elves):

    position = elf[POSITION]
    adjacent_postions = [add_vector(position, vector) for vector in ADJACENT_AREA]

    return all(not is_elf_in_position(elves, adjacent_position) for adjacent_position in adjacent_postions)


def add_target(target, target_position, elf_id):

    if target_position in target:

        target[target_position].append(elf_id)

        return target
    
    target[target_position] = [elf_id]

    return target


def calculate_next_position_elf(elf, elves, directions, target):

    position = elf[POSITION]

    if is_elf_alone(elf, elves):
        elf[TARGET_POSITION] = position
        return

    for direction in directions:

        if space_available(elf, elves, direction):
            elf_id = elf[ELF_ID]

            target_position = add_vector(position, direction[DIR_VEC])
            elf[TARGET_POSITION] = target_position
            
            add_target(target, target_position, elf_id)
            
            return
    
    elf[TARGET_POSITION] = position
    return


def space_available(elf, elves, direction):

    position = elf[POSITION]
    space = get_space(position, direction)

    return all([not is_elf_in_position(elves, space_pos) for space_pos in space])


def get_space(position, direction):

    space = [add_vector(position, vector) for vector in direction[DIR_AREA]]
    return space


def add_vector(position, vector):

    p_x, p_y = position
    v_x, v_y = vector

    return (p_x + v_x, p_y + v_y)


def directions_gen():

    directions = [NORTH_DIR, SOUTH_DIR, WEST_DIR, EAST_DIR]

    while True:
        yield directions

        chg_dir = directions.pop(0)
        directions.append(chg_dir)
 
 
def process_positions(elves, target):

    for elf in elves.values():

        position = elf[POSITION]
        target_position = elf[TARGET_POSITION]

        if target_position == position:
            continue

        if len(target[target_position]) == 1:
            elf[POSITION] = target_position
        
        if len(target[target_position]) > 1:
            continue
    
    return elves, target
 
 
def calculate_minimum_rectangle(elves):

    min_x = math.inf
    max_x = - math.inf
    min_y = math.inf
    max_y = - math.inf

    for elf in elves.values():
        x, y = elf[POSITION]

        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    
    return min_x, min_y, max_x, max_y


def calculate_covered_ground(elves, min_x, min_y, max_x, max_y):

    ground = 0

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if not is_elf_in_position(elves, (x, y)):
                ground += 1
    
    return ground

 
 
 
 
 
 
 
 
 
 
 
