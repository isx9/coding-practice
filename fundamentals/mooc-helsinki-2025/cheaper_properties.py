class RealProperty:
    """A property with rooms, size, price per square metre and a description."""

    def __init__(self, rooms: int, square_meters: int, price_per_sqm: int, description: str):
        self.rooms = rooms
        self.square_meters = square_meters
        self.price_per_sqm = price_per_sqm
        self.description = description

    def total_price(self):
        """Return the total price of the property."""
        return self.price_per_sqm * self.square_meters

    def bigger(self, compared_to: 'RealProperty'):
        """Return True if this property is larger than the other."""
        return self.square_meters > compared_to.square_meters

    def price_difference(self, compared_to: 'RealProperty'):
        """Return the absolute difference in total price."""
        return abs(self.total_price() - compared_to.total_price())

    def more_expensive(self, compared_to: 'RealProperty'):
        """Return True if this property costs more than the other."""
        return self.total_price() > compared_to.total_price()

    def __repr__(self):
        return (f'RealProperty(rooms = {self.rooms}, square_meters = {self.square_meters}, '
                f'price_per_sqm = {self.price_per_sqm}, description = {self.description})')


def cheaper_properties(properties: list, reference: RealProperty):
    """Return (property, price difference) pairs for properties cheaper than the reference."""
    return [
        (prop, reference.price_difference(prop))
        for prop in properties
        if reference.more_expensive(prop)
    ]
