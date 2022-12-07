with open("input.txt") as f:
    datastream = f.read()


def read_next_n(start_index: int, n: int, data: str) -> str:
    return data[start_index: start_index+n]


def solve_for_marker_length(marker_length):
    for char_index in range(len(datastream)):
        possible_marker = read_next_n(char_index, marker_length, datastream)
        if len(set(possible_marker)) == len(possible_marker) and len(possible_marker) == marker_length:
            print(possible_marker, "character at", char_index + marker_length)
            break
