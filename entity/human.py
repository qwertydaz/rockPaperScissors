from entity.player import Player
from enums.choice import Choice


class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose(self, choice):
        if type(choice) is int:
            choice = Choice(choice)
        elif not isinstance(choice, Choice):
            raise TypeError("choice must be a Choice enum")

        self.choice = choice
