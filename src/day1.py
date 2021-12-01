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

    # Part 2
    sum_blocks = 3
    total = 0
    for i in range(0, len(file_lines)):
        if i >= sum_blocks:
            last_block_start = i - sum_blocks
            last_block = file_lines[last_block_start : last_block_start + sum_blocks]
            last_sum = sum(last_block, 0)
            
            current_block_start = last_block_start + 1
            current_block = file_lines[current_block_start : current_block_start + sum_blocks]
            current_sum = sum(current_block, 0)

            if len(last_block) != 3 or len(current_block) != 3:
                break
            if current_sum > last_sum:
                total += 1

    print(f'Depth measurement sums increased {total} times')

