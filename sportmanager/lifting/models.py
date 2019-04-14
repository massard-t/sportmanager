"""Lifting-related models."""
import datetime

from django.db import models


class Workout(models.Model):
    """A Workout model."""
    name = models.CharField(max_length=120)
    description = models.CharField(blank=True, max_length=120)
    date = models.DateTimeField(default=datetime.datetime.now)
     #_feelings = (
        # ('OK', 'ok'),
        # ('KO', 'ko'),
    # )
    # feelings = models.CharField(choices=_feelings)

    def __str__(self):
        _date = self.date.strftime("%d/%m/%Y")
        return '{} ({})'.format(self.name, self.date.isoformat())


class Set(models.Model):
    """Define a set composed of multiple reps."""
    reps_count = models.PositiveIntegerField('Repetition Count')
    rest_period = models.DurationField(default=datetime.time(minute=1, second=30))
    exercise = models.ForeignKey('Exercise', models.CASCADE)
    workout = models.ForeignKey('Workout', models.CASCADE)

    def __str__(self):
        return '{} [{}] (rest: {}s)'.format(self.exercise.base_exercise.name, self.reps_count, self.rest_period.total_seconds())


class Exercise(models.Model):
    """Define a set's exercise"""
    base_exercise = models.ForeignKey('BaseExercise', models.PROTECT)
    weight = models.DecimalField('Weight in kg', default=0, decimal_places=2, max_digits=10)

    def __str__(self):
        return '{} - ({}kg)'.format(self.base_exercise.name, self.weight)


class BaseExercise(models.Model):
    """Define an Exercise to add to the catalog."""
    name = models.CharField(default="Unnamed", max_length=120)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name.title()
