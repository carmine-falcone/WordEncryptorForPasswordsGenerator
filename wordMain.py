#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Transform letters into their respective numbers, great for generating passwords!
Example:
user@linux ~/ python3 word.py
1)      Encrypt
2)      Decrypt
>>> 1
Do you want to remove the spaces? (If you remove it, it will not be possible to do the reverse process!)[Y/N]:
>>>n
GETPASS[Y/N]?: n
WORD: $!#Thisisverysafe
Retry WORD: $!#Thisisverysafe
Size CYPHERTEXT: 41
Clean Text Size: 17
encrypted word: 41 40 20 8 9 19 9 19 22 5 18 25 19 1 6 5

1)      Encrypt
2)      Decrypt

>>> 2
Do you want to remove the spaces? (If you remove it, it will not be possible to do the reverse process!)[Y/N]:
>>> n
GETPASS[Y/N]?: n
WORD: 41 40 20 8 9 19 9 19 22 5 18 25 19 1 6 5
Retry WORD: 41 40 20 8 9 19 9 19 22 5 18 25 19 1 6 5
Size: 16
Decrypted word: !#thisisverysafe

1)      Encrypt
2)      Decrypt

>>>





'''
#Modules
from __future__ import print_function
from time import sleep
from unidecode import unidecode
from getpass import getpass

import sys
#Modules from Core
from Core.Crypt import *


#Vars
panel = '''
1)      Encrypt
2)      Decrypt 
'''
try:
    raw_input
except:
    raw_input = str(input)
def GetWord():
    while 1:
        what = str(input("GETPASS[Y/N]?: "))
        #if confmodePassword['Valor']:
        if what.upper() == 'Y':
            word = getpass("WORD: ")
            word2 = getpass("Retry WORD: ")
            if word != word2:
                print("WRONG Pass!")
            else:
                break
        else:
            word = str(input("WORD: "))
            word2 = str(input("Retry WORD: "))
            if word != word2:
                print("WRONG Pass!")
            else:
                break
    word = word.lower()
    word = unidecode(word)
    return word

def main():
    print("The Default is still the only option :)\nAll letters were lowercase and accents removed!\nBETA VERSION!\n")
    print("Type exit to exit or Ctrl C")
    while 1:
        try:
            while 1:
                    print(panel)
                    number = str(input(">>> "))
                    if number != '1' and number != '2':
                        if number.lower() == 'exit':
                            print("\nBye bye :]")
                            sys.exit()
                        else:
                            print("Wrong alternative!")
    
                    else:
                        break
            while 1:
                print("Do you want to remove the spaces? (If you remove it, it will not be possible to do the reverse process!)[Y/N]: ")
                delet = str(input(">>> "))
                delet = delet.upper()
                if delet != 'Y' and delet != 'N':
                    print("Wrong alternative!")
                else:
                    break
            word = GetWord()
            if number == '1':
                final = Encrypt(word)
                if delet == 'S':
                    print("Size CYPHERTEXT: %d\nClean Text Size: %d\nencrypted word: %s"%(len(final),len(word),final.replace(" ", "")))
                else:
                    print("Size CYPHERTEXT: %d\nClean Text Size: %d\nencrypted word: %s"%(len(final),len(word), final))

            else:
                final = Decrypt(word)
                print("Size: %d\nDecrypted word: %s"%(len(final),final))
        except KeyboardInterrupt:
            print("\nBye bye :]")
            sys.exit()

if __name__ == '__main__':
    main()
