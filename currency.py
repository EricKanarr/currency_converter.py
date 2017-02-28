class DifferentCurrencyCodeError(Exception):
    pass

class UnsupportedOperationError(Exception):
    pass

class Currency:
    def __init__(self, symbol, amount):
        self.symbol = symbol
        self.amount = amount
        # symbol[$, £, ¥]
        # code[USD, EUR, JPY]

    def __str__(self):
        return self.symbol + str(self.amount)

    def __eq__(self, other):
        return self.symbol == other.symbol and self.amount == other.amount

    def __add__(self, other):
        if self.symbol == other.symbol:
            return Currency(self.symbol, self.amount + other.amount)
        else:
            raise DifferentCurrencyCodeError("You can't add two different currencies")


    def __sub__(self, other):
         if self.symbol == other.symbol:
             return Currency(self.symbol, self.amount - other.amount)
         else:
            raise DifferentCurrencyCodeError("You can't subtract two different currencies")


    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Currency(self.symbol, self.amount * other)
        else:
            raise UnsupportedOperationError("Other must be an int or float")
