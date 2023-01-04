import logging
import re
import copy
import math


STR_VALVE = 'Valve '
STR_FLOW = 'has flow rate='
STR_TUNNEL = '; tunnels lead to valves|; tunnel leads to valve'

def parse_line(line):
    line = line.replace(STR_VALVE, '')
    line = line.replace(STR_FLOW, '')
    line = re.sub(STR_TUNNEL, '', line)
    line = line.replace(',', '')
    
    tokens = line.split()
    
    valve = tokens.pop(0)
    rate = int(tokens.pop(0))
    valves_to = tokens
    
    return (valve, rate, valves_to)


VALVES_TO = 'valves_to'
RATE = 'rate'
HAS_RATE = 'has_rate'

def read_cave(lines):
    
    cave = {}
    
    for line in lines:
        (valve, rate, valves_to) = parse_line(line)
        
        has_rate = False
        
        if rate > 0:
            has_rate = True
        
        cave[valve] = {}
        
        cave[valve][VALVES_TO] = valves_to
        cave[valve][RATE] = rate
        cave[valve][HAS_RATE] = has_rate
    
    return cave


def read_file(file):
    
    with open(file) as f:
        lines = f.read().splitlines()
    
    cave = read_cave(lines)
    
    return cave


CURRENT_VALVE = 'current_valve'
VISITED_VALVES = 'visited_valves'
VALVES_ON = 'valves_on'
STEPS = 'steps'
PRESSURE = 'pressure'
PRESSURE_CUM = 'pressure_cum'
STATUS = 'status'

STATUS_ALIVE = 'status_alive'
STATUS_STALE = 'status_stale'


def get_path_state(valve, visited_valves, valves_on, steps, pressure, pressure_cum= 0, status=STATUS_ALIVE):
    
    path_state = {}
    
    path_state[CURRENT_VALVE] = valve
    path_state[VISITED_VALVES] = visited_valves
    path_state[VALVES_ON] = valves_on
    path_state[STEPS] = steps
    path_state[PRESSURE] = pressure
    path_state[PRESSURE_CUM] = pressure_cum
    path_state[STATUS] = status
    
    return path_state


def get_path_start(valve):
    
    path = {}
    
    path[PATH_TRACK] = [(ACTION_START, valve, 0)]
    path[PATH_STATE] = get_path_state(valve, {valve}, set(), 0, 0)
    
    return path


def potential_path_pressure(cave, path_state, time=30):
    
    steps = path_state[STEPS]
    pressure = calculate_pressure(cave, path_state[VALVES_ON])
    pressure_cum = path_state[PRESSURE_CUM]
    
    potential_pressure = pressure_cum + (time - steps) * pressure
    
    return potential_pressure


def max_pressure_on_valve(track, valve_ref):
    pressure = max([pressure for (_, valve, pressure) in track if valve == valve_ref])
    
    return pressure


def last_pressure(track):
    pressure = track[-1][2]
    
    return pressure


PATH_TRACK = 'track'
PATH_STATE = 'state'

ACTION_MOVE = 'move'
ACTION_OPEN = 'open'
ACTION_WAIT = 'wait'
ACTION_START = 'start'

def get_actions(cave, path):
    
    if path[PATH_STATE][STATUS] == STATUS_STALE:
        return None
    
    current_valve = path[PATH_STATE][CURRENT_VALVE]
    
    actions = []
    
    if cave[current_valve][HAS_RATE] and not current_valve in path[PATH_STATE][VALVES_ON]:
        actions.append( (ACTION_OPEN, current_valve) )
    
    for valve in cave[current_valve][VALVES_TO]:
        actions.append( (ACTION_MOVE, valve) )
    
    return actions


# def get_action_queue():
#     action_queue = []
#     
#     return action_queue


def calculate_pressure(cave, valves):
    
    pressure = 0
    
    for valve in valves:
        pressure += cave[valve][RATE]
    
    return pressure


# Path Uitlities

def get_path_with_action(cave, path, action):
    
    tmp_path = copy.deepcopy(path)
    
    add_action_to_path(cave, tmp_path, action)
    
    return tmp_path


def evolve_path(cave, path_set, path, actions):
    
    if path[PATH_STATE][STATUS] == STATUS_STALE:
        current_valve = path[PATH_STATE][CURRENT_VALVE]
        add_action_to_path(cave, path, (ACTION_WAIT, current_valve))
        
        path_set.remove(path)
        path_set.append(path)
        
        return
    
    new_paths = []
    
    for action in actions:
        new_path = get_path_with_action(cave, path, action)
        new_paths.append(new_path)
    
    if len(new_paths) == 0:
        path[PATH_STATE][STATUS] = STATUS_STALE
        return
    
    final_paths = []
    
    for new_path in new_paths:
        
        if not is_path_acceptable(cave, path_set, new_path):
            continue
        
        final_paths.append(new_path)
    
    if len(final_paths) == 0 and all_valves_on(cave, path):
            path[PATH_STATE][STATUS] = STATUS_STALE
            return
    
    path_set.remove(path)
    path_set.extend(final_paths)
        
    return


def is_path_acceptable(cave, path_set, path):
    
    for path_ref in path_set:
        if is_path_inferior(cave, path, path_ref):
            return False
    
    return True


def path_set_str(path_set):
    
    path_str = ''
    
    for path in path_set:
        path_str += str(path) + '\n'
    
    return path_str


def all_valves_on(cave, path):
    active_valves = {key for key, value in cave.items() if value[HAS_RATE]}
    
    path_valves = path[PATH_STATE][VALVES_ON]
    
    if (active_valves - path_valves) == set():
        return True
    
    return False


def calculate_pressure_on_path(path):
    
    track = path[PATH_TRACK]
    
    total_pressure = sum([pressure for (_, _, pressure) in track])
    
    return total_pressure


def count_paths_alive(path_set, max_steps):
    n_paths = sum([1 for path in path_set if path[PATH_STATE][STATUS] == STATUS_ALIVE or path[PATH_STATE][STEPS] < max_steps])
    
    return n_paths


def set_path_stale(path):
    path[PATH_STATE][STATUS] = STATUS_STALE


def matches_path_track(path, track_ref):
    
    path_track = path[PATH_TRACK]
    track_ref_len = len(track_ref)
    path_len = len(path_track)
    
    explore_len = min(track_ref_len, path_len)
    
    for i in range(0, explore_len):
        action_ref, valve_ref = track_ref[i]
        action, valve, _ = path_track[i]
        
        if action_ref != action or valve_ref != valve:
            return False
    
    return True


# Functions to modify a path

def is_path_inferior(cave, path, path_ref):
    
    state = path[PATH_STATE]
    state_ref = path_ref[PATH_STATE]
    
    # The two paths are comparable because the same number of valves are on
    
    if not state[VALVES_ON] == state_ref[VALVES_ON]:
        return False
    
    # The new path should have at least a new valve visited
    
    if not (state[VISITED_VALVES] - state_ref[VISITED_VALVES]) == set():
        return False
    
    if (state[STEPS] <= state_ref[STEPS]) and (state[PRESSURE_CUM] > state_ref[PRESSURE_CUM]):
        return False
    
    # condition = matches_path_track(path, SAMPLE_SOLUTION)
    
    if (state[STEPS] <= state_ref[STEPS]) and (state[PRESSURE] > state_ref[PRESSURE]):
        return False
    
    if (state[VALVES_ON] == state_ref[VALVES_ON]) and (state[VISITED_VALVES] == state_ref[VISITED_VALVES] and state_ref[STATUS] == STATUS_ALIVE):
        # if condition:
        #     pass

        return True

    # If everything is equal in number of active valves and visited valves
    # then the decision comes to number of steps and accumulated pressure
    
    if potential_path_pressure(cave, state) < potential_path_pressure(cave, state_ref):
        # if condition:
        #     pass
        
        return True
    
    return False


def add_action_to_path(cave, path, action):
    
    action_item, new_valve = action
    
    state = path[PATH_STATE]
    
    state[STEPS] += 1
    state[PRESSURE] = calculate_pressure(cave, state[VALVES_ON])
    state[PRESSURE_CUM] += state[PRESSURE]
    
    if action_item == ACTION_MOVE:
        state[CURRENT_VALVE] = new_valve
        state[VISITED_VALVES].add(new_valve)
    
    if action_item == ACTION_OPEN:
        state[VALVES_ON].add(new_valve)
        state[VISITED_VALVES] = {new_valve}
    
    if action_item == ACTION_WAIT:
        pass
    
    # Update Track
    
    track_item = (action_item, new_valve, state[PRESSURE])
    
    path[PATH_TRACK].append(track_item)
    

# SAMPLE_SOLUTION = [('start', 'AA'),
#     ('move', 'DD'),
#     ('open', 'DD'),
#     ('move', 'CC'),
#     ('move', 'BB'),
#     ('open', 'BB'),
#     ('move', 'AA'),
#     ('move', 'II'),
#     ('move', 'JJ'),
#     ('open', 'JJ'),
#     ('move', 'II'),
#     ('move', 'AA'),
#     ('move', 'DD'),
#     ('move', 'EE'),
#     ('move', 'FF'),
#     ('move', 'GG'),
#     ('move', 'HH'),
#     ('open', 'HH'),
#     ('move', 'GG'),
#     ('move', 'FF'),
#     ('move', 'EE'),
#     ('open', 'EE'),
#     ('move', 'DD'),
#     ('move', 'CC'),
#     ('open', 'CC')]

####

# Second strategy

"""
A second strategy to analyse the problem could be:
    1. Calculate walking distances between every active valve (Dijkstra)
    2. Analyse all potential combinations to activate valves
"""

def get_distance_dict(cave, valves):
    """
    Returns a dictionary where each key is a tuple with two valves, and its value is the distance
    """
   
   
   
    

def calculate_distance(cave, valve_a, valve_b):
    
    dists = {valve: (math.inf, False) for valve in cave}
    dists[valve_a] = (0, False)
    
    current_valve = valve_a
    
    while True:
        current_dist = dists[current_valve]
        
        for valve in cave[current_valve][VALVES_TO]:
            valve_dist = current_dist + 1
            if valve_dist < dists[valve]:
                dists[valve] = valve_dist
            
        sorted_dists = sorted(dists.items(), key=lambda x: x[1])
        current_valve = sorted_dists.keys()[0]
        
        
        
    














