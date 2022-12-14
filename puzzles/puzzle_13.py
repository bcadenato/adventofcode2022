# Read logic

def read_file(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()
    
    packets = []
    
    n_lines = len(lines)
    n_pairs = n_lines // 3 + (n_lines % 3) // 2
    
    for i in range(0, n_pairs):
        packet_left_line = i * 3
        packet_right_line = packet_left_line + 1
        
        packet_left = read_packet(lines[packet_left_line])
        packet_right = read_packet(lines[packet_right_line])
        
        packets.append( (packet_left, packet_right) )
    
    return packets


def read_file_2(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()
    
    packets = []
    
    n_lines = len(lines)
    n_pairs = n_lines // 3 + (n_lines % 3) // 2
    
    for i in range(0, n_pairs):
        packet_left_line = i * 3
        packet_right_line = packet_left_line + 1
        
        packet_left = read_packet(lines[packet_left_line])
        packet_right = read_packet(lines[packet_right_line])
        
        packets.extend([packet_left, packet_right])
    
    return packets



def read_packet(packet_str):
    packet = eval(packet_str)
    
    return packet


# Implement packet comparison logic

RIGHT = 1
EQUAL = 0
WRONG = -1

def compare_items(item_left, item_right):
    if isinstance(item_left, int) and isinstance(item_right, int):
        if item_left == item_right:
            return EQUAL
        if item_left < item_right:
            return RIGHT
        if item_left > item_right:
            return WRONG
    
    if isinstance(item_left, list) and isinstance(item_right, list):
        n_left = len(item_left)
        n_right = len(item_right)
        
        n_min = min(n_left, n_right)
        
        for i in range(0, n_min):
            item_comp = compare_items(item_left[i], item_right[i])
            
            if item_comp == RIGHT:
                return RIGHT
            elif item_comp == WRONG:
                return WRONG
        
        if n_left < n_right:
            return RIGHT
        elif n_left == n_right:
            return EQUAL
        elif n_left > n_right:
            return WRONG
    
    if isinstance(item_left, list) and isinstance(item_right, int):
        item_right = [item_right]
        
        return compare_items(item_left, item_right)
    
    if isinstance(item_left, int) and isinstance(item_right, list):
        item_left = [item_left]
        
        return compare_items(item_left, item_right)


def compare_packets(packet_left, packet_right):
    comp = compare_items(packet_left, packet_right)
    
    if comp == RIGHT:
        return True
    elif comp == WRONG:
        return False

        

    
    
