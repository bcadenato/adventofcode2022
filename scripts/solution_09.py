import puzzles.puzzle_09 as puzzle

# First Problem

SAMPLE_INPUT_FILE = 'input/sample_input_09.txt'

with open(SAMPLE_INPUT_FILE) as f:
    lines = f.read().splitlines()

sample_grid = {}
H_pos = (0, 0)
T_pos = (0, 0)

for line in lines:
    move = puzzle.read_move(line)
    (H_pos, T_pos) = puzzle.process_moves(sample_grid, H_pos, T_pos, move)

print(f'The number of knots visited by T is {puzzle.count_T_positions(sample_grid)}')

puzzle.paint_grid(sample_grid)

PROBLEM_INPUT_FILE = 'input/input_09.txt'

with open(PROBLEM_INPUT_FILE) as f:
    lines = f.read().splitlines()

problem_grid = {}
H_pos = (0, 0)
T_pos = (0, 0)

for line in lines:
    move = puzzle.read_move(line)
    (H_pos, T_pos) = puzzle.process_moves(problem_grid, H_pos, T_pos, move)

print(f'The number of knots visited by T is {puzzle.count_T_positions(problem_grid)}')

# Part two

problem_grid_2 = {}
chain = [(0, 0), ] * 10

for line in lines:
    move = puzzle.read_move(line)
    chain = puzzle.process_moves_chain(problem_grid_2, chain, move)

print(f'The number of knots visited by T is {puzzle.count_T_positions(problem_grid_2)}')


