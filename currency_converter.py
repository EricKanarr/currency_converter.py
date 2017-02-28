from currency import Currency


class UnknownCurrencyError(Exception):
    pass


class CurrencyConverter:
    def __init__(self, rates):
        self.rates = rates

    def convert(self, currency, to_code):
        if 'to_code' not in dict.rates():
            raise UnknownCurrencyError
        else:
            return currency * self.rates[to_code]


rates = {'USD': 1.0, 'EUR': 0.5, 'JPY': 100}

converter = CurrencyConverter(rates)

currency = Currency('$', 4.23)

print(currency)

converted_currency = converter.convert(currency, 'xxx')

print(converted_currency)
