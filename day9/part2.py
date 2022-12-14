from typing import Set, Tuple, Optional
from dataclasses import dataclass, field


@dataclass
class Coordinate:
    x: int
    y: int

    def move(self, x: int, y: int):
        self.x += x
        self.y += y


@dataclass
class Move:
    moves_x: int
    moves_y: int

    def can_move(self):
        # does not support moving in both directions
        return self.moves_x != 0 or self.moves_y != 0

    def get_move_direction(self):
        direction_x, direction_y = 0, 0
        if self.moves_x > 0:
            self.moves_x -= 1
            direction_x += 1
        elif self.moves_y > 0:
            self.moves_y -= 1
            direction_y += 1

        if self.moves_x < 0:
            self.moves_x += 1
            direction_x -= 1
        elif self.moves_y < 0:
            self.moves_y += 1
            direction_y -= 1

        return direction_x, direction_y


@dataclass
class Knot(Coordinate):
    _head: Optional["Knot"]
    _passed_coordinates: Set[Tuple[int, int]] = field(default_factory=set)

    @property
    def passed_coordinates_length(self) -> int:
        self._passed_coordinates.add((0, 0))  # quick fix derp
        return len(self._passed_coordinates)

    def follow(self):
        if not self._head:
            raise NotImplemented("follow is not supported for head")

        if self.is_touching_head():
            return

        if self.x == self._head.x:
            if self.y < self._head.y:
                """
                012345
                ....H.
                ......
                ....T.
                """
                self.move(0, 1)
            elif self.y > self._head.y:
                """
                012345
                ....T.
                ......
                ....H.
                """
                self.move(0, -1)
        elif self.y == self._head.y:
            if self.x < self._head.x:
                """
                012345
                .T.H..
                """
                self.move(1, 0)
            elif self.x > self._head.x:
                """
                012345
                .H.T..
                """
                self.move(-1, 0)
        else:
            self._follow_directionally()

        self._passed_coordinates.add((self.x, self.y))

    def _follow_directionally(self):
        if self.x < self._head.x:
            if self.y < self._head.y:
                """
                012345
                ..H..
                .....
                .T...
                """
                self.move(1, 1)
            elif self.y > self._head.y:
                """
                012345
                ..T..
                ....H
                .....
                """
                self.move(1, -1)

        elif self.x > self._head.x:
            if self.y < self._head.y:
                """
                012345
                .....
                .H...
                ...T.
                """
                self.move(-1, 1)
            if self.y > self._head.y:
                """
                012345
                ...T.
                .H...
                .....
                """
                self.move(-1, -1)

    def is_touching_head(self) -> bool:
        if not self._head:
            return True

        surrounding_directions = (
            (-1, 1),  (0, 1),  (1, 1),
            (-1, 0),           (1, 0),
            (-1, -1), (0, -1), (1, -1)
        )

        for surrounding_direction in surrounding_directions:
            surrounding_direction_x, surrounding_direction_y = surrounding_direction
            if self.x + surrounding_direction_x == self._head.x and self.y + surrounding_direction_y == self._head.y:
                return True

        return False


class Solver:
    @classmethod
    def parse_move(cls, move_input: str) -> Tuple[int, int]:
        direction_symbol, move_steps_string = move_input.split(" ")
        move_steps = int(move_steps_string)
        moves_x, moves_y = 0, 0

        if direction_symbol == "U":
            moves_y += move_steps
        elif direction_symbol == "R":
            moves_x += move_steps
        elif direction_symbol == "D":
            moves_y -= move_steps
        elif direction_symbol == "L":
            moves_x -= move_steps

        return moves_x, moves_y

    @classmethod
    def solve(cls):
        with open("input1.txt") as f:
            moves_data = f.read().split("\n")

        head = Knot(0, 0, None)
        _previous_knot = head
        knots = []

        for _ in range(9):  # not ten because head is a knot?
            knot = Knot(0, 0, _previous_knot)
            knots.append(knot)
            _previous_knot = knot

        tail = knots[-1]

        for move_data in moves_data:
            move = Move(*cls.parse_move(move_data))
            while move.can_move():
                head.move(*move.get_move_direction())
                for knot in knots:
                    knot.follow()

        print(tail.passed_coordinates_length)


Solver().solve()
