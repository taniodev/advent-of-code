"""Day 4: Ceres Search

https://adventofcode.com/2024/day/4
"""


def count_words(data, current_row, current_col, word):
    max_row = len(data) - 1
    max_col = len(data[current_row]) - 1

    # Search to the right
    text = data[current_row][current_col : current_col + len(word)]

    if current_row + len(word) - 1 > max_row:
        return text.count(word)

    # Down
    text += ''.join(
        data[current_row + x][current_col] for x in range(len(word))
    )

    # Down left
    if current_col - (len(word) - 1) >= 0:
        text += ''.join(
            data[current_row + x][current_col - x] for x in range(len(word))
        )

    # Down right
    if current_col + (len(word) - 1) <= max_col:
        text += ''.join(
            data[current_row + x][current_col + x] for x in range(len(word))
        )

    return text.count(word)


def main(file):
    data = file.readlines()
    word = 'XMAS'
    total = 0

    for row, content in enumerate(data):
        for col, letter in enumerate(content):
            if letter == word[0]:
                total += count_words(data, row, col, word)

            if letter == word[-1]:
                total += count_words(data, row, col, word[::-1])

    return total


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        result = main(file)
        print(result)
