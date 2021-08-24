import pytest
from game.simulator import Simulator
from game.warband import Warband
from cards.tier1 import *


def test_taunt():
    player1Warband = Warband('Player1',[RefreshingAnomoly()])
    player2Warband = Warband('Player2',[RefreshingAnomoly(), DragonspawnLieutenant(), RefreshingAnomoly()])

    simulator = Simulator(player1Warband, player2Warband)
    simulator.turn()
    print(simulator.defendingWarband.cards[1].name)
    print(simulator.defendingWarband.cards[1].health)
    assert simulator.defendingWarband.cards[1].health == 2
