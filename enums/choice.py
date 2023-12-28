from enum import Enum


class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
