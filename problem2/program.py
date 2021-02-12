#!/usr/bin/env python3

'''
TOPIC:      Sorting / Map
DIFFICULTY: Medium
SOURCE:     https://leetcode.com/problems/rank-teams-by-votes/
STORY:      US voters want to move to rank choice voting after 2020 election...
'''

import collections
import functools
import sys

# Constants

MAX_VOTES = 1000

# Functions

def count_votes(votes):
    ''' Count votes for each candidate: { candidate : { rank : count } } '''
    candidates = collections.defaultdict(lambda: collections.defaultdict(int))

    for vote in votes:
        for rank, candidate in enumerate(vote, 1):
            candidates[candidate][rank] += 1

    return candidates

def cmp(a, b):
    ''' https://docs.python.org/3.0/whatsnew/3.0.html#ordering-comparisons '''
    return (a > b) - (a < b)

def compare_candidates(a, b):
    ''' Compare votes for each candidate by rank and then tie-break by name '''
    a_name, a_count = a
    b_name, b_count = b

    for rank in range(1, MAX_VOTES + 1):
        if a_count.get(rank, 0) != b_count.get(rank, 0):
            return b_count.get(rank, 0) - a_count.get(rank, 0)  # Descending order

    return cmp(a_name, b_name) # Ascending order

def sort_candidates(candidates):
    key_func = functools.cmp_to_key(compare_candidates)
    return [c[0] for c in sorted(candidates.items(), key=key_func)]

# Main Execution

def main():
    for line in sys.stdin:
        candidates = count_votes(line.split())
        winners    = sort_candidates(candidates)
        print(''.join(winners))

if __name__ == '__main__':
    main()
