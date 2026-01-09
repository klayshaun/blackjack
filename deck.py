from cards import Card

class Deck:
    
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SUITES = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    
    def __init__ (self):
        self.drawpile = []
        self.discard_pile = []
        self.outPile = []
        self.setupDrawPile()

    def setupDrawPile(self):
        for rank in self.RANKS:
            for suites in self.SUITES:
                self.drawpile.append(Card(rank, suites))