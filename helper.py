import re

def clean_word(word):
    word = re.sub(r'[^A-Za-z]', "", word.lower())
    return word


