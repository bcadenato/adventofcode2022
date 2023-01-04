import puzzles.puzzle_23 as puzzle
import pprint

print("""
Part 1
""")

SAMPLE_FILE = 'input/sample_input_23_2.txt'

elves = puzzle.read_elves(SAMPLE_FILE)

dg = puzzle.directions_gen()

for round in range(10):
    directions = next(dg)
    elves, target = puzzle.calculate_next_position(elves, directions)

    # print(f'\nBeginning of round {round}:')
    # pprint.pprint(elves)
    # pprint.pprint(target)

    elves, target = puzzle.process_positions(elves, target)

    # print(f'\nEnd of round {round}:')
    # pprint.pprint(elves)
    # pprint.pprint(target)

min_x, min_y, max_x, max_y = puzzle.calculate_minimum_rectangle(elves)

ground = puzzle.calculate_covered_ground(elves, min_x, min_y, max_x, max_y)

print(f'\nCovered ground is {ground}')

print("""
Part 2
""")

SAMPLE_FILE = 'input/input_23.txt'

elves = puzzle.read_elves(SAMPLE_FILE)

dg = puzzle.directions_gen()

round = 0

while True:
    round += 1
    print(f'Starting round {round}')
    
    directions = next(dg)
    elves, target = puzzle.calculate_next_position(elves, directions)

    # print(f'\nBeginning of round {round}:')
    # pprint.pprint(elves)
    # pprint.pprint(target)

    elf_moves = [elf[puzzle.POSITION] == elf[puzzle.TARGET_POSITION] for elf in elves.values()]
    if all(elf_moves):
        break

    elves, target = puzzle.process_positions(elves, target)

    # print(f'\nEnd of round {round}:')
    # pprint.pprint(elves)
    # pprint.pprint(target)

print(f'\nThe number of rounds is {round}')
