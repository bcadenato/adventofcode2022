import itertools

def read_file(file):
    
    with open(file) as f:
        lines = f.read().splitlines()
    
    cubes = read_cubes(lines)
    
    return cubes

VOID = 0
LAVA = 1
VOID_INSIDE = 2
VOID_OUTSIDE = 3

def read_cubes(lines):
    
    cubes = {}
    
    for line in lines:
        cube = read_cube(line)
        cubes[cube] = LAVA
    
    return cubes


def read_cube(line):
    
    coords_str = line.split(sep=',')
    cube = (int(coords_str[0]), int(coords_str[1]), int(coords_str[2]))
    
    return cube

# Find adjacent cubes

def get_side_cubes(cube):
    
    x, y, z = cube
    
    cubes = [(x + 1, y, z),
             (x - 1, y, z),
             (x, y + 1, z),
             (x, y - 1, z),
             (x, y, z + 1),
             (x, y, z - 1)]
    
    return cubes


def is_cube_covered(cubes, cube):
    
    side_cubes = get_side_cubes(cube)
    
    side_cubes_exist = [side_cube in cubes for side_cube in side_cubes]
    
    return all(side_cubes_exist)


def count_exposed_sides(cubes, cube):
    
    side_cubes = get_side_cubes(cube)
    
    exposed_sides = 0
    
    for cube in side_cubes:
        if not cube in cubes:
            exposed_sides += 1
    
    return exposed_sides


# Work with a full space

def get_space_dimensions(cubes):
    
    x_max = max(cubes, key=lambda x: x[0])[0]
    x_min = min(cubes, key=lambda x: x[0])[0]
    
    y_max = max(cubes, key=lambda x: x[1])[1]
    y_min = min(cubes, key=lambda x: x[1])[1]
    
    z_max = max(cubes, key=lambda x: x[2])[2]
    z_min = min(cubes, key=lambda x: x[2])[2]
    
    return (x_min, y_min, z_min), (x_max, y_max, z_max)

def get_cube_space(cubes):
    
    p_min, p_max = get_space_dimensions(cubes)
    
    x_min, y_min, z_min = p_min
    x_max, y_max, z_max = p_max
    
    for p in itertools.product(range(x_min, x_max + 1),  range(y_min, y_max + 1),  range(z_min, z_max + 1)):
        
        if not p in cubes:
            
            cubes[p] = VOID
    
    return cubes


def classify_void(cubes):
    
    p_min, p_max = get_space_dimensions(cubes)
    
    x_min, y_min, z_min = p_min
    x_max, y_max, z_max = p_max
    
    void_cubes = [cube for cube in cubes if cubes[cube] == VOID and any([cube[0] == x_min,
                                                                         cube[0] == x_max,
                                                                         cube[1] == y_min,
                                                                         cube[1] == y_max,
                                                                         cube[2] == z_min,
                                                                         cube[2] == z_max])]
    
    while void_cubes:
        
        cube = void_cubes.pop(0)
        
        side_cubes = get_side_cubes(cube)
        
        for side_cube in side_cubes:
            
            if not side_cube in cubes:
                cubes[cube] = VOID_OUTSIDE
                continue
            
            if cubes[side_cube] == VOID_OUTSIDE:
                cubes[cube] = VOID_OUTSIDE
                continue
            
            if cubes[side_cube] == VOID:
                void_cubes.append(side_cube)
            
        if cubes[cube] == VOID:
            void_cubes.append(cube)
    
    void_cubes = [cube for cube in cubes if cubes[cube] == VOID]
    
    for cube in void_cubes:
        
        cubes[cube] = VOID_INSIDE
    
    return cubes

def get_cubes_inside(cubes):
    
    cubes_inside = [cube for cube in cubes if cubes[cube] == VOID_INSIDE]
    
    return cubes_inside


def get_cubes_lava(cubes):
    
    cubes_lava = [cube for cube in cubes if cubes[cube] == LAVA]
    
    return cubes_lava


def count_exposed_sides_2(cubes, cube):
    
    side_cubes = get_side_cubes(cube)
    
    exposed_sides = 0
    
    for cube in side_cubes:
        if not cube in cubes or cubes[cube] == VOID_OUTSIDE:
            exposed_sides += 1
    
    return exposed_sides


























