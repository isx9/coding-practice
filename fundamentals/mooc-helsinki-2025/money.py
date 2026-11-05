class Money:
    """An amount of money in euros and cents, supporting comparison and arithmetic."""

    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def in_cents(self):
        """Return the amount as a whole number of cents."""
        return self.__euros * 100 + self.__cents

    @staticmethod
    def __from_cents(total: int):
        return Money(total // 100, total % 100)

    def __str__(self):
        return f'{self.__euros}.{self.__cents:02d} eur'

    def __eq__(self, another):
        if not isinstance(another, Money):
            return NotImplemented
        return self.in_cents() == another.in_cents()

    def __lt__(self, another):
        if not isinstance(another, Money):
            return NotImplemented
        return self.in_cents() < another.in_cents()

    def __gt__(self, another):
        if not isinstance(another, Money):
            return NotImplemented
        return self.in_cents() > another.in_cents()

    def __add__(self, another):
        if not isinstance(another, Money):
            return NotImplemented
        return Money.__from_cents(self.in_cents() + another.in_cents())

    def __sub__(self, another):
        if not isinstance(another, Money):
            return NotImplemented
        difference = self.in_cents() - another.in_cents()
        if difference < 0:
            raise ValueError('a negative result is not allowed')
        return Money.__from_cents(difference)
