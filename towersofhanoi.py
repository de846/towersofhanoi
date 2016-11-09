#!/usr/bin/env python3
import argparse

DEFAULT_NUM_DISCS = 8

class HanoiTower(object):
    def __init__(self, num_discs=DEFAULT_NUM_DISCS):
       self._col_left = []
       self._col_mid = []
       self._col_right = []
       self._num_discs = num_discs
       for i in range(self._num_discs, 0, -1):
           self._col_left.append(i)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Towers of Hanoi")
    parser.add_argument('-n', '--num-discs', help='Number of discs until the universe ends', default=DEFAULT_NUM_DISCS, type=int)
    args = parser.parse_args()

    tower = HanoiTower(args.num_discs)
    print(tower._col_left)

