#!/usr/bin/env python3

from common import read_file_to_int_list

def calculate_sum(num_list, block_size):
    total = 0
    for i in range(0, len(num_list)):
        if i >= block_size:
            last_block_start = i - block_size
            last_block = num_list[last_block_start : last_block_start + block_size]
            last_sum = sum(last_block, 0)
            
            current_block_start = last_block_start + 1
            current_block = num_list[current_block_start : current_block_start + block_size]
            current_sum = sum(current_block, 0)

            if len(last_block) != block_size or len(current_block) != block_size:
                break
            if current_sum > last_sum:
                total += 1

    return total


if __name__ == '__main__':
    file_lines = read_file_to_int_list(1)
    # Part 1
    total = calculate_sum(file_lines, 1)
    print(f'Depth measurement increases {total} times')

    # Part 2
    total = calculate_sum(file_lines, 3)
    print(f'Depth measurement sums increased {total} times')

