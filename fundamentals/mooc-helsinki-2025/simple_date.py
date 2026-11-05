class SimpleDate:
    """A simplified date where every month has 30 days and every year 360 days."""

    def __init__(self, day: int, month: int, year: int):
        self._day = day
        self._month = month
        self._year = year

    def __str__(self):
        return f'{self._day}.{self._month}.{self._year}'

    def _to_days(self):
        """Convert this date to an absolute day count."""
        return self._year * 360 + self._month * 30 + self._day

    @staticmethod
    def _from_days(total: int):
        """Convert an absolute day count back into a SimpleDate."""
        year = total // 360
        total %= 360
        month = total // 30
        day = total % 30
        return SimpleDate(day, month, year)

    def __eq__(self, another):
        if not isinstance(another, SimpleDate):
            return NotImplemented
        return self._to_days() == another._to_days()

    def __lt__(self, another):
        if not isinstance(another, SimpleDate):
            return NotImplemented
        return self._to_days() < another._to_days()

    def __gt__(self, another):
        if not isinstance(another, SimpleDate):
            return NotImplemented
        return self._to_days() > another._to_days()

    def __add__(self, days: int):
        """Return a new date the given number of days later."""
        return SimpleDate._from_days(self._to_days() + days)

    def __sub__(self, another):
        """Return the difference between two dates in days."""
        return abs(self._to_days() - another._to_days())
