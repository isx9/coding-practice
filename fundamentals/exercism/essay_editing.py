"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed.

    Parameters:
        title (str): Essay title that needs title casing.
    Returns:
        str: The title string in title case (first letters capitalized).
    """
    words = title.split(" ")
    for index, word in enumerate(words):
        words[index] = word.capitalize()
    return " ".join(words)


def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.

    Parameters:
        sentence (str): A sentence to check.
    Returns:
        bool: Is the sentence punctuated correctly?
    """
    return sentence[-1] == "."


def clean_up_spacing(sentence):
    """Trim any leading or trailing whitespace from the sentence.

    Parameters:
        sentence (str): A sentence to clean of leading and trailing space characters.
    Returns:
        str: A sentence that has been cleaned of leading and trailing space characters.
    """
    return sentence.strip()


def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    Parameters:
        sentence (str): A sentence to replace words in.
        old_word (str): The word to replace.
        new_word (str): The replacement word.
    Returns:
        str: Input sentence with new words in place of old words.
    """
    words = sentence.split(" ")
    for index, word in enumerate(words):
        clean_word = word.strip(",;.!?':'")
        if clean_word == old_word:
            punctuation = word[len(clean_word):]
            words[index] = new_word + punctuation
    return " ".join(words)
