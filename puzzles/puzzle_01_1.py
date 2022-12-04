file_name = "input_01.txt"

with open(file_name) as f:
    data = f.read()

sum_current = 0
sum_max = 0

for line_no, line in enumerate(data.splitlines()):
    if line != "":
        i = int(line)
        print(f"Line {line_no} Calories {i}")
        sum_current += i
        print(f"Line {line_no} Sum Current {sum_current}")
    else:
        print(f"Elf {line_no}: Current Sum: {sum_current}")
        sum_max = max(sum_max, sum_current)
        sum_current = 0

sum_max = max(sum_max, sum_current)

print(f"Max Sum: {sum_max}")



