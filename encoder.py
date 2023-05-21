#!/usr/bin/python3 

import math 
import time 


#Encoder that uses:
# Caesar Cipher     1 
# ROT-13            2
# ATBASH            3
# Vigenre           4
# bacon             5
# letters to music  6
# ROT 47            7
# morse code        8 
# monoalphabetic    9 
# AFFINE           10 




menu = """
# Caesar Cipher     1 
# ROT-13            2
# ATBASH            3 
# Vigenre           4
# bacon             5
# letters to music  6
# ROT 47            7
# morse code        8 
# monoalphabetic    9 
# AFFINE           10 
        """


print("""Welcome to Jurassic Park! oh wait that's not right buy hey,
there's are some strange things here! Go ahead and choose one to test it out!""")
print(menu)

#CAESAR_CIPHER

class Caesar_Encipher():
    

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



#ROT-13

class Rot_me():

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


#ATBASH
class Atbash:
    def solve():
        text = input("Who would you like to take to the fall bash: ")
        N = ord('z') + ord('a')
        ans=''
        print(ans.join([chr(N - ord(s)) for s in text]), end='\n')




#BACON

lookup = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa',
          'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab',
          'K': 'ababa', 'L': 'ababb', 'M': 'abbaa', 'N': 'abbab', 'O': 'abbba',
          'P': 'abbbb', 'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb',
          'U': 'babaa', 'V': 'babab', 'W': 'babba', 'X': 'babbb', 'Y': 'bbaaa', 'Z': 'bbaab'}

class Bacon():
    def bacon_encrypt():
        message = input("What Mesage would you like to encrypt with some bacon? all capital letters: ")
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
 
        print(cipher)



#MUSIC NOTES
notes = { 'A':'DO', 'B':'RE', 'C':'MI', 'D':'FA', 'E':'SOL', 'F':'LA', 'G':'SI'}
class Music():
    def letters_to_music_notes():
        letters_to_convert = input("What are the letters you want to turn into music notes (C,D,E,F,G,A): ")
        cipher = ''
        for letter in letters_to_convert:
            if(letter != ' '):
                # adds the ciphertext corresponding to the
                # plaintext from the dictionary
                cipher += notes[letter]
            else:
                # adds space
                cipher += ' '
 
        print(cipher)


#ROT47

class Rot_again():
    def rot47():
        s = input("WHAT WOULD YOU LIKE TO USE ROT47 FOR: ")
        x = []
        for i in range(len(s)):
            j = ord(s[i])
            if j >= 33 and j <= 126:
                x.append(chr(33 + ((j + 14) % 94)))
            else:
                x.append(s[i])
        print(''.join(x))



# MORSE CODE 
CHARS_TO_MORSE_CODE_MAPPING = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '\'': '· − − − − ·',
    '!': '− · − · − −',
    '/': '− · · − ·',
    '(': '− · − − ·',
    ')': '− · − − · −',
    '&': '· − · · ·',
    ':': '− − − · · ·',
    ';': '− · − · − ·',
    '=': '− · · · −',
    '+': '· − · − ·',
    '-': '− · · · · −',
    '_': '· · − − · −',
    '"': '· − · · − ·',
    '$': '· · · − · · −',
    '@': '· − − · − ·',
}
class Morsels_of_MorseCode():
    def to_morse_code():
        morse_code = input("WHAT IS NEEDED FOR THE WAR SIR...:")
        for char in morse_code:
            # checking for space
            # to add single space after every character and double space after every word
            if char == ' ':
                morse_code += '  '
            else:
                # adding encoded morse code to the result
                morse_code += CHARS_TO_MORSE_CODE_MAPPING[char.upper()] + ' '
        print(morse_code)





choice = input("What is your choice: ")


if choice == "1":
    Caesar_Encipher.Caesar_cipher()
elif choice == "2":
    Rot_me.rot_13()
elif choice == "3":
    Atbash.solve()
elif choice == "4":
    print("In working progress...")
elif choice == "5":
    Bacon.bacon_encrypt()
elif choice == "6":
    Music.letters_to_music_notes()
elif choice == "7":
    Rot_again.rot47()
elif choice == "8":
    Morsels_of_MorseCode.to_morse_code()
elif choice == "9":
    print("In Working progess...")
elif choice == "10":
    print("In working progress...")
else:
    print("That's not a valid input!")