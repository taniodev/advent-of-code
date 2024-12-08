"""Day 3: Mull It Over (Part Two)

https://adventofcode.com/2024/day/3
"""
import re


def main(file):
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))")
    total = 0
    enabled = True

    for line in file:
        for num1, num2, do, donot in pattern.findall(line):
            if do or donot:
                enabled = bool(do)

            if enabled and num1 and num2:
                total += int(num1) * int(num2)

    return total


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        result = main(file)
        print(result)
