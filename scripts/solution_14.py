import logging
import puzzles.puzzle_14 as puzzle

logging.basicConfig(level=logging.WARNING)

print("""Part 1
""")

print("""
Sample solution
""")

SAMPLE_FILE = 'input/sample_input_14.txt'

sample_lines = puzzle.read_lines(SAMPLE_FILE)
cave = puzzle.read_cave(sample_lines)

cave_str = puzzle.cave_to_str(cave)

for line in cave_str:
    print(line)

status = puzzle.STATUS_MOVE
sand_count = 0

while status != puzzle.STATUS_VOID:
    
    logging.debug(f'Dropping unit of sand number {sand_count}')
    
    status = puzzle.drop_sand(cave, (0, 500))
    
    if status == puzzle.STATUS_SETTLED:
        sand_count += 1

print(f'Operation completed with status {status} after {sand_count} units of sand')

cave_str = puzzle.cave_to_str(cave)

for line in cave_str:
    print(line)

print("""
Problem solution
""")

PROBLEM_FILE = 'input/input_14.txt'

problem_lines = puzzle.read_lines(PROBLEM_FILE)
cave = puzzle.read_cave(problem_lines)

status = puzzle.STATUS_MOVE
sand_count = 0

while status != puzzle.STATUS_VOID:
    
    logging.debug(f'Dropping unit of sand number {sand_count}')
    
    status = puzzle.drop_sand(cave, (0, 500))
    
    if status == puzzle.STATUS_SETTLED:
        sand_count += 1

print(f'Operation completed with status {status} after {sand_count} units of sand')

print("""
Part 2
""")

print("""
Sample solution
""")

sample_lines = puzzle.read_lines(SAMPLE_FILE)
cave = puzzle.read_cave(sample_lines)

puzzle.print_cave(cave)

min_row, min_col, max_row, max_col = puzzle.get_dims(cave)

puzzle.add_floor(cave, max_row + 2)

puzzle.fill_cave(cave)

puzzle.print_cave(cave)

status = puzzle.STATUS_MOVE
sand_count = 0

while not status == puzzle.STATUS_BLOCKED:
    status = puzzle.drop_sand(cave, (0, 500))
    
    if status == puzzle.STATUS_SETTLED:
            sand_count += 1

print(f'Sand hole blocked after {sand_count} units of sand')

print()

puzzle.print_cave(cave)

print("""
Problem solution
""")

problem_lines = puzzle.read_lines(PROBLEM_FILE)
cave = puzzle.read_cave(problem_lines)

puzzle.print_cave(cave)

min_row, min_col, max_row, max_col = puzzle.get_dims(cave)

puzzle.add_floor(cave, max_row + 2)

puzzle.fill_cave(cave)

status = puzzle.STATUS_MOVE
sand_count = 0

while not status == puzzle.STATUS_BLOCKED:
    status = puzzle.drop_sand(cave, (0, 500))
    
    if status == puzzle.STATUS_SETTLED:
            sand_count += 1

print(f'Sand hole blocked after {sand_count} units of sand')










