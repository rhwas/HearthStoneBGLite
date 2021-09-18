import unittest
import copy
from game.Card import Card
from game.warband import Warband
from utils.warbandlogic import *

class TestWarbandLogic(unittest.TestCase):

    def setUp(self):
        self.attributes = {"divineshield": False, "taunt": False, "battlecry": False, "deathrattle": False, "reborn": False, "atstartofcombat": False, "bloodgem": False, "refresh": False}
        self.card = Card('test', 1, 1, 1, positionID=0, attributes=self.attributes, image='')
        self.tauntCard = self.card.copy()
        self.tauntCard.attributes["taunt"] = True
        self.warband = Warband('TestPlayer', [])
        self.damage = 1

    def test_remove_card(self):
        warband = Warband('TestPlayer', [self.card])
        remove_card(warband, self.card)
        self.assertNotIn(self.card, self.warband.cards)
        self.assertIn(self.card.positionID, self.warband.positionID)

    def test_remove_card_that_is_not_there(self):
        otherCard = copy.deepcopy(self.card)
        warband = Warband('TestPlayer', [otherCard])
        with self.assertRaises(ValueError):
            remove_card(warband, self.card)
    
    def test_kill_card(self):
        warband = Warband('TestPlayer', [self.card])
        initialAttackingPosition = warband.attackingPosition
        kill_card(warband, self.card)
        self.assertNotIn(self.card, self.warband.cards)
        self.assertEqual(initialAttackingPosition, warband.attackingPosition)
    
    def test_kill_card_that_is_not_in_warband(self):
        warband = Warband('TestPlayer', [])
        initialAttackingPosition = warband.attackingPosition
        with self.assertRaises(ValueError):
            kill_card(warband, self.card)
        self.assertEqual(initialAttackingPosition, warband.attackingPosition)
    
    def test_select_attacking_card_returns_a_card_type(self):
        warband = Warband('TestPlayer', [self.card])
        attackingCard = select_attacking_card(warband)
        self.assertIsInstance(attackingCard, Card)
    
    def test_select_attacking_card_no_cards_available(self):
        with self.assertRaises(IndexError):
            attackingCard = select_attacking_card(self.warband)
    
    def test_select_defending_card_returns_a_card_type(self):
        warband = Warband('TestPlayer', [self.card])
        defendingCard = select_defending_card(warband)
        self.assertIsInstance(defendingCard, Card)
    
    def test_select_defending_card_returns_a_taunt_when_taunts_available(self):
        warband = Warband('TestPlayer', [self.tauntCard])
        defendingCard = select_defending_card(warband)
        self.assertIs(defendingCard.attributes["taunt"], True)
    
    def test_select_defending_card_no_cards_available(self):
        with self.assertRaises(ValueError):
            defendingCard = select_defending_card(self.warband)