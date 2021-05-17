import pytest
from game.simulator import Simulator
from game.warband import Warband
from cards.tier1 import *

simulator = Simulator(None, None)

attackingWarband = Warband('Player1',[DragonspawnLieutenant()])
defendingWarband = Warband('Player2',[AcolyteOfCThun(), AcolyteOfCThun(), AcolyteOfCThun(), AcolyteOfCThun()])

def test_answer():
    assert simulator.simulate(attackingWarband, defendingWarband) == 4