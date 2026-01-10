from cards import Card
import random

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
    
    def __str__(self):
        return "\n".join(str(card) for card in self.drawpile)
    
    def __eq__(self, other):
        if not isinstance(other, Deck):
            return NotImplemented
        return (self.drawpile == other.drawpile and
                self.discard_pile == other.discard_pile and
                self.outPile == other.outPile)
                        

    def drawCard(self):
        drawCard = self.drawpile.pop(0)
        self.outPile.append(drawCard)
        return drawCard
    
    def discard(self, card):
        returnedcard = card
        self.outPile.remove(returnedcard)
        self.discard_pile.append(returnedcard)

    def deckShuffle(self, seed=None):
        rng = random.Random(seed)
        for i in range(len(self.drawpile) - 1, 0, -1):
            j = rng.randint(0, i)
            self.drawpile[i], self.drawpile[j] = self.drawpile[j], self.drawpile[i]