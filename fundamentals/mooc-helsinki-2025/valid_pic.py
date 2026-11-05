from datetime import datetime

CENTURY_BY_SIGN = {'+': 1800, '-': 1900, 'A': 2000}
CONTROL_CHARACTERS = '0123456789ABCDEFHJKLMNPRSTUVWXY'


def is_it_valid(pic: str):
    """Check whether a Finnish personal identity code (PIC) is valid."""
    if len(pic) != 11:
        return False

    sign = pic[6]
    if sign not in CENTURY_BY_SIGN:
        return False

    try:
        day = int(pic[0:2])
        month = int(pic[2:4])
        year = CENTURY_BY_SIGN[sign] + int(pic[4:6])
        identifier = int(pic[0:6] + pic[7:10])
        datetime(year, month, day)
    except ValueError:
        return False

    expected = CONTROL_CHARACTERS[identifier % 31]
    return expected == pic[10]
