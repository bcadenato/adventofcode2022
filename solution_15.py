from itertools import accumulate
import logging
import puzzles.puzzle_15 as puzzle

logging.basicConfig(level=logging.WARNING)

print("""
Part 1
""")

print("""
Sample solution
""")

SAMPLE_FILE = 'input/sample_input_15.txt'

sample_devices = puzzle.read_file(SAMPLE_FILE)

print(sample_devices)

SAMPLE_ROW = 10

range_list =  puzzle.get_range_list(sample_devices, SAMPLE_ROW)

print()
print(range_list)

merge_range = list(accumulate(range_list, puzzle.merge_range))

print()
print(merge_range[-1])

r_len = puzzle.range_len(merge_range[-1])

beacons_row = puzzle.get_beacons_in_row(sample_devices, SAMPLE_ROW)

n_beacons = len(beacons_row)

sample_solution = r_len - n_beacons

print()
print(f'Solution to sample problem is {sample_solution} positions')

print("""
Problem solution
""")

PROBLEM_FILE = 'input/input_15.txt'

problem_devices = puzzle.read_file(PROBLEM_FILE)

PROBLEM_ROW = 2000000

range_list =  puzzle.get_range_list(problem_devices, PROBLEM_ROW)

print()
print(range_list)

merge_range = list(accumulate(range_list, puzzle.merge_range))

print()
print(merge_range[-1])

r_len = puzzle.range_len(merge_range[-1])

beacons_row = puzzle.get_beacons_in_row(problem_devices, PROBLEM_ROW)
sensors_row = puzzle.get_sensors_in_row(problem_devices, PROBLEM_ROW)

n_beacons = len(beacons_row)
n_sensors = len(sensors_row)

print()
print(f'There are {n_beacons} beacons in row {PROBLEM_ROW}')
print(f'There are {n_sensors} sensors in row {PROBLEM_ROW}')
print(beacons_row)

sample_solution = r_len - n_beacons

print()
print(f'Solution to sample problem is {sample_solution} positions')

print("""
Part 2
""")

print("""
Sample solution
""")

logging.basicConfig(level=logging.DEBUG)

for row in range(0, 21):
    try:
        range_covered = puzzle.get_coverage(sample_devices, row)
    except Exception as exception:
        print(f'Row is {row}')
        print(exception)


print("""
Sample solution
""")

for row in range(0, 4000000):
    try:
        range_covered = puzzle.get_coverage(problem_devices, row)
    except Exception as exception:
        print(f'Row is {row}')
        print(exception)


















