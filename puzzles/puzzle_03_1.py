FILE_NAME = "input_05.txt"

with open(FILE_NAME) as f:
    data = f.read()

def break_items(items):
    items_length = len(items)
    mid_item = items_length // 2
    a = items[0:mid_item]
    b = items[mid_item:]
    return (a, b)

def find_item(pocket_a, pocket_b):
    for item in pocket_a:
        if item in pocket_b:
            return item

def get_priority(item):
    if ord(item) >= ord('a'):
        priority = ord(item) - ord('a') + 1
    else:
        priority = ord(item) - ord('A') + 27
    return priority

priority_sum = 0

for rucksack in data.splitlines():
    pocket_a, pocket_b = break_items(rucksack)
    item = find_item(pocket_a, pocket_b)
    priority = get_priority(item)
    priority_sum += priority
    print(f"Rucksack {rucksack} has item {item} with priority {priority}")

print(f"Total priority is {priority_sum}")

