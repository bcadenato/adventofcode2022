import logging
import puzzles.puzzle_16 as puzzle
import pprint
import itertools

logging.basicConfig(level=logging.WARNING, filename='logs/puzzle_16.log', filemode='w')

print("""
Part 1
""")

FILE = 'input/input_16.txt'

cave = puzzle.read_file(FILE)

# Test code

active_valves = puzzle.get_active_valves(cave)

# for valve in active_valves:
#     print(f"Valve {valve} has pressure {cave[valve]['rate']}")

valve_start = 'AA'

valves_set = active_valves | {valve_start}

valves_dists = puzzle.get_distance(cave, valves_set)

# for item in valves_dists.items():
#     print(item)

# start_path = puzzle.get_starting_path('AA', active_valves)
# 
# potential_paths = puzzle.get_potential_paths(cave, valves_dists, start_path, 1)
# 
# for path in potential_paths:
#     print(path)
# 
# start_path = puzzle.add_paths(cave, valves_dists, start_path, 30)
# 
# pressure_list = puzzle.calculate_pressure_path(start_path, 30)
# 
# print(max(pressure_list))
# 
# paths_len = puzzle.len_path(start_path)
# 
# print(max(paths_len))

print("""
Part 2
""")

max_time = 26

start_path = puzzle.get_starting_path_2('AA', active_valves)

start_path = puzzle.add_paths_2(cave, valves_dists, start_path, max_time, 1, 'AA')

# print(start_path)

pressure_list = puzzle.calculate_pressure_path_2(start_path, max_time)

print(f'\nThe maximum pressure is: {max(pressure_list)}')

path_list = puzzle.collect_end_paths(start_path, max_time)

print(f'\nThe number of final paths is {len(path_list)}')

total_pressure_list = []

for path in path_list:
    valves = path['valves']
    pressure_cum_1 = path['pressure_cum']
    
    next_path = puzzle.get_starting_path_2('AA', valves)
    next_path = puzzle.add_paths_2(cave, valves_dists, next_path, max_time, 1, 'AA')
    
    pressure_list = puzzle.calculate_pressure_path_2(next_path, max_time)
    pressure_cum_2 = max(pressure_list)
    
    total_pressure_cum = pressure_cum_1 + pressure_cum_2
    
    total_pressure_list.append(total_pressure_cum)

print(f'\nThe maximum pressure is: {max(total_pressure_list)}')

    
    
    












