def read_move(line):
    direction, step = line.split()
    step = int(step)
    return (direction, step)


def process_moves(grid, H_pos, T_pos, move):
    direction, steps = move
    
    for i in range(steps):
        (H_pos, T_pos) = process_move(grid, H_pos, T_pos, direction)
    
    return (H_pos, T_pos)


def process_moves_chain(grid, chain, move):
    direction, steps = move
    
    for i in range(steps):
        chain = process_move_chain(grid, chain, direction)
    
    return chain


def process_move(grid, H_pos, T_pos, direction):
    
#    print(f'H_pos = {H_pos} T_pos = {T_pos} Dir = {direction} ', end = '')
    
    H_row, H_col = H_pos
    T_row, T_col = T_pos
    
    (H_row, H_col) = move_knot(H_pos, direction)
    (T_row, T_col) = process_move_T((H_row, H_col), (T_row, T_col))
    
    grid[(T_row, T_col)] = True
    
#    print(f'H_pos = {(H_row, H_col)} T_pos = {(T_row, T_col)}')
    
    return ((H_row, H_col), (T_row, T_col))


def move_knot(K_pos, direction):
    
    K_row, K_col = K_pos
    
    if direction == 'R':
        K_col += 1
    elif direction == 'L':
        K_col -= 1
    elif direction == 'D':
        K_row -= 1
    elif direction == 'U':
        K_row += 1
    
    return (K_row, K_col)
    

def process_move_chain(grid, chain, direction):
    chain[0] = move_knot(chain[0], direction)
    
    for i in range(1, len(chain)):
        chain[i] = process_move_T(chain[i-1], chain[i])
    
    grid[chain[-1]] = True
    
    return chain
    

def process_move_T(H_pos, T_pos):
    H_row, H_col = H_pos
    T_row, T_col = T_pos
    row_diff = H_row - T_row
    col_diff = H_col - T_col
    
    if abs(row_diff) <= 1 and abs(col_diff) <= 1:
        return T_pos
    
    if row_diff == 0 and abs(col_diff) == 2:
        T_col += col_diff // 2
        return (T_row, T_col)
    elif col_diff == 0 and abs(row_diff) == 2:
        T_row += row_diff // 2
        return (T_row, T_col)
    
    if abs(row_diff) == 1 and abs(col_diff) == 2:
        T_row += row_diff
        T_col += col_diff // 2
        return (T_row, T_col)
    elif abs(row_diff) == 2 and abs(col_diff) == 1:
        T_row += row_diff // 2
        T_col += col_diff
        return (T_row, T_col)
    
    if abs(row_diff) == 2 and abs(col_diff) == 2:
        T_row += row_diff // 2
        T_col += col_diff // 2
        return (T_row, T_col)
    
    print(f'process_move_T didn\'t finish')
    print(f'H_pos {H_pos} T_pos {T_pos}')
    

def count_T_positions(grid):
    items = grid.items()
    return len(items)


def paint_grid(grid):
    keys = grid.keys()
    min_row, max_row = 0, 0
    min_col, max_col = 0, 0
    
    for key in keys:
        row, col = key
        
        if row < min_row: 
            min_row = row
        elif row > max_row:
            max_row = row
        
        if col < min_col:
            min_col = col
        elif col > max_col:
            max_col = col
    
    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            if (row, col) in grid:
                print('#', end = '')
            else:
                print('.', end = '')
        
        print('')

        

    
    
