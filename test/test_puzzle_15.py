import puzzles.puzzle_15 as puzzle


def test_read_line_1():
    line = 'Sensor at x=2, y=18: closest beacon is at x=-2, y=15'
    
    s_x = 2
    s_y = 18
    b_x = -2
    b_y = 15
    
    assert puzzle.read_line(line) == ( (s_x, s_y), (b_x, b_y) )


def test_calc_distance_1():
    p_a = (0, 0)
    p_b = (-5, -2)
    
    assert puzzle.calc_distance(p_a, p_b) == 7
