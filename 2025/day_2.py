"""
find the invalid IDs by looking for any ID 
    which is made only of some sequence of digits repeated twice. 
So, 55 (5 twice), 
    6464 (64 twice), and 
    123123 (123 twice) would all be invalid IDs.
None of the numbers have leading zeroes; 0101 isn't an ID at all. 101 is a valid ID that you would ignore.
Your job is to find all of the invalid IDs that appear in the given ranges.

What do you get if you add up all of the invalid IDs ?
"""

# split the str in half and check if both str equal

from __future__ import annotations

class IdRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

def main():
    with open("day_2_input.txt", mode="r", encoding="utf-8") as file:
        id_input = file.read().strip().split(",")

    result = 0
    for id_range in id_input:
        tmp = id_range.split("-")
        r = IdRange(int(tmp[0]), int(tmp[1]))
        for i in range(r.start, r.end+1):
            s = str(i)
            mid = len(s) // 2
            left = s[:mid]
            right = s[mid:]
            if left == right:
                result += i
    
    print(result)

main()