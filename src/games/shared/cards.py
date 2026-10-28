import random

class Card:
    def __init__(self, rank: str, suit: str) -> None:
        self.rank: str = rank
        self.suit: str = suit

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

class Deck:
    SUITS: list[str] = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS: list[str] = [
        "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "Jack", "Queen", "King", "Ace"
    ]

    def __init__(self, num_decks: int = 1) -> None:
        self.num_decks: int = num_decks
        self.cards: list[Card] = []

        self.reset()


    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise ValueError("No cards left in the deck!")

        return self.cards.pop()

    def reset(self) -> None:
        self.cards.clear()

        for _ in range(self.num_decks):
            for suit in self.SUITS:
                for rank in self.RANKS:
                    self.cards.append(Card(rank, suit))

    def __len__(self) -> int:
        return len(self.cards)
