import puzzles.puzzle_10 as puzzle

# Load data

SAMPLE_INPUT = 'input/sample_input_10.txt'

sample_commands = puzzle.read_input(SAMPLE_INPUT)

(sample_cycle, sample_X, sample_cpu_track) = puzzle.process_commands(sample_commands, 0, 1)

puzzle.calculate_signal_strength(sample_cpu_track)

sample_crt = puzzle.calculate_crt(sample_cpu_track)

for row in sample_crt:
    print(row)


print("""
Problem input
""")

PROBLEM_INPUT = 'input/input_10.txt'

problem_commands = puzzle.read_input(PROBLEM_INPUT)

(problem_cycle, problem_X, problem_cpu_track) = puzzle.process_commands(problem_commands, 0, 1)

puzzle.calculate_signal_strength(problem_cpu_track)

problem_crt = puzzle.calculate_crt(problem_cpu_track)

for row in problem_crt:
    print(row)



