"""Day 4: Ceres Search (Part Two)

https://adventofcode.com/2024/day/4
"""


def count_x_words(data, current_row, current_col, word):
    max_col = len(data[current_row]) - 1

    if current_col == 0 or current_col == max_col:
        return 0

    # Primary diagonal
    text1 = ''.join(
        data[(current_row - 1) + x][(current_col - 1) + x]
        for x in range(len(word))
    )

    # Secondary diagonal
    text2 = ''.join(
        data[(current_row - 1) + x][(current_col + 1) - x]
        for x in range(len(word))
    )

    if (text1 == word or text1 == word[::-1]) and (
        text2 == word or text2 == word[::-1]
    ):
        return 1

    return 0


def main(file):
    data = file.readlines()
    word = 'MAS'
    total = 0

    for row in range(1, len(data) - 1):
        for col, letter in enumerate(data[row]):
            if letter == 'A':
                total += count_x_words(data, row, col, word)

    return total


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        result = main(file)
        print(result)
