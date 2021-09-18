import unittest
from game.Card import Card
from utils.cardlogic import *

class TestCardLogic(unittest.TestCase):

    def setUp(self):
        self.card = Card('test',1,1,1,attack=1,health=0, image='')
        self.damage = 1

    def test_that_card_is_dead_with_zero_health(self):
        self.card.health = 0
        self.assertTrue(isCardDead(self.card))
    
    def test_that_card_is_dead_with_negative_health(self):
        self.card.health = -1
        self.assertTrue(isCardDead(self.card))
    
    def test_that_card_is_dead_with_positive_health(self):
        self.card.health = 1
        self.assertFalse(isCardDead(self.card))
    
    def test_inflict_positive_damage_to_card(self):
        self.damage = 1
        prevHealth = self.card.health
        inflict_damage_to_card(self.card, self.damage)
        self.assertEqual(self.card.health, prevHealth - self.damage)
    
    def test_inflict_zeo_damage_to_card(self):
        self.damage = 0
        prevHealth = self.card.health
        inflict_damage_to_card(self.card, self.damage)
        self.assertEqual(self.card.health, prevHealth)