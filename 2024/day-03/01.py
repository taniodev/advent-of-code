"""Day 3: Mull It Over

https://adventofcode.com/2024/day/3
"""
import re


def main(file):
    total = 0
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

    for line in file:
        values = re.findall(pattern, line)

        for pair in values:
            num1, num2 = pair
            total += int(num1) * int(num2)

    return total


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        result = main(file)
        print(result)
