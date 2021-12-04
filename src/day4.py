#!/usr/bin/env python3

from common import read_file_to_str_list

if __name__ == '__main__':
    file_lines = read_file_to_str_list(4)
    # Part 1
    drawn_numbers = file_lines[0].split(',')

    boards = []
    num_rows = 0 # Total number of rows is num_rows
    num_boards = -1 # Total number of boards is num_boards + 1
    for line in file_lines[1:]:
        if line == '':
            num_rows = 0
            num_boards += 1
            boards.append([])
        else:
            boards[num_boards].append([n for n in line.split(' ') if n != ''])
            num_rows += 1

    def calculate_answer(b, n):
        unmarked_sum = 0
        for c in range(len(b[0])):
            for r in range(num_rows):
                if b[c][r] != '-1':
                    unmarked_sum += int(b[c][r])
        print(f'Final score: {unmarked_sum * int(n)}')

    def check_boards(boards):
        for b in boards:
            num_columns = len(b[0])
            for c in range(num_columns):
                marked_elements = 0
                for r in range(num_rows):
                    if b[c][r] == '-1':
                        marked_elements += 1

                if marked_elements == num_rows:
                    return (True, b)
            
            for r in range(num_rows):
                marked_elements = 0
                for c in range(num_columns):
                    if b[c][r] == '-1':
                        marked_elements += 1

                if marked_elements == num_columns:
                    return (True, b)

        return (False, )


    def draw_numbers():
        for n in drawn_numbers:
            for b in boards:
                for r in range(num_rows):
                    try:
                        i = b[r].index(n)
                        b[r][i] = '-1'
                        result = check_boards(boards)
                        if result[0]:
                            calculate_answer(result[1], n)
                            return 
                    except ValueError:
                        pass
        return

    draw_numbers()
