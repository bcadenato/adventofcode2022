import pytest
import puzzles.puzzle_22 as puzzle

@pytest.fixture
def sample_input():
    SAMPLE_FILE = 'input/sample_input_22.txt'
    board, instructions = puzzle.read_file(SAMPLE_FILE)
    return board, instructions

def test_opposite_1(sample_input):
    position = (9, 1)
    direction = puzzle.DIR_LEFT
    board, instructions = sample_input
    
    opposite_position = puzzle.opposite(board, position, direction)
    
    assert opposite_position == (12, 1)


def test_opposite_2(sample_input):
    position = (9, 1)
    direction = puzzle.DIR_UP
    board, instructions = sample_input
    
    opposite_position = puzzle.opposite(board, position, direction)
    
    assert opposite_position == (9, 12)

def test_move_1(sample_input):
    board, instructions = sample_input
    state = puzzle.get_starting_state(board)
    
    new_state = puzzle.move(board, state, 10)
    
    assert new_state[puzzle.POSITION] == (11, 1)


def test_move_2(sample_input):
    board, instructions = sample_input
    state = puzzle.get_state((9, 4), puzzle.DIR_RIGHT)
    
    new_state = puzzle.move(board, state, 5)
    
    assert new_state[puzzle.POSITION] == (10, 4)


def test_process_instruction_1(sample_input):
    board, instructions = sample_input
    state = puzzle.get_starting_state(board)
    
    for i in range(6):
        new_state = puzzle.process_instruction(board, state, instructions[i])
    
    validation_state = puzzle.get_state((4, 6), puzzle.DIR_DOWN)
    
    assert state == validation_state


def test_process_instruction_2(sample_input):
    board, instructions = sample_input
    state = puzzle.get_starting_state(board)
    
    for instruction in instructions:
        new_state = puzzle.process_instruction(board, state, instruction)
    
    validation_state = puzzle.get_state((8, 6), puzzle.DIR_RIGHT)
    
    assert state == validation_state


def test_sample_password(sample_input):
    board, instructions = sample_input
    state = puzzle.get_starting_state(board)
    
    for instruction in instructions:
        new_state = puzzle.process_instruction(board, state, instruction)
    
    password = puzzle.get_password(new_state)
    
    assert password == 6032

















