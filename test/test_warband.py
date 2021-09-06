import unittest
from game.Card import Card
from game.warband import Warband

class TestWarband(unittest.TestCase):

    def setUp(self):
        self.card = Card('test',1,1,1,attack=1,health=0, positionID=0)
        self.tauntCard = Card('test_taunt',1,1,1,attack=1,health=0, positionID=0, taunt=True)
        self.warband = Warband('TestPlayer', [self.card, self.tauntCard, self.tauntCard])

    def test_get_taunts_is_list(self):
        self.assertIs(type(self.warband.getTauntsIndex()), list)
    
    def test_get_taunts_returns_only_taunts(self):
        [self.assertEqual(self.warband.cards[t].taunt, True) for t in self.warband.getTauntsIndex()]

    def test_get_taunts_returns_empty_list_if_no_taunts(self):
        warband = Warband('test', [self.card])
        self.assertEqual(warband.getTauntsIndex(), [])
