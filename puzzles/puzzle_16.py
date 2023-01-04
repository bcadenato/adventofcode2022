import logging
import re
import math
import itertools


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


# Cave utilities

def get_active_valves(cave):
    active_valves = {valve for valve in cave if cave[valve][HAS_RATE]}
    
    return active_valves


# Calculate path distances

def get_distance(cave, valves):
    """
    Returns a dictionary where each key is a tuple with two valves, and its value is the distance
    """
    pass
    
    distances = {}
    
    valves_pairs = itertools.permutations(valves, 2)
    
    for pair in valves_pairs:
        pair_distance = calculate_distance(cave, pair[0], pair[1])
        distances[pair] = pair_distance
    
    return distances


DISTANCE = 'distance'
VISITED = 'visited'


def calculate_distance(cave, valve_a, valve_b):
    
    dists = {valve: {DISTANCE: math.inf, VISITED: False} for valve in cave}
    dists[valve_a][DISTANCE] = 0
    
    current_valve = valve_a
    
    while not dists[current_valve][VISITED]:
        current_dist = dists[current_valve][DISTANCE]
        
        for valve in cave[current_valve][VALVES_TO]:
            valve_dist = current_dist + 1
            if valve_dist < dists[valve][DISTANCE]:
                dists[valve][DISTANCE] = valve_dist
        
        dists[current_valve][VISITED] = True
        
        sorted_dists = dict(sorted(dists.items(), key=lambda x: (x[1][VISITED], x[1][DISTANCE])))
        current_valve = list(sorted_dists.keys())[0]
        
        if current_valve == valve_b:
            break
    
    return dists[valve_b][DISTANCE]


# Calculate pressure released in path

def calculate_pressure(cave, distances, valve_start, valves, time):
    
    pressure_cum = 0
    pressure_rate = 0
    current_time = 0
    
    current_valve = valve_start
    n_valves = 0
    
    for valve in valves:
        walk_time = distances[(current_valve, valve)]
        activate_time = 1
        remaining_time = time - current_time
        
        if remaining_time <= (walk_time + activate_time):
            break
        
        n_valves += 1
        
        pressure_release = cave[valve][RATE]
        
        pressure_cum += pressure_rate * (walk_time + activate_time)
        pressure_rate += pressure_release
        current_time += (walk_time + activate_time)
        
        current_valve = valve
    
    remaining_time = time - current_time
    
    pressure_cum += pressure_rate * remaining_time
    
    logging.debug(f'{n_valves:2} processed out {len(valves)}')
    
    return pressure_cum


VALVE = 'valve'
TIME = 'time'
VALVES = 'valves'
PATHS = 'paths'
PRESSURE = 'pressure'
PRESSURE_CUM = 'pressure_cum'
ROUND = 'round'


def get_starting_path(valve, valves):
    
    path = {VALVE: valve, TIME: 0, VALVES: valves, PRESSURE: 0, PRESSURE_CUM: 0, PATHS: []}
    
    return path


def add_paths(cave, valves_distances, path, max_time):
    
    potential_paths = get_potential_paths(cave, valves_distances, path, max_time)
    
    for child_path in potential_paths:
        
        child_path = add_paths(cave, valves_distances, child_path, max_time)
    
    path[PATHS] = potential_paths
    
    return path


def get_potential_paths(cave, valves_distances, current_path, max_time):
    
    potential_paths = []
    
    current_valve = current_path[VALVE]
    current_time = current_path[TIME]
    remaining_valves = current_path[VALVES]
    current_pressure = current_path[PRESSURE]
    current_pressure_cum = current_path[PRESSURE_CUM]
    
    for valve in remaining_valves:
        walking_time = valves_distances[(current_valve, valve)]
        opening_time = 1
        action_time = walking_time + opening_time
        total_time = current_time + action_time
        
        new_valves = remaining_valves.copy()
        new_valves.remove(valve)
        
        pressure = current_pressure + cave[valve][RATE]
        
        pressure_flow = current_pressure * action_time
        pressure_cum = current_pressure_cum + pressure_flow
        
        if total_time < max_time:
            potential_paths.append({VALVE: valve, TIME: total_time, PRESSURE: pressure, PRESSURE_CUM: pressure_cum, VALVES: new_valves})
    
    return potential_paths


def calculate_pressure_path(target_path, max_time):
    
    paths = target_path[PATHS]
    time = target_path[TIME]
    pressure_cum = target_path[PRESSURE_CUM]
    pressure = target_path[PRESSURE]
    
    paths_len = len(paths)
    
    if paths_len == 0:
        remaining_time = max_time - time
        total_pressure = pressure_cum + pressure * remaining_time
        
        return [total_pressure]
    
    pressure_list = []
    
    for path in paths:
        total_pressure = calculate_pressure_path(path, max_time)
        pressure_list.extend(total_pressure)
    
    return pressure_list


def len_path(target_path):
    
    paths = target_path[PATHS]
    
    paths_len = len(paths)
    
    if paths_len == 0:
        return [1]
    
    total_len = []
    
    for path in paths:
        path_len = len_path(path)
        
        for i, l in enumerate(path_len):
            path_len[i] += 1
            
        total_len.extend(path_len)
    
    return total_len


def get_starting_path_2(valve, valves):
    
    path = {VALVE: valve, TIME: 0, VALVES: valves, PRESSURE: 0, PRESSURE_CUM: 0, ROUND: 1, PATHS: []}
    
    return path


def add_paths_2(cave, valves_distances, path, max_time, max_round, start_valve):
    
    path_round = path[ROUND]
    path_time = path[TIME]
    
    if path_round <= max_round:
        potential_paths = get_potential_paths_2(cave, valves_distances, path, max_time)
        
        for child_path in potential_paths:
            
            child_path = add_paths_2(cave, valves_distances, child_path, max_time, max_round, start_valve)
        
        if potential_paths == []:
            
            end_path = finish_path(path, max_time)
            
            current_valves = end_path[VALVES]
            current_round = end_path[ROUND]
            next_round = current_round + 1
            
            if next_round <= max_round:
                next_path = {VALVE: start_valve,
                             VALVES: current_valves,
                             TIME: 0,
                             PRESSURE: 0,
                             PRESSURE_CUM: 0,
                             ROUND: next_round,
                             PATHS: []}
                
                next_path = add_paths_2(cave, valves_distances, next_path, max_time, max_round, start_valve)
                
                end_path[PATHS].append(next_path)
        
            potential_paths.append(end_path)
        
        path[PATHS] = potential_paths
    
    return path


def finish_path(path, max_time):
    
    current_valve = path[VALVE]
    current_valves = path[VALVES]
    current_round = path[ROUND]
    
    current_time = path[TIME]
    current_pressure_cum = path[PRESSURE_CUM]
    current_pressure = path[PRESSURE]
    
    remaining_time = max_time - current_time
    total_pressure_cum = current_pressure_cum + remaining_time * current_pressure
    
    end_path = {VALVE: current_valve,
                VALVES: current_valves,
                TIME: max_time,
                PRESSURE: current_pressure,
                PRESSURE_CUM: total_pressure_cum,
                ROUND: current_round,
                PATHS: []}
    
    logging.debug(f'Finishing a path in valve {current_valve} with {current_pressure_cum}')
    
    return end_path


def get_potential_paths_2(cave, valves_distances, current_path, max_time):
    
    potential_paths = []
    
    current_valve = current_path[VALVE]
    current_round = current_path[ROUND]
    current_time = current_path[TIME]
    remaining_valves = current_path[VALVES]
    current_pressure = current_path[PRESSURE]
    current_pressure_cum = current_path[PRESSURE_CUM]
    
    for valve in remaining_valves:
        walking_time = valves_distances[(current_valve, valve)]
        opening_time = 1
        action_time = walking_time + opening_time
        total_time = current_time + action_time
        
        new_valves = remaining_valves.copy()
        new_valves.remove(valve)
        
        pressure = current_pressure + cave[valve][RATE]
        
        pressure_flow = current_pressure * action_time
        pressure_cum = current_pressure_cum + pressure_flow
        
        if total_time < max_time:
            potential_paths.append({VALVE: valve, TIME: total_time, PRESSURE: pressure, PRESSURE_CUM: pressure_cum, VALVES: new_valves, ROUND: current_round})
    
    return potential_paths


def calculate_pressure_path_2(target_path, max_time):
    
    paths = target_path[PATHS]
    time = target_path[TIME]
    pressure_cum = target_path[PRESSURE_CUM]
    pressure = target_path[PRESSURE]
    
    # if it is max_time return the actual pressure_cum
    
    if time == max_time:
    
        paths_len = len(paths)
        
        if paths_len == 0:
            
            return [pressure_cum]
        
        pressure_list = []
        
        for path in paths:
            child_pressure_list = calculate_pressure_path_2(path, max_time)
            
            for child_pressure in child_pressure_list:
                total_pressure = child_pressure + pressure_cum
                pressure_list.extend([total_pressure])
    
        return pressure_list
    
    # If it's not max_time then just return child pressures
    
    pressure_list = []
    
    for path in paths:
        total_pressure = calculate_pressure_path_2(path, max_time)
        pressure_list.extend(total_pressure)
    
    return pressure_list


def collect_end_paths(path, max_time):
    
    time = path[TIME]
    
    if time == max_time:
        return [path]
    
    child_paths = path[PATHS]
    
    path_list = []
    
    for path in child_paths:
        end_paths = collect_end_paths(path, max_time)
        path_list.extend(end_paths)
    
    return path_list
        





















