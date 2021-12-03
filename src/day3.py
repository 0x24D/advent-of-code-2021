#!/usr/bin/env python3

from common import read_file_to_str_list

if __name__ == '__main__':
    file_lines = read_file_to_str_list(3)
    # Part 1
    bits_range = range(len(file_lines[0]))
    bits_count = [[0, 0] for i in bits_range]
    for i in bits_range:
        for line in file_lines:
            bits_count[i][int(line[i])] += 1

    common_bits = []
    for i in bits_range:
        common_bits.append('0' if bits_count[i][0] > bits_count[i][1] else '1')

    gamma_rate = ''.join(common_bits)
    print(f'Calculated gamma rate is: {gamma_rate}')

    epsilon_rate = ''.join(['1' if i == '0' else '0' for i in gamma_rate])
    print(f'Calculated epsilon rate is: {epsilon_rate}')

    print(f'Calculated power consumption is: {int(gamma_rate, 2) * int(epsilon_rate, 2)}')

