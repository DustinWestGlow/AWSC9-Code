# Hello, here run tests and have fun
# write commands to print encrypted
# things to the terminal

from monoalphabetic import Monoalphabetic

# message = "and you too, brutus?"
key = 13
mono = Monoalphabetic()
abcm = mono.alphabet
mono.caesar(key) # mono.genmap("c", 3)
encrypted = mono.substitute(abcm)
again = mono.substitute(encrypted)
print(key)
print(abcm)
print(encrypted)
print(again)