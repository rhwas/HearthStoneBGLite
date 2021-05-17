from typing import TypeVar, Generic, List
import logging
import random as r
from cards.base import Card

T = TypeVar('T')

class Warband:
    def __init__(self, name:str, cards: List):
        """
        Base class for a player warband. A warband consists of a maximum of 7 cards.
        These cards are considered active and placed on the battlefield in front of the player.

        Arguments:
            arg {type} -- description

        Keyword Arguments:
            arg {type} -- description (default: {value})
        """
        self.ID = [0, 1, 2, 3, 4, 5, 6]
        self.name = name
        self.cards = []
        for c in cards:
            c.ID = self.ID.pop(0)
            self.cards.append(c)
        self.length = len(self.cards)
        self.attackingPosition = 0
        self.attackingCard = None
        self.defendingCard = None
    
    def copy(self):
        """
        Copy current warband.

        Returns:
            Warband {Warband()} -- copy of current warband state
        """
        return Warband(name=self.name, cards=[card.copy() for card in self.cards])

    def add_card(self, card: Generic[T]):
        """
        Adds a card to the right (back) of the current warband. Will not add if warband is 
        already 7 wide.

        Arguments:
            card {Card} -- card to be added to warband
        """
        if self.length < 7:
            card.ID = self.ID.pop(0)
            self.cards.append(card)
            self.length += 1
        else: logging.warning("Warband is full. Card not added.")
    
    def remove_card(self, card: Generic[T]):
        """
        Removes a card from the warband given an index (0-6).

        Arguments:
            card {Card} -- card to be added to warband
        """
        try:
            self.cards.remove(card)
            self.ID.insert(card.ID, card.ID)
            self.length -= 1
        except:
            logging.warning("Tried to remove card from warband. Either card does not exist in warband OR warband empty. Card given: %s.", card.name)

    def select_attacking_card(self):
        if self.attackingPosition == self.length:
            self.attackingPosition = 0
        elif self.attackingPosition > self.length and self.attackingPosition - 1 == self.length:
            self.attackingPosition = 0
        elif self.attackingPosition > self.length:
            self.attackingPosition = self.length - 1 
        card = self.cards[self.attackingPosition]
        self.attackingPosition += 1
        return card
    
    def select_defending_card(self):
        taunts = [idx for idx, card in enumerate(self.cards) if card.taunt]
        if len(taunts) > 0:
            return self.cards[taunts[r.randrange(0, len(taunts))]]
        else:
            return self.cards[r.randrange(0, len(self.cards))]
