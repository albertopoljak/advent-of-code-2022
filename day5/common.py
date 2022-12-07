import re


INPUT_CRATE_START_INDEX = 1
INPUT_CRATE_STEP_INDEX = 4
EMPTY_CRATE = " "


with open("input1_crates.txt") as f:
    lines = f.read().split("\n")


height = len(lines)
width = round(len(lines[-1]) / INPUT_CRATE_STEP_INDEX)
# leftmost list represents bottom
visual_crates = [[] for _ in range(height)]


for height_index, line_level in enumerate(reversed(lines)):
    for crate_index in range(INPUT_CRATE_START_INDEX, width * INPUT_CRATE_STEP_INDEX, INPUT_CRATE_STEP_INDEX):
        try:
            visual_crates[height_index].append(line_level[crate_index])
        except IndexError:
            # File input can be missing spaces at the end of the row, so we'll get index error. Treat as empty crate.
            visual_crates[height_index].append(EMPTY_CRATE)


# Now that we have visual matrix, we will inverse it to get crate stacks
crate_stacks = [[] for _ in range(width)]
for height_index, line_level in enumerate(visual_crates):
    for width_index, crate in enumerate(line_level):
        if crate == EMPTY_CRATE:
            continue

        crate_stacks[width_index].append(crate)


with open("input1_moves.txt") as f:
    move_list_inputs = f.read().split("\n")


move_pattern = re.compile(r"\d+")
move_list_commands = []  # list of lists containing 3 numbers
for move_list_input in move_list_inputs:
    move_list_commands.append([int(number) for number in move_pattern.findall(move_list_input)])
