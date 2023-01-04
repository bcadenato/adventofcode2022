import puzzles.puzzle_23 as puzzle
import pytest

SAMPLE_FILE = 'input/sample_input_23_1.txt'

def test_read_elves_1():
    
    elves, ground = puzzle.read_elves(SAMPLE_FILE)
    
    assert (2, 1) in [value[puzzle.POSITION] for value in elves.values()]
 

def test_get_spaces_1():

    position = (2, 1)

    spaces = puzzle.get_space(position, puzzle.NORTH_DIR)

    assert spaces == [(2, 0), (1, 0), (3, 0)]


def test_directions_gen_1():

    dg = puzzle.directions_gen()

    next(dg)
    directions = next(dg)

    assert directions[0] == puzzle.SOUTH_DIR

















