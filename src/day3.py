#!/usr/bin/env python3

from common import read_file_to_str_list

if __name__ == '__main__':
    file_lines = read_file_to_str_list(3)
    bits_range = range(len(file_lines[0]))

    def get_bits_count(file_lines):
        bits_count = [[0, 0] for i in bits_range]
        for i in bits_range:
            for line in file_lines:
                bits_count[i][int(line[i])] += 1
        return bits_count


    # Part 1
    bits_count = get_bits_count(file_lines)

    common_bits = []
    for i in bits_range:
        common_bits.append('0' if bits_count[i][0] > bits_count[i][1] else '1')

    gamma_rate = ''.join(common_bits)
    print(f'Calculated gamma rate is: {gamma_rate}')

    epsilon_rate = ''.join(['1' if i == '0' else '0' for i in gamma_rate])
    print(f'Calculated epsilon rate is: {epsilon_rate}')

    print(f'Calculated power consumption is: {int(gamma_rate, 2) * int(epsilon_rate, 2)}')

    # Part 2
    def get_rating(file_lines, predicate):
        lines = file_lines
        for i in bits_range:
            # Get bits_count in each iteration
            bits_count = get_bits_count(lines)
            bit = predicate(bits_count, i)
            valid_lines = [line for line in lines if line[i] == bit]
            lines = valid_lines
            if len(lines) == 1:
                break
        return lines[0]


    def oxygen_predicate(bits_count, i):
        return '1' if bits_count[i][1] >= bits_count[i][0] else '0'


    def co2_predicate(bits_count, i):
        return '0' if bits_count[i][0] <= bits_count[i][1] else '1'


    oxygen_generator_rating = ''.join(get_rating(file_lines, oxygen_predicate))
    co2_scrubber_rating = ''.join(get_rating(file_lines, co2_predicate))

    print(f'Ratings found: oxygen: {oxygen_generator_rating}, CO2: {co2_scrubber_rating}')

    print(f'Calculated life support rating: {int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)}')

