import copy
import itertools

def read_file(file):
    
    with open(file) as f:
        lines = f.read().splitlines()
    
    sequence = []
    
    for i, line in enumerate(lines):
        sequence.append( (int(line), i) )
    
    return sequence


def number_generator(sequence):
    
    seq = copy.copy(sequence)
    
    for item in itertools.cycle(seq):
        
        yield(item)


def mix_new(sequence, index, item):
    
    sequence_len = len(sequence)
    
    number, order = item
    
    successor_index = (index + 1) % sequence_len
    
    successor_item = sequence[successor_index]
    
    sequence.pop(index)
    
    successor_index = sequence.index(successor_item)
    
    new_index = (successor_index + number) % (sequence_len - 1)
    
    sequence.insert(new_index, item)
    
    return sequence


def clean_sequence(sequence):
    
    clean_seq = [item[0] for item in sequence]
    
    return clean_seq


def find_zero_index(sequence):
    
    zero_item = [item for item in sequence if item[0] == 0]
    
    zero_index = sequence.index(zero_item[0])
    
    return zero_index


def get_number(sequence, zero_index, position):
    
    item_index = (zero_index + position) % len(sequence)
    
    return sequence[item_index][0]


# def mix_old(sequence, index, item):
#     
#     sequence_len = len(sequence)
#     
#     number, order = item
#     
#     new_index = (index + number)
#     
#     if new_index < 0:
#         new_index = new_index % sequence_len - 1
#     elif new_index == 0:
#         new_index = sequence_len
#     elif new_index >= sequence_len:
#         new_index = new_index % sequence_len + 1
#     else:
#         new_index = new_index % sequence_len
#     
#     sequence.pop(index)
#     
#     sequence.insert(new_index, item)
#     
#     return sequence

















