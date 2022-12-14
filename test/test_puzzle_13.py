import puzzles.puzzle_13 as puzzle

def test_read_packet_1():
    assert puzzle.read_packet("[[4,4],4,4]") == list([[4,4],4,4])

def test_read_packet_2():
    assert puzzle.read_packet("[[[]]]") == list([[[]]])

def test_compare_items_ints_1():
    assert puzzle.compare_items(4, 3) == puzzle.WRONG

def test_compare_items_ints_2():
    assert puzzle.compare_items(4, 4) == puzzle.EQUAL

def test_compare_items_ints_3():
    assert puzzle.compare_items(4, 5) == puzzle.RIGHT

def test_compare_items_lists_1():
    assert puzzle.compare_items([4], [3]) == puzzle.WRONG

def test_compare_items_lists_2():
    assert puzzle.compare_items([4], [5]) == puzzle.RIGHT

def test_compare_items_lists_3():
    assert puzzle.compare_items([4, 2], [5]) == puzzle.RIGHT

def test_compare_items_lists_4():
    assert puzzle.compare_items([4], [5, 2]) == puzzle.RIGHT

def test_compare_items_list_int_1():
    assert puzzle.compare_items([4], 3) == puzzle.WRONG

def test_compare_items_list_int_2():
    assert puzzle.compare_items([4], 5) == puzzle.RIGHT

def test_compare_items_list_int_3():
    assert puzzle.compare_items([4, 5], 5) == puzzle.RIGHT

def test_compare_items_list_int_4():
    assert puzzle.compare_items(4, [5, 4]) == puzzle.RIGHT

def test_compare_items_sample_1():
    assert puzzle.compare_items([[1],[2,3,4]], [[1],4]) == puzzle.RIGHT

