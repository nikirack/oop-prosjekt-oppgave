from .rps import Rps
from .roulette import Roulette

# Gjør at jeg kan importere spillklassene direkte fra casino.game, i steden for å måtte importere de fra casino.game.name, der name er spillets navn 
__all__ = ["Rps", "Roulette"]
