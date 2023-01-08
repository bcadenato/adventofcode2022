import puzzles.puzzle_25 as puzzle

FILE_INPUT = 'input/input_25.txt'

with open(FILE_INPUT) as f:
    snafu_numbers = f.read().splitlines()

decimal_numbers = [puzzle.snafu_to_decimal(snafu_number) for snafu_number in snafu_numbers]

decimal_sum = sum(decimal_numbers)

snafu_sum = puzzle.decimal_to_snafu(decimal_sum)

print(f'The sum is {snafu_sum}')
