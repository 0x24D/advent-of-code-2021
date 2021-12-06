#!/usr/bin/env python3

from common import read_file_to_str_list

if __name__ == '__main__':    
    file_lines = read_file_to_str_list(6)
    # Part 1
    internal_timers = [int(i) for i in file_lines[0].split(',')]
    reset_length = 7
    new_days_extra = 2

    for d in range(80):
        timers_at_start_of_day = internal_timers
        for i, t in enumerate(timers_at_start_of_day):
            if t == 0:
                internal_timers[i] = reset_length
                internal_timers.append(reset_length + new_days_extra)
            internal_timers[i] -= 1

    print(f'Number of lanternfish after 80 days: {len(internal_timers)}')
                
