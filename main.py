from deck import Deck
from currency import Currency
from players import PLayers
from dealer import Dealer
from chips import Chips

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

def main():

    testdeck = Deck()

    testdeck.deckShuffle()

    chips = Chips(total=0)

# --- Buy-in (deposit) ---
    print("Buy-in with chips: 1, 5, 25, 100, 500, 1000")
    while True:
        amt = input("Add chip amount or 'done': ").lower().strip()
    
        if amt == "done":
            break
    
        try:
            chips.deposit(int(amt))
            print(f"Balance: {chips.total}")
        except Exception as e:
            print(e)

        if chips.total <= 0:
            print("No buy-in, no game.")
            return
# --- Place bet ---
        print(f"\nBalance before bet: {chips.total}")
    while True:
        bet_in = input("Place your bet (1/5/25/100/500/1000): ").strip()
        try:
            chips.place_bet(int(bet_in))
            break
        except Exception as e:
            print(e)

    print(f"Bet on table: {chips.bet}")
    print(f"Balance after bet (available): {chips.available()}\n")

    player = PLayers("Alice")
    player.drawcard(testdeck.drawCard())
    print(player)
   
    deal = Dealer("Dealer")
    deal.drawcard(testdeck.drawCard())
    print(deal)

   
    player.drawcard(testdeck.drawCard())
    print(player)

    print(f"After deal → Bet: {chips.bet}, Available: {chips.available()}, Total: {chips.total}")

    round_over = False

   

    while not round_over:
        action = input("Hit or Stand? ").lower().strip()

        if action == "hit":
            player.drawcard(testdeck.drawCard())
            print(player)

            
            player_total = hand_value(player.hand)
            print(f"Player total: {player_total}")

            if player_total > 21:
                print("Dealer wins (player busted).")
                chips.loseBet()
                round_over = True

        elif action == "stand":
            # dealer draws until 17 or more
            while hand_value(deal.hand) < 17:
                deal.drawcard(testdeck.drawCard())

            print(deal)

            player_total = hand_value(player.hand)
            dealer_total = hand_value(deal.hand)

            print(f"Player total: {player_total}")
            print(f"Dealer total: {dealer_total}")

            if dealer_total > 21:
                print("Player wins! Dealer busted.")
                chips.winBet()
            elif player_total > dealer_total:
                print("Player wins!")
                chips.winBet()
            elif dealer_total > player_total:
                print("Dealer wins!")
                chips.loseBet()
            elif player_total > 21:
                print("Dealer wins (player busted).")
                chips.loseBet()
            else:
                print("Push (tie).")
                chips.bet = 0

            round_over = True

        else:
            print("Type 'hit' or 'stand'.")
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