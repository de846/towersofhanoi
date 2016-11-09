#!/usr/bin/env python3
import argparse

DEFAULT_NUM_DISCS = 4

class HanoiTower(object):
    def __init__(self, num_discs, verbose=False):
        """
        Construct a new Hanoi Tower with 3 columns. Always assume our left column is our starting column
        :param num_discs: int of number of discs
        """
        self._col_left = []
        self._col_mid = []
        self._col_right = []
        self._num_discs = num_discs
        self._num_moves = 0
        self._chatty = verbose
        for i in range(self._num_discs, 0, -1):
            self._col_left.append(i)

    def _move(self, n, src, dest, slack):
        """
        Recursive-intended function to move discs from one column to another column.
        :param n: num discs, or depth of disc stack to operate at
        :param src: peg to move disc from
        :param dest: peg to move disc to
        :param slack: slack peg to move intermediary disc to
        :return: None
        """
        if n != 0:
            self._move(n - 1, src, slack, dest) # recursive case
            if self._chatty:
                print("#{}: Moving disc {} from top of {} to top of {}".format(self._num_moves + 1, n, src, dest))
            dest.append(src.pop()) # base case
            self._num_moves += 1
            self._move(n - 1, slack, dest, src) # recursive case


    def move_discs(self):
        if self._chatty:
            print("Starting Peg: {}".format(self._col_left))
            print("Destination Peg: {}".format(self._col_mid))
        self._move(self._num_discs, self._col_left, self._col_mid, self._col_right)
        print("Tower with {} discs solved in {} moves".format(self._num_discs, self._num_moves))
        if self._chatty:
            print("Starting Peg: {}".format(self._col_left))
            print("Destination Peg: {}".format(self._col_mid))

    def moves(self):
        return self._num_moves


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Towers of Hanoi")
    parser.add_argument('-n', '--num-discs', help='Number of discs until the universe ends', required=False, \
                        default=DEFAULT_NUM_DISCS, type=int)
    parser.add_argument('-v', '--verbose', action='store_true', help='Show moves')
    args = parser.parse_args()
    discs = args.num_discs

    tower = HanoiTower(discs, args.verbose)
    tower.move_discs()
