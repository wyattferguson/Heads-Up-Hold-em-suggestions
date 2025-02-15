"""
+ Moved all your player stuff here. This is where you can add more player specific logic.
+ try to keep your player file to just things that a single player would need
+ Take a peak at the next_move function, we've got a nice docstring underneath
+ Your logic for determining your next move will go in the 'next_move' function, I've added
a few examples to get you started.
"""

from enum import Enum

import colorama as color
from cards import Card


# Enum to make it easier to keep track of the players moves
class Play(Enum):
    WAIT = -1  # waiting for the player to make a first move
    CHECK = 0
    RAISE = 1
    FOLD = 2
    CALL = 3
    BET = 4
    ALL_IN = 5


class Player:
    hand: list[Card] = []

    def __init__(self, name: str, bank: int, color: str):
        self.name: str = name
        self.bank: int = bank
        self.color: str = color

    def next_move(
        self,
        enemy_play: Play,
        last_bet: int,
        stage: int,
        community: list[Card],
        pot: int,
        blind: int,
    ) -> tuple[Play, int]:
        """Determines the player's next move based on the current game state. This is super rough,
        but should give you a good starting point.

        Args:
            enemy_play (Play): The play made by the opponent
            stage (int): The current stage of the game
            community (list[Card]): The community cards available
            pot (int): Total amount of money in the pot
            blind (int): The blind amount
            last_bet (int): The last bet made

        Returns:
            tuple[Play, int]: Play to make and the amount to bet (0 if not betting)
        """

        if enemy_play == Play.WAIT:
            return (Play.CHECK, 0)
        elif enemy_play == Play.BET:
            # the has bet more then your bank go all in
            if last_bet > self.bank:
                return (Play.ALL_IN, self.bank)

            # call your opp's bet
            return (Play.CALL, last_bet)

        return (Play.CALL, 0)

    def __str__(self):
        """Print out the player's name, bank, and hand in a nice format"""
        return f"{self.color}{self.name}{color.Style.RESET_ALL} ({self.bank}) : {self.hand}"


if __name__ == "__main__":
    """Create a test player and draw some cards"""
    from cards import Deck

    deck = Deck()
    test_player = Player("Steve", 100, color.Fore.MAGENTA)
    test_player.hand = deck.draw(2)
    print(test_player)
