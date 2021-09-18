import unittest
from game.Card import Card
from game.warband import Warband

class TestWarband(unittest.TestCase):

    def setUp(self):
        self.attributes = {"divineshield": False, "taunt": False, "battlecry": False, "deathrattle": False, "reborn": False, "atstartofcombat": False, "bloodgem": False, "refresh": False}
        self.card = Card('test', 1, 1, 1, positionID=0, attributes=self.attributes, image='')
        self.tauntCard = self.card.copy()
        self.tauntCard.attributes["taunt"] = True
        self.warband = Warband('TestPlayer', [self.card, self.tauntCard, self.tauntCard])

    def test_get_taunts_is_list(self):
        self.assertIs(type(self.warband.getTauntsIndex()), list)
    
    def test_get_taunts_returns_only_taunts(self):
        [self.assertEqual(self.warband.cards[t].attributes["taunt"], True) for t in self.warband.getTauntsIndex()]

    def test_get_taunts_returns_empty_list_if_no_taunts(self):
        warband = Warband('test', [self.card])
        self.assertEqual(warband.getTauntsIndex(), [])
