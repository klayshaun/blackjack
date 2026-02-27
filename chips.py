
class Chips:
    ALLOWED = {1, 5, 25, 100, 500, 1000}

    def __init__(self, total=0):
        self.total = total
        self.bet = 0

    def deposit(self, amount: int):
        if amount not in self.ALLOWED:
            raise ValueError(f"Deposit must be one of: {sorted(self.ALLOWED)}")
        self.total += amount

    def place_bet(self, amount: int):
        if amount not in self.ALLOWED:
            raise ValueError(f"Bet must be one of: {sorted(self.ALLOWED)}")
        if amount > self.total:
            raise ValueError("Not enough balance to place that bet.")
        self.bet = amount

    def available(self) -> int:
        # money not currently on the table
        return self.total - self.bet

    def winBet(self):
        # win profit equal to bet (net +bet)
        self.total += self.bet
        self.bet = 0

    def loseBet(self):
        # lose bet (net -bet)
        self.total -= self.bet
        self.bet = 0