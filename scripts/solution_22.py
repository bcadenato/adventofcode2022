import puzzles.puzzle_22 as puzzle

print("""
Part 1
""")

SAMPLE_FILE = 'input/sample_input_22.txt'
PROBLEM_FILE = 'input/input_22.txt'

board, instructions = puzzle.read_file(PROBLEM_FILE)

state = puzzle.get_starting_state(board)

for instruction in instructions:
    state = puzzle.process_instruction(board, state, instruction)

password = puzzle.get_password(state)

print(f'The password is {password}')

print("""
Part 2
""")

sides = [ [puzzle.DIR_LEFT, puzzle.DIR_DOWN, (51, 51), (51, 100), (1, 101), (50, 101)], 
          [puzzle.DIR_LEFT, puzzle.DIR_RIGHT, (51, 1), (51, 50), (1, 150), (1, 101)],
          [puzzle.DIR_DOWN, puzzle.DIR_LEFT, (51, 150), (100, 150), (50, 151), (50, 200)],
          [puzzle.DIR_UP, puzzle.DIR_RIGHT, (51, 1), (100, 1), (1, 151), (1, 200)],
          [puzzle.DIR_DOWN, puzzle.DIR_LEFT, (101, 50), (150, 50), (100, 51), (100, 100)],
          [puzzle.DIR_RIGHT, puzzle.DIR_LEFT, (150, 50), (150, 1), (100, 101), (100, 150)],
          [puzzle.DIR_UP, puzzle.DIR_UP, (150, 1), (101, 1), (50, 200), (1, 200)] ]

side_table = puzzle.get_side_table(sides)

board, instructions = puzzle.read_file(PROBLEM_FILE)

state = puzzle.get_starting_state(board)

for instruction in instructions:
    state = puzzle.process_instruction_2(board, state, instruction, side_table)

password = puzzle.get_password(state)

print(f'The password is {password}')




















