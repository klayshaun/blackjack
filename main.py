from deck import Deck
from currency import Currency
from players import PLayers
from dealer import Dealer

def main():
    def hand_value(hand):
    # base values
        values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9,
              "10":10, "J":10, "Q":10, "K":10, "A":11}

        total = 0
        aces = 0

        for card in hand:
         total += values[card.rank]
         if card.rank == "A":
            aces += 1

    # If we busted and we have aces counted as 11, convert them to 1 (subtract 10 each)
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        return total
    
    testdeck = Deck()

    testdeck.deckShuffle()

    player = PLayers("Alice")
    player.drawcard(testdeck.drawCard())
    print(player)
   
    deal = Dealer("Dealer")
    deal.drawcard(testdeck.drawCard())
    print(deal)

   
    player.drawcard(testdeck.drawCard())
    print(player)

    while True:
        action = input("Hit or Stand? ").lower()

        if action == "hit":
            player.drawcard(testdeck.drawCard())
            print(player)

        elif action == "stand":
    # dealer draws until 17 or more
            while hand_value(deal.hand) < 17:
                deal.drawcard(testdeck.drawCard())

            print(deal)
            
        player_total = hand_value(player.hand)
        dealer_total = hand_value(deal.hand)

        print(f"Player total: {player_total}")
        print(f"Dealer total: {dealer_total}")

        if player_total > 21:
         print("Dealer wins (player busted).")
        elif dealer_total > 21:
         print("Player wins (dealer busted).")
        elif player_total > dealer_total:
         print("Player wins!")
        elif dealer_total > player_total:
         print("Dealer wins!")
        else:
         print("Push (tie).")
        break
    #print(player.hand)
    #deal.drawcard(testdeck.drawCard())
    #print(deal)
    
    #print(player)

    #print(deal)

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