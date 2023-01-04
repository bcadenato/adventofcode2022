import pytest
import puzzles.puzzle_16 as puzzle


@pytest.fixture
def test_cave_1():
    cave = puzzle.read_file('input/sample_input_16.txt')
    
    return cave


def test_parse_1():
    test_str = 'Valve AA has flow rate=0; tunnels lead to valves DD, II, BB'
    
    e_valve = 'AA'
    e_rate = 0
    e_valves_to = ['DD', 'II', 'BB']
    
    assert puzzle.parse_line(test_str) == (e_valve, e_rate, e_valves_to)


def test_parse_2():
    test_str = 'Valve AA has flow rate=0; tunnels lead to valves DD'
    
    e_valve = 'AA'
    e_rate = 0
    e_valves_to = ['DD']
    
    assert puzzle.parse_line(test_str) == (e_valve, e_rate, e_valves_to)


def test_path_inferior_1():
    path_1 = puzzle.get_path_state('AA', {'AA'}, set(), 2, 0)
    path_2 = puzzle.get_path_state('AA', {'AA'}, set(), 0, 0)
    
    assert puzzle.is_path_inferior(path_1, path_2) == True


def test_calculate_pressure_1(test_cave_1):

    valves = ['BB', 'DD']
    assert puzzle.calculate_pressure(test_cave_1, valves) == 33

    














