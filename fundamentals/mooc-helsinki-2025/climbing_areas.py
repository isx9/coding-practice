class ClimbingRoute:
    """A climbing route with a name, length in metres and grade."""

    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f'{self.name}, length {self.length} metres, grade {self.grade}'


class ClimbingArea:
    """A climbing area that contains several routes."""

    def __init__(self, name: str):
        self.name = name
        self.__routes = []

    def add_route(self, route: ClimbingRoute):
        """Add a route to the area."""
        self.__routes.append(route)

    def routes(self):
        """Return the number of routes in the area."""
        return len(self.__routes)

    def hardest_route(self):
        """Return the route with the highest grade, or None if there are no routes."""
        if not self.__routes:
            return None
        return max(self.__routes, key=lambda route: route.grade)

    def __str__(self):
        hardest = self.hardest_route()
        hardest_grade = hardest.grade if hardest else '-'
        return f'{self.name} {self.routes()} routes, hardest {hardest_grade}'


def sort_by_number_of_routes(areas: list):
    """Sort climbing areas by number of routes, fewest first."""
    return sorted(areas, key=lambda area: area.routes())


def sort_by_most_difficult(areas: list):
    """Sort climbing areas by their hardest route, hardest first."""
    return sorted(areas, key=lambda area: area.hardest_route().grade, reverse=True)
