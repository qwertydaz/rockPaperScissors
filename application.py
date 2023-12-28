from display.resultdisplay import ResultDisplay
from entity.cpu import CPU
from entity.human import Human
from menu.rpsmenu import RpsMenu
from constant.menuconstants import MenuConstants
from util.rpsutil import get_winner

if __name__ == "__main__":
    human = Human("Dáire")
    cpu = CPU()
    rps_menu = RpsMenu()
    round_count = 1

    print(MenuConstants.DIVIDER)
    print(MenuConstants.TITLE)
    print(MenuConstants.DIVIDER)

    # TODO: add main menu and pvp
    while True:
        print("\n\n" + MenuConstants.LONG_DIVIDER)
        print(MenuConstants.ROUND.format(round_count))
        round_count += 1

        # shows rock paper scissors menu
        rps_menu.show()
        choice = rps_menu.get_choice()

        # exits if user chooses 0
        if choice == 0:
            break

        # saves choices
        human.choose(choice)
        cpu.choose(rps_menu.num_of_options())

        # gets winner
        winner = get_winner(human, cpu)

        # shows winner
        ResultDisplay(winner, [human, cpu]).show()
