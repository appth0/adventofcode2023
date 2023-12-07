import re

def parse_table():
    file1 = open('input.txt', 'r')
    content = file1.readlines()
    return [list(x) for x in content]


def is_adjacent_to_symbol(table, row_i, col_i):
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            r = row_i+i
            c = col_i+j
            if r >=0 and c >= 0 and r < len(table) and c < len(table[r]):
                if not table[r][c].isnumeric() and table[r][c] != '.' and table[r][c] != '\n':
                    return True
    return False


def get_numbers_with_index_in_row(row_str):
    row_str = re.sub("[^0-9]", ".", row_str)
    result = []
    i = 0
    while i < len(row_str):
        char = row_str[i]
        index = i+1
        if char.isnumeric():
            while index < len(row_str) and row_str[index].isnumeric():
                index += 1
            num = row_str[i:index]
            result.append((int(num), i))
            i = index
        i += 1
    return result


table = parse_table()

file1 = open('input.txt', 'r')
content = file1.readlines()
result_nums = []

for i, line in enumerate(content):
    numbers_in_row = get_numbers_with_index_in_row(line)

    for num, index in numbers_in_row:
        length = len(str(num))
        for j in range(index, index+length):
            if is_adjacent_to_symbol(table, i, j):
                result_nums.append(int(num))
                break

print(sum(result_nums))

