import puzzles.puzzle_20 as puzzle
import logging

logging.basicConfig(level=logging.WARNING)

print("""
Part 1
""")

# First answer is 14262 - Answer is too high
# Second answer is 1644 - Answer is too low
# Final ansewr is 3700

SAMPLE_FILE = 'input/sample_input_20.txt'
PROBLEM_FILE = 'input/input_20.txt'

sequence = puzzle.read_file(PROBLEM_FILE)

logging.debug(sequence)
logging.debug(puzzle.clean_sequence(sequence))

ng = puzzle.number_generator(sequence)

for i in range(0, len(sequence)):
    
    item = next(ng)
    
    logging.debug(f'Next item is {item}')
    
    index = sequence.index(item)
    
    puzzle.mix_new(sequence, index, item)
    
    logging.debug(puzzle.clean_sequence(sequence))

# print()
# print(f'Sequence after mixing all numbers')
# print(sequence)

zero_index = puzzle.find_zero_index(sequence)
coord_1 = puzzle.get_number(sequence, zero_index, 1000)
coord_2 = puzzle.get_number(sequence, zero_index, 2000)
coord_3 = puzzle.get_number(sequence, zero_index, 3000)

print()
print(f'Sum of grove coordinates is {coord_1 + coord_2 + coord_3}')

print("""
Part 2
""")

DECRYPTION_KEY = 811589153

sequence = puzzle.read_file(PROBLEM_FILE)

sequence = [ (DECRYPTION_KEY * item[0], item[1]) for item in sequence ]

ng = puzzle.number_generator(sequence)

for i in range(0, len(sequence) * 10 ):
    
    item = next(ng)
    index = sequence.index(item)
    puzzle.mix_new(sequence, index, item)

zero_index = puzzle.find_zero_index(sequence)
coord_1 = puzzle.get_number(sequence, zero_index, 1000)
coord_2 = puzzle.get_number(sequence, zero_index, 2000)
coord_3 = puzzle.get_number(sequence, zero_index, 3000)

print()
print(f'Sum of grove coordinates is {coord_1 + coord_2 + coord_3}')

















