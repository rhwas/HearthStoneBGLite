from enum import Enum, auto

class Stage(Enum):
    Idle = auto()
    onAtt = auto()
    Att = auto()
    OnDmg = auto()
    OnDeath = auto()