#!/usr/bin/env python
# coding: utf-8
"""
Synchronizes workouts in the ./data dir with the Trello board
"""
import os

__author__ = 'Theo Massard <massar_t@etna-alternance.net>'

TYPES = ('push', 'pull', 'leg')


def get_workout_type(fname):
    for workout_type in TYPES:
        if workout_type in fname:
            return (workout_type, fname)


def find_workouts(directory='./data'):
    """Returns a list of tuples

    (workout_type, workout_file)
    """
    for fname in os.listdir(directory):
        print(get_workout_type(fname))


def main():
    "Main function"
    find_workouts()


if __name__ == '__main__':
    main()
