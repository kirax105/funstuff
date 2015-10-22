class PlayingCard:

    # Create a card by specifying suit and value
    def __init__(self, suit, value):
        """Initialize an instance of Playing Card"""
        self._suit = suit
        self._value = value

    # Gets the cards suit
    def get_suit(self):

        return self._suit

    # Gets the cards value
    def get_value(self):

        return self._value

    # Checks to see if which card is greater
    def greater(self, card, other_card):

        # Create a list displaying all the suits in order
        suits = ["Clubs", "Hearts", "Diamonds", "Spades"]

        # Get both cards values and store in variable
        card_value = self.get_value(card)
        other_value = self.get_value(other_card)

        # Get both cards suits and store in variable
        card_suit = self.get_suit(card)
        other_card_suit = self.get_suit(other_card)

        # Checks to see where the specified suit is located in the suit list
        suitCard = suits.index(card_suit)
        suitOther = suits.index(other_card_suit)

        # Checks the cards value to see if its greater, less, or equal to the compared card
        if card_value > other_value:
            print("Card value is greater!")
        elif card_value < other_value:
            print("Other Card value is greater!")
        elif card_value == other_value:
            print("Equal, checking suit!")
        # If the cards value is equal, check the suit location in list
        if suitCard > suitOther:
            print("Card suit is greater!")
        elif suitCard < suitOther:
            print("Other suit is greater!")
        elif suitCard == suitOther:
            print("Both cards the same!")
