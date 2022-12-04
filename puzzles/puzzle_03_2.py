FILE_NAME = "input_05.txt"

with open(FILE_NAME) as f:
    data = f.read()

def break_items(items):
    items_length = len(items)
    mid_item = items_length // 2
    a = items[0:mid_item]
    b = items[mid_item:]
    return (a, b)

def find_item(rucksack_a, rucksack_b, rucksack_c):
    for item in rucksack_a:
        if item in rucksack_b and item in rucksack_c:
            return item

def get_priority(item):
    if ord(item) >= ord('a'):
        priority = ord(item) - ord('a') + 1
    else:
        priority = ord(item) - ord('A') + 27
    return priority

priority_sum = 0
rucksacks = data.splitlines()

for i in range(0, len(rucksacks), 3):
    item = find_item(rucksacks[i], rucksacks[i+1], rucksacks[i+2])
    priority = get_priority(item)
    priority_sum += priority
    print(f"Item is {item} with priority {priority}")

print(f"Total priority of badges is {priority_sum}")
