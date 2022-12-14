import math

def read_map(lines):
    map = {}
    
    map['nodes'] = {}
    
    map['rows'] = len(lines)
    map['cols'] = len(lines[0])
    
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            
            map['nodes'][(i, j)] = {}
            map['nodes'][(i, j)]['visited'] = False
            map['nodes'][(i, j)]['predecessor'] = None
            
            if char == 'S':
                map['nodes'][(i, j)]['value'] = 'a'
                map['nodes'][(i, j)]['cost'] = math.inf
                map['start'] = (i, j)
                continue
            
            if char == 'E':
                map['nodes'][(i, j)]['value'] = 'z'
                map['nodes'][(i, j)]['cost'] = math.inf
                map['end'] = (i, j)
                continue
            
            map['nodes'][(i, j)]['value'] = char
            map['nodes'][(i, j)]['cost'] = math.inf
        
    return map


def get_value(map, node):
    value = map['nodes'][node]['value']
    
    return value


def get_neighbours(map, node_base, edge_function):
    """ A node is a neighbour if:
            - It can be reached through up, down, left, right
            - It's only one letter away
    """
    
    node_nb = []
    
    node_u = (node_base[0] - 1, node_base[1])
    node_d = (node_base[0] + 1, node_base[1])
    node_l = (node_base[0], node_base[1] - 1)
    node_r = (node_base[0], node_base[1] + 1)
    
    node_cand = [node_u, node_d, node_l, node_r]
    
    for node in node_cand:
        if is_neighbour(map, node, node_base, edge_function):
            node_nb.append(node)
    
    return node_nb


def is_edge(value_from, value_to):
    level_from = ord(value_from)
    level_to = ord(value_to)
    
    edge = level_to <= level_from + 1
    
    return edge


def is_edge_down(value_from, value_to):
    return is_edge(value_to, value_from)


def is_neighbour(map, node_to, node_from, edge_function):
    if node_to not in map['nodes']:
        return False
    
    node_to_value = get_value(map, node_to)
    node_from_value = get_value(map, node_from)
    
    return edge_function(node_from_value, node_to_value)


def calc_cost(map, node_from, node_to, cost_function = (lambda x: 1)):
    
    node_from_lvl = get_value(map, node_from)
    node_to_lvl = get_value(map, node_to)
    
    node_from_ord = ord(node_from_lvl)
    node_to_ord = ord(node_to_lvl)
    
    cost = cost_function(node_to_ord - node_from_ord)
    
    return cost


def create_unvisited(map):
    
    unvisited = set(map['nodes'].keys())
    
    return unvisited


def create_node_dist(map):
    
    nodes = list(map['nodes'].keys())
    
    node_dist = {}
    
    for node in nodes:
        node_dist[node] = None
    
    node_dist[map['start']] = 0
    
    return node_dist

    
def get_next_node(map):
    nodes = list(map['nodes'].items())
    nodes = list(filter(lambda x: not x[1]['visited'], nodes))
    nodes = list(filter(lambda x: x[1]['cost'] != math.inf, nodes))
    nodes = list(sorted(nodes, key=lambda x: x[1]['cost']))
    
    if len(nodes) > 0:
        return nodes[0][0]
    else:
        return None


def get_cost(map, node):
    cost = map['nodes'][node]['cost']
    
    return cost


def set_cost(map, node, cost):
    map['nodes'][node]['cost'] = cost


def set_predecessor(map, node, node_from):
    map['nodes'][node]['predecessor'] = node_from


def update_node_dist(map, node_from, node_to, cost):
    node_from_cost = get_cost(map, node_from)
    new_node_to_cost = node_from_cost + cost
    old_node_to_cost = get_cost(map, node_to)
    
    if old_node_to_cost > new_node_to_cost:
        set_cost(map, node_to, new_node_to_cost)
        set_predecessor(map, node_to, node_from)
        # print(f'{new_node_to_cost:3} to get to {node_to}')


def set_visited(map, node):
    map['nodes'][node]['visited'] = True


def is_visited(map, node):
    visited = map['nodes'][node]['visited']
    
    return visited


def find_path(map, start_node, end_node = None, edge_function = is_edge):
    set_cost(map, start_node, 0)
    
    end_visited = False
    
    while not end_visited:
        current_node = get_next_node(map)
        
        if current_node is None:
            break
        
        sample_nb = get_neighbours(map, current_node, edge_function)
        
        for node in sample_nb:
            cost = calc_cost(map, current_node, node)
            update_node_dist(map, current_node, node, cost)
            
        set_visited(map, current_node)
        
        # current_node = get_next_node(map)
        
        # print(f'{current_node} {map["nodes"][map["end"]]["cost"]}')
        
        if not end_node is None:
            end_visited = is_visited(map, end_node)


# IDEAS
# Print a map of covered steps to understand where it gets stuck

def print_map(map):
    
    c_visited = ord('a') - ord('A')
    
    print_str = []
    
    for row in range(map['rows']):
        print_str.append('')
        
        for col in range(map['cols']):
            node = (row, col)
            
            node_visited = is_visited(map, node)
            
            node_value = get_value(map, node)
            
            if not node_visited:
                node_str = node_value
            else:
                node_ord = ord(node_value) - c_visited
                node_chr = chr(node_ord)
                node_str = str(node_chr)
            
            print_str[row] += node_str
    
    return print_str


















