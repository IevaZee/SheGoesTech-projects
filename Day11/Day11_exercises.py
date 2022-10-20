# 1. The Shuffle

# write  a function get_shuffled_cards()

# Inside the function create  a 52-card list of tuples [("2", "diamonds ♦"), ("2", "hearts ♥"), ....., ("A", "spades ♠"), ("A", "clubs ♣")]

# The function returns a shuffled set of cards - the same list with tuples but shuffled!

# Find the correct method from built in random library.

# you can use a loop or use something from the library

# BONUS: Something can be useful from here: https://docs.python.org/3/library/itertools.html


# SOLUTION:

import itertools
import random

def get_shuffled_cards():
    suits = ["diamonds ♦", "hearts ♥", "spades ♠", "clubs ♣"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    card_list = list(itertools.product(values, suits))
    random.shuffle(card_list)
    return card_list


print(get_shuffled_cards())



# 2. Deck - probably for homework, see how far you get

# write a class Deck with the following attributes(variables)

# available - contains list of card tuples that can be used

# spent - contains list of card tuples that have been used

# there should be following methods:

# constructor (__init__) method

# initializes available with full 52 card list of tuples

# initializes spent with empty list

# shuffle(self):

# # shuffles available cards - works just like 1st function but works on available

# get_cards(self, count=1):
# # gets some number(default 1) of cards from available 
# adds these cards to spent
# returns these cards

# # you can add other methods and/or attributes if you wish to Deck class


# SOLUTION:

class Deck:
    suits = ["diamonds ♦", "hearts ♥", "spades ♠", "clubs ♣"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    
    def __init__(self):
        self.available = list(itertools.product(self.values, self.suits))
        self.shuffle()
        self.spent = []

    def shuffle(self):
        random.shuffle(self.available)
        return self

    def get_cards(self, count=1):
        take_away = self.available[:count]
        self.spent.extend(take_away)
        self.available = self.available[count:]
        return take_away


# TESTING:

# my_deck = Deck()
# my_cards = my_deck.get_cards(5)
# print(my_cards)
# single_card = my_deck.get_cards()
# print(single_card)
# print(my_deck.available)
# print(len(my_deck.available))
# print(my_deck.spent)



# 3. create a new deck in a different .py file from where Deck() is located, that means use import !

if __name__ == "__main__":
    card_list = get_shuffled_cards()
    print(card_list)
    my_deck = Deck()
    my_deck.shuffle()
    print(my_deck)
    print(my_deck.get_cards(3))