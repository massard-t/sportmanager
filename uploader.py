#!/usr/bin/env python
# coding: utf-8
"""
Synchronizes workouts in the ./data dir with the Trello board
"""
import os
from collections import namedtuple

__author__ = 'Theo Massard <massar_t@etna-alternance.net>'


TYPES = ('push', 'pull', 'leg')
Workout = namedtuple('Workout', ['w_type', 'w_day', 'w_name', 'w_data'])


def get_workout_type(fname):
    """Associates a filename to a workout type"""
    for workout_type in TYPES:
        if workout_type in fname:
            content = open(fname, 'r').read().split('\n')
            workout_nbr = fname.replace(workout_type, '')
            workout = Workout(
                w_type=workout_type,
                w_day=content[0],
                w_name=workout_type+workout_nbr,
                w_data='\n'.join(content[1:])
                )
            return workout


def find_workouts(directory='./data/'):
    """Returns a list of tuples

    (workout_type, workout_file)
    """
    workouts = [get_workout_type(directory+fname) for fname in os.listdir(directory)]
    print(workouts)


def main():
    "Main function"
    find_workouts()


if __name__ == '__main__':
    main()
