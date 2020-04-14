import sys


def text_analyzer(text=""):
    '''This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.'''

    if not(text):
        text = input("What is the text to analyse?\n")
    text = str(text)
    up = 0
    low = 0
    punct = 0
    space = 0
    for x in text:
        if x.islower():
            low += 1
        elif x.isupper():
            up += 1
        elif x.isspace():
            space += 1
        elif not(x.isalnum()):
            punct += 1
    print("The text contains {} characters:\n".format(len(text)))
    print(f"- {up} upper letters\n")
    print(f"- {low} lower letters\n")
    print(f"- {punct} punctuation marks\n")
    print(f"- {space} spaces")
