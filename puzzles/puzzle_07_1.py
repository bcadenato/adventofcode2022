import re

def parse(line):
    tokens = line.split()
    return tokens


def calc_size(tree):
    size = 0
    
    for leaf in tree.keys():
        if isinstance(tree[leaf], dict):
            if leaf in ['..']:
                continue
            size += calc_size(tree[leaf])
        elif leaf == '.':
            continue
        else:
            size += tree[leaf]
    
    return size


def path_to_dir(leaf):
    if '..' in leaf.keys():
        return path_to_dir(leaf['..']) + '/' + leaf['.']
    return ''


def get_dirs(tree):
    dir_dict = {}
    
    for leaf in tree.keys():
        if isinstance(tree[leaf], dict):
            if leaf in ['..']:
                continue
            
            leaf_path = path_to_dir(tree[leaf])
            
            leaf_size = calc_size(tree[leaf])
            dir_dict[leaf_path] = leaf_size
            
            leaf_dict = get_dirs(tree[leaf])
            dir_dict.update(leaf_dict)
    
    return dir_dict

def process_lines(lines):
    tree = dict([('.', '/')])
    current_leaf = tree
    
    for i, line in enumerate(lines):
        tokens = parse(line)
        
        if tokens[0] == '$':
            if tokens[1] == 'cd':
                if tokens[2] == '/':
                    current_leaf = tree
                elif tokens[2] == '..':
                    current_leaf = current_leaf['..']
                else:
                    current_leaf = current_leaf[tokens[2]]
                continue
        
            if tokens[1] == 'ls':
                continue
        
        if tokens[0] == 'dir':
            current_leaf[tokens[1]] = {}
            current_leaf[tokens[1]]['..'] = current_leaf
            current_leaf[tokens[1]]['.'] = tokens[1]
            continue
        
        current_leaf[tokens[1]] = int(tokens[0])
    
    return tree


def print_tree(tree, level = 0):
    for leaf in tree.keys():
        if isinstance(tree[leaf], dict):
            if leaf in ['..']:
                continue
            
            print(f'{"  " * level}- {leaf} (dir, size={calc_size(tree[leaf])})')
            print_tree(tree[leaf], level + 1)
        elif leaf == '.':
            continue
        else:
            print(f'{"  " * level}- {leaf} (file, size={tree[leaf]})')


SIZE_LIMIT = 100000

# Test example

TEST_INPUT = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

test_tree = process_lines(TEST_INPUT.splitlines())

test_dirs = get_dirs(test_tree)

test_solution = sum([test_dirs[key]
    for key in test_dirs.keys()
    if test_dirs[key] <= SIZE_LIMIT])

print(f"The test solution is {test_solution}")

print_tree(test_tree)

print(f'\n')

# Solve the problem

FILE_INPUT = "puzzles/input_07.txt"

with open(FILE_INPUT) as f:
    lines = f.read().splitlines()

tree = process_lines(lines)

tree_dirs = get_dirs(tree)

solution = sum([tree_dirs[dir]
    for dir in tree_dirs.keys()
    if tree_dirs[dir] <= SIZE_LIMIT])

print(f'The solution is {solution}')

for dir in tree_dirs.keys():
    print(f'size {tree_dirs[dir]:12} dir {dir}')
