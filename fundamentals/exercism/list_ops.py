def append(list1, list2):
    """Return list1 with all items from list2 added to its end."""
    list1.extend(list2)
    return list1


def concat(lists):
    """Return a single flattened list combining all items from a series of lists."""
    combined = []
    for sublist in lists:
        combined += sublist
    return combined


def filter(function, lst):
    """Return a list of items from lst for which function(item) is True."""
    result = []
    for item in lst:
        if function(item):
            result.append(item)
    return result


def length(lst):
    """Return the total number of items in lst."""
    count = 0
    for item in lst:
        count += 1
    return count


def map(function, lst):
    """Return a list of the results of applying function to each item in lst."""
    result = []
    for item in lst:
        result.append(function(item))
    return result


def foldl(function, lst, initial):
    """Fold lst into a single value by applying function to the accumulator
    and each item, from left to right.
    """
    accumulator = initial
    for item in lst:
        accumulator = function(accumulator, item)
    return accumulator


def foldr(function, lst, initial):
    """Fold lst into a single value by applying function to the accumulator
    and each item, from right to left.
    """
    accumulator = initial
    for item in reversed(lst):
        accumulator = function(accumulator, item)
    return accumulator


def reverse(lst):
    """Return a new list with the items of lst in reversed order."""
    result = []
    for item in lst:
        result.insert(0, item)
    return result
