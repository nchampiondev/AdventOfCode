"""
each line of digits in your input corresponds to a single bank of batteries
The batteries are each labeled with their joltage rating, a value from 1 to 9
you need to turn on exactly two batteries
the joltage that the bank produces is equal to the number formed by the digits on the batteries you've turned on
find the largest possible joltage each bank (two largest from left to right)
In 987654321111111, you can make the largest joltage possible, 98
In 818181911112111, the largest joltage you can produce is 92
The total output joltage is the sum of the maximum joltage from each bank
what is the total output joltage?
"""

from __future__ import annotations

def getBankOutput(bank: str):
    battery_val = 0
    max_val_1 = 0
    max_val_2 = 0
    max_index_1 = 0
    max_index_2 = 0
    bank_length = len(bank)

    for battery_index in range(0, bank_length):
        battery_val = int(bank[battery_index])
        if battery_index < bank_length-1 and battery_val > max_val_1:
            max_val_2 = max_val_1
            max_index_2 = max_index_1
            max_val_1 = battery_val
            max_index_1 = battery_index
        elif battery_val == max_val_1 or battery_val > max_val_2:
            max_val_2 = battery_val
            max_index_2 = battery_index
        if max_index_1 >= max_index_2:
            max_val_2 = battery_val
            max_index_2 = battery_index

    output = str(max_val_1) + str(max_val_2)

    print(f"{bank} {output}")

    return int(output)

def main():
    total_output = 0

    with open("day_3_input.txt", mode="r", encoding="utf-8") as file:
        for line in file:
            bank = line.strip()
            total_output += getBankOutput(bank)

    print(total_output)

main()