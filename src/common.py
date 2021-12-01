#!/usr/bin/env python3

def read_file_to_int_list(n):
    with open(f'../inputs/day{n}.txt', 'r') as inputFile:
        file_lines = [int(line) for line in inputFile]
    return file_lines

def read_file_to_str_list(n):
    with open(f'../inputs/day{n}.txt', 'r') as inputFile:
        file_lines = [line.replace('\n', '') for line in inputFile]
    return file_lines
            
