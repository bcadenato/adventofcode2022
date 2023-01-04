import pytest
import puzzles.puzzle_19 as puzzle


# Test blueprints

@pytest.fixture
def blueprint_str_sample_1():
    blueprint_str_sample = 'Blueprint 1: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 20 clay. Each geode robot costs 4 ore and 7 obsidian.'
    return blueprint_str_sample


def test_read_blueprint_1(blueprint_str_sample_1):
    blueprint = puzzle.read_blueprint(blueprint_str_sample_1)
    
    assert blueprint[puzzle.BP_ID] == 1


def test_new_operation_1(blueprint_str_sample_1):
    operation = puzzle.get_new_operation(blueprint_str_sample_1)
    
    assert operation[puzzle.OP_LOG][puzzle.LOG_STATE][puzzle.RB_ORE] == 1


# Test operations

@pytest.fixture
def operation_1(blueprint_str_sample_1):
    blueprint = puzzle.read_blueprint(blueprint_str_sample_1)
    operation = puzzle.get_new_operation(blueprint)
    
    return operation


def test_harvest_1(operation_1):
    log = operation_1[puzzle.OP_LOG]
    
    log = puzzle.harvest(log)
    log = puzzle.harvest(log)
    
    assert log[puzzle.LOG_STATE][puzzle.RS_ORE] == 2


def test_build_robot_1(operation_1):
    blueprint = operation_1[puzzle.OP_BLUEPRINT]
    log = operation_1[puzzle.OP_LOG]
    
    log = puzzle.harvest(log)
    log = puzzle.harvest(log)
    log = puzzle.harvest(log)
    log = puzzle.build_robot(blueprint, log, puzzle.RB_ORE)
    
    assert log[puzzle.LOG_STATE][puzzle.RB_ORE] == 2


def test_process_robot_1(operation_1):
    blueprint = operation_1[puzzle.OP_BLUEPRINT]
    log = operation_1[puzzle.OP_LOG]
    
    next_log = puzzle.process_robot(blueprint, log, puzzle.RB_ORE)
    
    assert next_log[puzzle.LOG_STATE][puzzle.RB_ORE] == 2


def test_process_robot_2(operation_1):
    blueprint = operation_1[puzzle.OP_BLUEPRINT]
    log = operation_1[puzzle.OP_LOG]
    
    next_log = puzzle.process_robot(blueprint, log, puzzle.RB_CLAY)
    
    assert next_log[puzzle.LOG_STATE][puzzle.RB_CLAY] == 1


def test_next_robots_1(operation_1):
    log = operation_1[puzzle.OP_LOG]
    
    robots = puzzle.get_next_robots(log)
    
    assert robots == [puzzle.RB_CLAY, puzzle.RB_ORE]


def test_simulation_1(operation_1):
    blueprint = operation_1[puzzle.OP_BLUEPRINT]
    log = operation_1[puzzle.OP_LOG]
    
    robots = puzzle.get_next_robots(log)
    
    end_logs = []
    
    for robot in robots:
        next_log = puzzle.process_robot(blueprint, log, robot)
        end_logs.append(next_log)
    
    assert end_logs[0][puzzle.LOG_TIME], end_logs[1][puzzle.LOG_TIME] == (4, 5)


def test_simulation_2(operation_1):
    blueprint = operation_1[puzzle.OP_BLUEPRINT]
    log = operation_1[puzzle.OP_LOG]
    
    log = puzzle.simulate_log(blueprint, log, 4)
    end_logs = puzzle.prune_logs(log, 4)
    
    assert len(end_logs) == 2


def test_log_signature_1(operation_1):
    blueprint = operation_1[puzzle.OP_BLUEPRINT]
    log = operation_1[puzzle.OP_LOG]
    
    log = puzzle.harvest(log)
    log = puzzle.harvest(log)
    log = puzzle.harvest(log)
    
    log_signature = puzzle.get_log_signature(log)
    
    assert log_signature == ((1, 0, 0, 0, 3, 0, 0, 0), 3)
    













