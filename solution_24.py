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

# print(f'\nStart position is {start_position}\nGoal position is {goal_position}')

# paths = {}
# min_time = math.inf

# # Start algorithm

# position = start_position
# time = 0
# distance = puzzle.calculate_distance(position, goal_position)

# explore_queue = [(position, time, distance)]

# iterations = 0

# while explore_queue:

#     iterations += 1

#     explore_queue.sort(key=lambda x: (x[2] + x[1], x[2], x[1]), reverse=True)
#     position, time, distance = explore_queue.pop()

#     # print(f'Exploring position {position} at time {time} - Iteration {iterations}')

#     if (position, time, distance) in paths:
#         continue

#     if position == goal_position:
#         print(f'Got to goal after {time} minutes')

#         if time < min_time:
#             min_time = time

#         break

#     if (time + distance) > min_time:
#         break

#     paths[(position, time, distance)] = True

#     time += 1

#     moves = puzzle.get_moves(valley[time], position)
#     options = sorted([(move, time, puzzle.calculate_distance(move, goal_position)) for move in moves], key=lambda x: x[2], reverse=True)
#     explore_queue.extend(options)

# print("""
# Part 2
# """)

# # Second part

# start_position = (120, 26)
# goal_position = (1, 0)

# print(f'\nStart position is {start_position}\nGoal position is {goal_position}')

# paths = {}
# min_time = math.inf

# position = start_position
# time = 269
# distance = puzzle.calculate_distance(position, goal_position)

# explore_queue = [(position, time, distance)]

# iterations = 0

# while explore_queue:

#     iterations += 1

#     explore_queue.sort(key=lambda x: (x[2] + x[1], x[2], x[1]), reverse=True)
#     position, time, distance = explore_queue.pop()

#     # print(f'Exploring position {position} at time {time} - Iteration {iterations}')

#     if (position, time, distance) in paths:
#         continue

#     if position == goal_position:
#         print(f'Got to goal after {time} minutes')

#         if time < min_time:
#             min_time = time

#         break

#     if (time + distance) > min_time:
#         break

#     paths[(position, time, distance)] = True

#     time += 1

#     moves = puzzle.get_moves(valley[time], position)
#     options = sorted([(move, time, puzzle.calculate_distance(move, goal_position)) for move in moves], key=lambda x: x[2], reverse=True)
#     explore_queue.extend(options)


# start_position = (1, 0)
# goal_position = (120, 26)

# print(f'\nStart position is {start_position}\nGoal position is {goal_position}')

# paths = {}
# min_time = math.inf

# position = start_position
# time = 555
# distance = puzzle.calculate_distance(position, goal_position)

# explore_queue = [(position, time, distance)]

# iterations = 0

# while explore_queue:

#     iterations += 1

#     explore_queue.sort(key=lambda x: (x[2] + x[1], x[2], x[1]), reverse=True)
#     position, time, distance = explore_queue.pop()

#     # print(f'Exploring position {position} at time {time} - Iteration {iterations}')

#     if (position, time, distance) in paths:
#         continue

#     if position == goal_position:
#         print(f'Got to goal after {time} minutes')

#         if time < min_time:
#             min_time = time

#         break

#     if (time + distance) > min_time:
#         break

#     paths[(position, time, distance)] = True

#     time += 1

#     moves = puzzle.get_moves(valley[time], position)
#     options = sorted([(move, time, puzzle.calculate_distance(move, goal_position)) for move in moves], key=lambda x: x[2], reverse=True)
#     explore_queue.extend(options)























