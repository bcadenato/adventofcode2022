def map_forest(forest_raw):
    forest = {}
    
    tree_rows = forest_raw.splitlines()
    
    for row, tree_row in enumerate(tree_rows):
        tree_cols = len(tree_row)
        
        for col, tree_col in enumerate(tree_row):
            forest[(row, col)] = {'tree_height': int(tree_row[col]),
                                  'visible': False}
    
    forest['rows'] = len(tree_rows)
    forest['cols'] = len(tree_row)
    
    return forest

def visible_left(forest):
    for row in range(0, forest['rows']):
        max_h = -1
        
        for col in range(0, forest['cols']):
            if forest[(row, col)]['tree_height'] > max_h:
                forest[(row, col)]['visible'] = True
                max_h = forest[(row, col)]['tree_height']


def visible_right(forest):
    for row in range(0, forest['rows']):
        max_h = -1
        
        for col in reversed(range(0, forest['cols'])):
            if forest[(row, col)]['tree_height'] > max_h:
                forest[(row, col)]['visible'] = True
                max_h = forest[(row, col)]['tree_height']


def visible_top(forest):
    for col in range(0, forest['cols']):
        max_h = -1
        
        for row in range(0, forest['rows']):
            if forest[(row, col)]['tree_height'] > max_h:
                forest[(row, col)]['visible'] = True
                max_h = forest[(row, col)]['tree_height']


def visible_bottom(forest):
    for col in range(0, forest['cols']):
        max_h = -1
        
        for row in reversed(range(0, forest['rows'])):
            if forest[(row, col)]['tree_height'] > max_h:
                forest[(row, col)]['visible'] = True
                max_h = forest[(row, col)]['tree_height']


def count_visible(forest):
    visible_left(forest)
    visible_right(forest)
    visible_top(forest)
    visible_bottom(forest)
    
    visible_n = 0
    
    for row in range(0, forest['rows']):
        for col in range(0, forest['cols']):
            if forest[(row, col)]['visible']:
                visible_n += 1
    
    return visible_n


# Solve Test

TEST_FOREST_RAW = """30373
25512
65332
33549
35390"""

test_forest = map_forest(TEST_FOREST_RAW)

print(f'Visible trees in sample is {count_visible(test_forest)}')

# Solve Puzzle

FILE_INPUT = "puzzles/input_08.txt"

with open(FILE_INPUT) as f:
    forest_raw = f.read()

forest = map_forest(forest_raw)

print(f'Visible trees in problem is {count_visible(forest)}')


        
        
        
        
        
