def is_triangle(sides):
    """Check whether the given sides can form a valid triangle."""
    a, b, c = sides
    return a > 0 and b > 0 and c > 0 and a + b >= c and b + c >= a and a + c >= b


def equilateral(sides):
    """Check whether a triangle is equilateral (all three sides equal)."""
    if not is_triangle(sides):
        return False
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    """Check whether a triangle is isosceles (at least two sides equal)."""
    if not is_triangle(sides):
        return False
    return sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]


def scalene(sides):
    """Check whether a triangle is scalene (all three sides different)."""
    if not is_triangle(sides):
        return False
    return sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]
