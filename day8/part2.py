import math
from collections import namedtuple
Direction = namedtuple("Direction", "x_offset y_offset")
top = Direction(0, 1)
right = Direction(1, 0)
down = Direction(0, -1)
left = Direction(-1, 0)
directions = top, right, down, left


def is_tree_outside_bounds(forest_data, tree_x_index, tree_y_index):
    return (
            tree_x_index < 0 or
            tree_y_index < 0 or
            tree_x_index > len(forest_data[0]) - 1 or
            tree_y_index > len(forest_data) - 1
    )


def get_tree_scenic_score_direction(
        forest_data, direction: Direction,
        current_x_index, current_y_index,
        tree_height: int, current_scenic_score: int
):
    current_x_index += direction.x_offset
    current_y_index += direction.y_offset

    if is_tree_outside_bounds(forest_data, current_x_index, current_y_index):
        return current_scenic_score

    if tree_height > forest_data[current_y_index][current_x_index]:
        current_scenic_score += 1
    elif tree_height <= forest_data[current_y_index][current_x_index]:
        return current_scenic_score + 1  # including the edge

    return get_tree_scenic_score_direction(
        forest_data, direction, current_x_index, current_y_index, tree_height, current_scenic_score
    )


def get_tree_scenic_score_total(forest_data, tree_x_index: int, tree_y_index: int):
    tree_height = forest_data[tree_y_index][tree_x_index]

    return math.prod(
        get_tree_scenic_score_direction(forest_data, direction, tree_x_index, tree_y_index, tree_height, 0)
        for direction in directions
    )


with open("input.txt") as f:
    data = tuple(tuple(int(height) for height in line) for line in f.read().split("\n"))


highest_scenic_score = 0
for y_index, tree_line in enumerate(data):
    for x_index in range(len(tree_line)):
        scenic_score = get_tree_scenic_score_total(data, x_index, y_index)
        if scenic_score > highest_scenic_score:
            highest_scenic_score = scenic_score


print(highest_scenic_score)
