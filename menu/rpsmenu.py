from menu.menutemplate import MenuTemplate
from constant.rpsmenuconstants import RpsMenuConstants


class RpsMenu(MenuTemplate):
    def __init__(self):
        super().__init__(
            "\n" + RpsMenuConstants.TITLE,
            RpsMenuConstants.DIVIDER,
            [
                RpsMenuConstants.ROCK,
                RpsMenuConstants.PAPER,
                RpsMenuConstants.SCISSORS
            ],
            RpsMenuConstants.EXIT
        )
