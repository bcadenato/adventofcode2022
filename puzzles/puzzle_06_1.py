from collections import deque

FILE_INPUT = 'puzzles/input_06.txt'

def is_marker(code):
    code_set = set(code)
    no_duplicates = len(code_set) == 4
    return no_duplicates
    

def find_index(message):
    message_len = len(message)
    
    if message_len >= 4:
        code = deque(message[0:4])
        if is_marker(code):
            return 4
    
    for i, char in enumerate(message[4:]):
        code.popleft()
        code.append(char)
        if is_marker(code):
            return i + 5

# Test the code with examples

TEST_01 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
TEST_02 = 'nppdvjthqldpwncqszvftbrmjlhg'
TEST_03 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
TEST_04 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

test_01_idx = find_index(TEST_01)
print(f"TEST_01 marker position is {test_01_idx}")

test_02_idx = find_index(TEST_02)
print(f"TEST_02 marker position is {test_02_idx}")

test_03_idx = find_index(TEST_03)
print(f"TEST_02 marker position is {test_03_idx}")

test_04_idx = find_index(TEST_04)
print(f"TEST_02 marker position is {test_04_idx}")

# Solve the problem

with open(FILE_INPUT) as f:
    message = f.read()

message_idx = find_index(message)

print(f"Marker index is {message_idx}")

for i in range(message_idx - 5, message_idx +5):
    print(f"{message[i - 1]} is char number {i}")


