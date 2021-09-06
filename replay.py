import json
import os
import glob

replays = glob.glob('replays/*')
f = open(replays[0])

replay = json.load(f)

class Replay():

    def __init__(self, player1Warband, player2Warband):
        self.player1Warband = player1Warband
        self.player2Warband = player2Warband
        self.turns = []
    
    def add_turn(self, turn):
        pass