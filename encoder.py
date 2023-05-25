#!/usr/bin/python3 

import math 
import time 


#Encoder that uses:
# Caesar Cipher 1 
# ROT-13        2
# XOR FF        3
# Affine Cipher 4
# Atbash Cipher 5
# Bacon Cipher  6
# Music Notes   7
# ROT-47        8 
# Morse Code    9 
# Enigma Machine 10 


# Pseudo Code 

# Prints WELCOME TO JURASSIC PARK, oh wait no that's not right but hey 
# there are some strange things here! Go ahead and choose one to test it out! 

# shows list of 10 ciphers to choose from

# Choose 1 good sir! 

# checks to see if it's between 1 and 10 if not error 

# Chooses 1 

# alright you chose #blank# wonderful! What is the string you want to encode? 

# enters string, does it have to check for any invalid characters? 

# Encrypts it using the provided function and/or class 

# prints out encoded value 

# here you are my sir! 

# Asks if there's anything else the user wants to encode y/n 

# if not, exit, if yes 

# Goodbye good sir! Hope to encode something again soon! 


menu = """1. Caesar 
          2. ROT-13
          #3. XOR FF -> figuring this one out 
          4. Affine
          5. Atbash 
          6. Bacon
          7. Music Notes
          8. ROT-47
          9. Morse Code 
          10. ENIGMA MACHINE!! """


print("""Welcome to Jurassic Park! oh wait that's not right buy hey,
there's are some strange things here! Go ahead and choose one to test it out!""")
print(menu)


#CAESAR_CIPHER

def Caesar_cipher(): # can only do ascii no digits, must check for that
    strings = input("What is the string you want to cipher from caesar: ")
    shift   = int(input("How many shifts: "))
    result = ""

    for x in strings:
        x = ord(x)
        x += shift
        if x > 126:
            x = x - 95
        elif x < 32:
            x = x + 95 
        else: 
            result += chr(x)
    print(strings)
    print(result)


#ROT13

def rot_13():
    strings = input("Don't be rotten, use rot 13!: ")

    result = ""
    for x in strings:
        x = ord(x)
        x += 13 
        if x > 65 and x < 90:
            x = x + 13
            result += chr(x)
        elif x > 32:
            x = x - 26 
            result += chr(x)
        elif x > 97 and x < 122:
            x = x + 13
            result += chr(x)
        elif x  > 97:
            x = x - 26
            result += chr(x)
        else:
            result += chr(x)
    print(strings)
    print(result)


# def xor_me(): 


#AFFINE CIPHER

class Affine(object):
    global encrypt_me
    encrypt_me = input("What is the string you want to encrypt: ")
    DIE = int(input("What is the die number you want to use: "))
    KEY = str(input("Give me three numbers for the key separated by spaces: "))
    KEY = KEY.split(' ')
    KEY = [int(x) for x in KEY]
  
    def __init__(self):
        pass
    def encryptcharacters(self, char):
        K1, K2, kI = self.KEY
        return chr((K1 * ord(char) + K2) % self.DIE)

    def encrypt(self, string):
        return "".join(map(self.encryptcharacters, string))

    
    def decryptcharacters(self, char):
        K1, K2, KI = self.KEY
        return chr(KI * (ord(char) - K2) % self.DIE)

    def decrypt(self, string):
        return "".join(map(self.decryptcharacters, string))


    def output():
        print(Affine.encrypt(encrypt_me))


#ATBASH CIPHER

class Atbash:
    def solve(self, text):
        N = ord('z') + ord('a')
        ans=''
        return ans.join([chr(N - ord(s)) for s in text])


#BACON CIPHER

lookup = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa',
          'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab',
          'K': 'ababa', 'L': 'ababb', 'M': 'abbaa', 'N': 'abbab', 'O': 'abbba',
          'P': 'abbbb', 'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb',
          'U': 'babaa', 'V': 'babab', 'W': 'babba', 'X': 'babbb', 'Y': 'bbaaa', 'Z': 'bbaab'}
 
# Function to encrypt the string according to the cipher provided
 
 
def bacon_encrypt(message):
    cipher = ''
    for letter in message:
        # checks for space
        if(letter != ' '):
            # adds the ciphertext corresponding to the
            # plaintext from the dictionary
            cipher += lookup[letter]
        else:
            # adds space
            cipher += ' '
 
    return cipher








def encryption_choice(choice):
    choice_library = {
        1: Caesar_cipher(),
        2: rot_13(),
        3: Affine(),
        4: Atbash(),
        5: bacon_encrypt(),

    }
         

