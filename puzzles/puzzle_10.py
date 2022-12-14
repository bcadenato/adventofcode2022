CMD_NOOP = 'noop'
CMD_ADDX = 'addx'

# Read functions

def read_input(input_file):
    with open(input_file) as f:
        lines = f.read().splitlines()
    
    command = []
    
    for line in lines:
        command.append(parse_line(line))
    
    return command


def parse_line(line):
    command = line.split()
    
    if command[0] == CMD_NOOP:
        return command
    
    if command[0] == CMD_ADDX:
        command[1] = int(command[1])
        return command


# Process commands

def process_commands(commands, cycle, X):
    cpu_track = {}
    
    for command in commands:
        (cycle, X, cpu_track) = process_command(command, cycle, X, cpu_track)
    
    return (cycle, X, cpu_track)


def process_command(command, cycle, X, cpu_track):
    if command[0] == CMD_NOOP:
        cycle += 1
        cpu_track[cycle] = X
        return (cycle, X, cpu_track)
    
    if command[0] == CMD_ADDX:
        cycle += 1
        cpu_track[cycle] = X
        
        cycle += 1
        cpu_track[cycle] = X
        
        X += command[1]
        
        return (cycle, X, cpu_track)


# Calculate and return Signal Strength

def calculate_signal_strength(cpu_track):
    signal_strength = 0
    
    for i in range(20, 221, 40):
        signal_strength += i * cpu_track[i]
        print(f'cycle {i} {cpu_track[i]}')
    
    print(f'Signal Strength is {signal_strength}')


# Print CRT

def calculate_crt(cpu_track):
    crt = []
    
    for row in range(0, 6):
        crt.append('')
        
        for col in range(0, 40):
            cycle = row * 40 + col + 1
            sprite_center = cpu_track[cycle]
            
            if abs(col - sprite_center) <= 1:
                crt[row] += ('#')
            else:
                crt[row] += ('.')
    
    return crt

