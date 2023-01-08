import puzzles.puzzle_25 as puzzle

def test_snafu_to_decimal_1():

    snafu = '1-'

    decimal_value = puzzle.snafu_to_decimal(snafu)

    assert decimal_value == 4


def test_decimal_to_snafu_1():

    decimal = 2022

    snafu = puzzle.decimal_to_snafu(decimal)

    assert snafu == '1=11-2'