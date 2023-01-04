import puzzles.puzzle_17 as puzzle
import pytest

@pytest.fixture
def tunnel_empty():
    tunnel = puzzle.get_new_tunnel()
    
    return tunnel


def test_right_move_1(tunnel_empty):
    
    start_coord = (3, 4)
    
    rock = puzzle.ROCK_1
    
    right_move, right_coord = puzzle.move_rock_right(start_coord, rock, tunnel_empty)
    
    assert (right_move, right_coord) == (True, (4, 4))
    
    
def test_right_move_2(tunnel_empty):
    
    start_coord = (4, 4)
    
    rock = puzzle.ROCK_1
    
    right_move, right_coord = puzzle.move_rock_right(start_coord, rock, tunnel_empty)
    
    assert (right_move, right_coord) == (False, (4, 4))
    

def test_down_move_1(tunnel_empty):
    
    start_coord = (3, 2)
    
    rock = puzzle.ROCK_5
    
    down_move, down_coord = puzzle.move_rock_down(start_coord, rock, tunnel_empty)
    
    assert (down_move, down_coord) == (True, (3, 1)) 

def test_down_move_2(tunnel_empty):
    
    start_coord = (3, 1)
    
    rock = puzzle.ROCK_5
    
    down_move, down_coord = puzzle.move_rock_down(start_coord, rock, tunnel_empty)
    
    assert (down_move, down_coord) == (False, (3, 1))


def test_wind_move_1(tunnel_empty):
    
    start_coord = (3, 4)
    
    rock = puzzle.ROCK_1
    
    move, coord = puzzle.move_rock_wind(start_coord, rock, tunnel_empty, '>')
    
    assert (move, coord) == (True, (4, 4))


def test_wind_move_2(tunnel_empty):
    
    start_coord = (3, 4)
    
    rock = puzzle.ROCK_1
    
    move, coord = puzzle.move_rock_wind(start_coord, rock, tunnel_empty, '<')
    
    assert (move, coord) == (True, (2, 4))

# Cycle detect

@pytest.fixture
def cycle_str():
    return '01234235235235235'

def test_cycle_detect_1(cycle_str):
    
    status, item = puzzle.detect_cycle(cycle_str)
    
    assert status, item == (puzzle.CYCLE_SUCCESS, (5, 3))


















