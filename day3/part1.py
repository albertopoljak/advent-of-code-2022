from string import ascii_letters

priorities = {letter: priority_index + 1 for priority_index, letter in enumerate(ascii_letters)}


with open("input1.txt") as f:
    rucksack_lines = f.readlines()


total_priority_sum = 0


for rucksack_line in rucksack_lines:
    half_index = len(rucksack_line) // 2
    compartement_left, compartement_right = rucksack_line[:half_index], rucksack_line[half_index:len(rucksack_line)]
    duplicate_characters = set(compartement_left).intersection(compartement_right)
    for character in duplicate_characters:
        total_priority_sum += priorities[character]


print(total_priority_sum)
