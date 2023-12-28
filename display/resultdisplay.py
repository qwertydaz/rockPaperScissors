from constant.resultdisplayconstants import ResultDisplayConstants
from display.displaytemplate import DisplayTemplate
from entity.player import Player


class ResultDisplay(DisplayTemplate):
    def __init__(self, result, players):
        if not isinstance(result, Player) and result is not None:
            raise TypeError("result must be a player or None")
        if not all(isinstance(player, Player) for player in players):
            raise TypeError("players must be a list of players")

        self.result = result
        self.players = players

        choice1 = ResultDisplayConstants.INLINE_DIVIDER.format(players[0].name, players[0].choice)
        choice2 = ResultDisplayConstants.INLINE_DIVIDER.format(players[1].name, players[1].choice)

        if result is None:
            super().__init__(
                "\n" + ResultDisplayConstants.TITLE,
                ResultDisplayConstants.DIVIDER,
                [
                    choice1,
                    choice2,
                    "\n" + ResultDisplayConstants.TIE
                ]
            )
            return

        winner = ResultDisplayConstants.WINS.format(result.name)

        super().__init__(
            "\n" + ResultDisplayConstants.TITLE,
            ResultDisplayConstants.DIVIDER,
            [
                choice1,
                choice2,
                "\n" + winner
            ]
        )
