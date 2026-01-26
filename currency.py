


from __future__ import annotations

class Currency:
    USD_PER_UNIT = {
        "USD": 1.0,
        "EUR": 1.09,
        "GBP": 1.27,
        "JPY": 0.0068,
    }

    def __init__(self, amount: float, typeOf: str):
        self.amount = float(amount)
        self.typeOf = typeOf.upper()
        self.history = []
        self._record("INIT", self.amount)

    def _record(self, action: str, value: float, note: str = ""):
        self.history.append({
            "action": action,
            "value": float(value),
            "balance": float(self.amount),
            "note": note
        })

    def __repr__(self):
        return f"Currency(amount={self.amount:.2f}, typeOf='{self.typeOf}')"

    def __eq__(self, other):
        if not isinstance(other, Currency):
            return NotImplemented
        return float(self.to_usd()) == float(other.to_usd())

    def deposit(self, deposit_amount: float, note: str = ""):
        deposit_amount = float(deposit_amount)
        if deposit_amount < 0:
            raise ValueError("deposit_amount must be >= 0")
        self.amount += deposit_amount
        self._record("DEPOSIT", deposit_amount, note)
        return self

    def withdraw(self, withdraw_amount: float, note: str = ""):
        withdraw_amount = float(withdraw_amount)
        if withdraw_amount < 0:
            raise ValueError("withdraw_amount must be >= 0")
        if withdraw_amount > self.amount:
            raise ValueError("Insufficient funds")
        self.amount -= withdraw_amount
        self._record("WITHDRAW", -withdraw_amount, note)
        return self

    def to_usd(self) -> float:
        if self.typeOf not in self.USD_PER_UNIT:
            raise ValueError(f"Unknown currency: {self.typeOf}")
        return self.amount * self.USD_PER_UNIT[self.typeOf]

    @classmethod
    def _from_usd(cls, usd_amount: float, target_currency: str) -> float:
        target_currency = target_currency.upper()
        if target_currency not in cls.USD_PER_UNIT:
            raise ValueError(f"Unknown currency: {target_currency}")
        return usd_amount / cls.USD_PER_UNIT[target_currency]

    def convert_to(self, new_currency: str) -> "Currency":
        new_currency = new_currency.upper()
        usd_value = self.to_usd()
        new_amount = self._from_usd(usd_value, new_currency)
        converted = Currency(new_amount, new_currency)
        converted._record("CONVERT_FROM", self.amount, f"from {self.typeOf}")
        return converted

    # Required dunders
    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            return self.deposit(other, note="__iadd__")
        if isinstance(other, Currency):
            added = other.convert_to(self.typeOf).amount
            return self.deposit(added, note=f"__iadd__ from {other.typeOf}")
        return NotImplemented

    def __isub__(self, other):
        if isinstance(other, (int, float)):
            return self.withdraw(other, note="__isub__")
        if isinstance(other, Currency):
            subbed = other.convert_to(self.typeOf).amount
            return self.withdraw(subbed, note=f"__isub__ from {other.typeOf}")
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = Currency(self.amount * float(other), self.typeOf)
            result._record("MUL", other, "__mul__")
            return result
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            other = float(other)
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = Currency(self.amount / other, self.typeOf)
            result._record("DIV", other, "__truediv__")
            return result
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Currency):
            return self.to_usd() <= other.to_usd()
        if isinstance(other, (int, float)):
            return self.amount <= float(other)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Currency):
            return self.to_usd() >= other.to_usd()
        if isinstance(other, (int, float)):
            return self.amount >= float(other)
        return NotImplemented

    def __float__(self):
        return float(self.amount)

    def __int__(self):
        return int(self.amount)
