"""
This file contains the game logic for the poker game.
+ Rolled each round into a nice to use Enum
"""

from enum import Enum

from cards import Card, Deck
from player import Player


# You dont have to use an enum for the rounds but its keeps it clean and easy to read
class Round(Enum):
    PREFLOP = 0
    FLOP = 1
    TURN = 2
    RIVER = 3
    END = 4


# move the game logic out of the player class
class Game:
    def __init__(self, players: list[Player], blind: int, ante: int):
        self.deck: Deck = Deck()
        self.players: list[Player] = players
        self.community_cards: list[Card] = []
        self.pot: int = 0
        self.stage: Round = Round.PREFLOP
        self.blind: int = blind
        self.ante: int = ante
        self.is_running = True

    def new_game(self):
        self.is_running = True
        self.deck = Deck()
        self.community_cards = []

        # deal each player a hand and take ante's
        for idx, p in enumerate(self.players):
            self.players[idx].hand = self.deck.draw(2)
            self.players[idx].bank -= self.ante

        # draw 3 cards for the community cards
        self.community_cards = self.deck.draw(3)

        # add the total of all the players ante's to the pot
        self.pot = sum(p.ante for p in self.players)

    def next_round(self):
        """Move to the next round of the game."""
        self.stage = Round(self.stage.value + 1)
        match self.stage:
            case Round.FLOP:
                self.community_cards += self.deck.draw(3)
            case Round.TURN:
                self.community_cards += self.deck.draw(1)
            case Round.RIVER:
                self.community_cards += self.deck.draw(1)
            case Round.END:
                self.game_over()

    def game_over(self):
        # end the game loop
        self.is_running = False

    def __str__(self):
        """Nicely format entire game state"""
        return (
            f"Round: {self.stage.name}\n"
            f"Pot: {self.pot} | Ante: {self.ante} Blind: {self.blind}\n"
            f"Community Cards: {' '.join(str(card) for card in self.community_cards)}\n"
            f"Players: {', '.join(str(player.name) for player in self.players)}"
        )


if __name__ == "__main__":
    # create a test game / players
    import colorama as color

    game = Game(
        [Player("Jane", 100, color.Fore.CYAN), Player("Bill", 100, color.Fore.MAGENTA)],
        10,
        5,
    )
    game.next_round()

    print(game)
