# Reading files logic

def read_input(input_file):
    with open(input_file) as f:
        lines = f.read().splitlines()
    
    lines_len = len(lines)
    monkey_len = lines_len // 7 + (lines_len % 7) // 6
    
    monkey_data = []
    
    for i in range(0, monkey_len):
        line_start = i * 7
        line_end = line_start + 6
        
        monkey_data.append(read_monkey_input(lines[line_start:line_end]))
    
    return monkey_data


def read_monkey_input(monkey_input):
    monkey = {}
    
    # Obtain monkey number
    
    monkey_id = int(monkey_input[0].strip(':').split()[1])
    
    # Build monkey items list
    
    monkey_items = read_monkey_items(monkey_input[1])
    
    # Monkey operation
    
    monkey_operation = read_monkey_operation(monkey_input[2])
    
    # Monkey assignment logic
    
    (monkey_factor, monkey_assignment) = read_monkey_assignment(monkey_input[3], monkey_input[4], monkey_input[5])
    
    # Build monkey
    
    monkey['id'] = monkey_id
    monkey['items'] = monkey_items
    monkey['operation'] = monkey_operation
    monkey['factor'] = monkey_factor
    monkey['assignment'] = monkey_assignment
    monkey['inspected'] = 0
    
    return monkey


def read_monkey_items(monkey_items_str):
    monkey_items = []
    
    monkey_items_str = monkey_items_str.strip('  Starting items: ')
    
    monkey_items_str = monkey_items_str.split(',')
    
    for item in monkey_items_str:
        monkey_items.append(int(item))
    
    return monkey_items


def read_monkey_operation(monkey_operation_str):
    
    monkey_operation_str = monkey_operation_str.strip('  Operation: new = ')
    
    operation_tokens = monkey_operation_str.split()
    
    operator = operation_tokens[1]
    
    param = operation_tokens[2]
    
    if param == 'old':
        operation_str = 'lambda x: x ' + operator + ' x'
    else:
        operation_str = 'lambda x: x ' + operator +  ' ' + param 
    
    monkey_operation = eval(operation_str)
    
    return monkey_operation


def read_monkey_assignment(condition_str, action_true_str, action_false_str):
    
    condition_str = condition_str.strip('  Test: divisible by ')
    
    monkey_factor = int(condition_str)
    
    action_true_str = action_true_str.strip('    If true: throw to monkey ')
    
    action_false_str = action_false_str.strip('    If false: throw to monkey ')
    
    operation_str = 'lambda x: ' + action_true_str + ' if x % ' + condition_str + ' == 0 else ' + action_false_str
    
    monkey_assignment = eval(operation_str)
    
    return (monkey_factor, monkey_assignment)


# Play round logic

def operation_bored(item):
    item = item // 3
    
    return item


def play_round(monkey_data, bored = operation_bored):
    
    for monkey in monkey_data:
        monkey_data = play_round_monkey(monkey_data, monkey, bored)
    
    return monkey_data


def play_round_monkey(monkey_data, monkey, bored = operation_bored):
    
    items_len = len(monkey['items'])
    
    for i in range(0, items_len):
        item = monkey['items'].pop(0)
        item = monkey['operation'](item)
        item = bored(item)
        monkey_target = monkey['assignment'](item)
        monkey_data[monkey_target]['items'].append(item)
        monkey['inspected'] += 1
    
    return monkey_data


# Calculate monkey business

def calculate_monkey_business(monkey_data):
    monkey_inspections = [(monkey['id'], monkey['inspected']) for monkey in monkey_data]
    
    monkey_inspections = sorted(monkey_inspections, key=lambda item: item[1], reverse = True)
    
    monkey_business = monkey_inspections[0][1] * monkey_inspections[1][1]
    
    return monkey_business


# Get boredom factor

def get_boredom_factor(monkey_data):
    p = 1
    
    for monkey in monkey_data:
        p *= monkey['factor']
    
    return p
        


