#!/usr/bin/env python3

from common import read_file_to_str_list

if __name__ == '__main__':
    def get_overlapping_points_count(line_plots, include_diagonal_lines = False):
        plotted_points = {}
        for line in line_plots:
            x1, y1 = int(line[0][0]), int(line[0][1])
            x2, y2 = int(line[1][0]), int(line[1][1])
            if x1 == x2:
                step = 1 if y2 > y1 else -1
                for i in range(y1, y2 + step, step):
                    point = f'{x1},{i}'
                    if point in plotted_points:
                        plotted_points[point] += 1
                    else:
                        plotted_points[point] = 1
            elif y1 == y2:
                step = 1 if x2 > x1 else -1
                for i in range(x1, x2 + step, step):
                    point = f'{i},{y1}'
                    if point in plotted_points:
                        plotted_points[point] += 1
                    else:
                        plotted_points[point] = 1
            elif include_diagonal_lines:
                x_step = 1 if x2 > x1 else -1
                y_step = 1 if y2 > y1 else -1
                for i, _ in enumerate(range(x1, x2 + x_step, x_step)):
                    x = x1 + (i * x_step)
                    y = y1 + (i * y_step)
                    point = f'{x},{y}'
                    if point in plotted_points:
                        plotted_points[point] += 1
                    else:
                        plotted_points[point] = 1

        return len([v for v in plotted_points.values() if v > 1])

    def get_pair(line):
        first_pair_end = line.index(' ') # ' '
        second_pair_start = first_pair_end + 4 # x
        return (line[:first_pair_end].split(','), line[second_pair_start::].split(','))
    
    file_lines = read_file_to_str_list(5)
    line_plots = [get_pair(line) for line in file_lines]
    
    # Part 1
    print(f'Number of overlapping points: {get_overlapping_points_count(line_plots)}')
    
    # Part 2
    print(f'Number of overlapping points (including diagonal lines): {get_overlapping_points_count(line_plots, True)}')
                   
