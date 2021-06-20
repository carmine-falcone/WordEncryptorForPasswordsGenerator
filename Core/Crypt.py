#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Encrypter e decrypter! - by carmine-falcone!
Crypt!
'''

def Encrypt(word):
    e = ''
    for i in word:
        if i == 'a':
            e += i.replace("a", '1 ')
        if i == 'b':
             e += i.replace("b", '2 ')
        if i == 'c':
             e += i.replace("c", '3 ')
        if i == 'd':
             e += i.replace("d", '4 ')
        if i == 'e':
             e += i.replace("e", '5 ')
        if i == 'f':
             e += i.replace("f", '6 ')
        if i == 'g':
             e += i.replace("g", '7 ')
        if i == 'h':
             e += i.replace("h", '8 ')
        if i == 'i':
             e += i.replace("i", '9 ')
        if i == 'j':
             e += i.replace("j", '10 ')
        if i == 'k':
             e += i.replace("k", '11 ')
        if i == 'l':
             e += i.replace("l", '12 ')
        if i == 'm':
             e += i.replace("m", '13 ')
        if i == 'n':
             e += i.replace("n", '14 ')
        if i == 'o':
             e += i.replace("o", '15 ')
        if i == 'p':
             e += i.replace("p", '16 ')
        if i == 'q':
             e += i.replace("q", '17 ')
        if i == 'r':
             e += i.replace("r", '18 ')
        if i == 's':
             e += i.replace("s", '19 ')
        if i == 't':
             e += i.replace("t", '20 ')
        if i == 'u':
             e += i.replace("u", '21 ')
        if i == 'v':
             e += i.replace("v", '22 ')
        if i == 'w':
             e += i.replace("w", '23 ')
        if i == 'x':
             e += i.replace("x", '24 ')
        if i == 'y':
             e += i.replace("y", '25 ')
        if i == 'z':
             e += i.replace("z", '26 ')
        if i == " ":
             e += i.replace(" ", '27 ')
        if i == "0":
             e += i.replace('0', '28 ')
        if i == "1":
             e += i.replace('1', '29 ')
        if i == "2":
             e += i.replace('2', '30 ')
        if i == "3":
             e += i.replace("3", '31 ')
        if i == "4":
             e += i.replace('4', '32 ')
        if i == "5":
             e += i.replace('5', '33 ')
        if i == "6":
             e += i.replace('6', '34 ')
        if i == "7":
             e += i.replace('7', '35 ')
        if i == "8":
             e += i.replace('8', '36 ')
        if i == '9':
             e += i.replace("9", '37 ')
        if i == '@':
             e += i.replace("@", "38 ")
        if i == '.':
             e += i.replace(".", '39 ')
        if i == '#':
             e += i.replace("#", '40 ')
        if i == '!':
             e += i.replace("!", "41 ")
        if i == '_':
             e += i.replace("_", "42 ")
    return e
def Decrypt(word):
    e = ''
    for i in word.split():
        if i == '1':
            e += i.replace("1", 'a')
        if i == '2':
             e += i.replace("2", 'b')
        if i == '3':
             e += i.replace("3", 'c')
        if i == '4':
             e += i.replace("4", 'd')
        if i == '5':
             e += i.replace("5", 'e')
        if i == '6':
             e += i.replace("6", 'f')
        if i == '7':
             e += i.replace("7", 'g')
        if i == '8':
             e += i.replace("8", 'h')
        if i == '9':
             e += i.replace("9", 'i')
        if i == '10':
             e += i.replace("10", 'j')
        if i == '11':
             e += i.replace("11", 'k')
        if i == '12':
             e += i.replace("12", 'l')
        if i == '13':
             e += i.replace("13", 'm')
        if i == '14':
             e += i.replace("14", 'n')
        if i == '15':
             e += i.replace("15", 'o')
        if i == '16':
             e += i.replace("16", 'p')
        if i == '17':
             e += i.replace("17", 'q')
        if i == '18':
             e += i.replace("18", 'r')
        if i == '19':
             e += i.replace("19", 's')
        if i == '20':
             e += i.replace("20", 't')
        if i == '21':
             e += i.replace("21", 'u')
        if i == '22':
             e += i.replace("22", 'v')
        if i == '23':
             e += i.replace("23", 'w')
        if i == '24':
             e += i.replace("24", 'x')
        if i == '25':
             e += i.replace("25", 'y')
        if i == '26':
             e += i.replace("26", 'z')
        if i == "27":
             e += i.replace("27", " ")
        if i == '28':
             e += i.replace("28", "0")
        if i == "29":
             e += i.replace('29', '1')
        if i == "30":
             e += i.replace('30', '2')
        if i == "31":
             e += i.replace("31", '3')
        if i == "32":
             e += i.replace('32', '4')
        if i == "33":
             e += i.replace('33', '5')
        if i == "34":
             e += i.replace('34', '6')
        if i == "35":
             e += i.replace('35', '7')
        if i == "36":
             e += i.replace('36', '8')
        if i == '37':
             e += i.replace("37", '9')
        if i == '38':
             e += i.replace("38", "@")
        if i == '39':
             e += i.replace("39", '.')
        if i == '40':
             e += i.replace("40", '#')
        if i == '41':
             e += i.replace("41", "!")
        if i == '42':
             e += i.replace("42", "_")
    return e
