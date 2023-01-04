import puzzles.puzzle_17 as puzzle

tunnel = puzzle.get_new_tunnel()

puzzle.print_tunnel(tunnel, 8)

PROBLEM_FILE = 'input/input_17.txt'

with open(PROBLEM_FILE) as f:
    wind_string = f.read().splitlines()[0]

SAMPLE_STRING = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'

wind_gen = puzzle.wind_generator(wind_string)
rock_gen = puzzle.rock_generator(puzzle.ROCKS)

for i in range(0, 2022):
    rock = next(rock_gen)
    coord = puzzle.next_rock_coords(tunnel)
    
    down_move = True
    
    while down_move:
        
        wind = next(wind_gen)
        move, coord = puzzle.move_rock_wind(coord, rock, tunnel, wind)
        
        down_move, coord = puzzle.move_rock_down(coord, rock, tunnel)
    
    puzzle.set_rock(coord, rock, tunnel)


rock_height = tunnel[puzzle.STATE][puzzle.ROCK_HEIGHT]
print(f'\nFinal coord is {coord}\nFinal height is {rock_height}')

print("""
Part 2
""")

ITERATIONS = 1000000000000

tunnel = puzzle.get_new_tunnel()

wind_gen = puzzle.wind_generator_2(wind_string)
rock_gen = puzzle.rock_generator(puzzle.ROCKS)

track_sequence = []
height_sequence = []

for i in range(0, 50000):
    rock = next(rock_gen)
    coord = puzzle.next_rock_coords(tunnel)
    
    down_move = True
    
    while down_move:
        
        wind_index, wind = next(wind_gen)
        move, coord = puzzle.move_rock_wind(coord, rock, tunnel, wind)
        
        down_move, coord = puzzle.move_rock_down(coord, rock, tunnel)
    
    puzzle.set_rock(coord, rock, tunnel)

    rock_height = puzzle.get_tunnel_rock_height(tunnel)
    track = (wind_index, rock[puzzle.ID], coord[0])
    track_sequence.append(track)
    height_sequence.append(rock_height)
    
cycle_status, cycle = puzzle.detect_cycle(track_sequence)

print(f'The cycle search ended with status {cycle_status} and cycle {cycle}')

if cycle_status == puzzle.CYCLE_SUCCESS:
    index, cycle_len = cycle
    
    # Height patterns don't stabilise until a few cycles
    index = index + cycle_len * 5
    
    start_cycle_height = height_sequence[index - 1]
    cycle_height = height_sequence[index -1 + cycle_len] - height_sequence[index - 1]
    
    cycles_n, cycles_stub = divmod((ITERATIONS - index), cycle_len)
    
    stub_height = height_sequence[index - 1 + cycles_stub] - height_sequence[index - 1]
    
    total_height = start_cycle_height + cycle_height * cycles_n + stub_height
    
    print(f'Total height is {total_height}')


# First try was 1,564,705,882,325 - The answer was too low
# Second try was 1,564,705,882,328 - The answer was too high
# Thrid try was 1,564,705,882,327
 



