#!/usr/bin/python3
"""
Module 5-text_indentation contains one function:
text_indentation(text)
"""
def text_indentation(text):
    """ text_indentation prints a string with two newlines
    after the symbols ".", "?", and ":", as well as stripping
    leading and trailing spaces from each new line created

    Args:
        text: must be a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace(". ", ".\n\n").replace("? ", "?\n\n").replace(": ", ":\n\n")
    sentences = text.splitlines(keepends=True)
    textprint = ""
    for sent in sentences:
        textprint += sent.strip(" ")
    print(textprint, end="")

