"""Module for checking whether a sentence is a pangram."""

import string


def is_pangram(sentence):
    """Check whether sentence contains every letter of the English alphabet."""
    alphabet = string.ascii_lowercase
    letters = set()
    for char in sentence.lower():
        if char in alphabet:
            letters.add(char)
    return len(letters) == 26
