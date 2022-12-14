import puzzles.puzzle_11 as puzzle

# Part 1

print("""
Part 1
""")

# Sample solution

SAMPLE_INPUT = 'input/sample_input_11.txt'

sample_monkey_data = puzzle.read_input(SAMPLE_INPUT)

for i in range(0, 20):
    puzzle.play_round(sample_monkey_data)

sample_monkey_business = puzzle.calculate_monkey_business(sample_monkey_data)

# Problem solution

print(f'Sample Monkey Business is {sample_monkey_business}')

PROBLEM_INPUT = 'input/input_11.txt'

problem_monkey_data = puzzle.read_input(PROBLEM_INPUT)

for i in range(0, 20):
    puzzle.play_round(problem_monkey_data)

problem_monkey_business = puzzle.calculate_monkey_business(problem_monkey_data)

print(f'problem Monkey Business is {problem_monkey_business}')

# Part 2

print("""
Part 2
""")

# Sample solution

sample_monkey_data = puzzle.read_input(SAMPLE_INPUT)

sample_boredom_factor = puzzle.get_boredom_factor(sample_monkey_data)

no_bored = lambda x: x % sample_boredom_factor

for i in range(0, 10000):
    puzzle.play_round(sample_monkey_data, bored = no_bored)

sample_monkey_business = puzzle.calculate_monkey_business(sample_monkey_data)

print(f'Sample Monkey Business is {sample_monkey_business}')

# Problem solution

problem_monkey_data = puzzle.read_input(PROBLEM_INPUT)

problem_boredom_factor = puzzle.get_boredom_factor(problem_monkey_data)

no_bored = lambda x: x % problem_boredom_factor

for i in range(0, 10000):
    puzzle.play_round(problem_monkey_data, bored = no_bored)

problem_monkey_business = puzzle.calculate_monkey_business(problem_monkey_data)

print(f'Problem Monkey Business is {problem_monkey_business}')

