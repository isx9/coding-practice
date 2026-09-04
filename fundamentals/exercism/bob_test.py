"""Determine Bob's response to a remark based on its punctuation/case."""


def response(hey_bob):
    text = hey_bob.strip()
    if not text:
        return "Fine. Be that way!"
    if text.isupper() and text.endswith("?"):
        return "Calm down, I know what I'm doing!"
    if text.isupper():
        return "Whoa, chill out!"
    if text.endswith("?"):
        return "Sure."
    return "Whatever."
