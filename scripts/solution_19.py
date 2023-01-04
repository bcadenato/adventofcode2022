import itertools
import operator
import puzzles.puzzle_19 as puzzle

print("""
Part 1
""")

# First answer has been 873 - It is too low
# Final answer is 988

SAMPLE_FILE = 'input/sample_input_19.txt'
PROBLEM_FILE = 'input/input_19.txt'

blueprints = puzzle.read_blueprint_file(SAMPLE_FILE)

operations = []

for blueprint in blueprints:
    operations.append(puzzle.get_new_operation(blueprint))

MAX_TIME = 24

quality_levels = []

# for operation in operations:
#     blueprint = operation[puzzle.OP_BLUEPRINT]
#     start_log = operation[puzzle.OP_LOG]
#     
#     start_log = puzzle.simulate_log(blueprint, start_log, MAX_TIME)
#     
#     end_logs = puzzle.prune_logs(start_log, MAX_TIME)
#     
#     print(f'Blueprint ID: {blueprint[puzzle.BP_ID]:2} Number of leaves = {len(end_logs)}')
#     
#     max_log = puzzle.max_geode(start_log, MAX_TIME)
#     
#     max_geode_number = max_log[puzzle.LOG_STATE][puzzle.RS_GEODE]
#     
#     quality_level = blueprint[puzzle.BP_ID] * max_geode_number
#     
#     quality_levels.append(quality_level)
# 
# total_quality_level = list(itertools.accumulate(quality_levels, operator.add))
# 
# print()
# print(f'Total quality level is {total_quality_level[-1]}')

print("""
Part 2
""")

# First answer is 7700 - Answer is too low

blueprints = puzzle.read_blueprint_file(PROBLEM_FILE)

operations = []

for i in range(0, 3):
    operations.append(puzzle.get_new_operation(blueprints[i]))

MAX_TIME = 32

max_geode_levels = []

for operation in operations:
    blueprint = operation[puzzle.OP_BLUEPRINT]
    start_log = operation[puzzle.OP_LOG]
    
    start_log = puzzle.simulate_log(blueprint, start_log, MAX_TIME)
    
    end_logs = puzzle.prune_logs(start_log, MAX_TIME)
    
    print(f'Blueprint ID: {blueprint[puzzle.BP_ID]:2} Number of leaves = {len(end_logs)}')
    
    max_log = puzzle.max_geode(start_log, MAX_TIME)
    
    max_log_signature = puzzle.get_log_signature(max_log)
    
    print(f'Max Log signature is {max_log_signature}')
    
    max_geode_number = max_log[puzzle.LOG_STATE][puzzle.RS_GEODE]
    
    max_geode_levels.append(max_geode_number)

max_geode_level = list(itertools.accumulate(max_geode_levels, operator.mul))

print()
print(f'Max Geodes Product is {max_geode_level[-1]}')

