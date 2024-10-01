from getpass import getpass as input

player1_score = 0
player2_score = 0

while True:
	player_1 = input("Player 1, choose R, P or S: ").lower()
	player_2 = input("Player 2, choose R, P or S: ").lower()
	
	if player_1 == "r" and player_2 == "r":
		print("It's a tie!")
	elif player_1 == "r" and player_2 == "p":
		player2_score += 1
		print("Player 2 wins!")
	elif player_1 == "r" and player_2 == "s":
		player1_score += 1
		print("Player 1 wins!")
	elif player_1 == "p" and player_2 == "r":
		player1_score += 1
		print("Player 1 wins!")
	elif player_1 == "p" and player_2 == "p":
		print("It's a tie!")
	elif player_1 == "p" and player_2 == "s":
		player2_score += 1
		print("Player 2 wins!")
	elif player_1 == "s" and player_2 == "r":
		player2_score += 1
		print("Player 2 wins!")
	elif player_1 == "s" and player_2 == "p":
		player1_score += 1
		print("Player 1 wins!")
	elif player_1 == "s" and player_2 == "s":
		print("It's a tie!")
	else:
		print("Invalid input. Please try again.")

	if player1_score == 3:
		print("Player 1 Wins! Your score is ", player1_score)
		break
	elif player2_score == 3:
		print("Player 2 Wins! Your score is ", player2_score)
		exit()
	else:
		continue
