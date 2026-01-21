#!/usr/bin/python3
# Returns the length of a string and its first character
def multiple_returns(sentence):
    """Return a tuple with the length of a string and its first character."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
