"""Day 2: Red-Nosed Reports (Part Two)

https://adventofcode.com/2024/day/2
"""


def is_safe(report):
    increasing = {1, 2, 3}
    decreasing = {-1, -2, -3}
    differences = {report[x] - report[x - 1] for x in range(1, len(report))}

    if differences <= increasing or differences <= decreasing:
        return True


def main(file):
    num_safe_reports = 0

    for line in file:
        report = [int(level) for level in line.split()]

        for index in range(len(report)):
            tmp_report = report[:index] + report[index + 1 :]

            if is_safe(tmp_report):
                num_safe_reports += 1
                break

    return num_safe_reports


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        result = main(file)
        print(result)
