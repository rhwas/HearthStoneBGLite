
def isCardDead(card):
    """
    Check if the card is dead. i.e. has no health left.
    
    Arguments:
        card -- Card object
    Returns:
        bool -- Whether card is dead
    """
    if card.health <= 0: return True
    return False

def inflict_damage_to_card(card, amount):
    """
    Inflict an amount of damage to a card
    
    Arguments:
        card -- Card object
        amount -- amount of damage
    """
    card.health -= amount