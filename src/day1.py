#!/usr/bin/env python3

from common import read_file_to_int_list

if __name__ == '__main__':
    file_lines = read_file_to_int_list(1)
    # Part 1
    total = 0
    last_num = 0
    for i, n in enumerate(file_lines):
        if i != 0 and n > last_num:
            total += 1
        last_num = n

    print(f'Depth measurement increases {total} times')
