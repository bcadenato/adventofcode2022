import re

FILE_INPUT = "puzzles/input_05.txt"
CRATES_HEIGHT = 8
STACKS_N = 9
MOVES_ROW = 10


def read_input(data):
    lines = data.splitlines()
    crates = lines[0:CRATES_HEIGHT]
    moves = lines[MOVES_ROW:]
    return (crates, moves)


def read_crates(crates, stack_no):
    crates_len = len(crates)
    stack = []
    stack_pos = (stack_no) * 4 + 1
    
    for row in reversed(range(0, crates_len)):
        row_len = len(crates[row])
        
        if stack_pos < row_len:
            crate = crates[row][stack_pos]
            if crate == ' ':
                return stack
            stack.append(crate)
        else: 
            return stack
        
    return stack 

MOVE_PATTERN = "move (\d*) from (\d) to (\d)"

def parse_move(move):
    (items_no, stack_from, stack_to) = re.findall(MOVE_PATTERN, move)[0]
    return (int(items_no), int(stack_from) - 1, int(stack_to) - 1)


def make_move(stacks, items_no, stack_from, stack_to):
    for i in range(0, items_no):
        item = stacks[stack_from].pop()
        stacks[stack_to].append(item)


# Validate solution

stacks = [
    ['Z', 'N'],
    ['M', 'C', 'D'],
    ['P']]

TEST_MOVES = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

moves = TEST_MOVES.splitlines()

for move in moves:
    items_no, stack_from, stack_to = parse_move(move)
    make_move(stacks, items_no, stack_from, stack_to)


# Problem solution

with open(FILE_INPUT) as f:
    data = f.read()

crates, moves = read_input(data)

stacks = list(range(0, STACKS_N))

for stack_no in range(0, STACKS_N):
    stacks[stack_no] = read_crates(crates, stack_no)

for move in moves:
    items_no, stack_from, stack_to = parse_move(move)
    make_move(stacks, items_no, stack_from, stack_to)

top_items = ''

for i, stack in enumerate(stacks):
    top_items += stack[-1]


    


















