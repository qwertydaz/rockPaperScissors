from random import Random
from entity.player import Player
from enums.choice import Choice


class CPU(Player):

    def __init__(self):
        super().__init__("CPU")
        self.random = Random()

    def choose(self, num_choices):
        self.choice = Choice(self.random.randint(1, num_choices))
