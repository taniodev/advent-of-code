"""Day 1: Historian Hysteria

https://adventofcode.com/2024/day/1
"""


def main(file):
    left_list = []
    right_list = []
    total_distance = 0

    for line in file:
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))

    left_list.sort()
    right_list.sort()

    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)

    return total_distance


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        result = main(file)
        print(result)
