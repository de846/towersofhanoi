#!/usr/bin/env python3
import argparse

DEFAULT_NUM_DISCS = 8

class HanoiTower(object):
    def __init__(self, num_discs=DEFAULT_NUM_DISCS):
       self._col_left = []
       self._col_mid = []
       self._col_right = []
       self._num_discs = num_discs


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Towers of Hanoi")
    parser.add_argument('-n', '--num-discs', help='Number of discs until the universe ends')
    args = parser.parse_args()

