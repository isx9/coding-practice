"""Isogram exercise."""


def is_isogram(phrase):
    """Determine whether a phrase is an isogram.

    An isogram is a word or phrase without a repeating letter,
    ignoring spaces and hyphens. Case is ignored.

    :param phrase: str - the phrase to check.
    :return: bool - True if the phrase is an isogram, False otherwise.
    """
    repetitions = []
    for char in phrase.lower():
        if char in {" ", "-"}:
            continue
        if char in repetitions:
            return False
        repetitions.append(char)

    return True
