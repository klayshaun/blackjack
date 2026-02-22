




class PLayers:
    def __init__(self, name="BoB"):
        self.name = name
        self.hand = []
        self.score = 0

    def __str__(self):
        pass

    def __eq__(self, value):
        pass

    def drawcard(self, card):
        self.hand.append(card)
    
    def discardCard(self, cardIdx):
        returnedCard = self.hand.pop(cardIdx)
        return returnedCard
    #def calcScore(self):
        if len(self.hand) != 0:
            self.score += Rankedvalues 

        


class human(PLayers):
    pass