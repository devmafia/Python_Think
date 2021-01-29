import random

class Card:
    """Represents a standard playing card."""

    # class attributes
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    # instance attributes
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        # check the suits
        if self.suit < other.suit: return True
        if self.suit > other.suit: return False

        # suits are the same... check  ranks
        return  self.rank < other.rank

    """
    tuples alternative

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2
    """

queen_of_diamonds = Card(1, 12)

class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def sort(self):
        self.cards.sort()

    def deal_hands(n_hands, n_cards):
        hands = []
        # check than for the global scope

        print(n_hands)
        print(n_cards)
        for i in range(n_hands):
            hand = Hand(deck)
            for c in range(n_cards):
                card = Card(random.randint(1,4), random.randint(1,14))
                hand.cards.append(card)
            hands.append(hand)
            print(hand)

        return hands

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = [];
        self.label = label

deck = Deck()
deck.shuffle()
print(deck)

hands = deck.deal_hands(8, 7)
print(hands)
