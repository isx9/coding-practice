class Item:
    """An item with a name and a weight in kilograms."""

    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        """Return the item's name."""
        return self.__name

    def weight(self):
        """Return the item's weight."""
        return self.__weight

    def __str__(self):
        return f'{self.__name} ({self.__weight} kg)'


class Suitcase:
    """A suitcase that holds items up to a maximum weight."""

    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__items = []

    def add_item(self, item: Item):
        """Add the item if it fits within the weight limit."""
        if self.weight() + item.weight() <= self.__max_weight:
            self.__items.append(item)

    def print_items(self):
        """Print every item in the suitcase."""
        for item in self.__items:
            print(item)

    def weight(self):
        """Return the combined weight of the items."""
        return sum(item.weight() for item in self.__items)

    def heaviest_item(self):
        """Return the heaviest item, or None if the suitcase is empty."""
        if not self.__items:
            return None
        return max(self.__items, key=lambda item: item.weight())

    def __str__(self):
        count = len(self.__items)
        word = 'item' if count == 1 else 'items'
        return f'{count} {word} ({self.weight()} kg)'


class CargoHold:
    """A cargo hold that holds suitcases up to a maximum weight."""

    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__suitcases = []

    def weight(self):
        """Return the combined weight of the suitcases."""
        return sum(suitcase.weight() for suitcase in self.__suitcases)

    def add_suitcase(self, suitcase: Suitcase):
        """Add the suitcase if it fits within the weight limit."""
        if self.weight() + suitcase.weight() <= self.__max_weight:
            self.__suitcases.append(suitcase)

    def print_items(self):
        """Print every item in every suitcase."""
        for suitcase in self.__suitcases:
            suitcase.print_items()

    def __str__(self):
        count = len(self.__suitcases)
        word = 'suitcase' if count == 1 else 'suitcases'
        remaining = self.__max_weight - self.weight()
        return f'{count} {word}, space for {remaining} kg'
