#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace(". ", ".\n\n").replace("? ", "?\n\n").replace(": ", ":\n\n")
    sentences = text.splitlines(keepends=True)
    textprint = ""
    for sent in sentences:
        textprint += sent.strip(" ")
    print(textprint, end="")

