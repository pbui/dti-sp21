#!/usr/bin/env python3

'''
TOPIC:      Stack
DIFFICULTY: Easy
SOURCE:     https://leetcode.com/problems/simplify-path/
STORY:      Students learning about Unix filesystems...
'''

import sys

# Functions

def canonical_path(s):
    path = []

    for token in s.split('/'):
        if path and token == '..':
            path.pop(-1)
        elif not token in ('', '.', '..'):
            path.append(token)

    return '/' + '/'.join(path)

# Main Execution

def main():
    for line in sys.stdin:
        print(canonical_path(line.strip()))

if __name__ == '__main__':
    main()
