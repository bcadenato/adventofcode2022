def process_max(i, top):
    if i >= top[2]:
        top[0], top[1], top[2] = top[1], top[2], i
    elif i >= top[1]:
        top[0], top[1] = top[1], i
    elif i >= top[0]:
        top[0] = i

    return top


FILE_NAME = "input_01.txt"

with open(FILE_NAME) as f:
    data = f.read()

sum_current = 0
sum_max = [0, 0, 0]

for line_no, line in enumerate(data.splitlines()):
    if line != "":
        i = int(line)
        sum_current += i
    else:
        sum_max = process_max(sum_current, sum_max)
        sum_current = 0

sum_max = process_max(i, sum_max)

print(f"Top three elves: {sum_max}")
print(f"Max Sum: {sum(sum_max)}")



