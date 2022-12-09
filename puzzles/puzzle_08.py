
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


def calc_score(forest, curr_tree, trees_iter):
    score = 0
    height = forest[curr_tree]['tree_height']
    
    for tree in trees_iter:
        if forest[tree]['tree_height'] < height:
            score += 1
            continue
        if forest[tree]['tree_height'] >= height:
            score += 1
            break
    
    return score


def calc_iter(curr_tree, n_rows, n_cols):
    curr_row, curr_col = curr_tree
    
    iter_right = [(curr_row, col) for col in range(curr_col + 1, n_cols)]
    iter_left = [(curr_row, col) for col in reversed(range(0, curr_col))]
    iter_down = [(row, curr_col) for row in range(curr_row + 1, n_rows)]
    iter_up = [(row, curr_col) for row in reversed(range(0, curr_row))]

    return (iter_right, iter_left, iter_down, iter_up)


def calc_score_tree(forest, curr_tree):
    iter_right, iter_left, iter_down, iter_up = calc_iter(curr_tree, forest['rows'], forest['cols'])
    
    score_right = calc_score(forest, curr_tree, iter_right)
    score_left = calc_score(forest, curr_tree, iter_left)
    score_down = calc_score(forest, curr_tree, iter_down)
    score_up = calc_score(forest, curr_tree, iter_up)
    
    tree_score = score_right * score_left * score_down * score_up
    
    return tree_score


def calc_forest_score(forest):
    n_rows = forest['rows']
    n_cols = forest['cols']
    
    for row in range(n_rows):
        for col in range(n_cols):
            curr_tree = (row, col)
            tree_score = calc_score_tree(forest, curr_tree)
            forest[curr_tree]['scenic_score'] = tree_score


def find_max_score(forest):
    max_score = -1
    max_tree = (-1, -1)
    
    n_rows = forest['rows']
    n_cols = forest['cols']
    
    for row in range(n_rows):
        for col in range(n_cols):
            curr_tree = (row, col)
            tree_score = forest[curr_tree]['scenic_score']
            if tree_score > max_score:
                max_score = tree_score
                max_tree = curr_tree
    
    return (max_tree, max_score)
