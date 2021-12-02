#!/usr/bin/env python3

from common import read_file_to_str_list

if __name__ == '__main__':
    file_lines = read_file_to_str_list(2)
    # Part 1
    horizontal_position, depth = 0, 0
    for line in file_lines:
        direction, distance = line.split()
        if direction == 'forward':
            horizontal_position += int(distance)
        elif direction == 'down':
            depth += int(distance)
        else:
            depth -= int(distance)

    print(f'Final horizontal position * final depth = {horizontal_position * depth}')

    # Part 2
    horizontal_position, depth, aim = 0, 0, 0
    for line in file_lines:
        direction, distance = line.split()
        distance = int(distance)
        if direction == 'forward':
            horizontal_position += distance
            depth += (aim * distance)
        elif direction == 'down':
            aim += distance
        else:
            aim -= distance

    print(f'Final horizontal position * final depth = {horizontal_position * depth}')

