import puzzles.puzzle_12 as puzzle

# Part 1

print("""
Part 1
""")

# Sample 

SAMPLE_INPUT = 'input/sample_input_12.txt'

with open(SAMPLE_INPUT) as f:
    sample_lines = f.read().splitlines()

sample_map = puzzle.read_map(sample_lines)

puzzle.find_path(sample_map, sample_map['start'])
# puzzle.find_path(sample_map, sample_map['start'], sample_map['end'])

print(f'Shortest number of steps is {sample_map["nodes"][sample_map["end"]]["cost"]}')

print("""Sample map
""")

sample_map_str = puzzle.print_map(sample_map)

for line in sample_map_str:
    print(line)

print("""
Sample solution - Part 2
""")

sample_map_2 = puzzle.read_map(sample_lines)

puzzle.find_path(sample_map_2, sample_map_2['end'], edge_function = puzzle.is_edge_down)

sample_start_nodes = list(sample_map_2['nodes'].items())
sample_start_nodes = list(filter(lambda x: x[1]['value'] == 'a', sample_start_nodes))
sample_start_nodes = list(sorted(sample_start_nodes, key=lambda x: x[1]['cost']))

for node in sample_start_nodes:
    print(node)

sample_map_str = puzzle.print_map(sample_map_2)

for line in sample_map_str:
    print(line)

# Problem

PROBLEM_INPUT = 'input/input_12.txt'

with open(PROBLEM_INPUT) as f:
    problem_lines = f.read().splitlines()

problem_map = puzzle.read_map(problem_lines)

end_node = problem_map['end']

puzzle.find_path(problem_map, problem_map['start'], end_node)

print("""
Problem
""")

print(f'Shortest number of steps is {problem_map["nodes"][end_node]["cost"]}')

print("""
Problem map
""")

problem_map_str = puzzle.print_map(problem_map)

for line in problem_map_str:
    print(line)

print("""
Problem solution - Part 2
""")

problem_map_2 = puzzle.read_map(problem_lines)

puzzle.find_path(problem_map_2, problem_map_2['end'], edge_function = puzzle.is_edge_down)

problem_start_nodes = list(problem_map_2['nodes'].items())
problem_start_nodes = list(filter(lambda x: x[1]['value'] == 'a', problem_start_nodes))
problem_start_nodes = list(sorted(problem_start_nodes, key=lambda x: x[1]['cost']))

print(f'The shortest starting point is {problem_start_nodes[0][0]}')

# for node in problem_start_nodes:
#     print(node)

problem_map_str = puzzle.print_map(problem_map_2)

for line in problem_map_str:
    print(line)



