import games
from player import Player


nikolai = Player("Nikolai")

dice = games.Dice(6)

print(dice.play(nikolai, bet=1000))

nikolai.show_balance()