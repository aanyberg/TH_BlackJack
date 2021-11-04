import unittest
from blackjack import *


class HandTestCases(unittest.TestCase):
    def test_ace_of_diamonds(self):
        card = Card("\u2666", "A")
        self.assertEqual(values[card.rank], 11)

    def test_king_of_clubs(self):
        card = Card("\u2663", "K")
        self.assertEqual(values[card.rank], 10)

    def test_three_of_spades(self):
        card = Card("\u2660", "3")
        self.assertEqual(values[card.rank], 3)

    def test_if_ace(self):
        hand = Hand()
        card = Card("\u2665", "A")
        if card.rank == "A":
            hand.aces += 1
        self.assertTrue(hand.aces > 0)


class DeckTestCases(unittest.TestCase):
    def test_deck_length(self):
        self.assertEqual(312, len(Deck()))  # Check to see if there is 6 decks

    def test_deck_shuffle(self):
        deck_1 = Deck()
        deck_2 = Deck()
        deck_1.shuffle()
        deck_2.shuffle()
        self.assertNotEqual(str(deck_1), str(deck_2))


if __name__ == '__main__':
    unittest.main()
