import puzzles.puzzle_21 as puzzle

print("""
Part 1
""")

SAMPLE_FILE = 'input/sample_input_21.txt'
PROBLEM_FILE = 'input/input_21.txt'
MONKEY_ROOT = 'root'

monkey_dict = puzzle.read_monkey_file(PROBLEM_FILE)

monkey_root = puzzle.process_monkey_dict(monkey_dict, MONKEY_ROOT)

print(monkey_root.value())

print("""
Part 2
""")

monkey_root = puzzle.process_monkey_dict_2(monkey_dict, MONKEY_ROOT)

solution = monkey_root.solve()

print(f'Solution is {solution}')

















