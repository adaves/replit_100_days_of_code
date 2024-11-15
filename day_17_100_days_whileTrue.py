# day_17_100_days_paperRockScissors


def get_player_choice(player_num):
    """This function take in the players_num and returns each players choice."""
    while True:
        choice = input(f"Player {player_num}, choose R, P, or S: ").lower()
        if choice in ["r", "s", "p"]:
            return choice
        print("Invalid input, please choose R, P, or S.")


def determine_winner(player_1, player_2):
    """This function returns who wins the match"""
    if player_1 == player_2:
        return "tie"
    elif (
        (player_1 == "r" and player_2 == "s")
        or (player_1 == "p" and player_2 == "r")
        or (player_1 == "s" and player_2 == "p")
    ):
        return "player_1"
    else:
        return "player_2"


def print_winner(winner):
    """This function prints who wins the game."""
    if winner == "tie":
        print("Its a tie")
    elif winner == "player_1":
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")


# initialize players scores
player1_score = 0
player2_score = 0

while True:
    player_1 = get_player_choice(1)
    player_2 = get_player_choice(2)

    winner = determine_winner(player_1, player_2)
    print_winner(winner)

    if winner == "player_1":
        player1_score += 1
    elif winner == "player_2":
        player2_score += 1

    if player1_score == 3:
        print(f"Player 1 Wins, the score is {player1_score}")
        break
    elif player2_score == 3:
        print(f"Player 2 Wins, the score is {player2_score}")
        break
