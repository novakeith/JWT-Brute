#!/usr/bin/env python3
#jwtbrute.py
#Brute force JWT files based on alphabet and key length
#set myToken, myAlpha, myLength, and minLength according to what you need

import jwt
import sys
from itertools import chain, product

found = False
attempts = 0
myToken = ""
myAlpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-+"
myLength = 4 #max length of guess
minLength = 4 #min length of guess

def brute(charset, keylength, keymin):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(keymin, keylength + 1)))

for keyl in brute(myAlpha, myLength, minLength):
    attempts += 1
    try:
        jwt.decode(myToken, keyl, algorithms=["HS256"])
        sys.stdout.write("Key Found! %s\n" % (keyl))
        sys.stdout.flush()
        found = True
    except jwt.exceptions.InvalidSignatureError:
        pass

    #optional, but I like seeing progress in my terminal
    if attempts % 1000 == 0:
        sys.stdout.write("Currently on attempt %s\n" % (attempts))
        sys.stdout.write("Current Guess: %s\n" % (keyl))

    if found == True:
        sys.exit("Key found in %s attempts." % (attempts))
