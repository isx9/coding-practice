from random import choice, shuffle

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
DIGITS = '0123456789'
SPECIAL_CHARACTERS = '!?=+-()#'


def generate_strong_password(length: int, numbers: bool, special_characters: bool):
    """Generate a random password with at least one character of each requested type."""
    password_chars = [choice(LETTERS)]
    pool = LETTERS

    if numbers:
        password_chars.append(choice(DIGITS))
        pool += DIGITS

    if special_characters:
        password_chars.append(choice(SPECIAL_CHARACTERS))
        pool += SPECIAL_CHARACTERS

    while len(password_chars) < length:
        password_chars.append(choice(pool))

    shuffle(password_chars)
    return ''.join(password_chars)
