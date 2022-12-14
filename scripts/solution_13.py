import puzzles.puzzle_13 as puzzle
import functools

print("""First part
""")

print("""
Sample test
""")

SAMPLE_FILE = 'input/sample_input_13.txt'

sample_packets = puzzle.read_file(SAMPLE_FILE)

sample_indices = []

for i, packet in enumerate(sample_packets):
    right_order = puzzle.compare_packets(packet[0], packet[1])
    
    if right_order:
        sample_indices.append(i + 1)

sample_indices_sum = sum(sample_indices)

puzzle.compare_items([[1],[2,3,4]], [[1],4])

print(sample_indices)

print(f'The sum of indices is {sample_indices_sum}')

print("""
Problem
""")

PROBLEM_FILE = 'input/input_13.txt'

problem_packets = puzzle.read_file(PROBLEM_FILE)

problem_indices = []

for i, packet in enumerate(problem_packets):
    right_order = puzzle.compare_packets(packet[0], packet[1])
    
    if right_order:
        problem_indices.append(i + 1)

problem_indices_sum = sum(problem_indices)

print(problem_indices)

print(f'The sum of indices is {problem_indices_sum}')

print("""
Second part
""")

distress_1 = [[2]]
distress_2 = [[6]]

sample_packets = puzzle.read_file_2(SAMPLE_FILE)

sample_packets.extend([distress_1, distress_2])

sample_packets_sorted = sorted(sample_packets, key=functools.cmp_to_key(puzzle.compare_items), reverse=True)

sample_distress_1_index = sample_packets_sorted.index(distress_1) + 1
sample_distress_2_index = sample_packets_sorted.index(distress_2) + 1

print(f'Sample decoder key is {sample_distress_1_index * sample_distress_2_index}')

problem_packets = puzzle.read_file_2(PROBLEM_FILE)

problem_packets.extend([distress_1, distress_2])

problem_packets_sorted = sorted(problem_packets, key=functools.cmp_to_key(puzzle.compare_items), reverse=True)

problem_distress_1_index = problem_packets_sorted.index(distress_1) + 1
problem_distress_2_index = problem_packets_sorted.index(distress_2) + 1

print(f'Problem decoder key is {problem_distress_1_index * problem_distress_2_index}')

