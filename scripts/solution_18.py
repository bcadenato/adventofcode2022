import puzzles.puzzle_18 as puzzle

print("""
Part 1
""")

SAMPLE_FILE = 'input/sample_input_18.txt'
PROBLEM_FILE = 'input/input_18.txt'

cubes = puzzle.read_file(PROBLEM_FILE)

exposed_sides = 0

for cube in cubes:
    
    exposed_sides += puzzle.count_exposed_sides(cubes, cube)

print(f'Total number of exposed sides is {exposed_sides}')

print("""
Part 2
""")

# First try was 3,336 - The answer is too high
# First try was 347 - The answer is too low

cubes = puzzle.get_cube_space(cubes)

cubes = puzzle.classify_void(cubes)

exposed_sides_2 = 0

for cube in puzzle.get_cubes_lava(cubes):
    
    exposed_sides_2 += puzzle.count_exposed_sides_2(cubes, cube)

print(f'Total number of exposed sides is {exposed_sides_2}')
















