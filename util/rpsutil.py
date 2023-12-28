from enums.choice import Choice

winning_combos = {
    (Choice.ROCK, Choice.SCISSORS),
    (Choice.SCISSORS, Choice.PAPER),
    (Choice.PAPER, Choice.ROCK)
}


def get_winner(player1, player2):
    if player1.choice == player2.choice:
        return None

    if (player1.choice, player2.choice) in winning_combos:
        return player1

    return player2
