from deck import Deck
from currency import Currency
from players import PLayers
from dealer import Dealer

def main():
    
    testdeck = Deck()
    
    deal = Dealer("Dealer")
    deal.drawcard(testdeck.drawCard())
    deal.drawcard(testdeck.drawCard())

    player = PLayers("Alice")
    player.drawcard(testdeck.drawCard())
    player.drawcard(testdeck.drawCard())

    
    #print(player.hand)

    
    print(player)

    print(deal)

    #testdeck.deckShuffle()
   
    #print ("\n")

    #print (testdeck)

    #wallet = Currency(100, "USD")
    #wallet += 25          # hypotheticaldeposit
    #wallet -= 40          # hypothetical bet/withdraw
    #print(wallet)         # Currency(amount=85.00, typeOf='USD')

    #euro_wallet = wallet.convert_to("EUR")
    #print(euro_wallet)

    #print(wallet.history) # \shows recorded transactions

if __name__ == "__main__":
    main()