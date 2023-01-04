import logging
import puzzles.puzzle_16 as puzzle

logging.basicConfig(level=logging.WARNING, filename='logs/puzzle_16.log', filemode='w')

print("""
Part 1
""")

SAMPLE_FILE = 'input/sample_input_16.txt'

sample_cave = puzzle.read_file(SAMPLE_FILE)

path_set = []

current_path = puzzle.get_path_start('AA')

path_set.append(current_path)

actions = puzzle.get_actions(sample_cave, current_path)

puzzle.evolve_path(sample_cave, path_set, current_path, actions)

n_paths_alive = puzzle.count_paths_alive(path_set, 30)

i = 1

while n_paths_alive > 0:
    current_path = path_set[0]
    
    logging.debug(f'Sample Path:\n\n{current_path} in step {i}')
    
    actions = puzzle.get_actions(sample_cave, current_path)
    
    logging.debug(f'Sample Actions:\n\n{actions} in step {i}\n')
    
    if current_path[puzzle.PATH_STATE][puzzle.STEPS] <= 30:
        puzzle.evolve_path(sample_cave, path_set, current_path, actions)
        logging.debug(f'Paths ongoing after step {i}\n{puzzle.path_set_str(path_set)}')
    else:
        puzzle.set_path_stale(current_path)
    
    n_paths_alive = puzzle.count_paths_alive(path_set, 30)
    
    logging.debug(f'Step {i} with {n_paths_alive} paths alive\n\n{path_set}')
    
    i += 1


print(f'Path set after loop {i}:\n\n{puzzle.path_set_str(path_set)}')

max_pressure = 0

for path in path_set:
    total_path_pressure = puzzle.calculate_pressure_on_path(path)
    
    max_pressure = max(max_pressure, total_path_pressure)
    
    print(f'Total pressure is {total_path_pressure}')

print(f'\nMax Pressure is {max_pressure}')

print("""
Problem solution
""")

PROBLEM_FILE = 'input/input_16.txt'

problem_cave = puzzle.read_file(PROBLEM_FILE)

path_set = []

current_path = puzzle.get_path_start('AA')

path_set.append(current_path)

actions = puzzle.get_actions(problem_cave, current_path)

puzzle.evolve_path(problem_cave, path_set, current_path, actions)

n_paths_alive = puzzle.count_paths_alive(path_set, 30)

i = 1

while n_paths_alive > 0:
    current_path = path_set[0]
    
    logging.debug(f'Problem Path:\n\n{current_path} in step {i}')
    
    actions = puzzle.get_actions(problem_cave, current_path)
    
    logging.debug(f'Problem Actions:\n\n{actions} in step {i}\n')
    
    if current_path[puzzle.PATH_STATE][puzzle.STEPS] <= 30:
        puzzle.evolve_path(problem_cave, path_set, current_path, actions)
        logging.debug(f'Paths ongoing after step {i}\n{puzzle.path_set_str(path_set)}')
    else:
        puzzle.set_path_stale(current_path)
    
    n_paths_alive = puzzle.count_paths_alive(path_set, 30)
    
    logging.warning(f'Step {i} with {n_paths_alive} paths alive')
    
    i += 1


print(f'Path calculation finished after loop {i}')

max_pressure = 0

for path in path_set:
    total_path_pressure = puzzle.calculate_pressure_on_path(path)
    
    max_pressure = max(max_pressure, total_path_pressure)

print(f'\nMax Pressure is {max_pressure}')











