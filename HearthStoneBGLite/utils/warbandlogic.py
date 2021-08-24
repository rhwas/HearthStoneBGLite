from typing import TypeVar, Generic, List, Type
import logging
import random as r
from game.warband import Warband
from game.Card import Card

def add_card_right(warband: Type[Warband], card: Type[Card]) -> None:
    """
    Adds a card to the right (back) of the current warband. Will not add if warband is 
    already 7 wide.

    Arguments:
        warband {Warband} -- target warband
        card {Card} -- card to be added to warband
    """
    if warband.length < 7:
        card.positionID = warband.positionID.pop(-1)
        warband.cards.append(card)
        warband.length += 1
    else: logging.warning("Warband is full. Card not added.")

def add_card_left(warband: Type[Warband], card: Type[Card]) -> None:
    """
    Adds a card to the left (front) of the current warband. Will not add if warband is 
    already 7 wide.

    Arguments:
        warband {Warband} -- target warband
        card {Card} -- card to be added to warband
    """
    if warband.length < 7:
        card.positionID = warband.positionID.pop(0)
        warband.cards.insert(0, card)
        warband.length += 1
    else: logging.warning("Warband is full. Card not added.")

def remove_card(warband: Type[Warband], card: Type[Card]) -> None:
    """
    Remove a card from the warband.

    Arguments:
        warband {Warband} -- target warband
        card {Card} -- card to be removed
    """
    warband.positionID.insert(card.positionID, card.positionID)
    warband.cards.remove(card)

def kill_card(warband: Type[Warband], card: Type[Card]) -> None:
    """
    Kills a card from the warband.

    Arguments:
        warband {Warband} -- target warband
        card {Card} -- card to be removed
    """
    remove_card(warband, card)
    warband.attackingPosition -= 1

def select_attacking_card(attackingWarband: Type[Warband]) -> Type[Card]:
    """
    Select a card from the attacking warband.

    Arguments:
        attackingWarband {Warband} -- attacking warband
    Returns:
        card {Card} -- attacking card
    """
    return attackingWarband.cards[attackingWarband.attackingPosition]

def select_defending_card(defendingWarband: Type[Warband]) -> Type[Card]:
    """
    Select a card from the defending warband.

    Arguments:
        defendingWarband {Warband} -- defending warband
    Returns:
        card {Card} -- defending card
    """
    taunts = defendingWarband.getTaunts()
    if len(taunts) > 0:
        return defendingWarband.cards[taunts[r.randrange(0, len(taunts))]]
    else:
        return defendingWarband.cards[r.randrange(0, len(defendingWarband.cards))]











# def remove_card(warband, card):
#     """
#     Remove a card from the warband.

#     Arguments:
#         card {Card} -- card to be removed from warband
#     """
#     if card.reborn:
#         warband.cards[card.positionID].health = 1
#         warband.cards[card.positionID].attack = warband.cards[card.positionID].base_attack
#         warband.cards[card.positionID].reborn = False
#     else:
#         warband.cards.remove(card)
#         warband.positionID.insert(card.positionID, card.positionID)
#     # except Exception as e:
#     #     logging.warning("Tried to remove card from warband. Either card does not exist in warband OR warband empty. Card given: %s.", card.name)
#     #     logging.warning(e)