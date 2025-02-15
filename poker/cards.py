"""
+ Put all you card data and logic in one nice place

+ Use dataclasses to make your code more readable, and eliminate the boilerplate
of using a class for data.

+ When you find yourself repeating the same blocks of code over and over, you can
probably make a function or class to handle that for you.

+ Notice in the draw section where checking for edge cases and throwing errors now.
"""

import random
from dataclasses import dataclass

import colorama as color


# Simple enum to keep all the card suits in one place
@dataclass
class Suit:
    name: str
    icon: str
    color: str


# The card class was just being used for data, so lets just make it a dataclass
@dataclass
class Card:
    name: str
    rank: int
    suit: Suit

    def __eq__(self, value):
        """Is this card equal to another card?"""
        return self.rank == value.rank

    def __lt__(self, value):
        """Is this card less than another card?"""
        return self.rank <= value.rank

    def __gt__(self, value):
        """Is this card greater than another card?"""
        return self.rank > value.rank

    def __repr__(self):
        """Return a string representation of the card"""
        return f"{self.suit.color}{self.name}{self.suit.icon}{color.Style.RESET_ALL}"

    def __str__(self) -> str:
        """Do all the formating to make your card nice and pretty when printed"""
        return f"{self.suit.color}{self.name}{self.suit.icon}{color.Style.RESET_ALL}"


class Deck:
    values: list[str] = [
        "🂲2",
        "🂳3",
        "🂴4",
        "🂵5",
        "🂶6",
        "🂷7",
        "🂸8",
        "🂹9",
        "🂺10",
        "🂻J",
        "🂽Q",
        "🂾K",
        "🂱A",
    ]

    # Define all your suits with their icons and colors
    suits: list[Suit] = [
        Suit(name="heart", icon="♥", color=color.Fore.RED),
        Suit(name="diamond", icon="♦", color=color.Fore.YELLOW),
        Suit(name="club", icon="♣", color=color.Fore.GREEN),
        Suit(name="spade", icon="♤", color=color.Fore.BLUE),
    ]

    def __init__(self):
        self.cards: list[Card] = []

        # generate a deck from scratch no need to predefine it
        for suit in self.suits:
            for i, value in enumerate(self.values, start=2):
                self.cards.append(
                    Card(
                        name=value,
                        rank=i,
                        suit=suit,
                    )
                )

        # shuffle the deck
        random.shuffle(self.cards)

    def draw(self, card_count: int = 1) -> list[Card]:
        """Draw cards from deck

        Args:
            card_count (int, optional): Number of cards to draw. Defaults to 1.

        Raises:
            ValueError: Must have cards left in the deck to draw
            ValueError: Cards to draw must be great then 1

        Returns:
            list[Card]: _description_
        """
        # check there are any cards left in the deck
        if len(self.cards) < card_count:
            raise ValueError("No more cards in the deck to draw.")

        # check the user is trying to draw at least one card
        if card_count < 1:
            raise ValueError("Must draw at least one card.")

        # take the top card(s) off the deck
        return [self.cards.pop() for _ in range(card_count)]

    def __str__(self) -> str:
        """Print out the deck of cards in a nice format"""
        return " ".join([str(card) for card in self.cards])


if __name__ == "__main__":
    # Create a new deck and print it
    deck = Deck()
    print(deck)

    # draw 5 cards and print them out
    hand = deck.draw(5)
    print(f"Your Hand: {hand}")
