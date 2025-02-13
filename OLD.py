import random
import time

# Introduction
print()
print("This game simulates Heads-Up Texas Hold'em Poker. It requires two players. To keep hands secret, please look away during opponent's turn.")
print("For privacy, it is best to keep the height of the terminal under 9 lines. The only 'safe' time to scroll up is before any player hands have been revealed.")
print("Time step can be adjusted by modifying variable step. Recommended step = 1.")
print('When integers are requested (as in "How many...?" queries), entering anything else will break the game.')
print("If a player breaks the script, accidentally or otherwise, fair play says to modify players' starting chip sizes (lines 37,38) to represent a folded hand.")
print("BET, CHECK, CALL, RAISE, and FOLD can all be entered by typing a single letter, 'b', 'c', 'c', 'r', and 'f' respectively.")
print("If your opponent has pushed ALL-IN, do NOT raise them, or else you will be stuck in an infinite spiral of rejection. Just CALL or FOLD.")
print("If the program seems to have stopped when pressing ENTER to see cards, try BACKSPACE and then ENTER again.")
input("Enter ANY KEY to begin.")

# Timestep variable. Set to 1 for normal gameplay, 0 for instant
step = 1

# The deck of 52 cards.
deck = ['2h','3h','4h','5h','6h','7h','8h','9h','10h','Jh','Qh','Kh','Ah',
        '2d','3d','4d','5d','6d','7d','8d','9d','10d','Jd','Qd','Kd','Ad',
        '2c','3c','4c','5c','6c','7c','8c','9c','10c','Jc','Qc','Kc','Ac',
        '2s','3s','4s','5s','6s','7s','8s','9s','10s','Js','Qs','Ks','As']

# Configurable starting conditions.
def restart():
    global name_p1,name_p2,chips_start,chips_p1,chips_p2,ante,blind
    global hand_p1,hand_p2,community,made_p1,made_p2,to_call_p1,to_call_p2
    global stage,pot,size,both_check,p1,p2,tie,first_player,next_player

    for i in range(12):
        print()

    name_p1 = input("Enter name of Player 1: ")
    name_p2 = input("Enter name of Player 2: ")
    chips_start = int(input("How many chips to start? "))
    chips_p1 = chips_start # Adjust these values accordingly if the script was broken mid-game.
    chips_p2 = chips_start # Adjust these values accordingly if the script was broken mid-game.
    ante = int(input("Ante size? "))
    blind = int(input("Blind size? "))

    hand_p1, hand_p2, community = [], [], []
    made_p1, made_p2, to_call_p1, to_call_p2 = 0, 0, 0, 0
    stage, pot, size = 0, 0, 0
    both_check = 0
    p1 = 'p1'
    p2 = 'p2'
    tie = 'tie'
    first_player = 'p2'
    next_player = 'p1'

    next()

# Restarting the round
def next():
    global card1,card2,card3,card4,card5,card6,card7,card8,card9
    global hand_p1,hand_p2,community
    global made_p1,made_p2,to_call_p1,to_call_p2
    global stage,pot,size,both_check
    global deck,first_player,next_player
    global check_p1, check_p2, bet_p1, bet_p2, raised_p1, raised_p2

    deck = ['2h','3h','4h','5h','6h','7h','8h','9h','10h','Jh','Qh','Kh','Ah',
            '2d','3d','4d','5d','6d','7d','8d','9d','10d','Jd','Qd','Kd','Ad',
            '2c','3c','4c','5c','6c','7c','8c','9c','10c','Jc','Qc','Kc','Ac',
            '2s','3s','4s','5s','6s','7s','8s','9s','10s','Js','Qs','Ks','As']

    card1,card2,card3,card4,card5,card6,card7,card8,card9 = 0,0,0,0,0,0,0,0,0
    hand_p1,hand_p2,community = [],[],[]
    made_p1,made_p2,to_call_p1,to_call_p2 = 0,0,0,0
    stage,pot,size,both_check = 0,0,0,0
    check_p1, bet_p1, raised_p1 = False, False, False
    check_p2, bet_p2, raised_p2 = False, False, False

    if first_player == 'p1':
        first_player = 'p2'
    else:
        first_player = 'p1'
    dealer()

def dealer():
    global both_check
    global stage
    global first_player
    global to_call_p1, to_call_p2
    global check_p1, bet_p1, raised_p1
    global check_p2, bet_p1, raised_p2
    stage += 1

    if stage == 1:
        both_check = 0
        to_call_p1, to_call_p2 = 0,0
        check_p1,check_p2,bet_p1,bet_p2,raised_p1,raised_p2 = False, False, False, False, False, False
        preflop()
    if stage == 2:
        both_check = 0
        to_call_p1, to_call_p2 = 0, 0
        check_p1, check_p2, bet_p1, bet_p2, raised_p1, raised_p2 = False, False, False, False, False, False
        flop()
    if stage == 3:
        both_check = 0
        to_call_p1, to_call_p2 = 0, 0
        check_p1, check_p2, bet_p1, bet_p2, raised_p1, raised_p2 = False, False, False, False, False, False
        turn()
    if stage == 4:
        both_check = 0
        to_call_p1, to_call_p2 = 0, 0
        check_p1, check_p2, bet_p1, bet_p2, raised_p1, raised_p2 = False, False, False, False, False, False
        river()
    if stage == 5:
        both_check = 0
        to_call_p1, to_call_p2 = 0, 0
        check_p1, check_p2, bet_p1, bet_p2, raised_p1, raised_p2 = False, False, False, False, False, False
        showdown()

def preflop():
    global chips_p1
    global chips_p2
    global pot
    global stage
    global to_call_p1
    global to_call_p2
    stage = 1

    print()
    print("************************************************************************************************************************************************")
    print()
    print("Let's shuffle up and deal! Starting chip stacks at", chips_start)
    card1 = random.choice(deck)
    deck.remove(card1)
    hand_p1.append(card1)
    card2 = random.choice(deck)
    deck.remove(card2)
    hand_p1.append(card2)
    card3 = random.choice(deck)
    deck.remove(card3)
    hand_p2.append(card3)
    card4 = random.choice(deck)
    deck.remove(card4)
    hand_p2.append(card4)

    print("Ante up!", ante,"chips to play.")
    chips_p1 -= ante
    chips_p2 -= ante
    pot += (ante * 2)

    if first_player == 'p1':
        time.sleep(step)
        print(name_p1," to start...")
        chips_p2 -= blind
        pot += blind
        to_call_p1 += blind
        if blind > 0:
            print("Paying blind of",blind,"chips...")
        time.sleep(step * 2)
        play_p1()
    elif first_player == 'p2':
        time.sleep(step)
        print(name_p2,"to start...")
        chips_p1 -= blind
        pot += blind
        to_call_p2 += blind
        if blind > 0:
            print("Paying blind of",blind,"chips...")
        time.sleep(step * 2)
        play_p2()
    elif next_player == 'p1':
        time.sleep(step)
        print(name_p1,"to start...")
        play_p1()
    elif next_player == 'p2':
        time.sleep(step)
        print(name_p2,"to start...")
        play_p2()

def flop():
    global stage
    stage = 2

    print()
    card5 = random.choice(deck)
    deck.remove(card5)
    community.append(card5)
    card6 = random.choice(deck)
    deck.remove(card6)
    community.append(card6)
    card7 = random.choice(deck)
    deck.remove(card7)
    community.append(card7)

    if next_player == 'p1':
        time.sleep(step)
        print(name_p1," to start...")
        play_p1()
    if next_player == 'p2':
        time.sleep(step)
        print(name_p2,"to start...")
        play_p2()

def turn():
    global stage
    stage = 3

    print()
    card8 = random.choice(deck)
    deck.remove(card8)
    community.append(card8)

    if next_player == 'p1':
        time.sleep(step)
        print(name_p1,"to start...")
        play_p1()
    if next_player == 'p2':
        time.sleep(step)
        print(name_p2,"to start...")
        play_p2()

def river():
    global stage
    stage = 4

    print()
    card9 = random.choice(deck)
    deck.remove(card9)
    community.append(card9)

    if next_player == 'p1':
        time.sleep(step)
        print(name_p1,"to start...")
        play_p1()
    if next_player == 'p2':
        time.sleep(step)
        print(name_p2,"to start...")
        play_p2()

def showdown():
    global stage
    stage = 5

    # Skipping to showdown if ALL-IN
    if len(community) == 0:
        card5 = random.choice(deck)
        deck.remove(card5)
        community.append(card5)
        card6 = random.choice(deck)
        deck.remove(card6)
        community.append(card6)
        card7 = random.choice(deck)
        deck.remove(card7)
        community.append(card7)
    if len(community) == 3:
        card8 = random.choice(deck)
        deck.remove(card8)
        community.append(card8)
    if len(community) == 4:
        card9 = random.choice(deck)
        deck.remove(card9)
        community.append(card9)

    print('******************************** SHOWDOWN ********************************')
    print()
    print("Community cards are: ",community)
    time.sleep(step * 2)
    print(name_p1,"'s cards are: ", hand_p1)
    time.sleep(step * 2)
    print(name_p2,"'s cards are: ", hand_p2)
    time.sleep(step * 2)
    resolve()

def award(x):
    global chips_p1
    global chips_p2
    global pot

    if x == p1:
        chips_p1 += pot
        print("Awarding",name_p1, pot, "chips.")
    elif x == p2:
        chips_p2 += pot
        print("Awarding",name_p2, pot, "chips.")
    elif x == tie:
        if (pot % 2) == 0:
            chips_p1 += (pot//2)
            chips_p2 += (pot//2)
            print("Splitting the pot of", pot, "chips.")
        elif (pot % 2) != 0:
            pot -= 1
            chips_p1 += (pot//2)
            chips_p2 += (pot//2)
            print("Pot has an odd number. House takes one chip.\n Splitting the new pot of",pot,"chips.")
    else:
        print("Error awarding pot")

    if chips_p1 > 0 and chips_p2 > 0:
        reset = str.lower(input("Enter R to RESET, else press ENTER to play NEXT hand."))
        if reset == 'r':
            restart()
    elif chips_p1 <= 0:
        print(name_p1,"has busted out!",name_p2,"takes the game!")
        input("Game will now RESET. Press ENTER when ready.")
        restart()
    elif chips_p2 <= 0:
        print(name_p2, "has busted out!", name_p1, "takes the game!")
        input("Game will now RESET. Press ENTER when ready.")
        restart()
    next()


# Check hands at showdown and determine winner.
# #Contains 9 defs for each hand type.
def resolve():
    def royalflushcheck(a, b, c):
        global made_p1, made_p2
        global hand_p1, hand_p2, community

        # Resetting variables
        royal_Ah, royal_Kh, royal_Qh, royal_Jh, royal_10h = False, False, False, False, False
        royal_Ad, royal_Kd, royal_Qd, royal_Jd, royal_10d = False, False, False, False, False
        royal_Ac, royal_Kc, royal_Qc, royal_Jc, royal_10c = False, False, False, False, False
        royal_As, royal_Ks, royal_Qs, royal_Js, royal_10s = False, False, False, False, False

        # Checking player 1's cards for Royal Flush
        for n in a:
            if n == 'Ah':
                royal_Ah = True
            if n == 'Kh':
                royal_Kh = True
            if n == 'Qh':
                royal_Qh = True
            if n == 'Jh':
                royal_Jh = True
            if n == '10h':
                royal_10h = True
            if n == 'Ad':
                royal_Ad = True
            if n == 'Kd':
                royal_Kd = True
            if n == 'Qd':
                royal_Qd = True
            if n == 'Jd':
                royal_Jd = True
            if n == '10d':
                royal_10d = True
            if n == 'Ac':
                royal_Ac = True
            if n == 'Kc':
                royal_Kc = True
            if n == 'Qc':
                royal_Qc = True
            if n == 'Jc':
                royal_Jc = True
            if n == '10c':
                royal_10c = True
            if n == 'As':
                royal_As = True
            if n == 'Ks':
                royal_Ks = True
            if n == 'Qs':
                royal_Qs = True
            if n == 'Js':
                royal_Js = True
            if n == '10s':
                royal_10s = True

        # Checking community cards for Player 1
        for n in c:
            if n == 'Ah':
                royal_Ah = True
            if n == 'Kh':
                royal_Kh = True
            if n == 'Qh':
                royal_Qh = True
            if n == 'Jh':
                royal_Jh = True
            if n == '10h':
                royal_10h = True
            if n == 'Ad':
                royal_Ad = True
            if n == 'Kd':
                royal_Kd = True
            if n == 'Qd':
                royal_Qd = True
            if n == 'Jd':
                royal_Jd = True
            if n == '10d':
                royal_10d = True
            if n == 'Ac':
                royal_Ac = True
            if n == 'Kc':
                royal_Kc = True
            if n == 'Qc':
                royal_Qc = True
            if n == 'Jc':
                royal_Jc = True
            if n == '10c':
                royal_10c = True
            if n == 'As':
                royal_As = True
            if n == 'Ks':
                royal_Ks = True
            if n == 'Qs':
                royal_Qs = True
            if n == 'Js':
                royal_Js = True
            if n == '10s':
                royal_10s = True

        if (royal_Ah == True) and (royal_Kh == True) and (royal_Qh == True) and (royal_Jh == True) and (
                royal_10h == True):
            made_p1 = 9
            print(name_p1, "has made a royal flush! Holy moly!")
        if (royal_Ad == True) and (royal_Kd == True) and (royal_Qd == True) and (royal_Jd == True) and (
                royal_10d == True):
            made_p1 = 9
            print(name_p1, "has made a royal flush! Holy moly!")
        if (royal_Ac == True) and (royal_Kc == True) and (royal_Qc == True) and (royal_Jc == True) and (
                royal_10c == True):
            made_p1 = 9
            print(name_p1, "has made a royal flush! Holy moly!")
        if (royal_As == True) and (royal_Ks == True) and (royal_Qs == True) and (royal_Js == True) and (
                royal_10s == True):
            made_p1 = 9
            print(name_p1, "has made a royal flush! Holy moly!")

            # Resetting variables for player 2
        royal_Ah, royal_Kh, royal_Qh, royal_Jh, royal_10h = False, False, False, False, False
        royal_Ad, royal_Kd, royal_Qd, royal_Jd, royal_10d = False, False, False, False, False
        royal_Ac, royal_Kc, royal_Qc, royal_Jc, royal_10c = False, False, False, False, False
        royal_As, royal_Ks, royal_Qs, royal_Js, royal_10s = False, False, False, False, False

        # Checking player 2's cards for Royal Flush
        for n in b:
            if n == 'Ah':
                royal_Ah = True
            if n == 'Kh':
                royal_Kh = True
            if n == 'Qh':
                royal_Qh = True
            if n == 'Jh':
                royal_Jh = True
            if n == '10h':
                royal_10h = True
            if n == 'Ad':
                royal_Ad = True
            if n == 'Kd':
                royal_Kd = True
            if n == 'Qd':
                royal_Qd = True
            if n == 'Jd':
                royal_Jd = True
            if n == '10d':
                royal_10d = True
            if n == 'Ac':
                royal_Ac = True
            if n == 'Kc':
                royal_Kc = True
            if n == 'Qc':
                royal_Qc = True
            if n == 'Jc':
                royal_Jc = True
            if n == '10c':
                royal_10c = True
            if n == 'As':
                royal_As = True
            if n == 'Ks':
                royal_Ks = True
            if n == 'Qs':
                royal_Qs = True
            if n == 'Js':
                royal_Js = True
            if n == '10s':
                royal_10s = True

        # Checking community cards for Player 2
        for n in c:
            if n == 'Ah':
                royal_Ah = True
            if n == 'Kh':
                royal_Kh = True
            if n == 'Qh':
                royal_Qh = True
            if n == 'Jh':
                royal_Jh = True
            if n == '10h':
                royal_10h = True
            if n == 'Ad':
                royal_Ad = True
            if n == 'Kd':
                royal_Kd = True
            if n == 'Qd':
                royal_Qd = True
            if n == 'Jd':
                royal_Jd = True
            if n == '10d':
                royal_10d = True
            if n == 'Ac':
                royal_Ac = True
            if n == 'Kc':
                royal_Kc = True
            if n == 'Qc':
                royal_Qc = True
            if n == 'Jc':
                royal_Jc = True
            if n == '10c':
                royal_10c = True
            if n == 'As':
                royal_As = True
            if n == 'Ks':
                royal_Ks = True
            if n == 'Qs':
                royal_Qs = True
            if n == 'Js':
                royal_Js = True
            if n == '10s':
                royal_10s = True

        if (royal_Ah == True) and (royal_Kh == True) and (royal_Qh == True) and (royal_Jh == True) and (
                royal_10h == True):
            made_p2 = 9
            print(name_p2, "has made a royal flush! Holy moly!")
        if (royal_Ad == True) and (royal_Kd == True) and (royal_Qd == True) and (royal_Jd == True) and (
                royal_10d == True):
            made_p2 = 9
            print(name_p2, "has made a royal flush! Holy moly!")
        if (royal_Ac == True) and (royal_Kc == True) and (royal_Qc == True) and (royal_Jc == True) and (
                royal_10c == True):
            made_p2 = 9
            print(name_p2, "has made a royal flush! Holy moly!")
        if (royal_As == True) and (royal_Ks == True) and (royal_Qs == True) and (royal_Js == True) and (
                royal_10s == True):
            made_p2 = 9
            print(name_p2, "has made a royal flush! Holy moly!")

        # Resolving the showdown
        if made_p1 > made_p2:
            print(name_p1, "wins the hand!")
            award(p1)
        elif made_p2 > made_p1:
            print(name_p2, "wins the hand!")
            award(p2)
        elif made_p1 == 9 and made_p2 == 9:
            print("Words cannot express what has just occurred here!")
            award(tie)
        else:
            straightflushcheck(hand_p1, hand_p2, community)
    def straightflushcheck(a, b, c):
        global made_p1, made_p2
        global hand_p1, hand_p2, community

        top_p1 = 0
        top_p2 = 0
        set_ranks_p1 = set()
        set_ranks_p2 = set()


        # Gathering the ranks in Player 1's hand as a SET
        for n in a:
            if n[0:-1] == 'A':
                set_ranks_p1.add(14)
                set_ranks_p1.add(1)
            if n[0:-1] == 'K':
                set_ranks_p1.add(13)
            if n[0:-1] == 'Q':
                set_ranks_p1.add(12)
            if n[0:-1] == 'J':
                set_ranks_p1.add(11)
            if n[0:-1] == '10':
                set_ranks_p1.add(10)
            if n[0:-1] == '9':
                set_ranks_p1.add(9)
            if n[0:-1] == '8':
                set_ranks_p1.add(8)
            if n[0:-1] == '7':
                set_ranks_p1.add(7)
            if n[0:-1] == '6':
                set_ranks_p1.add(6)
            if n[0:-1] == '5':
                set_ranks_p1.add(5)
            if n[0:-1] == '4':
                set_ranks_p1.add(4)
            if n[0:-1] == '3':
                set_ranks_p1.add(3)
            if n[0:-1] == '2':
                set_ranks_p1.add(2)

        # Gathering the ranks in community as a SET for player 1
        for n in c:
            if n[0:-1] == 'A':
                set_ranks_p1.add(14)
                set_ranks_p1.add(1)
            if n[0:-1] == 'K':
                set_ranks_p1.add(13)
            if n[0:-1] == 'Q':
                set_ranks_p1.add(12)
            if n[0:-1] == 'J':
                set_ranks_p1.add(11)
            if n[0:-1] == '10':
                set_ranks_p1.add(10)
            if n[0:-1] == '9':
                set_ranks_p1.add(9)
            if n[0:-1] == '8':
                set_ranks_p1.add(8)
            if n[0:-1] == '7':
                set_ranks_p1.add(7)
            if n[0:-1] == '6':
                set_ranks_p1.add(6)
            if n[0:-1] == '5':
                set_ranks_p1.add(5)
            if n[0:-1] == '4':
                set_ranks_p1.add(4)
            if n[0:-1] == '3':
                set_ranks_p1.add(3)
            if n[0:-1] == '2':
                set_ranks_p1.add(2)

        # Checking Player 1 for Straight Flush
        if 10 in set_ranks_p1 and 11 in set_ranks_p1 and 12 in set_ranks_p1 and 13 in set_ranks_p1 and 14 in set_ranks_p1:
            top_p1 = 14

            if 'Ah' in hand_p1 or 'Ah' in community:  # Heart check
                if 'Kh' in hand_p1 or 'Kh' in community:
                    if 'Qh' in hand_p1 or 'Qh' in community:
                        if 'Jh' in hand_p1 or 'Jh' in community:
                            if '10h' in hand_p1 or '10h' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if 'Ad' in hand_p1 or 'Ad' in community:  # Diamond check
                if 'Kd' in hand_p1 or 'Kd' in community:
                    if 'Qd' in hand_p1 or 'Qd' in community:
                        if 'Jd' in hand_p1 or 'Jd' in community:
                            if '10d' in hand_p1 or '10d' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if 'Ac' in hand_p1 or 'Ac' in community:  # Club check
                if 'Kc' in hand_p1 or 'Kc' in community:
                    if 'Qc' in hand_p1 or 'Qc' in community:
                        if 'Jc' in hand_p1 or 'Jc' in community:
                            if '10c' in hand_p1 or '10c' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if 'As' in hand_p1 or 'As' in community:  # Spade check
                if 'Ks' in hand_p1 or 'Ks' in community:
                    if 'Qs' in hand_p1 or 'Qs' in community:
                        if 'Js' in hand_p1 or 'Js' in community:
                            if '10s' in hand_p1 or '10s' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8
        elif 9 in set_ranks_p1 and 10 in set_ranks_p1 and 11 in set_ranks_p1 and 12 in set_ranks_p1 and 13 in set_ranks_p1:
            top_p1 = 13

            if 'Kh' in hand_p1 or 'Kh' in community:
                if 'Qh' in hand_p1 or 'Qh' in community:
                    if 'Jh' in hand_p1 or 'Jh' in community:
                        if '10h' in hand_p1 or '10h' in community:
                            if '9h' in hand_p1 or '9h' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if 'Kd' in hand_p1 or 'Kd' in community:
                if 'Qd' in hand_p1 or 'Qd' in community:
                    if 'Jd' in hand_p1 or 'Jd' in community:
                        if '10d' in hand_p1 or '10d' in community:
                            if '9d' in hand_p1 or '9d' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if 'Kc' in hand_p1 or 'Kc' in community:
                if 'Qc' in hand_p1 or 'Qc' in community:
                    if 'Jc' in hand_p1 or 'Jc' in community:
                        if '10c' in hand_p1 or '10c' in community:
                            if '9c' in hand_p1 or '9c' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if 'Ks' in hand_p1 or 'Ks' in community:
                if 'Qs' in hand_p1 or 'Qs' in community:
                    if 'Js' in hand_p1 or 'Js' in community:
                        if '10s' in hand_p1 or '10s' in community:
                            if '9s' in hand_p1 or '9s' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8
        elif 8 in set_ranks_p1 and 9 in set_ranks_p1 and 10 in set_ranks_p1 and 11 in set_ranks_p1 and 12 in set_ranks_p1:
            top_p1 = 12

            if 'Qh' in hand_p1 or 'Qh' in community:
                if 'Jh' in hand_p1 or 'Jh' in community:
                    if '10h' in hand_p1 or '10h' in community:
                        if '9h' in hand_p1 or '9h' in community:
                            if '8h' in hand_p1 or '8h' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if 'Qd' in hand_p1 or 'Qd' in community:
                if 'Jd' in hand_p1 or 'Jd' in community:
                    if '10d' in hand_p1 or '10d' in community:
                        if '9d' in hand_p1 or '9d' in community:
                            if '8d' in hand_p1 or '8d' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if 'Qc' in hand_p1 or 'Qc' in community:
                if 'Jc' in hand_p1 or 'Jc' in community:
                    if '10c' in hand_p1 or '10c' in community:
                        if '9c' in hand_p1 or '9c' in community:
                            if '8c' in hand_p1 or '8c' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if 'Qs' in hand_p1 or 'Qs' in community:
                if 'Js' in hand_p1 or 'Js' in community:
                    if '10s' in hand_p1 or '10s' in community:
                        if '9s' in hand_p1 or '9s' in community:
                            if '8s' in hand_p1 or '8s' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8
        elif 7 in set_ranks_p1 and 8 in set_ranks_p1 and 9 in set_ranks_p1 and 10 in set_ranks_p1 and 11 in set_ranks_p1:
            top_p1 = 11

            if 'Jh' in hand_p1 or 'Jh' in community:
                if '10h' in hand_p1 or '10h' in community:
                    if '9h' in hand_p1 or '9h' in community:
                        if '8h' in hand_p1 or '8h' in community:
                            if '7h' in hand_p1 or '7h' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if 'Jd' in hand_p1 or 'Jd' in community:
                if '10d' in hand_p1 or '10d' in community:
                    if '9d' in hand_p1 or '9d' in community:
                        if '8d' in hand_p1 or '8d' in community:
                            if '7d' in hand_p1 or '7d' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if 'Jc' in hand_p1 or 'Jc' in community:
                if '10c' in hand_p1 or '10c' in community:
                    if '9c' in hand_p1 or '9c' in community:
                        if '8c' in hand_p1 or '8c' in community:
                            if '7c' in hand_p1 or '7c' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if 'Js' in hand_p1 or 'Js' in community:
                if '10s' in hand_p1 or '10s' in community:
                    if '9s' in hand_p1 or '9s' in community:
                        if '8s' in hand_p1 or '8s' in community:
                            if '7s' in hand_p1 or '7s' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8
        elif 6 in set_ranks_p1 and 7 in set_ranks_p1 and 8 in set_ranks_p1 and 9 in set_ranks_p1 and 10 in set_ranks_p1:
            top_p1 = 10

            if '10h' in hand_p1 or '10h' in community:
                if '9h' in hand_p1 or '9h' in community:
                    if '8h' in hand_p1 or '8h' in community:
                        if '7h' in hand_p1 or '7h' in community:
                            if '6h' in hand_p1 or '6h' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if '10d' in hand_p1 or '10d' in community:
                if '9d' in hand_p1 or '9d' in community:
                    if '8d' in hand_p1 or '8d' in community:
                        if '7d' in hand_p1 or '7d' in community:
                            if '6d' in hand_p1 or '6d' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if '10c' in hand_p1 or '10c' in community:
                if '9c' in hand_p1 or '9c' in community:
                    if '8c' in hand_p1 or '8c' in community:
                        if '7c' in hand_p1 or '7c' in community:
                            if '6c' in hand_p1 or '6c' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if '10s' in hand_p1 or '10s' in community:
                if '9s' in hand_p1 or '9s' in community:
                    if '8s' in hand_p1 or '8s' in community:
                        if '7s' in hand_p1 or '7s' in community:
                            if '6s' in hand_p1 or '6s' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8
        elif 5 in set_ranks_p1 and 6 in set_ranks_p1 and 7 in set_ranks_p1 and 8 in set_ranks_p1 and 9 in set_ranks_p1:
            top_p1 = 9

            if '9h' in hand_p1 or '9h' in community:
                if '8h' in hand_p1 or '8h' in community:
                    if '7h' in hand_p1 or '7h' in community:
                        if '6h' in hand_p1 or '6h' in community:
                            if '5h' in hand_p1 or '5h' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if '9d' in hand_p1 or '9d' in community:
                if '8d' in hand_p1 or '8d' in community:
                    if '7d' in hand_p1 or '7d' in community:
                        if '6d' in hand_p1 or '6d' in community:
                            if '5d' in hand_p1 or '5d' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if '9c' in hand_p1 or '9c' in community:
                if '8c' in hand_p1 or '8c' in community:
                    if '7c' in hand_p1 or '7c' in community:
                        if '6c' in hand_p1 or '6c' in community:
                            if '5c' in hand_p1 or '5c' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if '9s' in hand_p1 or '9s' in community:
                if '8s' in hand_p1 or '8s' in community:
                    if '7s' in hand_p1 or '7s' in community:
                        if '6s' in hand_p1 or '6s' in community:
                            if '5s' in hand_p1 or '5s' in community:
                                made_p1 = 8
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8
        elif 4 in set_ranks_p1 and 5 in set_ranks_p1 and 6 in set_ranks_p1 and 7 in set_ranks_p1 and 8 in set_ranks_p1:
            top_p1 = 8

            if '8h' in hand_p1 or '8h' in community:
                if '7h' in hand_p1 or '7h' in community:
                    if '6h' in hand_p1 or '6h' in community:
                        if '5h' in hand_p1 or '5h' in community:
                            if '4h' in hand_p1 or '4h' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if '8d' in hand_p1 or '8d' in community:
                if '7d' in hand_p1 or '7d' in community:
                    if '6d' in hand_p1 or '6d' in community:
                        if '5d' in hand_p1 or '5d' in community:
                            if '4d' in hand_p1 or '4d' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if '8c' in hand_p1 or '8c' in community:
                if '7c' in hand_p1 or '7c' in community:
                    if '6c' in hand_p1 or '6c' in community:
                        if '5c' in hand_p1 or '5c' in community:
                            if '4c' in hand_p1 or '4c' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if '8s' in hand_p1 or '8s' in community:
                if '7s' in hand_p1 or '7s' in community:
                    if '6s' in hand_p1 or '6s' in community:
                        if '5s' in hand_p1 or '5s' in community:
                            if '4s' in hand_p1 or '4s' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8
        elif 3 in set_ranks_p1 and 4 in set_ranks_p1 and 5 in set_ranks_p1 and 6 in set_ranks_p1 and 7 in set_ranks_p1:
            top_p1 = 7

            if '7h' in hand_p1 or '7h' in community:
                if '6h' in hand_p1 or '6h' in community:
                    if '5h' in hand_p1 or '5h' in community:
                        if '4h' in hand_p1 or '4h' in community:
                            if '3h' in hand_p1 or '3h' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if '7d' in hand_p1 or '7d' in community:
                if '6d' in hand_p1 or '6d' in community:
                    if '5d' in hand_p1 or '5d' in community:
                        if '4d' in hand_p1 or '4d' in community:
                            if '3d' in hand_p1 or '3d' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if '7c' in hand_p1 or '7c' in community:
                if '6c' in hand_p1 or '6c' in community:
                    if '5c' in hand_p1 or '5c' in community:
                        if '4c' in hand_p1 or '4c' in community:
                            if '3c' in hand_p1 or '3c' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if '7s' in hand_p1 or '7s' in community:
                if '6s' in hand_p1 or '6s' in community:
                    if '5s' in hand_p1 or '5s' in community:
                        if '4s' in hand_p1 or '4s' in community:
                            if '3s' in hand_p1 or '3s' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8
        elif 2 in set_ranks_p1 and 3 in set_ranks_p1 and 4 in set_ranks_p1 and 5 in set_ranks_p1 and 6 in set_ranks_p1:
            top_p1 = 6

            if '6h' in hand_p1 or '6h' in community:
                if '5h' in hand_p1 or '5h' in community:
                    if '4h' in hand_p1 or '4h' in community:
                        if '3h' in hand_p1 or '3h' in community:
                            if '2h' in hand_p1 or '2h' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if '6d' in hand_p1 or '6d' in community:
                if '5d' in hand_p1 or '5d' in community:
                    if '4d' in hand_p1 or '4d' in community:
                        if '3d' in hand_p1 or '3d' in community:
                            if '2d' in hand_p1 or '2d' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if '6c' in hand_p1 or '6c' in community:
                if '5c' in hand_p1 or '5c' in community:
                    if '4c' in hand_p1 or '4c' in community:
                        if '3c' in hand_p1 or '3c' in community:
                            if '2c' in hand_p1 or '2c' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if '6s' in hand_p1 or '6s' in community:
                if '5s' in hand_p1 or '5s' in community:
                    if '4s' in hand_p1 or '4s' in community:
                        if '3s' in hand_p1 or '3s' in community:
                            if '2s' in hand_p1 or '2s' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8
        elif 1 in set_ranks_p1 and 2 in set_ranks_p1 and 3 in set_ranks_p1 and 4 in set_ranks_p1 and 5 in set_ranks_p1:
            top_p1 = 5

            if '5h' in hand_p1 or '5h' in community:
                if '4h' in hand_p1 or '4h' in community:
                    if '3h' in hand_p1 or '3h' in community:
                        if '2h' in hand_p1 or '2h' in community:
                            if 'Ah' in hand_p1 or 'Ah' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if '5d' in hand_p1 or '5d' in community:
                if '4d' in hand_p1 or '4d' in community:
                    if '3d' in hand_p1 or '3d' in community:
                        if '2d' in hand_p1 or '2d' in community:
                            if 'Ad' in hand_p1 or 'Ad' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if '5c' in hand_p1 or '5c' in community:
                if '4c' in hand_p1 or '4c' in community:
                    if '3c' in hand_p1 or '3c' in community:
                        if '2c' in hand_p1 or '2c' in community:
                            if 'Ac' in hand_p1 or 'Ac' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

            if '5s' in hand_p1 or '5s' in community:
                if '4s' in hand_p1 or '4s' in community:
                    if '3s' in hand_p1 or '3s' in community:
                        if '2s' in hand_p1 or '2s' in community:
                            if 'As' in hand_p1 or 'As' in community:
                                print(name_p1, 'has made a straight flush!')
                                if made_p1 < 8:
                                    made_p1 = 8

        # Going to Player 2
        # Gathering the ranks in Player 2's hand as a SET
        for n in b:
            if n[0:-1] == 'A':
                set_ranks_p2.add(14)
                set_ranks_p2.add(1)
            if n[0:-1] == 'K':
                set_ranks_p2.add(13)
            if n[0:-1] == 'Q':
                set_ranks_p2.add(12)
            if n[0:-1] == 'J':
                set_ranks_p2.add(11)
            if n[0:-1] == '10':
                set_ranks_p2.add(10)
            if n[0:-1] == '9':
                set_ranks_p2.add(9)
            if n[0:-1] == '8':
                set_ranks_p2.add(8)
            if n[0:-1] == '7':
                set_ranks_p2.add(7)
            if n[0:-1] == '6':
                set_ranks_p2.add(6)
            if n[0:-1] == '5':
                set_ranks_p2.add(5)
            if n[0:-1] == '4':
                set_ranks_p2.add(4)
            if n[0:-1] == '3':
                set_ranks_p2.add(3)
            if n[0:-1] == '2':
                set_ranks_p2.add(2)

        # Gathering the ranks in community as a SET for player 2
        for n in c:
            if n[0:-1] == 'A':
                set_ranks_p2.add(14)
                set_ranks_p2.add(1)
            if n[0:-1] == 'K':
                set_ranks_p2.add(13)
            if n[0:-1] == 'Q':
                set_ranks_p2.add(12)
            if n[0:-1] == 'J':
                set_ranks_p2.add(11)
            if n[0:-1] == '10':
                set_ranks_p2.add(10)
            if n[0:-1] == '9':
                set_ranks_p2.add(9)
            if n[0:-1] == '8':
                set_ranks_p2.add(8)
            if n[0:-1] == '7':
                set_ranks_p2.add(7)
            if n[0:-1] == '6':
                set_ranks_p2.add(6)
            if n[0:-1] == '5':
                set_ranks_p2.add(5)
            if n[0:-1] == '4':
                set_ranks_p2.add(4)
            if n[0:-1] == '3':
                set_ranks_p2.add(3)
            if n[0:-1] == '2':
                set_ranks_p2.add(2)

        # Checking Player 2 for Straight Flush
        if 10 in set_ranks_p2 and 11 in set_ranks_p2 and 12 in set_ranks_p2 and 13 in set_ranks_p2 and 14 in set_ranks_p2:
            top_p2 = 14
            if 'Ah' in hand_p2 or 'Ah' in community:  # Heart check
                if 'Kh' in hand_p2 or 'Kh' in community:
                    if 'Qh' in hand_p2 or 'Qh' in community:
                        if 'Jh' in hand_p2 or 'Jh' in community:
                            if '10h' in hand_p2 or '10h' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if 'Ad' in hand_p2 or 'Ad' in community:  # Diamond check
                if 'Kd' in hand_p2 or 'Kd' in community:
                    if 'Qd' in hand_p2 or 'Qd' in community:
                        if 'Jd' in hand_p2 or 'Jd' in community:
                            if '10d' in hand_p2 or '10d' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if 'Ac' in hand_p2 or 'Ac' in community:  # Club check
                if 'Kc' in hand_p2 or 'Kc' in community:
                    if 'Qc' in hand_p2 or 'Qc' in community:
                        if 'Jc' in hand_p2 or 'Jc' in community:
                            if '10c' in hand_p2 or '10c' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if 'As' in hand_p2 or 'As' in community:  # Spade check
                if 'Ks' in hand_p2 or 'Ks' in community:
                    if 'Qs' in hand_p2 or 'Qs' in community:
                        if 'Js' in hand_p2 or 'Js' in community:
                            if '10s' in hand_p2 or '10s' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8
        elif 9 in set_ranks_p2 and 10 in set_ranks_p2 and 11 in set_ranks_p2 and 12 in set_ranks_p2 and 13 in set_ranks_p2:
            top_p2 = 13

            if 'Kh' in hand_p2 or 'Kh' in community:
                if 'Qh' in hand_p2 or 'Qh' in community:
                    if 'Jh' in hand_p2 or 'Jh' in community:
                        if '10h' in hand_p2 or '10h' in community:
                            if '9h' in hand_p2 or '9h' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if 'Kd' in hand_p2 or 'Kd' in community:
                if 'Qd' in hand_p2 or 'Qd' in community:
                    if 'Jd' in hand_p2 or 'Jd' in community:
                        if '10d' in hand_p2 or '10d' in community:
                            if '9d' in hand_p2 or '9d' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if 'Kc' in hand_p2 or 'Kc' in community:
                if 'Qc' in hand_p2 or 'Qc' in community:
                    if 'Jc' in hand_p2 or 'Jc' in community:
                        if '10c' in hand_p2 or '10c' in community:
                            if '9c' in hand_p2 or '9c' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if 'Ks' in hand_p2 or 'Ks' in community:
                if 'Qs' in hand_p2 or 'Qs' in community:
                    if 'Js' in hand_p2 or 'Js' in community:
                        if '10s' in hand_p2 or '10s' in community:
                            if '9s' in hand_p2 or '9s' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8
        elif 8 in set_ranks_p2 and 9 in set_ranks_p2 and 10 in set_ranks_p2 and 11 in set_ranks_p2 and 12 in set_ranks_p2:
            top_p2 = 12

            if 'Qh' in hand_p2 or 'Qh' in community:
                if 'Jh' in hand_p2 or 'Jh' in community:
                    if '10h' in hand_p2 or '10h' in community:
                        if '9h' in hand_p2 or '9h' in community:
                            if '8h' in hand_p2 or '8h' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if 'Qd' in hand_p2 or 'Qd' in community:
                if 'Jd' in hand_p2 or 'Jd' in community:
                    if '10d' in hand_p2 or '10d' in community:
                        if '9d' in hand_p2 or '9d' in community:
                            if '8d' in hand_p2 or '8d' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if 'Qc' in hand_p2 or 'Qc' in community:
                if 'Jc' in hand_p2 or 'Jc' in community:
                    if '10c' in hand_p2 or '10c' in community:
                        if '9c' in hand_p2 or '9c' in community:
                            if '8c' in hand_p2 or '8c' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if 'Qs' in hand_p2 or 'Qs' in community:
                if 'Js' in hand_p2 or 'Js' in community:
                    if '10s' in hand_p2 or '10s' in community:
                        if '9s' in hand_p2 or '9s' in community:
                            if '8s' in hand_p2 or '8s' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8
        elif 7 in set_ranks_p2 and 8 in set_ranks_p2 and 9 in set_ranks_p2 and 10 in set_ranks_p2 and 11 in set_ranks_p2:
            top_p2 = 11

            if 'Jh' in hand_p2 or 'Jh' in community:
                if '10h' in hand_p2 or '10h' in community:
                    if '9h' in hand_p2 or '9h' in community:
                        if '8h' in hand_p2 or '8h' in community:
                            if '7h' in hand_p2 or '7h' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if 'Jd' in hand_p2 or 'Jd' in community:
                if '10d' in hand_p2 or '10d' in community:
                    if '9d' in hand_p2 or '9d' in community:
                        if '8d' in hand_p2 or '8d' in community:
                            if '7d' in hand_p2 or '7d' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if 'Jc' in hand_p2 or 'Jc' in community:
                if '10c' in hand_p2 or '10c' in community:
                    if '9c' in hand_p2 or '9c' in community:
                        if '8c' in hand_p2 or '8c' in community:
                            if '7c' in hand_p2 or '7c' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if 'Js' in hand_p2 or 'Js' in community:
                if '10s' in hand_p2 or '10s' in community:
                    if '9s' in hand_p2 or '9s' in community:
                        if '8s' in hand_p2 or '8s' in community:
                            if '7s' in hand_p2 or '7s' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8
        elif 6 in set_ranks_p2 and 7 in set_ranks_p2 and 8 in set_ranks_p2 and 9 in set_ranks_p2 and 10 in set_ranks_p2:
            top_p2 = 10

            if '10h' in hand_p2 or '10h' in community:
                if '9h' in hand_p2 or '9h' in community:
                    if '8h' in hand_p2 or '8h' in community:
                        if '7h' in hand_p2 or '7h' in community:
                            if '6h' in hand_p2 or '6h' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if '10d' in hand_p2 or '10d' in community:
                if '9d' in hand_p2 or '9d' in community:
                    if '8d' in hand_p2 or '8d' in community:
                        if '7d' in hand_p2 or '7d' in community:
                            if '6d' in hand_p2 or '6d' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if '10c' in hand_p2 or '10c' in community:
                if '9c' in hand_p2 or '9c' in community:
                    if '8c' in hand_p2 or '8c' in community:
                        if '7c' in hand_p2 or '7c' in community:
                            if '6c' in hand_p2 or '6c' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if '10s' in hand_p2 or '10s' in community:
                if '9s' in hand_p2 or '9s' in community:
                    if '8s' in hand_p2 or '8s' in community:
                        if '7s' in hand_p2 or '7s' in community:
                            if '6s' in hand_p2 or '6s' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8
        elif 5 in set_ranks_p2 and 6 in set_ranks_p2 and 7 in set_ranks_p2 and 8 in set_ranks_p2 and 9 in set_ranks_p2:
            top_p2 = 9

            if '9h' in hand_p2 or '9h' in community:
                if '8h' in hand_p2 or '8h' in community:
                    if '7h' in hand_p2 or '7h' in community:
                        if '6h' in hand_p2 or '6h' in community:
                            if '5h' in hand_p2 or '5h' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if '9d' in hand_p2 or '9d' in community:
                if '8d' in hand_p2 or '8d' in community:
                    if '7d' in hand_p2 or '7d' in community:
                        if '6d' in hand_p2 or '6d' in community:
                            if '5d' in hand_p2 or '5d' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if '9c' in hand_p2 or '9c' in community:
                if '8c' in hand_p2 or '8c' in community:
                    if '7c' in hand_p2 or '7c' in community:
                        if '6c' in hand_p2 or '6c' in community:
                            if '5c' in hand_p2 or '5c' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if '9s' in hand_p2 or '9s' in community:
                if '8s' in hand_p2 or '8s' in community:
                    if '7s' in hand_p2 or '7s' in community:
                        if '6s' in hand_p2 or '6s' in community:
                            if '5s' in hand_p2 or '5s' in community:
                                made_p2 = 8
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8
        elif 4 in set_ranks_p2 and 5 in set_ranks_p2 and 6 in set_ranks_p2 and 7 in set_ranks_p2 and 8 in set_ranks_p2:
            top_p2 = 8

            if '8h' in hand_p2 or '8h' in community:
                if '7h' in hand_p2 or '7h' in community:
                    if '6h' in hand_p2 or '6h' in community:
                        if '5h' in hand_p2 or '5h' in community:
                            if '4h' in hand_p2 or '4h' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if '8d' in hand_p2 or '8d' in community:
                if '7d' in hand_p2 or '7d' in community:
                    if '6d' in hand_p2 or '6d' in community:
                        if '5d' in hand_p2 or '5d' in community:
                            if '4d' in hand_p2 or '4d' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if '8c' in hand_p2 or '8c' in community:
                if '7c' in hand_p2 or '7c' in community:
                    if '6c' in hand_p2 or '6c' in community:
                        if '5c' in hand_p2 or '5c' in community:
                            if '4c' in hand_p2 or '4c' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if '8s' in hand_p2 or '8s' in community:
                if '7s' in hand_p2 or '7s' in community:
                    if '6s' in hand_p2 or '6s' in community:
                        if '5s' in hand_p2 or '5s' in community:
                            if '4s' in hand_p2 or '4s' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8
        elif 3 in set_ranks_p2 and 4 in set_ranks_p2 and 5 in set_ranks_p2 and 6 in set_ranks_p2 and 7 in set_ranks_p2:
            top_p2 = 7

            if '7h' in hand_p2 or '7h' in community:
                if '6h' in hand_p2 or '6h' in community:
                    if '5h' in hand_p2 or '5h' in community:
                        if '4h' in hand_p2 or '4h' in community:
                            if '3h' in hand_p2 or '3h' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if '7d' in hand_p2 or '7d' in community:
                if '6d' in hand_p2 or '6d' in community:
                    if '5d' in hand_p2 or '5d' in community:
                        if '4d' in hand_p2 or '4d' in community:
                            if '3d' in hand_p2 or '3d' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if '7c' in hand_p2 or '7c' in community:
                if '6c' in hand_p2 or '6c' in community:
                    if '5c' in hand_p2 or '5c' in community:
                        if '4c' in hand_p2 or '4c' in community:
                            if '3c' in hand_p2 or '3c' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if '7s' in hand_p2 or '7s' in community:
                if '6s' in hand_p2 or '6s' in community:
                    if '5s' in hand_p2 or '5s' in community:
                        if '4s' in hand_p2 or '4s' in community:
                            if '3s' in hand_p2 or '3s' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8
        elif 2 in set_ranks_p2 and 3 in set_ranks_p2 and 4 in set_ranks_p2 and 5 in set_ranks_p2 and 6 in set_ranks_p2:
            top_p2 = 6

            if '6h' in hand_p2 or '6h' in community:
                if '5h' in hand_p2 or '5h' in community:
                    if '4h' in hand_p2 or '4h' in community:
                        if '3h' in hand_p2 or '3h' in community:
                            if '2h' in hand_p2 or '2h' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if '6d' in hand_p2 or '6d' in community:
                if '5d' in hand_p2 or '5d' in community:
                    if '4d' in hand_p2 or '4d' in community:
                        if '3d' in hand_p2 or '3d' in community:
                            if '2d' in hand_p2 or '2d' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if '6c' in hand_p2 or '6c' in community:
                if '5c' in hand_p2 or '5c' in community:
                    if '4c' in hand_p2 or '4c' in community:
                        if '3c' in hand_p2 or '3c' in community:
                            if '2c' in hand_p2 or '2c' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if '6s' in hand_p2 or '6s' in community:
                if '5s' in hand_p2 or '5s' in community:
                    if '4s' in hand_p2 or '4s' in community:
                        if '3s' in hand_p2 or '3s' in community:
                            if '2s' in hand_p2 or '2s' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8
        elif 1 in set_ranks_p2 and 2 in set_ranks_p2 and 3 in set_ranks_p2 and 4 in set_ranks_p2 and 5 in set_ranks_p2:
            top_p2 = 5

            if '5h' in hand_p2 or '5h' in community:
                if '4h' in hand_p2 or '4h' in community:
                    if '3h' in hand_p2 or '3h' in community:
                        if '2h' in hand_p2 or '2h' in community:
                            if 'Ah' in hand_p2 or 'Ah' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if '5d' in hand_p2 or '5d' in community:
                if '4d' in hand_p2 or '4d' in community:
                    if '3d' in hand_p2 or '3d' in community:
                        if '2d' in hand_p2 or '2d' in community:
                            if 'Ad' in hand_p2 or 'Ad' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if '5c' in hand_p2 or '5c' in community:
                if '4c' in hand_p2 or '4c' in community:
                    if '3c' in hand_p2 or '3c' in community:
                        if '2c' in hand_p2 or '2c' in community:
                            if 'Ac' in hand_p2 or 'Ac' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

            if '5s' in hand_p2 or '5s' in community:
                if '4s' in hand_p2 or '4s' in community:
                    if '3s' in hand_p2 or '3s' in community:
                        if '2s' in hand_p2 or '2s' in community:
                            if 'As' in hand_p2 or 'As' in community:
                                print(name_p2, 'has made a straight flush!')
                                if made_p2 < 8:
                                    made_p2 = 8

        # Comparing hands for showdown
        if made_p1 > made_p2:
            print(name_p1, "wins the hand!")
            award(p1)
        elif made_p2 > made_p1:
            print(name_p2, "wins the hand!")
            award(p2)
        elif made_p1 == 8 and made_p2 == 8:
            if top_p1 > top_p2:
                print(name_p1, "wins the hand!")
                award(p1)
            elif top_p2 > top_p1:
                print(name_p2, "wins the hand!")
                award(p2)
            elif top_p1 == top_p2:
                print("It's a tie!")
                award(tie)
        else:
            quadcheck(hand_p1, hand_p2, community)
    def quadcheck(a, b, c):
        global made_p1
        global made_p2
        global hand_p1
        global hand_p2
        global community

        (num_A, num_K, num_Q, num_J, num_10, num_9, num_8,
         num_7, num_6, num_5, num_4, num_3, num_2) = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        quad_p1 = 0
        quad_p2 = 0
        kicker_p1 = 0
        kicker_p2 = 0

        # Counting the ranks in Player 1's hand'
        for n in a:
            if n[0:-1] == 'A':
                num_A += 1
            if n[0:-1] == 'K':
                num_K += 1
            if n[0:-1] == 'Q':
                num_Q += 1
            if n[0:-1] == 'J':
                num_J += 1
            if n[0:-1] == '10':
                num_10 += 1
            if n[0:-1] == '9':
                num_9 += 1
            if n[0:-1] == '8':
                num_8 += 1
            if n[0:-1] == '7':
                num_7 += 1
            if n[0:-1] == '6':
                num_6 += 1
            if n[0:-1] == '5':
                num_5 += 1
            if n[0:-1] == '4':
                num_4 += 1
            if n[0:-1] == '3':
                num_3 += 1
            if n[0:-1] == '2':
                num_2 += 1

        # Counting the ranks in community
        for n in c:
            if n[0:-1] == 'A':
                num_A += 1
            if n[0:-1] == 'K':
                num_K += 1
            if n[0:-1] == 'Q':
                num_Q += 1
            if n[0:-1] == 'J':
                num_J += 1
            if n[0:-1] == '10':
                num_10 += 1
            if n[0:-1] == '9':
                num_9 += 1
            if n[0:-1] == '8':
                num_8 += 1
            if n[0:-1] == '7':
                num_7 += 1
            if n[0:-1] == '6':
                num_6 += 1
            if n[0:-1] == '5':
                num_5 += 1
            if n[0:-1] == '4':
                num_4 += 1
            if n[0:-1] == '3':
                num_3 += 1
            if n[0:-1] == '2':
                num_2 += 1

        # Did Player 1 make 4oak?
        if num_A == 4:
            if made_p1 < 7:
                made_p1 = 7
                quad_p1 = 14
                print(name_p1, "has made quad Aces!")
        if num_K == 4:
            if made_p1 < 7:
                made_p1 = 7
                quad_p1 = 13
                print(name_p1, "has made quad Kings!")
        if num_Q == 4:
            if made_p1 < 7:
                made_p1 = 7
                quad_p1 = 12
                print(name_p1, "has made quad Queens!")
        if num_J == 4:
            if made_p1 < 7:
                made_p1 = 7
                quad_p1 = 11
                print(name_p1, "has made quad Jacks!")
        if num_10 == 4:
            if made_p1 < 7:
                made_p1 = 7
                quad_p1 = 10
                print(name_p1, "has made quad tens!")
        if num_9 == 4:
            if made_p1 < 7:
                made_p1 = 7
                quad_p1 = 9
                print(name_p1, "has made quad nines!")
        if num_8 == 4:
            if made_p1 < 7:
                made_p1 = 7
                quad_p1 = 8
                print(name_p1, "has made quad eights!")
        if num_7 == 4:
            if made_p1 < 7:
                made_p1 = 7
                quad_p1 = 7
                print(name_p1, "has made quad sevens!")
        if num_6 == 4:
            if made_p1 < 7:
                made_p1 = 7
                quad_p1 = 6
                print(name_p1, "has made quad sixes!")
        if num_5 == 4:
            if made_p1 < 7:
                made_p1 = 7
                quad_p1 = 5
                print(name_p1, "has made quad fives!")
        if num_4 == 4:
            if made_p1 < 7:
                made_p1 = 7
                quad_p1 = 4
                print(name_p1, "has made quad fours!")
        if num_3 == 4:
            if made_p1 < 7:
                made_p1 = 7
                quad_p1 = 3
                print(name_p1, "has made quad threes!")
        if num_2 == 4:
            if made_p1 < 7:
                made_p1 = 7
                quad_p1 = 2
                print(name_p1, "has made quad deuces!")

        # Checking Player 1's kicker_p1
        if made_p1 == 7:
            if num_A < 4 and num_A > 0:
                kicker_p1 = 14
            if num_K < 4 and num_K > 0:
                if kicker_p1 < 14:
                    kicker_p1 = 13
            if num_Q < 4 and num_Q > 0:
                if kicker_p1 < 13:
                    kicker_p1 = 12
            if num_J < 4 and num_J > 0:
                if kicker_p1 < 12:
                    kicker_p1 = 11
            if num_10 < 4 and num_10 > 0:
                if kicker_p1 < 11:
                    kicker_p1 = 10
            if num_9 < 4 and num_9 > 0:
                if kicker_p1 < 10:
                    kicker_p1 = 9
            if num_8 < 4 and num_8 > 0:
                if kicker_p1 < 9:
                    kicker_p1 = 8
            if num_7 < 4 and num_7 > 0:
                if kicker_p1 < 8:
                    kicker_p1 = 7
            if num_6 < 4 and num_6 > 0:
                if kicker_p1 < 7:
                    kicker_p1 = 6
            if num_5 < 4 and num_5 > 0:
                if kicker_p1 < 6:
                    kicker_p1 = 5
            if num_4 < 4 and num_4 > 0:
                if kicker_p1 < 5:
                    kicker_p1 = 4
            if num_3 < 4 and num_3 > 0:
                if kicker_p1 < 4:
                    kicker_p1 = 3
            if num_2 < 4 and num_2 > 0:
                if kicker_p1 < 3:
                    kicker_p1 = 2

        # Resetting for Player 2
        (num_A, num_K, num_Q, num_J, num_10, num_9, num_8,
         num_7, num_6, num_5, num_4, num_3, num_2) = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

        # Counting the ranks in Player 2's hand'
        for n in b:
            if n[0:-1] == 'A':
                num_A += 1
            if n[0:-1] == 'K':
                num_K += 1
            if n[0:-1] == 'Q':
                num_Q += 1
            if n[0:-1] == 'J':
                num_J += 1
            if n[0:-1] == '10':
                num_10 += 1
            if n[0:-1] == '9':
                num_9 += 1
            if n[0:-1] == '8':
                num_8 += 1
            if n[0:-1] == '7':
                num_7 += 1
            if n[0:-1] == '6':
                num_6 += 1
            if n[0:-1] == '5':
                num_5 += 1
            if n[0:-1] == '4':
                num_4 += 1
            if n[0:-1] == '3':
                num_3 += 1
            if n[0:-1] == '2':
                num_2 += 1

        # Counting the ranks in community for Player 2
        for n in c:
            if n[0:-1] == 'A':
                num_A += 1
            if n[0:-1] == 'K':
                num_K += 1
            if n[0:-1] == 'Q':
                num_Q += 1
            if n[0:-1] == 'J':
                num_J += 1
            if n[0:-1] == '10':
                num_10 += 1
            if n[0:-1] == '9':
                num_9 += 1
            if n[0:-1] == '8':
                num_8 += 1
            if n[0:-1] == '7':
                num_7 += 1
            if n[0:-1] == '6':
                num_6 += 1
            if n[0:-1] == '5':
                num_5 += 1
            if n[0:-1] == '4':
                num_4 += 1
            if n[0:-1] == '3':
                num_3 += 1
            if n[0:-1] == '2':
                num_2 += 1

        # Did Player 2 make a 4OAK?
        if num_A == 4:
            if made_p2 < 7:
                made_p2 = 7
                quad_p2 = 14
                print(name_p2, "has made quad Aces!")
        if num_K == 4:
            if made_p2 < 7:
                made_p2 = 7
                quad_p2 = 13
                print(name_p2, "has made quad Kings!")
        if num_Q == 4:
            if made_p2 < 7:
                made_p2 = 7
                quad_p2 = 12
                print(name_p2, "has made quad Queens!")
        if num_J == 4:
            if made_p2 < 7:
                made_p2 = 7
                quad_p2 = 11
                print(name_p2, "has made quad Jacks!")
        if num_10 == 4:
            if made_p2 < 7:
                made_p2 = 7
                quad_p2 = 10
                print(name_p2, "has made quad tens!")
        if num_9 == 4:
            if made_p2 < 7:
                made_p2 = 7
                quad_p2 = 9
                print(name_p2, "has made quad nines!")
        if num_8 == 4:
            if made_p2 < 7:
                made_p2 = 7
                quad_p2 = 8
                print(name_p2, "has made quad eights!")
        if num_7 == 4:
            if made_p2 < 7:
                made_p2 = 7
                quad_p2 = 7
                print(name_p2, "has made quad sevens!")
        if num_6 == 4:
            if made_p2 < 7:
                made_p2 = 7
                quad_p2 = 6
                print(name_p2, "has made quad sixes!")
        if num_5 == 4:
            if made_p2 < 7:
                made_p2 = 7
                quad_p2 = 5
                print(name_p2, "has made quad fives!")
        if num_4 == 4:
            if made_p2 < 7:
                made_p2 = 7
                quad_p2 = 4
                print(name_p2, "has made quad fours!")
        if num_3 == 4:
            if made_p2 < 7:
                made_p2 = 7
                quad_p2 = 3
                print(name_p2, "has made quad threes!")
        if num_2 == 4:
            if made_p2 < 7:
                made_p2 = 7
                quad_p2 = 2
                print(name_p2, "has made quad deuces!")

        # Checking Player 2's kicker_p2
        if made_p2 == 7:
            if num_A < 4 and num_A > 0:
                kicker_p2 = 14
            if num_K < 4 and num_K > 0:
                if kicker_p2 < 14:
                    kicker_p2 = 13
            if num_Q < 4 and num_Q > 0:
                if kicker_p2 < 13:
                    kicker_p2 = 12
            if num_J < 4 and num_J > 0:
                if kicker_p2 < 12:
                    kicker_p2 = 11
            if num_10 < 4 and num_10 > 0:
                if kicker_p2 < 11:
                    kicker_p2 = 10
            if num_9 < 4 and num_9 > 0:
                if kicker_p2 < 10:
                    kicker_p2 = 9
            if num_8 < 4 and num_8 > 0:
                if kicker_p2 < 9:
                    kicker_p2 = 8
            if num_7 < 4 and num_7 > 0:
                if kicker_p2 < 8:
                    kicker_p2 = 7
            if num_6 < 4 and num_6 > 0:
                if kicker_p2 < 7:
                    kicker_p2 = 6
            if num_5 < 4 and num_5 > 0:
                if kicker_p2 < 6:
                    kicker_p2 = 5
            if num_4 < 4 and num_4 > 0:
                if kicker_p2 < 5:
                    kicker_p2 = 4
            if num_3 < 4 and num_3 > 0:
                if kicker_p2 < 4:
                    kicker_p2 = 3
            if num_2 < 4 and num_2 > 0:
                if kicker_p2 < 3:
                    kicker_p2 = 2

        # Comparing hands for showdown
        if made_p1 > made_p2:
            print(name_p1, "wins the hand!")
            award(p1)
        elif made_p2 > made_p1:
            print(name_p2, "wins the hand!")
            award(p2)
        elif made_p1 == 7 and made_p2 == 7:
            if quad_p1 > quad_p2:
                print(name_p1, "wins the hand!")
                award(p1)
            elif quad_p2 > quad_p1:
                print(name_p2, "wins the hand!")
                award(p2)
            elif quad_p1 == quad_p2:
                if kicker_p1 > kicker_p2:
                    print(name_p1, "wins the hand!")
                    award(p1)
                elif kicker_p2 > kicker_p1:
                    print(name_p2, "wins the hand!")
                    award(p2)
                elif kicker_p1 == kicker_p2:
                    print("It's a tie!")
                    award(tie)

        else:
            fullhousecheck(hand_p1, hand_p2, community)
    def fullhousecheck(a, b, c):
        global made_p1
        global made_p2
        global hand_p1
        global hand_p2
        global community

        (num_A, num_K, num_Q, num_J, num_10, num_9, num_8,
         num_7, num_6, num_5, num_4, num_3, num_2) = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        pairs = 0
        sets = 0
        set_p1 = 0
        set_p2 = 0
        pair_p1 = 0
        pair_p2 = 0

        # Counting the ranks in Player 1's hand
        for n in a:
            if n[0:-1] == 'A':
                num_A += 1
            if n[0:-1] == 'K':
                num_K += 1
            if n[0:-1] == 'Q':
                num_Q += 1
            if n[0:-1] == 'J':
                num_J += 1
            if n[0:-1] == '10':
                num_10 += 1
            if n[0:-1] == '9':
                num_9 += 1
            if n[0:-1] == '8':
                num_8 += 1
            if n[0:-1] == '7':
                num_7 += 1
            if n[0:-1] == '6':
                num_6 += 1
            if n[0:-1] == '5':
                num_5 += 1
            if n[0:-1] == '4':
                num_4 += 1
            if n[0:-1] == '3':
                num_3 += 1
            if n[0:-1] == '2':
                num_2 += 1

        # Counting the ranks in community
        for n in c:
            if n[0:-1] == 'A':
                num_A += 1
            if n[0:-1] == 'K':
                num_K += 1
            if n[0:-1] == 'Q':
                num_Q += 1
            if n[0:-1] == 'J':
                num_J += 1
            if n[0:-1] == '10':
                num_10 += 1
            if n[0:-1] == '9':
                num_9 += 1
            if n[0:-1] == '8':
                num_8 += 1
            if n[0:-1] == '7':
                num_7 += 1
            if n[0:-1] == '6':
                num_6 += 1
            if n[0:-1] == '5':
                num_5 += 1
            if n[0:-1] == '4':
                num_4 += 1
            if n[0:-1] == '3':
                num_3 += 1
            if n[0:-1] == '2':
                num_2 += 1

                # Counting Player 1's sets
                if num_A == 3:
                    sets += 1
                    set_p1 = 14
                if num_K == 3:
                    sets += 1
                    if set_p1 < 14:
                        set_p1 = 13
                if num_Q == 3:
                    sets += 1
                    if set_p1 < 13:
                        set_p1 = 12
                if num_J == 3:
                    sets += 1
                    if set_p1 < 12:
                        set_p1 = 11
                if num_10 == 3:
                    sets += 1
                    if set_p1 < 11:
                        set_p1 = 10
                if num_9 == 3:
                    sets += 1
                    if set_p1 < 10:
                        set_p1 = 9
                if num_8 == 3:
                    sets += 1
                    if set_p1 < 9:
                        set_p1 = 8
                if num_7 == 3:
                    sets += 1
                    if set_p1 < 8:
                        set_p1 = 7
                if num_6 == 3:
                    sets += 1
                    if set_p1 < 7:
                        set_p1 = 6
                if num_5 == 3:
                    sets += 1
                    if set_p1 < 6:
                        set_p1 = 5
                if num_4 == 3:
                    sets += 1
                    if set_p1 < 5:
                        set_p1 = 4
                if num_3 == 3:
                    sets += 1
                    if set_p1 < 4:
                        set_p1 = 3
                if num_2 == 3:
                    sets += 1
                    if set_p1 < 3:
                        set_p1 = 2

        # Counting Player 1's sets
        if num_A == 3:
            sets += 1
            set_p1 = 14
        if num_K == 3:
            sets += 1
            if set_p1 < 14:
                set_p1 = 13
        if num_Q == 3:
            sets += 1
            if set_p1 < 13:
                set_p1 = 12
        if num_J == 3:
            sets += 1
            if set_p1 < 12:
                set_p1 = 11
        if num_10 == 3:
            sets += 1
            if set_p1 < 11:
                set_p1 = 10
        if num_9 == 3:
            sets += 1
            if set_p1 < 10:
                set_p1 = 9
        if num_8 == 3:
            sets += 1
            if set_p1 < 9:
                set_p1 = 8
        if num_7 == 3:
            sets += 1
            if set_p1 < 8:
                set_p1 = 7
        if num_6 == 3:
            sets += 1
            if set_p1 < 7:
                set_p1 = 6
        if num_5 == 3:
            sets += 1
            if set_p1 < 6:
                set_p1 = 5
        if num_4 == 3:
            sets += 1
            if set_p1 < 5:
                set_p1 = 4
        if num_3 == 3:
            sets += 1
            if set_p1 < 4:
                set_p1 = 3
        if num_2 == 3:
            sets += 1
            if set_p1 < 3:
                set_p1 = 2



        # Counting Player 1's pairs
        if sets > 0:
            if (num_A >= 2) and (set_p1 != 14):
                pairs += 1
                pair_p1 = 14
            if (num_K >= 2) and (set_p1 != 13):
                pairs += 1
                if pair_p1 < 14:
                    pair_p1 = 13
            if (num_Q >= 2) and (set_p1 != 12):
                pairs += 1
                if pair_p1 < 13:
                    pair_p1 = 12
            if (num_J >= 2) and (set_p1 != 11):
                pairs += 1
                if pair_p1 < 12:
                    pair_p1 = 11
            if (num_10 >= 2) and (set_p1 != 10):
                pairs += 1
                if pair_p1 < 11:
                    pair_p1 = 10
            if (num_9 >= 2) and (set_p1 != 9):
                pairs += 1
                if pair_p1 < 10:
                    pair_p1 = 9
            if (num_8 >= 2) and (set_p1 != 8):
                pairs += 1
                if pair_p1 < 9:
                    pair_p1 = 8
            if (num_7 >= 2)  and (set_p1 != 7):
                pairs += 1
                if pair_p1 < 8:
                    pair_p1 = 7
            if (num_6 >= 2) and (set_p1 != 6):
                pairs += 1
                if pair_p1 < 7:
                    pair_p1 = 6
            if (num_5 >= 2) and (set_p1 != 9):
                pairs += 1
                if pair_p1 < 6:
                    pair_p1 = 5
            if (num_4 >= 2) and (set_p1 != 9):
                pairs += 1
                if pair_p1 < 5:
                    pair_p1 = 4
            if (num_3 >= 2) and (set_p1 != 9):
                pairs += 1
                if pair_p1 < 4:
                    pair_p1 = 3
            if (num_2 >= 2) and (set_p1 != 9):
                pairs += 1
                if pair_p1 < 3:
                    pair_p1 = 2



        # Did Player 1 make a full house?
        if pairs >= 1 and sets >= 1:
            if made_p1 < 6:
                made_p1 = 6
                print(name_p1, "has made a full house!")

        (num_A, num_K, num_Q, num_J, num_10, num_9, num_8,
         num_7, num_6, num_5, num_4, num_3, num_2) = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        pairs = 0
        sets = 0

        # Counting the ranks in Player 2's hand
        for n in b:
            if n[0:-1] == 'A':
                num_A += 1
            if n[0:-1] == 'K':
                num_K += 1
            if n[0:-1] == 'Q':
                num_Q += 1
            if n[0:-1] == 'J':
                num_J += 1
            if n[0:-1] == '10':
                num_10 += 1
            if n[0:-1] == '9':
                num_9 += 1
            if n[0:-1] == '8':
                num_8 += 1
            if n[0:-1] == '7':
                num_7 += 1
            if n[0:-1] == '6':
                num_6 += 1
            if n[0:-1] == '5':
                num_5 += 1
            if n[0:-1] == '4':
                num_4 += 1
            if n[0:-1] == '3':
                num_3 += 1
            if n[0:-1] == '2':
                num_2 += 1

        # Counting the ranks in community
        for n in c:
            if n[0:-1] == 'A':
                num_A += 1
            if n[0:-1] == 'K':
                num_K += 1
            if n[0:-1] == 'Q':
                num_Q += 1
            if n[0:-1] == 'J':
                num_J += 1
            if n[0:-1] == '10':
                num_10 += 1
            if n[0:-1] == '9':
                num_9 += 1
            if n[0:-1] == '8':
                num_8 += 1
            if n[0:-1] == '7':
                num_7 += 1
            if n[0:-1] == '6':
                num_6 += 1
            if n[0:-1] == '5':
                num_5 += 1
            if n[0:-1] == '4':
                num_4 += 1
            if n[0:-1] == '3':
                num_3 += 1
            if n[0:-1] == '2':
                num_2 += 1



        # Counting Player 2's sets
        if num_A == 3:
            sets += 1
            set_p2 = 14
        if num_K == 3:
            sets += 1
            if set_p2 < 14:
                set_p2 = 13
        if num_Q == 3:
            sets += 1
            if set_p2 < 13:
                set_p2 = 12
        if num_J == 3:
            sets += 1
            if set_p2 < 12:
                set_p2 = 11
        if num_10 == 3:
            sets += 1
            if set_p2 < 11:
                set_p2 = 10
        if num_9 == 3:
            sets += 1
            if set_p2 < 10:
                set_p2 = 9
        if num_8 == 3:
            sets += 1
            if set_p2 < 9:
                set_p2 = 8
        if num_7 == 3:
            sets += 1
            if set_p2 < 8:
                set_p2 = 7
        if num_6 == 3:
            sets += 1
            if set_p2 < 7:
                set_p2 = 6
        if num_5 == 3:
            sets += 1
            if set_p2 < 6:
                set_p2 = 5
        if num_4 == 3:
            sets += 1
            if set_p2 < 5:
                set_p2 = 4
        if num_3 == 3:
            sets += 1
            if set_p2 < 4:
                set_p2 = 3
        if num_2 == 3:
            sets += 1
            if set_p2 < 3:
                set_p2 = 2

        # Counting Player 2's pairs
        if sets > 0:
            if (num_A >= 2) and (set_p2 != 14):
                pairs += 1
                pair_p2 = 14
            if (num_K >= 2) and (set_p2 != 13):
                pairs += 1
                if pair_p2 < 14:
                    pair_p2 = 13
            if (num_Q >= 2) and (set_p2 != 12):
                pairs += 1
                if pair_p2 < 13:
                    pair_p2 = 12
            if (num_J >= 2) and (set_p2 != 11):
                pairs += 1
                if pair_p2 < 12:
                    pair_p2 = 11
            if (num_10 >= 2) and (set_p2 != 10):
                pairs += 1
                if pair_p2 < 11:
                    pair_p2 = 10
            if (num_9 >= 2) and (set_p2 != 9):
                pairs += 1
                if pair_p2 < 10:
                    pair_p2 = 9
            if (num_8 >= 2) and (set_p2 != 8):
                pairs += 1
                if pair_p2 < 9:
                    pair_p2 = 8
            if (num_7 >= 2) and (set_p2 != 7):
                pairs += 1
                if pair_p2 < 8:
                    pair_p2 = 7
            if (num_6 >= 2) and (set_p2 != 6):
                pairs += 1
                if pair_p2 < 7:
                    pair_p2 = 6
            if (num_5 >= 2) and (set_p2 != 9):
                pairs += 1
                if pair_p2 < 6:
                    pair_p2 = 5
            if (num_4 >= 2) and (set_p2 != 9):
                pairs += 1
                if pair_p2 < 5:
                    pair_p2 = 4
            if (num_3 >= 2) and (set_p2 != 9):
                pairs += 1
                if pair_p2 < 4:
                    pair_p2 = 3
            if (num_2 >= 2) and (set_p2 != 9):
                pairs += 1
                if pair_p2 < 3:
                    pair_p2 = 2

        # Did Player 2 make a full house?
        if pairs >= 1 and sets >= 1:
            if made_p2 < 6:
                made_p2 = 6
                print(name_p2, "has made a full house!")

        # Comparing hands for showdown
        if made_p1 > made_p2:
            print(name_p1, "wins the hand!")
            award(p1)
        elif made_p2 > made_p1:
            print(name_p2, "wins the hand!")
            award(p2)
        elif made_p1 == 6 and made_p2 == 6:
            if set_p1 > set_p2:
                print(name_p1, "wins!")
                award(p1)
            elif set_p2 > set_p1:
                print(name_p2, "wins!")
                award(p2)
            elif set_p1 == set_p2:
                if pair_p1 > pair_p2:
                    print(name_p1, "wins!")
                    award(p1)
                elif pair_p2 > pair_p1:
                    print(name_p2, "wins!")
                    award(p2)
                elif pair_p1 == pair_p2:
                    print("It's a tie! (ignore kickers, need to code em)")
                    award(tie)
        else:
            flushcheck(hand_p1, hand_p2, community)
    def flushcheck(a, b, c):
        global made_p1, made_p2
        global hand_p1, hand_p2, community
        num_heart, num_diamond, num_club, num_spade = 0, 0, 0, 0

        top_p1 = 0
        top_p2 = 0
        flush_h = 0
        flush_d = 0
        flush_c = 0
        flush_s = 0

        # Checking player 1 cards
        for n in a:
            if n[-1] == 'h':
                num_heart += 1
            if n[-1] == 'd':
                num_diamond += 1
            if n[-1] == 'c':
                num_club += 1
            if n[-1] == 's':
                num_spade += 1

        # Checking community cards
        for n in c:
            if n[-1] == 'h':
                num_heart += 1
            if n[-1] == 'd':
                num_diamond += 1
            if n[-1] == 'c':
                num_club += 1
            if n[-1] == 's':
                num_spade += 1

        # Has player 1 made a flush?
        if num_heart >= 5:
            flush_h = 1
        if num_diamond >= 5:
            flush_d = 1
        if num_club >= 5:
            flush_c = 1
        if num_spade >= 5:
            flush_s = 1

        if num_heart >= 5 or num_diamond >= 5 or num_club >= 5 or num_spade >= 5:
            print(name_p1, "has made a flush!")
            if made_p1 < 5:
                made_p1 = 5

        # Checking Player 1's RANKS to resolve flush ties
        for n in a:
            if flush_h == 1:
                if n == 'Ah':
                    top_p1 = 14
                if n == 'Kh':
                    if top_p1 < 14:
                        top_p1 = 13
                if n == 'Qh':
                    if top_p1 < 13:
                        top_p1 = 12
                if n == 'Jh':
                    if top_p1 < 12:
                        top_p1 = 11
                if n == '10h':
                    if top_p1 < 11:
                        top_p1 = 10
                if n == '9h':
                    if top_p1 < 10:
                        top_p1 = 9
                if n == '8h':
                    if top_p1 < 9:
                        top_p1 = 8
                if n == '7h':
                    if top_p1 < 8:
                        top_p1 = 7
                if n == '6h':
                    if top_p1 < 7:
                        top_p1 = 6
                if n == '5h':
                    if top_p1 < 6:
                        top_p1 = 5
                if n == '4h':
                    if top_p1 < 5:
                        top_p1 = 4
                if n == '3h':
                    if top_p1 < 4:
                        top_p1 = 3
                if n == '2h':
                    if top_p1 < 3:
                        top_p1 = 2
            if flush_d == 1:
                if n == 'Ad':
                    top_p1 = 14
                if n == 'Kd':
                    if top_p1 < 14:
                        top_p1 = 13
                if n == 'Qd':
                    if top_p1 < 13:
                        top_p1 = 12
                if n == 'Jd':
                    if top_p1 < 12:
                        top_p1 = 11
                if n == '10d':
                    if top_p1 < 11:
                        top_p1 = 10
                if n == '9d':
                    if top_p1 < 10:
                        top_p1 = 9
                if n == '8d':
                    if top_p1 < 9:
                        top_p1 = 8
                if n == '7d':
                    if top_p1 < 8:
                        top_p1 = 7
                if n == '6d':
                    if top_p1 < 7:
                        top_p1 = 6
                if n == '5d':
                    if top_p1 < 6:
                        top_p1 = 5
                if n == '4d':
                    if top_p1 < 5:
                        top_p1 = 4
                if n == '3d':
                    if top_p1 < 4:
                        top_p1 = 3
                if n == '2d':
                    if top_p1 < 3:
                        top_p1 = 2
            if flush_c == 1:
                if n == 'Ac':
                    top_p1 = 14
                if n == 'Kc':
                    if top_p1 < 14:
                        top_p1 = 13
                if n == 'Qc':
                    if top_p1 < 13:
                        top_p1 = 12
                if n == 'Jc':
                    if top_p1 < 12:
                        top_p1 = 11
                if n == '10c':
                    if top_p1 < 11:
                        top_p1 = 10
                if n == '9c':
                    if top_p1 < 10:
                        top_p1 = 9
                if n == '8c':
                    if top_p1 < 9:
                        top_p1 = 8
                if n == '7c':
                    if top_p1 < 8:
                        top_p1 = 7
                if n == '6c':
                    if top_p1 < 7:
                        top_p1 = 6
                if n == '5c':
                    if top_p1 < 6:
                        top_p1 = 5
                if n == '4c':
                    if top_p1 < 5:
                        top_p1 = 4
                if n == '3c':
                    if top_p1 < 4:
                        top_p1 = 3
                if n == '2c':
                    if top_p1 < 3:
                        top_p1 = 2
            if flush_s == 1:
                if n == 'As':
                    top_p1 = 14
                if n == 'Ks':
                    if top_p1 < 14:
                        top_p1 = 13
                if n == 'Qs':
                    if top_p1 < 13:
                        top_p1 = 12
                if n == 'Js':
                    if top_p1 < 12:
                        top_p1 = 11
                if n == '10s':
                    if top_p1 < 11:
                        top_p1 = 10
                if n == '9s':
                    if top_p1 < 10:
                        top_p1 = 9
                if n == '8s':
                    if top_p1 < 9:
                        top_p1 = 8
                if n == '7s':
                    if top_p1 < 8:
                        top_p1 = 7
                if n == '6s':
                    if top_p1 < 7:
                        top_p1 = 6
                if n == '5s':
                    if top_p1 < 6:
                        top_p1 = 5
                if n == '4s':
                    if top_p1 < 5:
                        top_p1 = 4
                if n == '3s':
                    if top_p1 < 4:
                        top_p1 = 3
                if n == '2s':
                    if top_p1 < 3:
                        top_p1 = 2

        # Reset for player 2 check
        num_heart, num_diamond, num_club, num_spade = 0, 0, 0, 0
        flush_h, flush_d, flush_c, flush_s = 0, 0, 0, 0

        # Checking player 2 cards
        for n in b:
            if n[-1] == 'h':
                num_heart += 1
            if n[-1] == 'd':
                num_diamond += 1
            if n[-1] == 'c':
                num_club += 1
            if n[-1] == 's':
                num_spade += 1

        # Checking community cards
        for n in c:
            if n[-1] == 'h':
                num_heart += 1
            if n[-1] == 'd':
                num_diamond += 1
            if n[-1] == 'c':
                num_club += 1
            if n[-1] == 's':
                num_spade += 1

        # Has player 2 made a flush?
        if num_heart >= 5:
            flush_h = 1
        if num_diamond >= 5:
            flush_d = 1
        if num_club >= 5:
            flush_c = 1
        if num_spade >= 5:
            flush_s = 1

        if num_heart >= 5 or num_diamond >= 5 or num_club >= 5 or num_spade >= 5:
            print(name_p2, "has made a flush!")
            if made_p2 < 5:
                made_p2 = 5

        # Checking Player 2's RANKS to resolve flush ties
        for n in b:
            if flush_h == 1:
                if n == 'Ah':
                    top_p2 = 14
                if n == 'Kh':
                    if top_p2 < 14:
                        top_p2 = 13
                if n == 'Qh':
                    if top_p2 < 13:
                        top_p2 = 12
                if n == 'Jh':
                    if top_p2 < 12:
                        top_p2 = 11
                if n == '10h':
                    if top_p2 < 11:
                        top_p2 = 10
                if n == '9h':
                    if top_p2 < 10:
                        top_p2 = 9
                if n == '8h':
                    if top_p2 < 9:
                        top_p2 = 8
                if n == '7h':
                    if top_p2 < 8:
                        top_p2 = 7
                if n == '6h':
                    if top_p2 < 7:
                        top_p2 = 6
                if n == '5h':
                    if top_p2 < 6:
                        top_p2 = 5
                if n == '4h':
                    if top_p2 < 5:
                        top_p2 = 4
                if n == '3h':
                    if top_p2 < 4:
                        top_p2 = 3
                if n == '2h':
                    if top_p2 < 3:
                        top_p2 = 2
            if flush_d == 1:
                if n == 'Ad':
                    top_p2 = 14
                if n == 'Kd':
                    if top_p2 < 14:
                        top_p2 = 13
                if n == 'Qd':
                    if top_p2 < 13:
                        top_p2 = 12
                if n == 'Jd':
                    if top_p2 < 12:
                        top_p2 = 11
                if n == '10d':
                    if top_p2 < 11:
                        top_p2 = 10
                if n == '9d':
                    if top_p2 < 10:
                        top_p2 = 9
                if n == '8d':
                    if top_p2 < 9:
                        top_p2 = 8
                if n == '7d':
                    if top_p2 < 8:
                        top_p2 = 7
                if n == '6d':
                    if top_p2 < 7:
                        top_p2 = 6
                if n == '5d':
                    if top_p2 < 6:
                        top_p2 = 5
                if n == '4d':
                    if top_p2 < 5:
                        top_p2 = 4
                if n == '3d':
                    if top_p2 < 4:
                        top_p2 = 3
                if n == '2d':
                    if top_p2 < 3:
                        top_p2 = 2
            if flush_c == 1:
                if n == 'Ac':
                    top_p2 = 14
                if n == 'Kc':
                    if top_p2 < 14:
                        top_p2 = 13
                if n == 'Qc':
                    if top_p2 < 13:
                        top_p2 = 12
                if n == 'Jc':
                    if top_p2 < 12:
                        top_p2 = 11
                if n == '10c':
                    if top_p2 < 11:
                        top_p2 = 10
                if n == '9c':
                    if top_p2 < 10:
                        top_p2 = 9
                if n == '8c':
                    if top_p2 < 9:
                        top_p2 = 8
                if n == '7c':
                    if top_p2 < 8:
                        top_p2 = 7
                if n == '6c':
                    if top_p2 < 7:
                        top_p2 = 6
                if n == '5c':
                    if top_p2 < 6:
                        top_p2 = 5
                if n == '4c':
                    if top_p2 < 5:
                        top_p2 = 4
                if n == '3c':
                    if top_p2 < 4:
                        top_p2 = 3
                if n == '2c':
                    if top_p2 < 3:
                        top_p2 = 2
            if flush_s == 1:
                if n == 'As':
                    top_p2 = 14
                if n == 'Ks':
                    if top_p2 < 14:
                        top_p2 = 13
                if n == 'Qs':
                    if top_p2 < 13:
                        top_p2 = 12
                if n == 'Js':
                    if top_p2 < 12:
                        top_p2 = 11
                if n == '10s':
                    if top_p2 < 11:
                        top_p2 = 10
                if n == '9s':
                    if top_p2 < 10:
                        top_p2 = 9
                if n == '8s':
                    if top_p2 < 9:
                        top_p2 = 8
                if n == '7s':
                    if top_p2 < 8:
                        top_p2 = 7
                if n == '6s':
                    if top_p2 < 7:
                        top_p2 = 6
                if n == '5s':
                    if top_p2 < 6:
                        top_p2 = 5
                if n == '4s':
                    if top_p2 < 5:
                        top_p2 = 4
                if n == '3s':
                    if top_p2 < 4:
                        top_p2 = 3
                if n == '2s':
                    if top_p2 < 3:
                        top_p2 = 2

        # Resolving the showdown
        if made_p1 > made_p2:
            print(name_p1, "wins the hand!")
            award(p1)
        elif made_p2 > made_p1:
            print(name_p2, "wins the hand!")
            award(p2)
        elif made_p1 == 5 and made_p2 == 5:
            if top_p1 > top_p2:
                print(name_p1, "wins the hand!")
                award(p1)
            elif top_p2 > top_p1:
                print(name_p2, "wins the hand!")
                award(p2)
            elif top_p1 == top_p2:
                print(
                    "It's a tie! Honestly I couldn't be fucked to code more once I realize I would have to count EACH rank in descending order.......")
                award(tie)
        else:
            straightcheck(hand_p1, hand_p2, community)
    def straightcheck(a, b, c):
        global made_p1
        global made_p2
        global hand_p1
        global hand_p2
        global community

        rank_A_high = 14
        rank_K = 13
        rank_Q = 12
        rank_J = 11
        rank_10 = 10
        rank_9 = 9
        rank_8 = 8
        rank_7 = 7
        rank_6 = 6
        rank_5 = 5
        rank_4 = 4
        rank_3 = 3
        rank_2 = 2
        rank_A_low = 1

        top_p1 = 0
        top_p2 = 0

        (num_A, num_K, num_Q, num_J, num_10, num_9, num_8,
         num_7, num_6, num_5, num_4, num_3, num_2) = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

        # Counting the ranks in Player 1's hand'
        for n in a:
            if n[0:-1] == 'A':
                num_A += 1
            if n[0:-1] == 'K':
                num_K += 1
            if n[0:-1] == 'Q':
                num_Q += 1
            if n[0:-1] == 'J':
                num_J += 1
            if n[0:-1] == '10':
                num_10 += 1
            if n[0:-1] == '9':
                num_9 += 1
            if n[0:-1] == '8':
                num_8 += 1
            if n[0:-1] == '7':
                num_7 += 1
            if n[0:-1] == '6':
                num_6 += 1
            if n[0:-1] == '5':
                num_5 += 1
            if n[0:-1] == '4':
                num_4 += 1
            if n[0:-1] == '3':
                num_3 += 1
            if n[0:-1] == '2':
                num_2 += 1

        # Counting the ranks in community
        for n in c:
            if n[0:-1] == 'A':
                num_A += 1
            if n[0:-1] == 'K':
                num_K += 1
            if n[0:-1] == 'Q':
                num_Q += 1
            if n[0:-1] == 'J':
                num_J += 1
            if n[0:-1] == '10':
                num_10 += 1
            if n[0:-1] == '9':
                num_9 += 1
            if n[0:-1] == '8':
                num_8 += 1
            if n[0:-1] == '7':
                num_7 += 1
            if n[0:-1] == '6':
                num_6 += 1
            if n[0:-1] == '5':
                num_5 += 1
            if n[0:-1] == '4':
                num_4 += 1
            if n[0:-1] == '3':
                num_3 += 1
            if n[0:-1] == '2':
                num_2 += 1

        set_straight_p1 = set()
        # Getting the rank values for nums as set:
        if num_A >= 1:
            set_straight_p1.add(rank_A_high)
            set_straight_p1.add(rank_A_low)
        if num_K >= 1:
            set_straight_p1.add(rank_K)
        if num_Q >= 1:
            set_straight_p1.add(rank_Q)
        if num_J >= 1:
            set_straight_p1.add(rank_J)
        if num_10 >= 1:
            set_straight_p1.add(rank_10)
        if num_9 >= 1:
            set_straight_p1.add(rank_9)
        if num_8 >= 1:
            set_straight_p1.add(rank_8)
        if num_7 >= 1:
            set_straight_p1.add(rank_7)
        if num_6 >= 1:
            set_straight_p1.add(rank_6)
        if num_5 >= 1:
            set_straight_p1.add(rank_5)
        if num_4 >= 1:
            set_straight_p1.add(rank_4)
        if num_3 >= 1:
            set_straight_p1.add(rank_3)
        if num_2 >= 1:
            set_straight_p1.add(rank_2)

        # Gearing up to check for the straight
        numerics = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        nums = set_straight_p1
        nums = sorted(set(nums))
        gaps = [[s, e] for s, e in zip(nums, nums[1:]) if s + 1 < e]
        edges = iter(nums[:1] + sum(gaps, []) + nums[-1:])
        ranges = (list(zip(edges, edges)))

        # Checking for P1 straight
        is_straight_p1 = 0
        for n in range(len(ranges)):
            former = []
            latter = []

            former_uncut = str(ranges[n])[:4]
            latter_uncut = str(ranges[n])[4:]

            for m in former_uncut:
                if m in numerics:
                    former.append(m)

            former = int(''.join(former))

            for i in latter_uncut:
                if i in numerics:
                    latter.append(i)

            latter = int(''.join(latter))

            if (latter - former) >= 4:
                is_straight_p1 = 1
                top_p1 = latter

        if is_straight_p1 == 1:
            print(name_p1, "has made a straight!")

        (num_A, num_K, num_Q, num_J, num_10, num_9, num_8,
         num_7, num_6, num_5, num_4, num_3, num_2) = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

        # Counting the ranks in Player 2's hand
        for n in b:
            if n[0:-1] == 'A':
                num_A += 1
            if n[0:-1] == 'K':
                num_K += 1
            if n[0:-1] == 'Q':
                num_Q += 1
            if n[0:-1] == 'J':
                num_J += 1
            if n[0:-1] == '10':
                num_10 += 1
            if n[0:-1] == '9':
                num_9 += 1
            if n[0:-1] == '8':
                num_8 += 1
            if n[0:-1] == '7':
                num_7 += 1
            if n[0:-1] == '6':
                num_6 += 1
            if n[0:-1] == '5':
                num_5 += 1
            if n[0:-1] == '4':
                num_4 += 1
            if n[0:-1] == '3':
                num_3 += 1
            if n[0:-1] == '2':
                num_2 += 1

        # Counting the ranks in community
        for n in c:
            if n[0:-1] == 'A':
                num_A += 1
            if n[0:-1] == 'K':
                num_K += 1
            if n[0:-1] == 'Q':
                num_Q += 1
            if n[0:-1] == 'J':
                num_J += 1
            if n[0:-1] == '10':
                num_10 += 1
            if n[0:-1] == '9':
                num_9 += 1
            if n[0:-1] == '8':
                num_8 += 1
            if n[0:-1] == '7':
                num_7 += 1
            if n[0:-1] == '6':
                num_6 += 1
            if n[0:-1] == '5':
                num_5 += 1
            if n[0:-1] == '4':
                num_4 += 1
            if n[0:-1] == '3':
                num_3 += 1
            if n[0:-1] == '2':
                num_2 += 1

        set_straight_p2 = set()
        # Getting the rank values for nums as set:
        if num_A >= 1:
            set_straight_p2.add(rank_A_high)
            set_straight_p2.add(rank_A_low)
        if num_K >= 1:
            set_straight_p2.add(rank_K)
        if num_Q >= 1:
            set_straight_p2.add(rank_Q)
        if num_J >= 1:
            set_straight_p2.add(rank_J)
        if num_10 >= 1:
            set_straight_p2.add(rank_10)
        if num_9 >= 1:
            set_straight_p2.add(rank_9)
        if num_8 >= 1:
            set_straight_p2.add(rank_8)
        if num_7 >= 1:
            set_straight_p2.add(rank_7)
        if num_6 >= 1:
            set_straight_p2.add(rank_6)
        if num_5 >= 1:
            set_straight_p2.add(rank_5)
        if num_4 >= 1:
            set_straight_p2.add(rank_4)
        if num_3 >= 1:
            set_straight_p2.add(rank_3)
        if num_2 >= 1:
            set_straight_p2.add(rank_2)

        # Gearing up to check for the straight
        numerics = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        nums = set_straight_p2
        nums = sorted(set(nums))
        gaps = [[s, e] for s, e in zip(nums, nums[1:]) if s + 1 < e]
        edges = iter(nums[:1] + sum(gaps, []) + nums[-1:])
        ranges = (list(zip(edges, edges)))

        # Checking for P2 straight
        is_straight_p2 = 0
        for n in range(len(ranges)):
            former = []
            latter = []

            former_uncut = str(ranges[n])[:4]
            latter_uncut = str(ranges[n])[4:]

            for m in former_uncut:
                if m in numerics:
                    former.append(m)

            former = int(''.join(former))

            for i in latter_uncut:
                if i in numerics:
                    latter.append(i)

            latter = int(''.join(latter))

            if (latter - former) >= 4:
                is_straight_p2 = 1
                top_p2 = latter

        if is_straight_p2 == 1:
            print(name_p2, "has made a straight!")

        # Comparing hands for showdown
        if is_straight_p1 == 1:
            if made_p1 < 4:
                made_p1 = 4
        if is_straight_p2 == 1:
            if made_p2 < 4:
                made_p2 = 4

        if made_p1 > made_p2:
            print(name_p1, "wins the hand!")
            award(p1)
        elif made_p2 > made_p1:
            print(name_p2, "wins the hand!")
            award(p2)
        elif made_p1 == 4 and made_p2 == 4:
            if top_p1 > top_p2:
                print(name_p1, "wins the hand!")
                award(p1)
            elif top_p2 > top_p1:
                print(name_p2, "wins the hand!")
                award(p2)
            elif top_p1 == top_p2:
                print("It's a tie!")
                award(tie)
        else:
            tripcheck(hand_p1, hand_p2, community)
    def tripcheck(a, b, c):
        global made_p1
        global made_p2
        global hand_p1
        global hand_p2
        global community

        (num_A, num_K, num_Q, num_J, num_10, num_9, num_8,
         num_7, num_6, num_5, num_4, num_3, num_2) = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        set_p1 = 0
        set_p2 = 0
        kicker1_p1 = 0
        kicker2_p1 = 0
        kicker1_p2 = 0
        kicker2_p2 = 0

        # Counting the ranks in Player 1's hand'
        for n in a:
            if n[0:-1] == 'A':
                num_A += 1
            if n[0:-1] == 'K':
                num_K += 1
            if n[0:-1] == 'Q':
                num_Q += 1
            if n[0:-1] == 'J':
                num_J += 1
            if n[0:-1] == '10':
                num_10 += 1
            if n[0:-1] == '9':
                num_9 += 1
            if n[0:-1] == '8':
                num_8 += 1
            if n[0:-1] == '7':
                num_7 += 1
            if n[0:-1] == '6':
                num_6 += 1
            if n[0:-1] == '5':
                num_5 += 1
            if n[0:-1] == '4':
                num_4 += 1
            if n[0:-1] == '3':
                num_3 += 1
            if n[0:-1] == '2':
                num_2 += 1

        # Counting the ranks in community
        for n in c:
            if n[0:-1] == 'A':
                num_A += 1
            if n[0:-1] == 'K':
                num_K += 1
            if n[0:-1] == 'Q':
                num_Q += 1
            if n[0:-1] == 'J':
                num_J += 1
            if n[0:-1] == '10':
                num_10 += 1
            if n[0:-1] == '9':
                num_9 += 1
            if n[0:-1] == '8':
                num_8 += 1
            if n[0:-1] == '7':
                num_7 += 1
            if n[0:-1] == '6':
                num_6 += 1
            if n[0:-1] == '5':
                num_5 += 1
            if n[0:-1] == '4':
                num_4 += 1
            if n[0:-1] == '3':
                num_3 += 1
            if n[0:-1] == '2':
                num_2 += 1

        # Did Player 1 make a set?
        if num_A == 3:
            if made_p1 < 3:
                made_p1 = 3
                set_p1 = 14
                print(name_p1, "has made a set of Aces!")
        if num_K == 3:
            if made_p1 < 3:
                made_p1 = 3
                set_p1 = 13
                print(name_p1, "has made a set of Kings!")
        if num_Q == 3:
            if made_p1 < 3:
                made_p1 = 3
                set_p1 = 12
                print(name_p1, "has made a set of Queens!")
        if num_J == 3:
            if made_p1 < 3:
                made_p1 = 3
                set_p1 = 11
                print(name_p1, "has made a set of Jacks!")
        if num_10 == 3:
            if made_p1 < 3:
                made_p1 = 3
                set_p1 = 10
                print(name_p1, "has made a set of tens!")
        if num_9 == 3:
            if made_p1 < 3:
                made_p1 = 3
                set_p1 = 9
                print(name_p1, "has made a set of nines!")
        if num_8 == 3:
            if made_p1 < 3:
                made_p1 = 3
                set_p1 = 8
                print(name_p1, "has made a set of eights!")
        if num_7 == 3:
            if made_p1 < 3:
                made_p1 = 3
                set_p1 = 7
                print(name_p1, "has made a set of sevens!")
        if num_6 == 3:
            if made_p1 < 3:
                made_p1 = 3
                set_p1 = 6
                print(name_p1, "has made a set of sixes!")
        if num_5 == 3:
            if made_p1 < 3:
                made_p1 = 3
                set_p1 = 5
                print(name_p1, "has made a set of fives!")
        if num_4 == 3:
            if made_p1 < 3:
                made_p1 = 3
                set_p1 = 4
                print(name_p1, "has made a set of fours!")
        if num_3 == 3:
            if made_p1 < 3:
                made_p1 = 3
                set_p1 = 3
                print(name_p1, "has made a set of threes!")
        if num_2 == 3:
            if made_p1 < 3:
                made_p1 = 3
                set_p1 = 2
                print(name_p1, "has made a set of deuces!")

        # Counting Player 1's kicker1_p1 and kicker2_p1
        if made_p1 == 3:
            if num_A == 1:
                kicker1_p1 = 14
            if num_K == 1:
                if kicker1_p1 > 13:
                    kicker2_p1 = 13
                else:
                    kicker1_p1 = 13
            if num_Q == 1:
                if kicker1_p1 > 12:
                    if kicker2_p1 < 12:
                        kicker2_p1 = 12
                else:
                    kicker1_p1 = 12
            if num_J == 1:
                if kicker1_p1 > 11:
                    if kicker2_p1 < 11:
                        kicker2_p1 = 11
                else:
                    kicker1_p1 = 11
            if num_10 == 1:
                if kicker1_p1 > 10:
                    if kicker2_p1 < 10:
                        kicker2_p1 = 10
                else:
                    kicker1_p1 = 10
            if num_9 == 1:
                if kicker1_p1 > 9:
                    if kicker2_p1 < 9:
                        kicker2_p1 = 9
                else:
                    kicker1_p1 = 9
            if num_8 == 1:
                if kicker1_p1 > 8:
                    if kicker2_p1 < 8:
                        kicker2_p1 = 8
                else:
                    kicker1_p1 = 8
            if num_7 == 1:
                if kicker1_p1 > 7:
                    if kicker2_p1 < 7:
                        kicker2_p1 = 7
                else:
                    kicker1_p1 = 7
            if num_6 == 1:
                if kicker1_p1 > 6:
                    if kicker2_p1 < 6:
                        kicker2_p1 = 6
                else:
                    kicker1_p1 = 6
            if num_5 == 1:
                if kicker1_p1 > 5:
                    if kicker2_p1 < 5:
                        kicker2_p1 = 5
                else:
                    kicker1_p1 = 5
            if num_4 == 1:
                if kicker1_p1 > 4:
                    if kicker2_p1 < 4:
                        kicker2_p1 = 4
                else:
                    kicker1_p1 = 4
            if num_3 == 1:
                if kicker1_p1 > 3:
                    if kicker2_p1 < 3:
                        kicker2_p1 = 3
                else:
                    kicker1_p1 = 3
            if num_2 == 1:
                if kicker1_p1 > 2:
                    if kicker2_p1 < 2:
                        kicker2_p1 = 2
                else:
                    kicker1_p1 = 2

        # Resetting for Player 2
        (num_A, num_K, num_Q, num_J, num_10, num_9, num_8,
         num_7, num_6, num_5, num_4, num_3, num_2) = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

        # Counting the ranks in Player 2's hand'
        for n in b:
            if n[0:-1] == 'A':
                num_A += 1
            if n[0:-1] == 'K':
                num_K += 1
            if n[0:-1] == 'Q':
                num_Q += 1
            if n[0:-1] == 'J':
                num_J += 1
            if n[0:-1] == '10':
                num_10 += 1
            if n[0:-1] == '9':
                num_9 += 1
            if n[0:-1] == '8':
                num_8 += 1
            if n[0:-1] == '7':
                num_7 += 1
            if n[0:-1] == '6':
                num_6 += 1
            if n[0:-1] == '5':
                num_5 += 1
            if n[0:-1] == '4':
                num_4 += 1
            if n[0:-1] == '3':
                num_3 += 1
            if n[0:-1] == '2':
                num_2 += 1

        # Counting the ranks in community for Player 2
        for n in c:
            if n[0:-1] == 'A':
                num_A += 1
            if n[0:-1] == 'K':
                num_K += 1
            if n[0:-1] == 'Q':
                num_Q += 1
            if n[0:-1] == 'J':
                num_J += 1
            if n[0:-1] == '10':
                num_10 += 1
            if n[0:-1] == '9':
                num_9 += 1
            if n[0:-1] == '8':
                num_8 += 1
            if n[0:-1] == '7':
                num_7 += 1
            if n[0:-1] == '6':
                num_6 += 1
            if n[0:-1] == '5':
                num_5 += 1
            if n[0:-1] == '4':
                num_4 += 1
            if n[0:-1] == '3':
                num_3 += 1
            if n[0:-1] == '2':
                num_2 += 1

        # Did Player 2 make a set?
        if num_A == 3:
            if made_p2 < 3:
                made_p2 = 3
                set_p2 = 14
                print(name_p2, "has made a set of Aces!")
        if num_K == 3:
            if made_p2 < 3:
                made_p2 = 3
                set_p2 = 13
                print(name_p2, "has made a set of Kings!")
        if num_Q == 3:
            if made_p2 < 3:
                made_p2 = 3
                set_p2 = 12
                print(name_p2, "has made a set of Queens!")
        if num_J == 3:
            if made_p2 < 3:
                made_p2 = 3
                set_p2 = 11
                print(name_p2, "has made a set of Jacks!")
        if num_10 == 3:
            if made_p2 < 3:
                made_p2 = 3
                set_p2 = 10
                print(name_p2, "has made a set of tens!")
        if num_9 == 3:
            if made_p2 < 3:
                made_p2 = 3
                set_p2 = 9
                print(name_p2, "has made a set of nines!")
        if num_8 == 3:
            if made_p2 < 3:
                made_p2 = 3
                set_p2 = 8
                print(name_p2, "has made a set of eights!")
        if num_7 == 3:
            if made_p2 < 3:
                made_p2 = 3
                set_p2 = 7
                print(name_p2, "has made a set of sevens!")
        if num_6 == 3:
            if made_p2 < 3:
                made_p2 = 3
                set_p2 = 6
                print(name_p2, "has made a set of sixes!")
        if num_5 == 3:
            if made_p2 < 3:
                made_p2 = 3
                set_p2 = 5
                print(name_p2, "has made a set of fives!")
        if num_4 == 3:
            if made_p2 < 3:
                made_p2 = 3
                set_p2 = 4
                print(name_p2, "has made a set of fours!")
        if num_3 == 3:
            if made_p2 < 3:
                made_p2 = 3
                set_p2 = 3
                print(name_p2, "has made a set of threes!")
        if num_2 == 3:
            if made_p2 < 3:
                made_p2 = 3
                set_p2 = 2
                print(name_p2, "has made a set of deuces!")

        # Counting Player 2's kicker1_p2 and kicker2_p2
        if made_p2 == 3:
            if num_A == 1:
                kicker1_p2 = 14
            if num_K == 1:
                if kicker1_p2 > 13:
                    kicker2_p2 = 13
                else:
                    kicker1_p2 = 13
            if num_Q == 1:
                if kicker1_p2 > 12:
                    if kicker2_p2 < 12:
                        kicker2_p2 = 12
                else:
                    kicker1_p2 = 12
            if num_J == 1:
                if kicker1_p2 > 11:
                    if kicker2_p2 < 11:
                        kicker2_p2 = 11
                else:
                    kicker1_p2 = 11
            if num_10 == 1:
                if kicker1_p2 > 10:
                    if kicker2_p2 < 10:
                        kicker2_p2 = 10
                else:
                    kicker1_p2 = 10
            if num_9 == 1:
                if kicker1_p2 > 9:
                    if kicker2_p2 < 9:
                        kicker2_p2 = 9
                else:
                    kicker1_p2 = 9
            if num_8 == 1:
                if kicker1_p2 > 8:
                    if kicker2_p2 < 8:
                        kicker2_p2 = 8
                else:
                    kicker1_p2 = 8
            if num_7 == 1:
                if kicker1_p2 > 7:
                    if kicker2_p2 < 7:
                        kicker2_p2 = 7
                else:
                    kicker1_p2 = 7
            if num_6 == 1:
                if kicker1_p2 > 6:
                    if kicker2_p2 < 6:
                        kicker2_p2 = 6
                else:
                    kicker1_p2 = 6
            if num_5 == 1:
                if kicker1_p2 > 5:
                    if kicker2_p2 < 5:
                        kicker2_p2 = 5
                else:
                    kicker1_p2 = 5
            if num_4 == 1:
                if kicker1_p2 > 4:
                    if kicker2_p2 < 4:
                        kicker2_p2 = 4
                else:
                    kicker1_p2 = 4
            if num_3 == 1:
                if kicker1_p2 > 3:
                    if kicker2_p2 < 3:
                        kicker2_p2 = 3
                else:
                    kicker1_p2 = 3
            if num_2 == 1:
                if kicker1_p2 > 2:
                    if kicker2_p2 < 2:
                        kicker2_p2 = 2
                else:
                    kicker1_p2 = 2

        # Comparing hands for showdown
        if made_p1 > made_p2:
            print(name_p1, "wins the hand!")
            award(p1)
        elif made_p2 > made_p1:
            print(name_p2, "wins the hand!")
            award(p2)
        elif made_p1 == 3 and made_p2 == 3:
            if set_p1 > set_p2:
                print(name_p1, "wins the hand!")
                award(p1)
            elif set_p2 > set_p1:
                print(name_p2, "wins the hand!")
                award(p2)
            elif set_p1 == set_p2:
                if kicker1_p1 > kicker1_p2:
                    print(name_p1, "wins the hand!")
                    award(p1)
                elif kicker1_p2 > kicker1_p1:
                    print(name_p2, "wins the hand!")
                    award(p2)
                elif kicker1_p1 == kicker1_p2:
                    if kicker2_p1 > kicker2_p2:
                        print(name_p1, "wins the hand!")
                        award(p1)
                    elif kicker2_p2 > kicker2_p1:
                        print(name_p2, "wins the hand!")
                        award(p2)
                    elif kicker2_p1 == kicker2_p2:
                        print("It's a tie! (Did it count the kickers right?)")
                        award(tie)
        else:
            twopaircheck(hand_p1, hand_p2, community)
    def twopaircheck(a, b, c):
        global made_p1
        global made_p2
        global hand_p1
        global hand_p2
        global community

        (num_A, num_K, num_Q, num_J, num_10, num_9, num_8,
         num_7, num_6, num_5, num_4, num_3, num_2) = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        pairs = 0
        highpair_p1 = 0
        highpair_p2 = 0
        lowpair_p1 = 0
        lowpair_p2 = 0
        kicker_p1 = 0
        kicker_p2 = 0

        # Counting the ranks in Player 1's hand
        for n in a:
            if n[0:-1] == 'A':
                num_A += 1
            if n[0:-1] == 'K':
                num_K += 1
            if n[0:-1] == 'Q':
                num_Q += 1
            if n[0:-1] == 'J':
                num_J += 1
            if n[0:-1] == '10':
                num_10 += 1
            if n[0:-1] == '9':
                num_9 += 1
            if n[0:-1] == '8':
                num_8 += 1
            if n[0:-1] == '7':
                num_7 += 1
            if n[0:-1] == '6':
                num_6 += 1
            if n[0:-1] == '5':
                num_5 += 1
            if n[0:-1] == '4':
                num_4 += 1
            if n[0:-1] == '3':
                num_3 += 1
            if n[0:-1] == '2':
                num_2 += 1

        # Counting the ranks in community
        for n in c:
            if n[0:-1] == 'A':
                num_A += 1
            if n[0:-1] == 'K':
                num_K += 1
            if n[0:-1] == 'Q':
                num_Q += 1
            if n[0:-1] == 'J':
                num_J += 1
            if n[0:-1] == '10':
                num_10 += 1
            if n[0:-1] == '9':
                num_9 += 1
            if n[0:-1] == '8':
                num_8 += 1
            if n[0:-1] == '7':
                num_7 += 1
            if n[0:-1] == '6':
                num_6 += 1
            if n[0:-1] == '5':
                num_5 += 1
            if n[0:-1] == '4':
                num_4 += 1
            if n[0:-1] == '3':
                num_3 += 1
            if n[0:-1] == '2':
                num_2 += 1

        # Counting Player 1's pairs
        if num_A == 2:
            pairs += 1
            highpair_p1 = 14
        if num_K == 2:
            pairs += 1
            if highpair_p1 > 13:
                lowpair_p1 = 13
            else:
                highpair_p1 = 13
        if num_Q == 2:
            pairs += 1
            if highpair_p1 > 12:
                if lowpair_p1 < 12:
                    lowpair_p1 = 12
            else:
                highpair_p1 = 12
        if num_J == 2:
            pairs += 1
            if highpair_p1 > 11:
                if lowpair_p1 < 11:
                    lowpair_p1 = 11
            else:
                highpair_p1 = 11
        if num_10 == 2:
            pairs += 1
            if highpair_p1 > 10:
                if lowpair_p1 < 10:
                    lowpair_p1 = 10
            else:
                highpair_p1 = 10
        if num_9 == 2:
            pairs += 1
            if highpair_p1 > 9:
                if lowpair_p1 < 9:
                    lowpair_p1 = 9
            else:
                highpair_p1 = 9
        if num_8 == 2:
            pairs += 1
            if highpair_p1 > 8:
                if lowpair_p1 < 8:
                    lowpair_p1 = 8
            else:
                highpair_p1 = 8
        if num_7 == 2:
            pairs += 1
            if highpair_p1 > 7:
                if lowpair_p1 < 7:
                    lowpair_p1 = 7
            else:
                highpair_p1 = 7
        if num_6 == 2:
            pairs += 1
            if highpair_p1 > 6:
                if lowpair_p1 < 6:
                    lowpair_p1 = 6
            else:
                highpair_p1 = 6
        if num_5 == 2:
            pairs += 1
            if highpair_p1 > 5:
                if lowpair_p1 < 5:
                    lowpair_p1 = 5
            else:
                highpair_p1 = 5
        if num_4 == 2:
            pairs += 1
            if highpair_p1 > 4:
                if lowpair_p1 < 4:
                    lowpair_p1 = 4
            else:
                highpair_p1 = 4
        if num_3 == 2:
            pairs += 1
            if highpair_p1 > 3:
                if lowpair_p1 < 3:
                    lowpair_p1 = 3
            else:
                highpair_p1 = 3
        if num_2 == 2:
            pairs += 1
            lowpair_p1 = 2

        # Did player 1 get a two pair?
        if pairs >= 2:
            if made_p1 < 2:
                made_p1 = 2
                print(name_p1, "has made a two-pair!")

        # Finding Player 1's kicker
        if made_p1 == 2:
            if num_A > 0:
                if highpair_p1 != 14 and lowpair_p1 != 14:
                    kicker_p1 = 14
            if num_K > 0:
                if highpair_p1 != 13 and lowpair_p1 != 13:
                    if kicker_p1 < 13:
                        kicker_p1 = 13
            if num_Q > 0:
                if highpair_p1 != 12 and lowpair_p1 != 12:
                    if kicker_p1 < 12:
                        kicker_p1 = 12
            if num_J > 0:
                if highpair_p1 != 11 and lowpair_p1 != 11:
                    if kicker_p1 < 11:
                        kicker_p1 = 11
            if num_10 > 0:
                if highpair_p1 != 10 and lowpair_p1 != 10:
                    if kicker_p1 < 10:
                        kicker_p1 = 10
            if num_9 > 0:
                if highpair_p1 != 9 and lowpair_p1 != 9:
                    if kicker_p1 < 9:
                        kicker_p1 = 9
            if num_8 > 0:
                if highpair_p1 != 8 and lowpair_p1 != 8:
                    if kicker_p1 < 8:
                        kicker_p1 = 8
            if num_7 > 0:
                if highpair_p1 != 7 and lowpair_p1 != 7:
                    if kicker_p1 < 7:
                        kicker_p1 = 7
            if num_6 > 0:
                if highpair_p1 != 6 and lowpair_p1 != 6:
                    if kicker_p1 < 6:
                        kicker_p1 = 6
            if num_5 > 0:
                if highpair_p1 != 5 and lowpair_p1 != 5:
                    if kicker_p1 < 5:
                        kicker_p1 = 5
            if num_4 > 0:
                if highpair_p1 != 4 and lowpair_p1 != 4:
                    if kicker_p1 < 4:
                        kicker_p1 = 4
            if num_3 > 0:
                if highpair_p1 != 3 and lowpair_p1 != 3:
                    if kicker_p1 < 3:
                        kicker_p1 = 3
            if num_2 > 0:
                if highpair_p1 != 2 and lowpair_p1 != 2:
                    if kicker_p1 < 2:
                        kicker_p1 = 2

        # Resetting for Player 2
        (num_A, num_K, num_Q, num_J, num_10, num_9, num_8,
         num_7, num_6, num_5, num_4, num_3, num_2) = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        pairs = 0


        # Counting the ranks in Player 2's hand
        for n in b:
            if n[0:-1] == 'A':
                num_A += 1
            if n[0:-1] == 'K':
                num_K += 1
            if n[0:-1] == 'Q':
                num_Q += 1
            if n[0:-1] == 'J':
                num_J += 1
            if n[0:-1] == '10':
                num_10 += 1
            if n[0:-1] == '9':
                num_9 += 1
            if n[0:-1] == '8':
                num_8 += 1
            if n[0:-1] == '7':
                num_7 += 1
            if n[0:-1] == '6':
                num_6 += 1
            if n[0:-1] == '5':
                num_5 += 1
            if n[0:-1] == '4':
                num_4 += 1
            if n[0:-1] == '3':
                num_3 += 1
            if n[0:-1] == '2':
                num_2 += 1

        # Counting the ranks in community
        for n in c:
            if n[0:-1] == 'A':
                num_A += 1
            if n[0:-1] == 'K':
                num_K += 1
            if n[0:-1] == 'Q':
                num_Q += 1
            if n[0:-1] == 'J':
                num_J += 1
            if n[0:-1] == '10':
                num_10 += 1
            if n[0:-1] == '9':
                num_9 += 1
            if n[0:-1] == '8':
                num_8 += 1
            if n[0:-1] == '7':
                num_7 += 1
            if n[0:-1] == '6':
                num_6 += 1
            if n[0:-1] == '5':
                num_5 += 1
            if n[0:-1] == '4':
                num_4 += 1
            if n[0:-1] == '3':
                num_3 += 1
            if n[0:-1] == '2':
                num_2 += 1

        # Counting Player 2's pairs
        if num_A == 2:
            pairs += 1
            highpair_p2 = 14
        if num_K == 2:
            pairs += 1
            if highpair_p2 > 13:
                lowpair_p2 = 13
            else:
                highpair_p2 = 13
        if num_Q == 2:
            pairs += 1
            if highpair_p2 > 12:
                if lowpair_p2 < 12:
                    lowpair_p2 = 12
            else:
                highpair_p2 = 12
        if num_J == 2:
            pairs += 1
            if highpair_p2 > 11:
                if lowpair_p2 < 11:
                    lowpair_p2 = 11
            else:
                highpair_p2 = 11
        if num_10 == 2:
            pairs += 1
            if highpair_p2 > 10:
                if lowpair_p2 < 10:
                    lowpair_p2 = 10
            else:
                highpair_p2 = 10
        if num_9 == 2:
            pairs += 1
            if highpair_p2 > 9:
                if lowpair_p2 < 9:
                    lowpair_p2 = 9
            else:
                highpair_p2 = 9
        if num_8 == 2:
            pairs += 1
            if highpair_p2 > 8:
                if lowpair_p2 < 8:
                    lowpair_p2 = 8
            else:
                highpair_p2 = 8
        if num_7 == 2:
            pairs += 1
            if highpair_p2 > 7:
                if lowpair_p2 < 7:
                    lowpair_p2 = 7
            else:
                highpair_p2 = 7
        if num_6 == 2:
            pairs += 1
            if highpair_p2 > 6:
                if lowpair_p2 < 6:
                    lowpair_p2 = 6
            else:
                highpair_p2 = 6
        if num_5 == 2:
            pairs += 1
            if highpair_p2 > 5:
                if lowpair_p2 < 5:
                    lowpair_p2 = 5
            else:
                highpair_p2 = 5
        if num_4 == 2:
            pairs += 1
            if highpair_p2 > 4:
                if lowpair_p2 < 4:
                    lowpair_p2 = 4
            else:
                highpair_p2 = 4
        if num_3 == 2:
            pairs += 1
            if highpair_p2 > 3:
                if lowpair_p2 < 3:
                    lowpair_p2 = 3
            else:
                highpair_p2 = 3
        if num_2 == 2:
            pairs += 1
            lowpair_p2 = 2

        # Did player 2 get a two pair?
        if pairs >= 2:
            if made_p2 < 2:
                made_p2 = 2
                print(name_p2, "has made a two-pair!")

        # Finding Player 2's kicker
        if made_p2 == 2:
            if num_A > 0:
                if highpair_p2 != 14 and lowpair_p2 != 14:
                    kicker_p2 = 14
            if num_K > 0:
                if highpair_p2 != 13 and lowpair_p2 != 13:
                    if kicker_p2 < 13:
                        kicker_p2 = 13
            if num_Q > 0:
                if highpair_p2 != 12 and lowpair_p2 != 12:
                    if kicker_p2 < 12:
                        kicker_p2 = 12
            if num_J > 0:
                if highpair_p2 != 11 and lowpair_p2 != 11:
                    if kicker_p2 < 11:
                        kicker_p2 = 11
            if num_10 > 0:
                if highpair_p2 != 10 and lowpair_p2 != 10:
                    if kicker_p2 < 10:
                        kicker_p2 = 10
            if num_9 > 0:
                if highpair_p2 != 9 and lowpair_p2 != 9:
                    if kicker_p2 < 9:
                        kicker_p2 = 9
            if num_8 > 0:
                if highpair_p2 != 8 and lowpair_p2 != 8:
                    if kicker_p2 < 8:
                        kicker_p2 = 8
            if num_7 > 0:
                if highpair_p2 != 7 and lowpair_p2 != 7:
                    if kicker_p2 < 7:
                        kicker_p2 = 7
            if num_6 > 0:
                if highpair_p2 != 6 and lowpair_p2 != 6:
                    if kicker_p2 < 6:
                        kicker_p2 = 6
            if num_5 > 0:
                if highpair_p2 != 5 and lowpair_p2 != 5:
                    if kicker_p2 < 5:
                        kicker_p2 = 5
            if num_4 > 0:
                if highpair_p2 != 4 and lowpair_p2 != 4:
                    if kicker_p2 < 4:
                        kicker_p2 = 4
            if num_3 > 0:
                if highpair_p2 != 3 and lowpair_p2 != 3:
                    if kicker_p2 < 3:
                        kicker_p2 = 3
            if num_2 > 0:
                if highpair_p2 != 2 and lowpair_p2 != 2:
                    if kicker_p2 < 2:
                        kicker_p2 = 2

        # Comparing hands for showdown
        if made_p1 > made_p2:
            print(name_p1, "wins the hand!")
            award(p1)
        elif made_p2 > made_p1:
            print(name_p2, "wins the hand!")
            award(p2)
        elif made_p1 == 2 and made_p2 == 2:
            if highpair_p1 > highpair_p2:
                print(name_p1, "wins the hand!")
                award(p1)
            elif highpair_p2 > highpair_p1:
                print(name_p2, "wins the hand!")
                award(p2)
            elif highpair_p1 == highpair_p2:
                if lowpair_p1 > lowpair_p2:
                    print(name_p1, "wins the hand!")
                    award(p1)
                elif lowpair_p2 > lowpair_p1:
                    print(name_p2, "wins the hand!")
                    award(p2)
                elif lowpair_p1 == lowpair_p2:
                    if kicker_p1 > kicker_p2:
                        print(name_p1, "wins the hand!")
                        award(p1)
                    elif kicker_p2 > kicker_p1:
                        print(name_p2, 'wins the hand!')
                        award(p2)
                    elif kicker_p1 == kicker_p2:
                        print("It's a tie! (Did it count the kicker right?)")
                        award(tie)
        else:
            paircheck(hand_p1, hand_p2, community)
    def paircheck(a, b, c):
        global made_p1
        global made_p2
        global hand_p1
        global hand_p2
        global community

        (num_A, num_K, num_Q, num_J, num_10, num_9, num_8,
         num_7, num_6, num_5, num_4, num_3, num_2) = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        pair_p1 = 0
        pair_p2 = 0
        kicker1_p1 = 0
        kicker2_p1 = 0
        kicker3_p1 = 0
        kicker1_p2 = 0
        kicker2_p2 = 0
        kicker3_p2 = 0

        # Counting the ranks in Player 1's hand'
        for n in a:
            if n[0:-1] == 'A':
                num_A += 1
            if n[0:-1] == 'K':
                num_K += 1
            if n[0:-1] == 'Q':
                num_Q += 1
            if n[0:-1] == 'J':
                num_J += 1
            if n[0:-1] == '10':
                num_10 += 1
            if n[0:-1] == '9':
                num_9 += 1
            if n[0:-1] == '8':
                num_8 += 1
            if n[0:-1] == '7':
                num_7 += 1
            if n[0:-1] == '6':
                num_6 += 1
            if n[0:-1] == '5':
                num_5 += 1
            if n[0:-1] == '4':
                num_4 += 1
            if n[0:-1] == '3':
                num_3 += 1
            if n[0:-1] == '2':
                num_2 += 1

        # Counting the ranks in community
        for n in c:
            if n[0:-1] == 'A':
                num_A += 1
            if n[0:-1] == 'K':
                num_K += 1
            if n[0:-1] == 'Q':
                num_Q += 1
            if n[0:-1] == 'J':
                num_J += 1
            if n[0:-1] == '10':
                num_10 += 1
            if n[0:-1] == '9':
                num_9 += 1
            if n[0:-1] == '8':
                num_8 += 1
            if n[0:-1] == '7':
                num_7 += 1
            if n[0:-1] == '6':
                num_6 += 1
            if n[0:-1] == '5':
                num_5 += 1
            if n[0:-1] == '4':
                num_4 += 1
            if n[0:-1] == '3':
                num_3 += 1
            if n[0:-1] == '2':
                num_2 += 1

        # Did player 1 make a pair?
        if num_A == 2:
            print(name_p1, "has made a pair of Aces!")
            made_p1 = 1
            pair_p1 = 14
        if num_K == 2:
            print(name_p1, "has made a pair of Kings!")
            made_p1 = 1
            pair_p1 = 13
        if num_Q == 2:
            print(name_p1, "has made a pair of Queens!")
            made_p1 = 1
            pair_p1 = 12
        if num_J == 2:
            print(name_p1, "has made a pair of Jacks!")
            made_p1 = 1
            pair_p1 = 11
        if num_10 == 2:
            print(name_p1, "has made a pair of tens!")
            made_p1 = 1
            pair_p1 = 10
        if num_9 == 2:
            print(name_p1, "has made a pair of nines!")
            made_p1 = 1
            pair_p1 = 9
        if num_8 == 2:
            print(name_p1, "has made a pair of eights!")
            made_p1 = 1
            pair_p1 = 8
        if num_7 == 2:
            print(name_p1, "has made a pair of sevens!")
            made_p1 = 1
            pair_p1 = 7
        if num_6 == 2:
            print(name_p1, "has made a pair of sixes!")
            made_p1 = 1
            pair_p1 = 6
        if num_5 == 2:
            print(name_p1, "has made a pair of fives!")
            made_p1 = 1
            pair_p1 = 5
        if num_4 == 2:
            print(name_p1, "has made a pair of fours!")
            made_p1 = 1
            pair_p1 = 4
        if num_3 == 2:
            print(name_p1, "has made a pair of threes!")
            made_p1 = 1
            pair_p1 = 3
        if num_2 == 2:
            print(name_p1, "has made a pair of deuces!")
            made_p1 = 1
            pair_p1 = 2

        # Looking for P1s kicker1_p1, kicker2_p1,kicker3_p1:
        if made_p1 == 1:
            if num_A == 1:
                kicker1_p1 = 14
            if num_K == 1:
                if kicker1_p1 > 13:
                    kicker2_p1 = 13
                else:
                    kicker1_p1 = 13
            if num_Q == 1:
                if kicker1_p1 > 12:
                    if kicker2_p1 > 12:
                        kicker3_p1 = 12
                    else:
                        kicker2_p1 = 12
                else:
                    kicker1_p1 = 12
            if num_J == 1:
                if kicker1_p1 > 11:
                    if kicker2_p1 > 11:
                        if kicker3_p1 < 11:
                            kicker3_p1 = 11
                    else:
                        kicker2_p1 = 11
                else:
                    kicker1_p1 = 11
            if num_10 == 1:
                if kicker1_p1 > 10:
                    if kicker2_p1 > 10:
                        if kicker3_p1 < 10:
                            kicker3_p1 = 10
                    else:
                        kicker2_p1 = 10
                else:
                    kicker1_p1 = 10
            if num_9 == 1:
                if kicker1_p1 > 9:
                    if kicker2_p1 > 9:
                        if kicker3_p1 < 9:
                            kicker3_p1 = 9
                    else:
                        kicker2_p1 = 9
                else:
                    kicker1_p1 = 9
            if num_8 == 1:
                if kicker1_p1 > 8:
                    if kicker2_p1 > 8:
                        if kicker3_p1 < 8:
                            kicker3_p1 = 8
                    else:
                        kicker2_p1 = 8
                else:
                    kicker1_p1 = 8
            if num_7 == 1:
                if kicker1_p1 > 7:
                    if kicker2_p1 > 7:
                        if kicker3_p1 < 7:
                            kicker3_p1 = 7
                    else:
                        kicker2_p1 = 7
                else:
                    kicker1_p1 = 7
            if num_6 == 1:
                if kicker1_p1 > 6:
                    if kicker2_p1 > 6:
                        if kicker3_p1 < 6:
                            kicker3_p1 = 6
                    else:
                        kicker2_p1 = 6
                else:
                    kicker1_p1 = 6
            if num_5 == 1:
                if kicker1_p1 > 5:
                    if kicker2_p1 > 5:
                        if kicker3_p1 < 5:
                            kicker3_p1 = 5
                    else:
                        kicker2_p1 = 5
                else:
                    kicker1_p1 = 5
            if num_4 == 1:
                if kicker1_p1 > 4:
                    if kicker2_p1 > 4:
                        if kicker3_p1 < 4:
                            kicker3_p1 = 4
                    else:
                        kicker2_p1 = 4
                else:
                    kicker1_p1 = 4
            if num_3 == 1:
                if kicker1_p1 > 3:
                    if kicker2_p1 > 3:
                        if kicker3_p1 < 3:
                            kicker3_p1 = 3
                    else:
                        kicker2_p1 = 3
                else:
                    kicker1_p1 = 3
            if num_2 == 1:
                if kicker1_p1 > 2:
                    if kicker2_p1 > 2:
                        if kicker3_p1 < 2:
                            kicker3_p1 = 2
                    else:
                        kicker2_p1 = 2
                else:
                    kicker1_p1 = 2

        # Resetting for Player 2
        (num_A, num_K, num_Q, num_J, num_10, num_9, num_8,
         num_7, num_6, num_5, num_4, num_3, num_2) = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

        # Counting the ranks in Player 2's hand'
        for n in b:
            if n[0:-1] == 'A':
                num_A += 1
            if n[0:-1] == 'K':
                num_K += 1
            if n[0:-1] == 'Q':
                num_Q += 1
            if n[0:-1] == 'J':
                num_J += 1
            if n[0:-1] == '10':
                num_10 += 1
            if n[0:-1] == '9':
                num_9 += 1
            if n[0:-1] == '8':
                num_8 += 1
            if n[0:-1] == '7':
                num_7 += 1
            if n[0:-1] == '6':
                num_6 += 1
            if n[0:-1] == '5':
                num_5 += 1
            if n[0:-1] == '4':
                num_4 += 1
            if n[0:-1] == '3':
                num_3 += 1
            if n[0:-1] == '2':
                num_2 += 1

        # Counting the ranks in community for Player 2
        for n in c:
            if n[0:-1] == 'A':
                num_A += 1
            if n[0:-1] == 'K':
                num_K += 1
            if n[0:-1] == 'Q':
                num_Q += 1
            if n[0:-1] == 'J':
                num_J += 1
            if n[0:-1] == '10':
                num_10 += 1
            if n[0:-1] == '9':
                num_9 += 1
            if n[0:-1] == '8':
                num_8 += 1
            if n[0:-1] == '7':
                num_7 += 1
            if n[0:-1] == '6':
                num_6 += 1
            if n[0:-1] == '5':
                num_5 += 1
            if n[0:-1] == '4':
                num_4 += 1
            if n[0:-1] == '3':
                num_3 += 1
            if n[0:-1] == '2':
                num_2 += 1

        # Did player 2 make a pair?
        if num_A == 2:
            print(name_p2, "has made a pair of Aces!")
            made_p2 = 1
            pair_p2 = 14
        if num_K == 2:
            print(name_p2, "has made a pair of Kings!")
            made_p2 = 1
            pair_p2 = 13
        if num_Q == 2:
            print(name_p2, "has made a pair of Queens!")
            made_p2 = 1
            pair_p2 = 12
        if num_J == 2:
            print(name_p2, "has made a pair of Jacks!")
            made_p2 = 1
            pair_p2 = 11
        if num_10 == 2:
            print(name_p2, "has made a pair of tens!")
            made_p2 = 1
            pair_p2 = 10
        if num_9 == 2:
            print(name_p2, "has made a pair of nines!")
            made_p2 = 1
            pair_p2 = 9
        if num_8 == 2:
            print(name_p2, "has made a pair of eights!")
            made_p2 = 1
            pair_p2 = 8
        if num_7 == 2:
            print(name_p2, "has made a pair of sevens!")
            made_p2 = 1
            pair_p2 = 7
        if num_6 == 2:
            print(name_p2, "has made a pair of sixes!")
            made_p2 = 1
            pair_p2 = 6
        if num_5 == 2:
            print(name_p2, "has made a pair of fives!")
            made_p2 = 1
            pair_p2 = 5
        if num_4 == 2:
            print(name_p2, "has made a pair of fours!")
            made_p2 = 1
            pair_p2 = 4
        if num_3 == 2:
            print(name_p2, "has made a pair of threes!")
            made_p2 = 1
            pair_p2 = 3
        if num_2 == 2:
            print(name_p2, "has made a pair of deuces!")
            made_p2 = 1
            pair_p2 = 2

        # Finding Player 2's kicker1_p2,kicker2_p2,kicker3_p2
        if made_p2 == 1:
            if num_A == 1:
                kicker1_p2 = 14
            if num_K == 1:
                if kicker1_p2 > 13:
                    kicker2_p2 = 13
                else:
                    kicker1_p2 = 13
            if num_Q == 1:
                if kicker1_p2 > 12:
                    if kicker2_p2 > 12:
                        kicker3_p2 = 12
                    else:
                        kicker2_p2 = 12
                else:
                    kicker1_p2 = 12
            if num_J == 1:
                if kicker1_p2 > 11:
                    if kicker2_p2 > 11:
                        if kicker3_p2 < 11:
                            kicker3_p2 = 11
                    else:
                        kicker2_p2 = 11
                else:
                    kicker1_p2 = 11
            if num_10 == 1:
                if kicker1_p2 > 10:
                    if kicker2_p2 > 10:
                        if kicker3_p2 < 10:
                            kicker3_p2 = 10
                    else:
                        kicker2_p2 = 10
                else:
                    kicker1_p2 = 10
            if num_9 == 1:
                if kicker1_p2 > 9:
                    if kicker2_p2 > 9:
                        if kicker3_p2 < 9:
                            kicker3_p2 = 9
                    else:
                        kicker2_p2 = 9
                else:
                    kicker1_p2 = 9
            if num_8 == 1:
                if kicker1_p2 > 8:
                    if kicker2_p2 > 8:
                        if kicker3_p2 < 8:
                            kicker3_p2 = 8
                    else:
                        kicker2_p2 = 8
                else:
                    kicker1_p2 = 8
            if num_7 == 1:
                if kicker1_p2 > 7:
                    if kicker2_p2 > 7:
                        if kicker3_p2 < 7:
                            kicker3_p2 = 7
                    else:
                        kicker2_p2 = 7
                else:
                    kicker1_p2 = 7
            if num_6 == 1:
                if kicker1_p2 > 6:
                    if kicker2_p2 > 6:
                        if kicker3_p2 < 6:
                            kicker3_p2 = 6
                    else:
                        kicker2_p2 = 6
                else:
                    kicker1_p2 = 6
            if num_5 == 1:
                if kicker1_p2 > 5:
                    if kicker2_p2 > 5:
                        if kicker3_p2 < 5:
                            kicker3_p2 = 5
                    else:
                        kicker2_p2 = 5
                else:
                    kicker1_p2 = 5
            if num_4 == 1:
                if kicker1_p2 > 4:
                    if kicker2_p2 > 4:
                        if kicker3_p2 < 4:
                            kicker3_p2 = 4
                    else:
                        kicker2_p2 = 4
                else:
                    kicker1_p2 = 4
            if num_3 == 1:
                if kicker1_p2 > 3:
                    if kicker2_p2 > 3:
                        if kicker3_p2 < 3:
                            kicker3_p2 = 3
                    else:
                        kicker2_p2 = 3
                else:
                    kicker1_p2 = 3
            if num_2 == 1:
                if kicker1_p2 > 2:
                    if kicker2_p2 > 2:
                        if kicker3_p2 < 2:
                            kicker3_p2 = 2
                    else:
                        kicker2_p2 = 2
                else:
                    kicker1_p2 = 2

        # Comparing for showdown
        if made_p1 > made_p2:
            print(name_p1, "wins the hand!")
            award(p1)
        elif made_p2 > made_p1:
            print(name_p2, "wins the hand!")
            award(p2)
        elif made_p1 == 1 and made_p2 == 1:
            if pair_p1 > pair_p2:
                print(name_p1, "wins the hand!")
                award(p1)
            elif pair_p2 > pair_p1:
                print(name_p2, "wins the hand!")
                award(p2)
            elif pair_p1 == pair_p2:
                if kicker1_p1 > kicker1_p2:
                    print(name_p1, "wins the hand!")
                    award(p1)
                elif kicker1_p2 > kicker1_p1:
                    print(name_p2, 'wins the hand!')
                    award(p2)
                elif kicker1_p2 == kicker1_p2:
                    if kicker2_p1 > kicker2_p2:
                        print(name_p1, "wins the hand!")
                        award(p1)
                    elif kicker2_p2 > kicker2_p1:
                        print(name_p2, 'wins the hand!')
                        award(p2)
                    elif kicker2_p1 == kicker2_p2:
                        if kicker3_p1 > kicker3_p2:
                            print(name_p1, "wins the hand!")
                            award(p1)
                        elif kicker3_p2 > kicker3_p1:
                            print(name_p2, 'wins the hand!')
                            award(p2)
                        elif kicker3_p1 == kicker3_p2:
                            print("It's a tie! (Did it count the kickers right?)")
                            award(tie)
        else:
            highcheck(hand_p1, hand_p2, community)
    def highcheck(a, b, c):
        global made_p1
        global made_p2
        global hand_p1
        global hand_p2
        global community

        # Resetting counts for individual cards in hand
        (num_A_1, num_K_1, num_Q_1, num_J_1, num_10_1, num_9_1, num_8_1,
         num_7_1, num_6_1, num_5_1, num_4_1, num_3_1, num_2_1) = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        (num_A_2, num_K_2, num_Q_2, num_J_2, num_10_2, num_9_2, num_8_2,
         num_7_2, num_6_2, num_5_2, num_4_2, num_3_2, num_2_2) = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

        # Counting player 1's card to find the highest
        for n in a:
            if n[0:-1] == 'A':
                num_A_1 += 1
            if n[0:-1] == 'K':
                num_K_1 += 1
            if n[0:-1] == 'Q':
                num_Q_1 += 1
            if n[0:-1] == 'J':
                num_J_1 += 1
            if n[0:-1] == '10':
                num_10_1 += 1
            if n[0:-1] == '9':
                num_9_1 += 1
            if n[0:-1] == '8':
                num_8_1 += 1
            if n[0:-1] == '7':
                num_7_1 += 1
            if n[0:-1] == '6':
                num_6_1 += 1
            if n[0:-1] == '5':
                num_5_1 += 1
            if n[0:-1] == '4':
                num_4_1 += 1
            if n[0:-1] == '3':
                num_3_1 += 1
            if n[0:-1] == '2':
                num_2_1 += 1

        # Counting player 2's card to find the highest
        for n in b:
            if n[0:-1] == 'A':
                num_A_2 += 1
            if n[0:-1] == 'K':
                num_K_2 += 1
            if n[0:-1] == 'Q':
                num_Q_2 += 1
            if n[0:-1] == 'J':
                num_J_2 += 1
            if n[0:-1] == '10':
                num_10_2 += 1
            if n[0:-1] == '9':
                num_9_2 += 1
            if n[0:-1] == '8':
                num_8_2 += 1
            if n[0:-1] == '7':
                num_7_2 += 1
            if n[0:-1] == '6':
                num_6_2 += 1
            if n[0:-1] == '5':
                num_5_2 += 1
            if n[0:-1] == '4':
                num_4_2 += 1
            if n[0:-1] == '3':
                num_3_2 += 1
            if n[0:-1] == '2':
                num_2_2 += 1

        # Comparing to see who has the highest card and announcing the victor.
        # Code something for pot keeping
        if num_A_1 > num_A_2:
            print(name_p1, "wins with an Ace high!")
            award(p1)
        if num_A_1 < num_A_2:
            print(name_p2, "wins with an Ace high!")
            award(p2)
        elif num_K_1 > num_K_2:
            print(name_p1, "wins with a King high!")
            award(p1)
        elif num_K_1 < num_K_2:
            print(name_p2, "wins with a King high!")
            award(p2)
        elif num_Q_1 > num_Q_2:
            print(name_p1, "wins with a Queen high!")
            award(p1)
        elif num_Q_1 < num_Q_2:
            print(name_p2, "wins with a Queen high!")
            award(p2)
        elif num_J_1 > num_J_2:
            print(name_p1, "wins with a Jack high!")
            award(p1)
        elif num_J_1 < num_J_2:
            print(name_p2, "wins with a Jack high!")
            award(p2)
        elif num_10_1 > num_10_2:
            print(name_p1, "wins with a ten high!")
            award(p1)
        elif num_10_1 < num_10_2:
            print(name_p2, "wins with a ten high!")
            award(p2)
        elif num_9_1 > num_9_2:
            print(name_p1, "wins with a nine high!")
            award(p1)
        elif num_9_1 < num_9_2:
            print(name_p2, "wins with a nine high!")
            award(p2)
        elif num_8_1 > num_8_2:
            print(name_p1, "wins with a eight high!")
            award(p1)
        elif num_8_1 < num_8_2:
            print(name_p2, "wins with a eight high!")
            award(p2)
        elif num_7_1 > num_7_2:
            print(name_p1, "wins with a seven high!")
            award(p1)
        elif num_7_1 < num_7_2:
            print(name_p2, "wins with a seven high!")
            award(p2)
        elif num_6_1 > num_6_2:
            print(name_p1, "wins with a six high!")
            award(p1)
        elif num_6_1 < num_6_2:
            print(name_p2, "wins with a six high!")
            award(p2)
        elif num_5_1 > num_5_2:
            print(name_p1, "wins with a five high! Ouch!")
            award(p1)
        elif num_5_1 < num_5_2:
            print(name_p2, "wins with a five high! Ouch!")
            award(p2)
        elif num_4_1 > num_4_2:
            print(name_p1, "wins with a four high! Yikes!")
            award(p1)
        elif num_4_1 < num_4_2:
            print(name_p2, "wins with a four high! Yikes!")
            award(p2)
        elif num_3_1 > num_3_2:
            print(name_p1, "wins with a three high! ... wait, that's not possible, is it?")
            award(p1)
        elif num_3_1 < num_3_2:
            print(name_p2, "wins with a three high! ... wait, that's not possible, is it?")
            award(p2)
        elif num_2_1 > num_2_2:
            print(name_p1, "wins with a deuce high! ... wait, there's no way that's even possible!")
            award(p1)
        elif num_2_1 < num_2_2:
            print(name_p2, "wins with a deuce high! ... wait, there's no way that's even possible!")
            award(p2)
        else:
            print("Somehow, some way, NOBODY won. What???")
            award(tie)

    royalflushcheck(hand_p1, hand_p2, community)    # Starts the daisy-chain to run the nested functions in the resolver.


#######################################################################################################################
# THE GAME!!!
# Player 1's turn
def play_p1():
    global pot, chips_p1, chips_p2
    global check_p1, bet_p1, raised_p1
    global check_p2, bet_p2, raised_p2
    global both_check
    global to_call_p1, to_call_p2

    if chips_p1 <= 0: showdown()

    # Resetting variables
    check_p1, bet_p1, raised_p1 = False, False, False
    size, to_call_p2 = 0, 0
    next_player = ''

    # Clearing the screen and reviewing the state of playing:
    print()
    print()
    print()
    print()
    print()
    print('********************************', name_p1, '********************************')
    print()

    # Review the state of play
    if stage == 1: print('Current stage: PREFLOP.')
    if stage == 2: print('Current stage: FLOP.')
    if stage == 3: print('Current stage: TURN.')
    if stage == 4: print('Current stage: RIVER.')
    if stage >= 2: print('The community cards are:', community)
    print(f'{name_p1}, you currently have {chips_p1} chips.')
    print(f'The pot size is currently {pot} chips.')
    print(f'Your opponent {name_p2} currently has {chips_p2} chips.')
    input(f"About to reveal {name_p1}'s cards. Press ENTER when {name_p2} is not looking.")
    print(f"Your cards are: {hand_p1}")

    if raised_p2 == True:
        if chips_p2 == 0 or to_call_p1 >= chips_p1:
            opallin_p1()
        else:
            opraise_p1()

    elif bet_p2 == True:
        if chips_p2 == 0 or to_call_p1 >= chips_p1:
            opallin_p1()
        else:
            opbet_p1()

    elif check_p2 == True: opcheck_p1()

    else: newstage_p1()

# Start new STAGE
def newstage_p1():
    global pot, chips_p1, chips_p2
    global check_p1, bet_p1, raised_p1
    global both_check
    global to_call_p1, to_call_p2

    decision = str.lower(input(f'{name_p1} to start. Will you CHECK or BET?'))[0]
    while decision != 'c' and decision != 'b':
        decision = str.lower(input('You must CHECK or BET.'))[0]
    if decision == 'c':
        both_check += 1
        if both_check == 2:
            next_player = 'p2'
            dealer()
        else:
            check_p1 = True
            play_p2()
    if decision == 'b':
        size = int(input('Bet how many chips? '))
        while size <= 0:
            size = int(input("You must bet positive number of chips. Bet how many chips? "))
        while size > chips_p1:
            size = int(input(f"You only have {chips_p1} chips! Bet how many chips?"))
        while size > (chips_p2 - to_call_p2):
            size = int(
                input(f"You may bet no more than your opponent's remaining {chips_p2} chips. Bet how many chips?"))
        chips_p1 -= size
        pot += size
        to_call_p2 += size
        if chips_p1 <= 0:
            print(name_p1, 'has gone ALL-IN!')
        bet_p1 = True
        play_p2()

# Opponent CHECKED
def opcheck_p1():
    global pot, chips_p1, chips_p2
    global check_p1, bet_p1, raised_p1
    global both_check, next_player
    global to_call_p1, to_call_p2

    decision = str.lower(input(f'{name_p2} has checked. Will you CHECK or BET?'))[0]
    while decision != 'c' and decision != 'b':
        decision = str.lower(input('You must CHECK or BET.'))[0]
    if decision == 'c':
        both_check += 1
        if both_check == 2:
            next_player = 'p2'
            dealer()
        else:
            check_p1 = True
            play_p2()
    if decision == 'b':
        size = int(input('Bet how many chips? '))
        while size <= 0:
            size = int(input("You must bet positive number of chips. Bet how many chips? "))
        while size > chips_p1:
            size = int(input(f"You only have {chips_p1} chips! Bet how many chips?"))
        while size > (chips_p2 - to_call_p2):
            size = int(
                input(f"You may bet no more than your opponent's remaining {chips_p2} chips. Bet how many chips?"))
        chips_p1 -= size
        pot += size
        to_call_p2 += size
        if chips_p1 <= 0:
            print(name_p1, 'has gone ALL-IN!')
        bet_p1 = True
        play_p2()

# Opponent BET
def opbet_p1():
    global pot, chips_p1, chips_p2
    global check_p1, bet_p1, raised_p1
    global both_check, next_player
    global to_call_p1, to_call_p2

    decision = str.lower(input(f'{name_p2} has bet {to_call_p1} chips. Will you CALL, RAISE or FOLD?'))[0]
    while decision != 'c' and decision != 'r' and decision != 'f':
        decision = str.lower(input('You must CALL, RAISE or FOLD.'))[0]

    if decision == 'f':
        print()
        print(f'{name_p1} folds!')
        award(p2)
    if decision == 'r':
        raise_p1 = int(input(f'Raise how many chips? Must be greater than {to_call_p1}: '))
        while raise_p1 <= to_call_p1:
            raise_p1 = int(
                input(f"You must raise more than {to_call_p1} chips. How much would you like to raise? "))
        chips_p1 -= raise_p1
        pot += raise_p1
        raise_p1 -= to_call_p1
        to_call_p2 = raise_p1
        to_call_p1 = 0
        if chips_p1 <= 0: print(name_p1, 'has gone ALL-IN!')
        raised_p1 = True
        play_p2()
    if decision == 'c':
        chips_p1 -= to_call_p1
        pot += to_call_p1
        to_call_p1 = 0
        if chips_p1 <= 0: print(name_p1, 'has gone ALL-IN!')
        next_player = 'p2'
        dealer()

# Opponent RAISED
def opraise_p1():
    global pot, chips_p1, chips_p2
    global check_p1, bet_p1, raised_p1
    global both_check, next_player
    global to_call_p1, to_call_p2

    decision = str.lower(input(f'{name_p2} has raised you an additional {to_call_p1} chips. Will you CALL, RAISE or FOLD?'))[0]
    while decision != 'c' and decision != 'r' and decision != 'f':
        decision = str.lower(input('You must CALL, RAISE or FOLD.'))[0]
    if decision == 'f':
        print()
        print(f'{name_p1} folds!')
        award(p2)
    if decision == 'r':
        raise_p1 = int(input(f'Raise how many chips? Must be greater than {to_call_p1}: '))
        while raise_p1 <= to_call_p1:
            raise_p1 = int(
                input(f"You must raise more than {to_call_p1} chips. How much would you like to raise? "))
        chips_p1 -= raise_p1
        pot += raise_p1
        raise_p1 -= to_call_p1
        to_call_p2 = raise_p1
        to_call_p1 = 0
        if chips_p1 <= 0: print(name_p1, 'has gone ALL-IN!')
        raised_p1 = True
        play_p2()
    if decision == 'c':
        chips_p1 -= to_call_p1
        pot += to_call_p1
        to_call_p1 = 0
        if chips_p1 <= 0: print(name_p1, 'has gone ALL-IN!')
        next_player = 'p2'
        dealer()

# Opponent bet you ALL-IN / themselves ALL-IN
def opallin_p1():
    global pot, chips_p1, chips_p2
    global check_p1, bet_p1, raised_p1
    global both_check, next_player
    global to_call_p1, to_call_p2

    if chips_p2 == 0 and to_call_p1 >= chips_p1:
        print(f'{name_p2} has gone ALL-IN with {to_call_p1} chips, pushing you ALL-IN!')
    elif chips_p2 == 0:
        print(f'{name_p2} has gone ALL-IN with {to_call_p1} chips!')
    elif to_call_p1 >= chips_p1:
        print(f'{name_p2} has pushed you ALL-IN for {to_call_p1} chips!')

    decision = str.lower(input(f'Will you CALL {to_call_p1} chips or FOLD?'))[0]
    while decision != 'c' and decision != 'f':
        decision = str.lower(input(f'You must CALL {to_call_p1} chips or FOLD.'))[0]
    if decision == 'f':
        print()
        print(f'{name_p1} folds!')
        award(p2)
    if decision == 'c':
        chips_p1 -= to_call_p1
        pot += to_call_p1
        print(name_p1, 'CALLS', to_call_p1, 'chips. Pot size now', pot, 'chips.')
        to_call_p1, to_call_p2 = 0, 0
        next_player = 'p2'
        showdown()

#########################################################################################################################
###########################################################################################################################
#########################################################################################################################

def play_p2():
    global pot, chips_p1, chips_p2
    global check_p2, bet_p2, raised_p2
    global check_p2, bet_p2, raised_p2
    global both_check
    global to_call_p1, to_call_p2

    if chips_p2 <= 0: showdown()

    # Resetting variables
    check_p2, bet_p2, raised_p2 = False, False, False
    size, to_call_p1 = 0, 0
    next_player = ''

    # Clearing the screen and reviewing the state of playing:
    print()
    print()
    print()
    print()
    print()
    print('********************************', name_p2, '********************************')
    print()

    # Review the state of play
    if stage == 1: print('Current stage: PREFLOP.')
    if stage == 2: print('Current stage: FLOP.')
    if stage == 3: print('Current stage: TURN.')
    if stage == 4: print('Current stage: RIVER.')
    if stage >= 2: print('The community cards are:', community)
    print(f'{name_p2}, you currently have {chips_p2} chips.')
    print(f'The pot size is currently {pot} chips.')
    print(f'Your opponent {name_p1} currently has {chips_p1} chips.')
    input(f"About to reveal {name_p2}'s cards. Press ENTER when {name_p1} is not looking.")
    print(f"Your cards are: {hand_p2}")

    if raised_p1 == True:
        if chips_p1 == 0 or to_call_p2 >= chips_p2:
            opallin_p2()
        else:
            opraise_p2()

    elif bet_p1 == True:
        if chips_p1 == 0 or to_call_p2 >= chips_p2:
            opallin_p2()
        else:
            opbet_p2()

    elif check_p1 == True: opcheck_p2()

    else: newstage_p2()

# Start new STAGE
def newstage_p2():
    global pot, chips_p1, chips_p2
    global check_p2, bet_p2, raised_p2
    global both_check, next_player
    global to_call_p1, to_call_p2

    decision = str.lower(input(f'{name_p2} to start. Will you CHECK or BET?'))[0]
    while decision != 'c' and decision != 'b':
        decision = str.lower(input('You must CHECK or BET.'))[0]
    if decision == 'c':
        both_check += 1
        if both_check == 2:
            next_player = 'p1'
            dealer()
        else:
            check_p2 = True
            play_p1()
    if decision == 'b':
        size = int(input('Bet how many chips? '))
        while size <= 0:
            size = int(input("You must bet positive number of chips. Bet how many chips? "))
        while size > chips_p2:
            size = int(input(f"You only have {chips_p2} chips! Bet how many chips?"))
        while size > (chips_p1 - to_call_p1):
            size = int(
                input(f"You may bet no more than your opponent's remaining {chips_p1} chips. Bet how many chips?"))
        chips_p2 -= size
        pot += size
        to_call_p1 += size
        if chips_p2 <= 0:
            print(name_p2, 'has gone ALL-IN!')
        bet_p2 = True
        play_p1()

# Opponent CHECKED
def opcheck_p2():
    global pot, chips_p1, chips_p2
    global check_p2, bet_p2, raised_p2
    global both_check, next_player
    global to_call_p1, to_call_p2

    decision = str.lower(input(f'{name_p1} has checked. Will you CHECK or BET?'))[0]
    while decision != 'c' and decision != 'b':
        decision = str.lower(input('You must CHECK or BET.'))[0]
    if decision == 'c':
        both_check += 1
        if both_check == 2:
            next_player = 'p1'
            dealer()
        else:
            check_p2 = True
            play_p1()
    if decision == 'b':
        size = int(input('Bet how many chips? '))
        while size <= 0:
            size = int(input("You must bet positive number of chips. Bet how many chips? "))
        while size > chips_p2:
            size = int(input(f"You only have {chips_p2} chips! Bet how many chips?"))
        while size > (chips_p1 - to_call_p1):
            size = int(
                input(f"You may bet no more than your opponent's remaining {chips_p1} chips. Bet how many chips?"))
        chips_p2 -= size
        pot += size
        to_call_p1 += size
        if chips_p2 <= 0:
            print(name_p2, 'has gone ALL-IN!')
        bet_p2 = True
        play_p1()

# Opponent BET
def opbet_p2():
    global pot, chips_p1, chips_p2
    global check_p2, bet_p2, raised_p2
    global both_check, next_player
    global to_call_p1, to_call_p2

    decision = str.lower(input(f'{name_p1} has bet {to_call_p2} chips. Will you CALL, RAISE or FOLD?'))[0]
    while decision != 'c' and decision != 'r' and decision != 'f':
        decision = str.lower(input('You must CALL, RAISE or FOLD.'))[0]

    if decision == 'f':
        print()
        print(f'{name_p2} folds!')
        award(p1)
    if decision == 'r':
        raise_p2 = int(input(f'Raise how many chips? Must be greater than {to_call_p2}: '))
        while raise_p2 <= to_call_p2:
            raise_p2 = int(input(f"You must raise more than {to_call_p2} chips. How much would you like to raise? "))
        chips_p2 -= raise_p2
        pot += raise_p2
        raise_p2 -= to_call_p2
        to_call_p1 = raise_p2
        to_call_p2 = 0
        if chips_p2 <= 0: print(name_p2, 'has gone ALL-IN!')
        raised_p2 = True
        play_p1()
    if decision == 'c':
        chips_p2 -= to_call_p2
        pot += to_call_p2
        to_call_p2 = 0
        if chips_p2 <= 0: print(name_p2, 'has gone ALL-IN!')
        next_player = 'p1'
        dealer()

# Opponent RAISED
def opraise_p2():
    global pot, chips_p1, chips_p2
    global check_p2, bet_p2, raised_p2
    global both_check, next_player
    global to_call_p1, to_call_p2

    decision = str.lower(input(f'{name_p1} has raised you an additional {to_call_p2} chips. Will you CALL, RAISE or FOLD?'))[0]
    while decision != 'c' and decision != 'r' and decision != 'f':
        decision = str.lower(input('You must CALL, RAISE or FOLD.'))[0]
    if decision == 'f':
        print()
        print(f'{name_p2} folds!')
        award(p1)
    if decision == 'r':
        raise_p2 = int(input(f'Raise how many chips? Must be greater than {to_call_p2}: '))
        while raise_p2 <= to_call_p2:
            raise_p2 = int(
                input(f"You must raise more than {to_call_p2} chips. How much would you like to raise? "))
        chips_p2 -= raise_p2
        pot += raise_p2
        raise_p2 -= to_call_p2
        to_call_p1 = raise_p2
        to_call_p2 = 0
        if chips_p2 <= 0: print(name_p2, 'has gone ALL-IN!')
        raised_p2 = True
        play_p1()
    if decision == 'c':
        chips_p2 -= to_call_p2
        pot += to_call_p2
        to_call_p2 = 0
        if chips_p2 <= 0: print(name_p2, 'has gone ALL-IN!')
        next_player = 'p1'
        dealer()

# Opponent bet you ALL-IN / themselves ALL-IN
def opallin_p2():
    global pot, chips_p1, chips_p2
    global check_p2, bet_p2, raised_p2
    global both_check, next_player
    global to_call_p1, to_call_p2

    if chips_p1 == 0 and to_call_p2 >= chips_p2:
        print(f'{name_p1} has gone ALL-IN with {to_call_p2} chips, pushing you ALL-IN!')
    elif chips_p1 == 0:
        print(f'{name_p1} has gone ALL-IN with {to_call_p2} chips!')
    elif to_call_p2 >= chips_p2:
        print(f'{name_p1} has pushed you ALL-IN for {to_call_p2} chips!')

    decision = str.lower(input(f'Will you CALL {to_call_p2} chips or FOLD?'))[0]
    while decision != 'c' and decision != 'f':
        decision = str.lower(input(f'You must CALL {to_call_p2} chips or FOLD.'))[0]
    if decision == 'f':
        print()
        print(f'{name_p2} folds!')
        award(p1)
    if decision == 'c':
        chips_p2 -= to_call_p2
        pot += to_call_p2
        print(name_p2, 'CALLS', to_call_p2, 'chips. Pot size now', pot, 'chips.')
        to_call_p2, to_call_p1 = 0, 0
        next_player = 'p1'
        showdown()

#######################################################################################################################
restart()
