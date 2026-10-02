"""Check whether brackets, braces and parentheses in a string are balanced."""


def is_paired(input_string):
    """Check that brackets, braces and parentheses are balanced and correctly nested."""
    brackets = []

    for char in input_string:
        if char in {'{', '[', '('}:
            brackets.append(char)
        if char == '}':
            if not brackets or brackets.pop() != '{':
                return False
        if char == ']':
            if not brackets or brackets.pop() != '[':
                return False
        if char == ')':
            if not brackets or brackets.pop() != '(':
                return False

    return not brackets
