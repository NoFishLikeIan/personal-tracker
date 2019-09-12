import string


def remove_punct(s: str):
    return s.translate(s.maketrans(dict.fromkeys(string.punctuation)))
