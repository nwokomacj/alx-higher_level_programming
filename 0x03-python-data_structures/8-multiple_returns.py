#!/usr/bin/python3

def multiple_returns(sentence):

    multup = ()
    if len(sentence) == 0:
        multup[0] = "None"
    else:
        multup = len(sentence), sentence[0]
        return multup
