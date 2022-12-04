from string import ascii_letters

priorities = {letter: priority_index + 1 for priority_index, letter in enumerate(ascii_letters)}


with open("input2.txt") as f:
    rucksack_lines = f.read().split("\n")

_group_temporal = []
rucksack_groups = []


for line_index, rucksack_line in enumerate(rucksack_lines):
    _group_temporal.append(rucksack_line)

    if (line_index + 1) % 3 == 0 and line_index > 0:
        rucksack_groups.append(_group_temporal)
        _group_temporal = []


total_priority_sum = 0


for rucksack_group in rucksack_groups:
    line_one, line_two, line_three = rucksack_group
    duplicate_characters = set(line_one).intersection(set(line_two)).intersection(set(line_three))
    for character in duplicate_characters:
        total_priority_sum += priorities[character]


print(total_priority_sum)
