"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from Card import Hand, Deck

class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}

        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def num_hist(self):
        """Builds a histogram of the numbers that appear in the hand.

        Stores the result in attribute numbers.
        """
        self.nums = {}

        for card in self.cards:
            self.nums[card.rank] = self.nums.get(card.rank, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """

        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_pair(self):

        for val in self.nums.values():
            if val >= 2:
                return True
        return False

    def has_twopair(self):

        counter = 0
        for val in self.nums.values():
            if val >= 2:
                counter += 1
        if counter >= 2:
            return True
        return False

    def classify(self, hand):

        self.label = ""

        if has_pair(self):
            self.label = "pair"
            if has_twopair(self):
                self.label = "twopair"
                if has_flush(self):
                    self.label = "flush"

def hand_probs(deck):

    deck.shuffle()

    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        print("#")
    print(deck)


if __name__ == '__main__':

    deck = Deck()
    hand_probs(deck)

    for n in range(10):
        print("#")

    # make a deck
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print(hand)
        hand.suit_hist()
        hand.num_hist()

        print(hand.suits)
        print(hand.has_flush())
        print(hand.nums)
        print(hand.has_pair())
        print(hand.has_twopair())

        print('')
