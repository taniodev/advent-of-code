"""Day 2: Red-Nosed Reports

https://adventofcode.com/2024/day/2
"""


def main(file):
    increasing = {1, 2, 3}
    decreasing = {-1, -2, -3}
    num_safe_reports = 0

    for line in file:
        report = [int(level) for level in line.split()]
        level_diffs = {
            report[x] - report[x - 1] for x in range(1, len(report))
        }

        if level_diffs <= increasing or level_diffs <= decreasing:
            num_safe_reports += 1

    return num_safe_reports


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        result = main(file)
        print(result)
