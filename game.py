import random

options: str = [
	"rock",
	"paper",
	"scissors"
]


def declare_winner(winner: str) -> None:
	if winner == "player":
		print("You win!")
	elif winner == "bot":
		print("Bot wins!")
	else:
		print("Tie!")


choice: str = input("Choose Rock, Paper, or Scissors: ").lower()
bot_choice: str = options[random.randint(0, 2)]

print(f"Bot chose {bot_choice}")

if choice == options[0]:
	# Player chose rock
	if bot_choice == options[0]:
		declare_winner("")
	elif bot_choice == options[1]:
		declare_winner("bot")
	else:
		declare_winner("player")
elif choice == options[1]:
	# Player chose paper
	if bot_choice == options[0]:
		declare_winner("player")
	elif bot_choice == options[1]:
		declare_winner("")
	else:
		declare_winner("bot")
elif choice == "scissors":
	# Player chose scissors
	if bot_choice == options[1]:
		declare_winner("player")
	elif bot_choice == options[0]:
		declare_winner("bot")
	else:
		declare_winner("")
else:
	print("No choice selected")
