import pytest
import puzzles.puzzle_14 as puzzle

@pytest.fixture
def sample_cave_1():
    return dict([((498, 4), '#'),
                 ((498, 5), '#'),
                 ((498, 6), '#')])

def test_add_wall_1(sample_cave_1):
    cave = {}
    start = (498, 4)
    end = (498, 6)
    
    assert puzzle.add_wall(cave, start, end) == sample_cave_1


def test_add_wall_2():
    cave_exp = dict([((496, 4), '#'),
                     ((497, 4), '#'),
                     ((498, 4), '#')])
    
    cave = {}
    start = (496, 4)
    end = (498, 4)
    
    assert puzzle.add_wall(cave, start, end) == cave_exp


def test_add_wall_3(sample_cave_1):
    cave = {}
    start = (498, 6)
    end = (498, 4)
    
    assert puzzle.add_wall(cave, start, end) == sample_cave_1


def test_get_cave_dims_1(sample_cave_1):
    assert puzzle.get_dims(sample_cave_1) == (498, 4, 498, 6)
    
