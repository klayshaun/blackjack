from deck import Deck
from currency import Currency

def main():
    
    testdeck = Deck()
    
    print (testdeck)

    testdeck.deckShuffle()
   
    print ("\n")

    print (testdeck)

    wallet = Currency(100, "USD")
    wallet += 25          # deposit
    wallet -= 40          # bet/withdraw
    print(wallet)         # Currency(amount=85.00, typeOf='USD')

    euro_wallet = wallet.convert_to("EUR")
    print(euro_wallet)

    print(wallet.history) # shows every change recorded

if __name__ == "__main__":
    main()
