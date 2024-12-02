"""Day 1: Historian Hysteria (Part Two)

https://adventofcode.com/2024/day/1
"""


def main(file):
    left_list = []
    right_list_repetitions = {}
    similarity_score = 0

    for line in file:
        left, right = line.split()
        left_list.append(int(left))
        right_number = int(right)

        if right_number not in right_list_repetitions:
            right_list_repetitions[right_number] = 1
            continue

        right_list_repetitions[right_number] += 1

    for number in left_list:
        if number in right_list_repetitions:
            similarity_score += number * right_list_repetitions[number]

    return similarity_score


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        result = main(file)
        print(result)
