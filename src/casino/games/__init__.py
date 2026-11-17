from .roulette import Roulette
from .rps import RPS

# Gjør at jeg kan importere spillklassene direkte fra casino.game, i steden for å måtte importere de fra casino.game.name, der name er spillets navn 
__all__ = ["RPS", "Roulette"]
