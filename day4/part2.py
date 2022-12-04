from typing import Tuple


with open("input2.txt") as f:
    assignment_lines = f.read().split("\n")


total_reconsideration_count = 0


def get_numbers_from_assignment_line(assignment_line: str) -> Tuple[int, int]:
    return tuple(int(number) for number in assignment_line.split("-"))


for assignment_line in assignment_lines:
    assignment_pair = assignment_line.split(",")
    first_assignment, second_assignment = assignment_pair
    first_assignment_start, first_assignment_end = get_numbers_from_assignment_line(first_assignment)
    second_assignment_start, second_assignment_end = get_numbers_from_assignment_line(second_assignment)

    if first_assignment_end >= second_assignment_start and first_assignment_start <= second_assignment_end:
        total_reconsideration_count += 1

print(total_reconsideration_count)
