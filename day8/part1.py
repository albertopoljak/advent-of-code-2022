from collections import namedtuple
Direction = namedtuple("Direction", "x_offset y_offset")
top = Direction(0, 1)
right = Direction(1, 0)
down = Direction(0, -1)
left = Direction(-1, 0)
directions = top, right, down, left


def is_tree_on_edge(forest_data, tree_x_index, tree_y_index):
    return (
            tree_x_index == 0 or
            tree_y_index == 0 or
            tree_x_index == len(forest_data[0]) - 1 or
            tree_y_index == len(forest_data) - 1
    )


def is_tree_visible_from_direction(forest_data, direction: Direction, current_x_index, current_y_index, tree_height):
    current_x_index += direction.x_offset
    current_y_index += direction.y_offset

    if is_tree_on_edge(forest_data, current_x_index, current_y_index):
        return tree_height > forest_data[current_y_index][current_x_index]
    elif tree_height <= forest_data[current_y_index][current_x_index]:
        return False
    else:
        return is_tree_visible_from_direction(forest_data, direction, current_x_index, current_y_index, tree_height)


def is_tree_visible(forest_data, tree_x_index: int, tree_y_index: int):
    tree_height = forest_data[tree_y_index][tree_x_index]

    if is_tree_on_edge(forest_data, tree_x_index, tree_y_index):
        return True

    return any(
        is_tree_visible_from_direction(forest_data, direction, tree_x_index, tree_y_index, tree_height)
        for direction in directions
    )


with open("input.txt") as f:
    data = tuple(tuple(int(height) for height in line) for line in f.read().split("\n"))


total = 0
for y_index, tree_line in enumerate(data):
    for x_index in range(len(tree_line)):
        if is_tree_visible(data, x_index, y_index):
            total += 1


print(total)
