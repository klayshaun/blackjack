from deck import Deck
from currency import Currency

def main():
    
    testdeck = Deck()
    
    print (testdeck)

    testdeck.deckShuffle()
   
    print ("\n")

    print (testdeck)

    print(Currency(100.0, "USD"))
    
    print(Currency(50.0, "USD"))


if __name__ == "__main__":
    main()
