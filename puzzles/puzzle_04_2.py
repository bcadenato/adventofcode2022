import re

FILE_INPUT = "input_04.txt"

with open(FILE_INPUT) as f:
    data = f.read()

def parse_asg(asg):
    s = re.findall(r"(\d*)-(\d*),(\d*)-(\d*)", asg)
    return (int(s[0][0]), int(s[0][1]), int(s[0][2]), int(s[0][3]))

def check_overlap(a_start, a_end, b_start, b_end):
    if (a_end >= b_start and b_end >= a_end) or\
       (b_end >= a_start and a_end >= b_end):
        return 1
    return 0

sum_overlaps = 0

for asg in data.splitlines():
    asg_a_start, asg_a_end, asg_b_start, asg_b_end = parse_asg(asg)
    overlap = check_overlap(asg_a_start, asg_a_end,
                            asg_b_start, asg_b_end)
    print(f"{asg} - Overlap = {overlap}")
    sum_overlaps += overlap

print(f"Total number of overlaps is {sum_overlaps}")

