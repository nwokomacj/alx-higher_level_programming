#!/usr/bin/python3
"""This file prints a text with 2 new lines"""

def text_indentation(text):
    """A function that prints text with 2 new lines
    after each of rither: '.','?', ':'
    Args:
        text: Must be a string
    Raises:
        TypeError: When text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = [".", ":", "?"]
    outcome = ""
    i = 0
    while i < len(text):
        if text[i] in punctuations:
            outcome += text[i] + "\n\n"
            i += 1
        else:
            outcome += text[i]
            i += 1
    outcome = outcome.strip()
    print(outcome)
    print("")
