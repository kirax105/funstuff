from PlayingCardClass import *
from random import *

def suits():

    card_suits = choice(['Clubs','Hearts','Diamonds','Spades'])

    return card_suits

def values():

    card_value = choice([1,2,3,4,5,6,7,8,9,10,11,13])

    return card_value


def main():
    """This function will create two cards and compare them"""

    hand = []

    hand1 = PlayingCard(suits(),values())

    hand.append(hand1.get_suit())
    hand.append(hand1.get_value())

    print(hand)
"""    print(hand1.get_value())
    print(hand2.get_suit())
    print(hand2.get_value())"""

main()
