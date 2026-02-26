from deck import Deck


class Dealer:
    def __init__(self, name="Dealer"):
        self.name = name
        self.hand = []
    
    def __str__(self):
        cards = ", ".join(str(c) for c in self.hand)
        return f"{self.name}: [{cards}]"

    def drawcard(self, card):
        self.hand.append(card)

