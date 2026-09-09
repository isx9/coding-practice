"""Module implementing the rotational (Caesar) cipher."""

import string


def rotate(text, key):
    """Shift each letter in text by key positions, preserving case and non-letter characters."""
    alphabet = string.ascii_lowercase
    if key > 26 or key < 0:
        raise ValueError("Key not valid, it must be between 0 and 26.")
    result = []
    for char in text:
        if char.lower() in alphabet and char.isupper():
            position = alphabet.index(char.lower())
            new_position = (position + key) % 26  # wraparound
            result.append(alphabet[new_position].upper())
        elif char in alphabet:
            position = alphabet.index(char)
            new_position = (position + key) % 26
            result.append(alphabet[new_position])
        else:
            result.append(char)
    return "".join(result)
