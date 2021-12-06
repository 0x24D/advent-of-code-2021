#!/usr/bin/env python3

from common import read_file_to_str_list

if __name__ == '__main__':    
    file_lines = read_file_to_str_list(6)
    # Part 1
    def part1(file_lines):
        internal_timers = [int(i) for i in file_lines[0].split(',')]
        reset_length = 7
        new_days_extra = 2

        num_days = 80
        for d in range(num_days):
            timers_at_start_of_day = internal_timers
            for i, t in enumerate(timers_at_start_of_day):
                if t == 0:
                    internal_timers[i] = reset_length
                    internal_timers.append(reset_length + new_days_extra)
                internal_timers[i] -= 1

        print(f'Number of lanternfish after {num_days} days: {len(internal_timers)}')

    part1(file_lines)

    # Part 2
    def part2(file_lines):
        internal_timers = [int(i) for i in file_lines[0].split(',')]
        reset_length = 7
        new_days_extra = 2
        max_days = reset_length + new_days_extra
        fish_counts = {i : 0 for i in range(max_days + 1)}
        for i in internal_timers:
            fish_counts[i] += 1

        num_days = 256
        for d in range(num_days):
            for i in range(max_days + 1):
                count = fish_counts[i]
                if i == 0:
                    # Move all 0-fish to reset_length and add an additional one to max_days - 1.
                    fish_counts[max_days] += count
                    fish_counts[reset_length] += count
                    fish_counts[0] = 0
                else:
                    # Decrease fishes' timers by one.
                    fish_counts[i - 1] += count
                    fish_counts[i] -= count

        print(f'Number of lanternfish after {num_days} days: {sum(fish_counts.values())}')

    part2(file_lines)

