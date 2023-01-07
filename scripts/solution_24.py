import puzzles.puzzle_24 as puzzle
import math

# INPUT_FILE = 'input/sample_input_24_2.txt'
INPUT_FILE = 'input/input_24.txt'

with open(INPUT_FILE) as f:
    valley_str = f.read()

valley = puzzle.Valley(valley_str)

min_x, max_x, min_y, max_y = valley.get_dims()

start_position = (min_x + 1, min_y)
goal_position = (max_x - 1, max_y)

time_1 = puzzle.calculate_shortest_path(valley, start_position, goal_position, start_time=0)
time_2 = puzzle.calculate_shortest_path(valley, goal_position, start_position, start_time=time_1)
time_3 = puzzle.calculate_shortest_path(valley, start_position, goal_position, start_time=time_2)

print(f'Part 1 - Total time is {time_1}')
print(f'Part 2 - Total time is {time_3}')























