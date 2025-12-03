"""
Dial with numbers 0 through 99 in order
A rotation starts with an L or R which indicates whether 
    the rotation should be to the left (toward lower numbers) 
    or to the right (toward higher numbers)
Turning the dial left from 0 one click makes it point at 99
Turning the dial right from 99 one click makes it point at 0
The dial starts by pointing at 50
Password is the number of times the dial is left pointing at 0 
    after any rotation in the sequence
"""

from __future__ import annotations

class DialPosition:
    def __init__(self, prev: DialPosition, position: int, next: DialPosition):
        self.prev = prev
        self.position = position
        self.next = next

class Dial:
    def __init__(self, start: int):
        positions = []

        first_position = DialPosition(None, 0, None)
        current_position = first_position
        prev_position = current_position

        positions.append(current_position)

        for i in range(1,99):
            current_position = DialPosition(prev_position, i, None)
            positions[i-1].next = current_position
            prev_position = current_position

            positions.append(current_position)

        current_position = DialPosition(prev_position, 99, first_position)
        positions[98].next = current_position
        positions[0].prev = current_position

        positions.append(current_position)

        self.positions = positions
        self.current = start

    def turn(self, rotation: str):
        #apply rotation on self.current

def main():
    password = 0
    dial = Dial(50)

    with open("day_1_input.txt", mode="r", encoding="utf-8") as file:
        for line in file:
            rotation = line.strip()


main()

