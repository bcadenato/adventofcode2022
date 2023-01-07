import math

CHAR_WALL = '#'
CHAR_WIND_UP = '^'
CHAR_WIND_DOWN = 'v'
CHAR_WIND_LEFT = '<'
CHAR_WIND_RIGHT = '>'
CHAR_GROUND = '.'
CHAR_MULTIPLE_WINDS = '*'

def get_valley_str(valley, min_x, max_x, min_y, max_y):
        str = ''

        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                str += valley[(x, y)]
            
            str += '\n'
        
        return str


class Valley:

    def __init__(self, valley_str):
        """Initialises a Valley object from a valley string"""
        valley0 = {}
        self.valley = [valley0]
        self.time = 0

        self.winds = []

        lines = valley_str.splitlines()

        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                valley0[(x, y)] = char
        
        self.min_x = min([key[0] for key in valley0])
        self.max_x = max([key[0] for key in valley0])
        self.min_y = min([key[1] for key in valley0])
        self.max_y = max([key[1] for key in valley0])

        self.wind_range_x_min = self.min_x + 1
        self.wind_range_x_max = self.max_x - 1
        self.wind_range_y_min = self.min_y + 1
        self.wind_range_y_max = self.max_y - 1
        
        for position, char in valley0.items():
            
            if char in [CHAR_WIND_UP, CHAR_WIND_DOWN]:
                self.winds.append(WindVertical(char, position, 
                                          (self.wind_range_y_min, 
                                           self.wind_range_y_max)))
        
            if char in [CHAR_WIND_LEFT, CHAR_WIND_RIGHT]:
                self.winds.append(WindHorizontal(char, position, 
                                            (self.wind_range_x_min, 
                                             self.wind_range_x_max)))


    def __getitem__(self, index):
        n_valley = len(self.valley)

        if index < n_valley:
            return self.valley[index]
        
        for i in range(n_valley, index + 1):
            valley_i = self._generate_valley(i)
            self.valley.append(valley_i)

        return self.valley[index]


    def __len__(self):
        return len(self.valley)
    

    def get_dims(self):
        return (self.min_x, self.max_x, self.min_y, self.max_y)
    

    def _generate_valley(self, index):
        wind_position = {}

        for wind in self.winds:
            wp = wind[index]
            wind_char = wind.get_char()

            if wp in wind_position:
                wind_position[wp].append(wind_char)
            else:
                wind_position[wp] = [wind_char]

        valley0 = self.valley[0]
        valleyt = {}

        for x in range(self.min_x, self.max_x + 1):
            for y in range(self.min_y, self.max_y + 1):

                char0 = valley0[(x, y)]

                if char0 == CHAR_WALL:
                    valleyt[(x, y)] = CHAR_WALL
                    continue
                
                if (x, y) in wind_position:

                    wp = wind_position[(x, y)]

                    if len(wp) > 1:
                        valleyt[(x, y)] = CHAR_MULTIPLE_WINDS
                    else:
                        valleyt[(x, y)] = wp[0]
                    
                    continue
                
                valleyt[(x, y)] = CHAR_GROUND
        
        return valleyt


VEC_UP = (0, -1)
VEC_DOWN = (0, 1)
VEC_LEFT = (-1, 0)
VEC_RIGHT = (1, 0)

class Wind:

    def __getitem__(self, index):
        pass

    def get_char(self):
        return self.wind_type

class WindVertical(Wind):

    def __init__(self, wind_type, start_position, wind_range):

        self.start_x, self.start_y = start_position
        self.wind_range_min, self.wind_range_max = wind_range
        self.wind_range_len = self.wind_range_max - self.wind_range_min + 1
        self.wind_type = wind_type

        if wind_type == CHAR_WIND_UP:
            self.y_chg = -1
        
        if wind_type == CHAR_WIND_DOWN:
            self.y_chg = 1
        
    def __getitem__(self, index):
        start_base = self.start_y - self.wind_range_min
        target_base = (start_base + self.y_chg * index) % self.wind_range_len
        target = target_base + self.wind_range_min
        return (self.start_x, target)


class WindHorizontal(Wind):

    def __init__(self, wind_type, start_position, wind_range):

        self.start_x, self.start_y = start_position
        self.wind_range_min, self.wind_range_max = wind_range
        self.wind_range_len = self.wind_range_max - self.wind_range_min + 1
        self.wind_type = wind_type

        if wind_type == CHAR_WIND_LEFT:
            self.x_chg = -1
        
        if wind_type == CHAR_WIND_RIGHT:
            self.x_chg = 1
        
    def __getitem__(self, index):
        start_base = self.start_x - self.wind_range_min
        target_base = (start_base + self.x_chg * index) % self.wind_range_len
        target = target_base + self.wind_range_min
        return (target, self.start_y)

MOVE_UP = (0, -1)
MOVE_DOWN = (0, 1)
MOVE_LEFT = (-1, 0)
MOVE_RIGHT = (1, 0)
WAIT = (0, 0)

ACTIONS = [WAIT,
           MOVE_UP,
           MOVE_DOWN,
           MOVE_LEFT,
           MOVE_RIGHT]


def add_vector(position, vector):

    x, y = position
    v_x, v_y = vector

    return (x + v_x, y + v_y)


def is_move_valid(valley, position):

    if position in valley:

        if valley[position] == CHAR_GROUND:
            return True
    
    return False


def get_moves(valley, position):
    """Returns a sequence with potential actions from current position"""

    moves = [add_vector(position, vector) for vector in ACTIONS]

    valid_moves = [position for position in moves if is_move_valid(valley, position)]

    return valid_moves


def calculate_distance(position, goal):
    """Returns the distance between a position and a goal"""

    p_x, p_y = position
    g_x, g_y = goal

    distance = abs(g_x - p_x) + abs(g_y - p_y)

    return distance


def calculate_shortest_path(valley, start_position, goal_position, start_time):

    paths = {}
    min_time = math.inf

    position = start_position
    time = start_time
    distance = calculate_distance(position, goal_position)

    explore_queue = [(position, time, distance)]

    iterations = 0

    while explore_queue:

        iterations += 1

        explore_queue.sort(key=lambda x: (x[2] + x[1], x[2], x[1]), reverse=True)
        position, time, distance = explore_queue.pop()

        if (position, time, distance) in paths:
            continue

        if position == goal_position:

            if time < min_time:
                min_time = time

            return time

        if (time + distance) > min_time:
            break

        paths[(position, time, distance)] = True

        time += 1

        moves = get_moves(valley[time], position)
        options = sorted([(move, time, calculate_distance(move, goal_position)) for move in moves], key=lambda x: x[2], reverse=True)
        explore_queue.extend(options)
























