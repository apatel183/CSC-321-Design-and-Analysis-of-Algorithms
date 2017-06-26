import random
import string

def cipher():
    user_input = input('Please enter your plaintext in all lowercase here: ')
    dictionary = dict()
    alphabet = list(string.ascii_lowercase)
    recode = list(string.ascii_lowercase)
    random.shuffle(recode)
    cipher = ''
    for i in range (26):
        dictionary[alphabet[i]] = recode[i]
    for text in user_input:
        if text in alphabet:
                cipher += dictionary[text]
        if text not in alphabet:
            cipher+=text
    print('Plaintext has been convert to ciphertext: ' + cipher)

root = cipher();
