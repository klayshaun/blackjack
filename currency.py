


#def balance():
    #balance = 0.0
    #deposit = 0.0
    #transactions = []
    #stored = input("deposit amount")
    #return "$" + int(stored)  + int(balance)

class Currency:
    def __init__(self, amount: float, typeOf: str, balance: float = 0.0):
        self.amount = amount
        self.typeOf = typeOf
        self.balance = []
    def __repr__(self):
        self.balance.append(self.amount)
        return f"Currency(amount={self.amount}, typeOf='{self.typeOf}', balance={self.balance})"
    def __eq__(self, other):
        if not isinstance(other, Currency):
            return NotImplemented
        return (self.amount == other.amount and
                self.typeOf == other.typeOf and
                self.balance == other.balance)
    def deposit(self, deposit_amount: float):
        self.balance += deposit_amount