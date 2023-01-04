import re
import copy

BLUEPRINT_PATTERN = r'Blueprint (\d*): Each ore robot costs (\d*) ore. Each clay robot costs (\d*) ore. Each obsidian robot costs (\d*) ore and (\d*) clay. Each geode robot costs (\d*) ore and (\d*) obsidian.'

BP_ID = 'bp_id' 
BP_ORE = 'bp_robot_ore' 
BP_CLAY = 'bp_robot_clay'
BP_OBSIDIAN = 'bp_robot_obsidian'
BP_GEODE = 'bp_robot_geode'

def read_blueprint(blueprint_str):
    
    blueprint = {}
    
    items = re.findall(BLUEPRINT_PATTERN, blueprint_str)[0]
    
    blueprint[BP_ID] = int(items[0])
    
    blueprint[BP_ORE] = int(items[1])
    blueprint[BP_CLAY] = int(items[2])
    blueprint[BP_OBSIDIAN] = (int(items[3]), int(items[4]))
    blueprint[BP_GEODE] = (int(items[5]), int(items[6]))
    
    return blueprint


def read_blueprint_file(file):
    with open(file) as f:
        lines = f.read().splitlines()
    
    blueprints = []
    
    for line in lines:
        blueprint = read_blueprint(line)
        blueprints.append(blueprint)
    
    return blueprints


OP_BLUEPRINT = 'operation_blueprint'
OP_LOG = 'operation_log'

LOG_STATE = 'log_state'
LOG_TIME = 'log_time'
LOG_NEXT = 'log_next'
LOG_PRE = 'log_previous'

RB_ORE = 'robot_ore'
RB_CLAY = 'robot_clay'
RB_OBSIDIAN = 'robot_obsidian'
RB_GEODE = 'robot_geode'

RS_ORE = 'resource_ore'
RS_CLAY = 'resource_clay'
RS_OBSIDIAN = 'resource_obsidian'
RS_GEODE = 'resource_geode'

def get_new_operation(blueprint):
    
    start_state = {RB_ORE: 1,
                   RB_CLAY: 0,
                   RB_OBSIDIAN: 0,
                   RB_GEODE: 0,
                   RS_ORE: 0,
                   RS_CLAY: 0,
                   RS_OBSIDIAN: 0,
                   RS_GEODE: 0}
    
    start_log = {LOG_STATE: start_state,
                 LOG_TIME: 0,
                 LOG_PRE: None,
                 LOG_NEXT: []}
    
    operation = {OP_BLUEPRINT: blueprint,
                 OP_LOG: start_log}
    
    return operation


def get_next_robots(log):
    """Returns a list of potential robots in a given state
    
    This is key to control the growth of the combinatorial tree.
    """
    
    state = log[LOG_STATE]
    
    rb_ore = state[RB_ORE]
    rb_clay = state[RB_CLAY]
    rb_obsidian = state[RB_OBSIDIAN]
    
    MAX_ORE = 4
    MAX_CLAY = 11
    MAX_OBSIDIAN = 8
    
    if state[RB_CLAY] == 0:
        next_robots = [RB_CLAY]
        
        if rb_ore <= MAX_ORE:
            next_robots.append(RB_ORE)
        
        return next_robots
    
    if state[RB_OBSIDIAN] == 0:
        next_robots = [RB_OBSIDIAN]
        
        if rb_ore <= 1:
            next_robots.append(RB_ORE)
        
        if rb_clay <= MAX_CLAY:
            next_robots.append(RB_CLAY)
        
        return next_robots

    next_robots = [RB_GEODE]
    
    if rb_clay <= 9:
        next_robots.append(RB_CLAY)
        
    if rb_obsidian <= MAX_OBSIDIAN:
        next_robots.append(RB_OBSIDIAN)
        
    return next_robots


def harvest(log):
    """Returns a next log state after harvesting one unit of time with every robot"""
    
    time = log[LOG_TIME]
    state = log[LOG_STATE]
    
    new_state = copy.deepcopy(state)
    
    new_state[RS_ORE] += new_state[RB_ORE]
    new_state[RS_CLAY] += new_state[RB_CLAY]
    new_state[RS_OBSIDIAN] += new_state[RB_OBSIDIAN]
    new_state[RS_GEODE] += new_state[RB_GEODE]
    
    time += 1
    
    new_log = {LOG_STATE: new_state,
               LOG_TIME: time,
               LOG_PRE: log,
               LOG_NEXT: []}
    
    log[LOG_NEXT].append(new_log)
    
    return new_log


def build_robot(blueprint, log, robot):
    """Builds a robot during the next minute on the current log and returns the next log"""
    
    time = log[LOG_TIME]
    state = log[LOG_STATE]
    
    rs_ore = state[RS_ORE]
    rs_clay = state[RS_CLAY]
    rs_obsidian = state[RS_OBSIDIAN]
    rs_geode = state[RS_GEODE]
    
    rb_ore = state[RB_ORE]
    rb_clay = state[RB_CLAY]
    rb_obsidian = state[RB_OBSIDIAN]
    rb_geode = state[RB_GEODE]
        
    if robot == RB_ORE:
        cost_ore = blueprint[BP_ORE]
        
        new_state = copy.deepcopy(state)
        
        new_state[RS_CLAY] = rs_clay + rb_clay
        new_state[RS_OBSIDIAN] = rs_obsidian + rb_obsidian
        new_state[RS_GEODE] = rs_geode + rb_geode
        
        new_state[RS_ORE] = rs_ore - cost_ore + rb_ore
        new_state[RB_ORE] += 1
        
        time += 1
        
        new_log = {LOG_STATE: new_state,
                   LOG_TIME: time,
                   LOG_PRE: log,
                   LOG_NEXT: []}
        
        log[LOG_NEXT].append(new_log)
        
        return new_log
    
    if robot == RB_CLAY:
        cost_ore = blueprint[BP_CLAY]
        
        new_state = copy.deepcopy(state)
        
        new_state[RS_CLAY] = rs_clay + rb_clay
        new_state[RS_OBSIDIAN] = rs_obsidian + rb_obsidian
        new_state[RS_GEODE] = rs_geode + rb_geode
        
        new_state[RS_ORE] = rs_ore - cost_ore + rb_ore
        new_state[RB_CLAY] = rb_clay + 1
        
        time += 1
        
        new_log = {LOG_STATE: new_state,
                   LOG_TIME: time,
                   LOG_PRE: log,
                   LOG_NEXT: []}
        
        log[LOG_NEXT].append(new_log)
        
        return new_log
    
    if robot == RB_OBSIDIAN:
        (cost_ore, cost_clay) = blueprint[BP_OBSIDIAN]
        
        new_state = copy.deepcopy(state)
        
        new_state[RS_OBSIDIAN] = rs_obsidian + rb_obsidian
        new_state[RS_GEODE] = rs_geode + rb_geode
        
        new_state[RS_ORE] = rs_ore - cost_ore + rb_ore
        new_state[RS_CLAY] = rs_clay - cost_clay + rb_clay
        new_state[RB_OBSIDIAN] = rb_obsidian + 1
        
        time += 1
        
        new_log = {LOG_STATE: new_state,
                   LOG_TIME: time,
                   LOG_PRE: log,
                   LOG_NEXT: []}
        
        log[LOG_NEXT].append(new_log)
        
        return new_log
    
    if robot == RB_GEODE:
        (cost_ore, cost_obsidian) = blueprint[BP_GEODE]
        
        new_state = copy.deepcopy(state)
        
        new_state[RS_CLAY] = rs_clay + rb_clay
        new_state[RS_GEODE] = rs_geode + rb_geode
        
        new_state[RS_ORE] = rs_ore - cost_ore + rb_ore
        new_state[RS_OBSIDIAN] = rs_obsidian - cost_obsidian + rb_obsidian
        new_state[RB_GEODE] = rb_geode + 1
        
        time += 1
        
        new_log = {LOG_STATE: new_state,
                   LOG_TIME: time,
                   LOG_PRE: log,
                   LOG_NEXT: []}
        
        log[LOG_NEXT].append(new_log)
        
        return new_log


def process_robot(blueprint, log, robot):
    """Returns a succesor log after harvesting until the target robot can be built"""
    
    while True:
        if can_build_robot(blueprint, log, robot):
            next_log = build_robot(blueprint, log, robot)
            return next_log
        
        log = harvest(log)


def can_build_robot(blueprint, log, robot):
    """Checks if a certain robot can be built out of a given state"""
    
    if robot == RB_ORE:
        cost_ore = blueprint[BP_ORE]
        rs_ore = log[LOG_STATE][RS_ORE]
        return rs_ore >= cost_ore
    
    if robot == RB_CLAY:
        cost_ore = blueprint[BP_CLAY]
        rs_ore = log[LOG_STATE][RS_ORE]
        return rs_ore >= cost_ore
    
    if robot == RB_OBSIDIAN:
        cost_ore, cost_clay = blueprint[BP_OBSIDIAN]
        rs_ore = log[LOG_STATE][RS_ORE]
        rs_clay = log[LOG_STATE][RS_CLAY]
        return rs_ore >= cost_ore and rs_clay >= cost_clay
    
    if robot == RB_GEODE:
        cost_ore, cost_obsidian = blueprint[BP_GEODE]
        rs_ore = log[LOG_STATE][RS_ORE]
        rs_obsidian = log[LOG_STATE][RS_OBSIDIAN]
        return rs_ore >= cost_ore and rs_obsidian >= cost_obsidian


def simulate_log(blueprint, log, max_time):
    """Simulates potential paths from a log."""
    
    log_queue = [log]
    log_signatures = {}
    
    while log_queue:
        
        cur_log = log_queue.pop(0)
        
        log_signature, log_time = get_log_signature(cur_log)
        
        if log_signature in log_signatures:
            continue
        else:
            log_signatures[log_signature] = log_time
        
        robots = get_next_robots(cur_log)
        
        for robot in robots:
            next_log = process_robot(blueprint, cur_log, robot)
            time = next_log[LOG_TIME]
            
            if time < max_time:
                log_queue.append(next_log)
    
    return log


def prune_logs(log, max_time):
    
    end_logs = []
    log_queue = [log]
    
    while log_queue:
        
        cur_log = log_queue.pop(0)
        
        log_childs = cur_log[LOG_NEXT]
        
        for log_child in log_childs:
            
            if log_child[LOG_TIME] == max_time:
                end_logs.append(log_child)
            else:
                log_queue.append(log_child)
    
    return end_logs


def max_geode(log, max_time):
    
    end_logs = prune_logs(log, max_time)
    
    max_geode = max(end_logs, key=lambda x: x[LOG_STATE][RS_GEODE])
    
    return max_geode


def log_str(log):
    
    log_str = ''
    
    state = log[LOG_STATE]
    time = log[LOG_TIME]
    
    log_str += f'Time elapsed: {time}\n'
    log_str += f'Ore Robots:      {state[RB_ORE]:2}  Ore units:      {state[RS_ORE]:2}\n'
    log_str += f'Clay Robots:     {state[RB_CLAY]:2}  Clay units:     {state[RS_CLAY]:2}\n'
    log_str += f'Obsidian Robots: {state[RB_OBSIDIAN]:2}  Obsidian units: {state[RS_OBSIDIAN]:2}\n'
    log_str += f'Geode Robots:    {state[RB_GEODE]:2}  Geode units:    {state[RS_GEODE]:2}\n'
    
    return log_str


def get_log_history(log):
    
    log_history = []
    
    log_history.append(log)
    
    while log[LOG_PRE]:
        log = log[LOG_PRE]
        log_history.append(log)
    
    return reversed(log_history)


def get_log_signature(log):
    """Returns a tuple with the number of robots and resources of a log"""
    
    time = log[LOG_TIME]
    state = log[LOG_STATE]
    
    rs_ore = state[RS_ORE]
    rs_clay = state[RS_CLAY]
    rs_obsidian = state[RS_OBSIDIAN]
    rs_geode = state[RS_GEODE]
    
    rb_ore = state[RB_ORE]
    rb_clay = state[RB_CLAY]
    rb_obsidian = state[RB_OBSIDIAN]
    rb_geode = state[RB_GEODE]
    
    return ((rb_ore, rb_clay, rb_obsidian, rb_geode, rs_ore, rs_clay, rs_obsidian, rs_geode), time)

















