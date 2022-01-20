#!/usr/bin/env python
import argparse


if __name__ == '__main__':

    # parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--maze-file', '-m',
        required=True,
        help='The .csv file containing the maze data.')

    args = parser.parse_args()

