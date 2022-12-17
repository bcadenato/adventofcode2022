from itertools import accumulate
import logging

SENSOR_TEXT = 'Sensor at '
BEACON_TEXT = ': closest beacon is at'

def read_line(line):
    line = line.replace(SENSOR_TEXT, '')
    line = line.replace(BEACON_TEXT, '')
    line = line.replace(',', '', 2)
    
    tokens = line.split()
    
    sensor_x = read_coord(tokens[0])
    sensor_y = read_coord(tokens[1])
    beacon_x = read_coord(tokens[2])
    beacon_y = read_coord(tokens[3])
    
    return ( (sensor_x, sensor_y), (beacon_x, beacon_y) )


def read_coord(coord):
    coord = int(coord[2:])
    
    return coord


def read_cave_map(lines):
    
    cave_map = []
    
    for line in lines:
        sensor, beacon = read_line(line)
        
        device = {}
        
        device['sensor'] = sensor
        device['beacon'] = beacon
        
        cave_map.append(device)
    
    return cave_map


def read_file(file):
    
    with open(file) as f:
        lines = f.read().splitlines()
    
    cave_map = read_cave_map(lines)
    
    return cave_map


def calc_distance(point_a, point_b):
    point_a_x, point_a_y = point_a
    point_b_x, point_b_y = point_b
    
    distance = abs(point_b_x - point_a_x) + abs(point_b_y - point_a_y)
    
    return distance


def get_range(point, distance, row):
    
    point_x, point_y = point
    
    dist_y = abs(point_y - row)
    
    width = max(0, distance - dist_y)
    
    if width == 0:
        return None
    else:
        range_start = point_x - width
        range_end = point_x + width
    
    return (range_start, range_end)

def get_range_list(devices, row):
    
    range_list = []
    
    for device in devices:
        
        sensor = device['sensor']
        beacon = device['beacon']
        
        distance = calc_distance(sensor, beacon)
        
        sensor_range = get_range(sensor, distance, row)
        
        if sensor_range is None:
            continue
        
        range_list.append(sensor_range)
    
    range_list.sort(key=lambda x: x[0])
    
    return range_list


def get_coverage(devices, row):
    range_list = get_range_list(devices, row)
    range_merge = list(accumulate(range_list, merge_range))
    
    return range_merge


def merge_range(r_a, r_b):
    r_a_start, r_a_end = r_a
    r_b_start, r_b_end = r_b
    
    if r_b < r_a:
        return merge_range(r_b, r_a)
    
    if r_b_start > r_a_end + 1:
        logging.debug(f'Range {r_a} and {r_b}')
        raise Exception(f'There is a gap in x {r_a[1] + 1}')
        return
    
    merge_start = r_a_start
    merge_end = max(r_a_end, r_b_end)
    
    return (merge_start, merge_end)


def range_len(r):
    r_start, r_end = r
    
    r_len = r_end - r_start + 1
    
    return r_len


def get_beacons_in_row(devices, row):
    
    beacon_set = set()
    
    for device in devices:
        beacon = device['beacon']
        
        if beacon[1] == row:
            beacon_set.add(beacon)
    
    return beacon_set


def get_sensors_in_row(devices, row):
    
    sensor_list = []
    
    for device in devices:
        sensor = device['sensor']
        
        if sensor[1] == row:
            sensor_list.append(sensor)
    
    return sensor_list




        









