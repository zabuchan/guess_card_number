import random

PLAYER_NUMBER = 3
CARDS_PER_PLAYER = 7
HIDDEN_CARDS = 7


# Todo: Create Test file
# Todo: Add function of Computer's turn
# Todo: GUI Interface

class Card:
	init_cards = [1,
	              2, 2,
	              3, 3, 3,
	              4, 4, 4, 4,
	              5, 5, 5, 5, 5,
	              6, 6, 6, 6, 6, 6,
	              7, 7, 7, 7, 7, 7, 7]

	@classmethod
	def show_init_cards(cls):
		return cls.init_cards


class Player:
	def __init__(self, name):
		self._name = name
		self._my_cards = []

	def __len__(self):
		return len(self._my_cards)

	def __getitem__(self, position):
		return self._my_cards[position]

	def __delitem__(self, key):
		self._my_cards.remove(key)

	@property
	def name(self):
		return self._name

	@property
	def cards(self):
		return self._my_cards

	def show_cards(self):
		return "{} Cards: {}".format(self.name, self._my_cards)

	def shuffle_cards(self):
		self._my_cards = random.sample(Card.init_cards, CARDS_PER_PLAYER)

		for card in self._my_cards:
			if card in Card.init_cards:
				Card.init_cards.remove(card)

	def remove_card(self, card):
		self._my_cards.remove(card)


class Game:
	turn = 1

	def __init__(self):
		pass

	def add_player(self, name):
		return Player(name)

	@classmethod
	def show_turn(cls):
		return cls.turn

	@classmethod
	def increment_turn(cls):
		cls.turn += 1


class Table(Player):
	turn = 1

	def __init__(self, name):
		super().__init__(name)

	def add_card(self, card):
		self._my_cards.append(card)


def main():
	print_header()

	game = Game()

	player1 = game.add_player('me')
	player2 = game.add_player('Computer1')
	player3 = game.add_player('Computer2')
	table = Table('Table')

	player1.shuffle_cards()
	player2.shuffle_cards()
	player3.shuffle_cards()

	while True:
		print("Turn {}:".format(Game.show_turn()))
		print("-------------------------------------------")
		print_card_hidden(player1.name, len(player1.cards))
		print(player2.show_cards())
		print(player3.show_cards())
		print_card_hidden('Unknown Cards: ', HIDDEN_CARDS)
		print(table.show_cards())

		print()
		choice = input("Your Turn: Guess the card number you have: ")
		# if not is_valid(choice):
		# 	exit()
		choice = int(choice.strip())
		print(choice)
		if choice in player1.cards:
			print("It is included in your cards!!!!!")
			print()
			player1.remove_card(choice)
			table.add_card(choice)
		else:
			print("Incorrect!!! Your guess was wrong!!")
			print()
		if not player1.cards:
			print("You Win!!!!!!!!!!!!!!!!!!!!!!")

		Game.increment_turn()


def is_valid(choice):
	# Todo:
	return True


def print_header():
	print("==============================================")
	print("                 DOMEMO APP")
	print("==============================================")
	print()


def print_card_hidden(name, number):
	"""
	# print_card_hidden(7)
	# >>>[?, ?, ?, ?, ?, ?, ?]
	# print_card_hidden(1)
	# >>>[?]
	"""
	print(name + ": [?" + ", ?".join(["" for _ in range(number)]) + "]")


if __name__ == '__main__':
	main()
