# Hello, this file "cracks" monoalphabetic ciphers
# by filing brute force results
# elsewhere we will use BF files to guess at
# the key, then reverse the key,
# of ciphertext from a monoalphabetic cipher

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


import random
print(f"MESSAGE: '{message}'")
print("ENCRYPTING...")
multiplied = random.choice(m_ks)
shifted = random.choice(c_ks)
encrypted = mc.encrypt(message, multiplied)
print(f"multiplicative '{multiplied}': {encrypted}")
encrypted = caesar_cipher(encrypted, shifted)
print(f"caesar '{shifted}': {encrypted}")

print("DECRYPTING...")
# decrypt attempts
attack_file = open("attacks_affine.txt", "w")
attack_file.write("shift,multiply,caesar,multiplicative,result\n")
for mult in m_ks:
    for shift in c_ks:
        c = encrypted
        m = caesar_cipher(c, shift)
        k = mc.encrypt(m, mult)
        p = k
        attack_file.write(f"{shift},{mult},{m},{k},{p}\n")
        if p == message:
            print(f"caesar '{shift}': {m}")
            print(f"multiplicative '{mult}': {k}")
            print("CRACKED!")
            print(f"message = '{p}'")
attack_file.close()