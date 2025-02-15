"""
+ First lets break out all the big components of the game into their own files. Players, The Deck,
and Game logic can all be in their own files. This makes them easier to test and maintain.

+ Removed all the 'globals', when you find your self using the same set of variables across alot
of related functions, thats a good sign it should be it own class.

+ Lets move all that floating code into a main function, you want one place where the game starts
thats easy to follow the program flow of, and with loose code everywhere its hard to follow and
will lead to bugs and headaches.

+ Added types to everything, makes it easier to code with type hinting from your
editor and less bugs from type errors.

+ Added nice __str__ functions to the classes so by default they print in a nice format.

+ This is all just a very very rough first go through to point you in the right direction.
"""

import colorama as color
from game import Game
from player import Player
from utils import clear_screen

color.init()


def main():
    # wipe the terminal using our function the utils file
    clear_screen()

    # use triple quotes to print multiline statements
    print("""
    This game simulates Heads-Up Texas Hold'em Poker. It requires two players.
    To keep hands secret, please look away during opponent's turn.

    When numbers are requested, entering anything but numbers will break the game.

    PEEK, BET, CHECK, CALL, RAISE, and FOLD can all be entered by typing a single
    letter, 'p' 'b', 'c', 'c', 'r', and 'f' respectively.

    Recommended console font size is 30 pt with the terminal fully expanded.

    If the program seems to have stopped when pressing ENTER to see cards,
    try BACKSPACE and then ENTER again. Pressing ENTER twice WILL crash the game!
    """)

    input("Press ENTER to begin.")

    # if you ever wanted to add more players then 2 you could make this a loop
    p1_name = input("Player one, input name: ")
    p2_name = input("Player two, input name: ")
    start_chips = int(input("How many chips to start? "))

    ante = int(input("Ante size? "))
    while ante >= start_chips:
        ante = int(input(f"Ante must be less than {start_chips}. Ante size? "))

    blind = int(input("Blind size? "))
    while blind >= (start_chips - ante):
        blind = int(input(f"Blind must be less than {start_chips - ante}. Blind size? "))

    # create both your players
    players = [
        Player(p1_name, start_chips, color.Fore.CYAN),
        Player(p2_name, start_chips, color.Fore.MAGENTA),
    ]

    game = Game(players, blind, ante)
    # main game loop
    while game.is_running:
        # all your game logic can stem from here
        game.next_round()


if __name__ == "__main__":
    main()
