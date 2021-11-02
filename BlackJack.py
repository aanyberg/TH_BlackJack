import random
import time
import os
from colorama import Fore, Back, Style

# Globals
running = True
suits = ["\u2666", "\u2665", "\u2663", "\u2660"]
ranks = (
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "J",
    "Q",
    "K",
    "A",
)
values = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11,
}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # Returns the suit and card value
    def __str__(self):
        return self.rank + self.suit


class Deck:
    # Creates 6 decks of cards and shuffles all the cards
    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks * 6:
                self.deck.append(Card(suit, rank))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "A":
            self.aces += 1

    # Adjust for aces depending on the hand value
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Actions:
    @staticmethod
    def hit(deck, hand):
        hand.add_card(deck.deal())
        hand.adjust_for_ace()

    # Conditions for hitting or standing
    @staticmethod
    def hit_or_stand(deck, hand):
        global running

        while True:
            x = input("\nStand or hit? Enter [h/s]")

            if x[0].lower() == "h":
                Actions.hit(deck, hand)

            elif x[0].lower() == "s":
                print("Player stands. Dealer is playing.")
                running = False

            else:
                print("Sorry, I don't understand that. Enter [h/s]")
                continue
            break

    # Shows both player cards but only one dealer card
    @staticmethod
    def show_some(player, dealer):
        print(Fore.GREEN + f"\nPlayers hand is:{Style.RESET_ALL}", *player.cards, sep="\n")
        print(Fore.GREEN + f"Hand value:{Style.RESET_ALL}", player.value, sep="\n")
        print(Fore.RED + f"\nDealers hand:{Style.RESET_ALL}")
        print("<hidden card>")
        print(f"{dealer.cards[1]}")

    # Shows all cards when the round is finished
    @staticmethod
    def show_all(player, dealer):
        print(Fore.GREEN + f"\nPlayers hand is:{Style.RESET_ALL}", *player.cards, sep="\n")
        print(Fore.GREEN + f"Hand value:{Style.RESET_ALL}", player.value, sep="\n")
        print(Fore.RED + f"\nDealers hand:{Style.RESET_ALL}", *dealer.cards,sep="\n")
        print(Fore.RED + f"Hand value:{Style.RESET_ALL}", dealer.value, sep="\n")

    @staticmethod
    def player_busts():
        print(Fore.BLUE + "\n<--- Player busts! --->", Style.RESET_ALL)

    @staticmethod
    def player_wins():
        print(Fore.BLUE + "\n<--- Player wins! --->", Style.RESET_ALL)

    @staticmethod
    def dealer_busts():
        print(Fore.BLUE + "\n<--- Dealer busts! --->", Style.RESET_ALL)

    @staticmethod
    def dealer_wins():
        print(Fore.BLUE + "\n<--- Dealer wins! --->", Style.RESET_ALL)

    @staticmethod
    def push():
        print(Fore.BLUE + "\nIt's a tie.", Style.RESET_ALL)


def main():
    deck = Deck()
    actions = Actions()
    global running

    while True:
        print("\n-----------------------------------------")
        print("          Welcome to BlackJack")
        print("-----------------------------------------")
        print("Try getting as close to 21 as you can without going over.\nDealer hits until 17.")

        player_hand = Hand()
        dealer_hand = Hand()
        for i in range(2):
            player_hand.add_card(deck.deal())
            dealer_hand.add_card(deck.deal())

        actions.show_some(player_hand, dealer_hand)

        while running:

            # Ask player for input
            actions.hit_or_stand(deck, player_hand)
            actions.show_some(player_hand, dealer_hand)

            if player_hand.value > 21:
                actions.player_busts()
                break

        # If there's no bust
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                actions.hit(deck, dealer_hand)

            # Show cards
            time.sleep(1)
            print("\n-----------------------------------------")
            print("          * Final Results *")
            print("-----------------------------------------")

            actions.show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                actions.dealer_busts()

            elif dealer_hand.value > player_hand.value:
                actions.dealer_wins()

            elif dealer_hand.value < player_hand.value:
                actions.player_wins()

            else:
                actions.push()

        new_game = input("\nWant to play another round? [Y/N]")
        while new_game.lower() not in ["y", "n"]:
            new_game = input("\nI didn't understand that? Please enter [Y/N]")
        if new_game[0] == "y":
            running = True
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        else:
            print("\n-----------------------See you next time!-----------------------")
            break


if __name__ == '__main__':
    main()