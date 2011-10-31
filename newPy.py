#!/usr/bin/python

import sys
import random
import string

class Password:
    def __init__(self, input):
        self.sequence = ''
        self.length = 0
        self.options = []
        self.password = ""

        self.checkOptions(input)
        self.createSequence()

    def checkOptions(self, input):
        length = ''
        num = ''
        for letter in input:
            if letter not in ['#', 'a', 'A', 's']:
                if 48 <= ord(letter) <= 57:
                    num += letter
            else:
                self.options.append(letter)
        if int(num) <= 0 or int(num) > 50:
            self.enterLength()
        else:
            self.length = int(num)

    def enterLength(self):
        print "Enter in a length greater than zero but less than 50."
        num = raw_input()
        try:
            num = int(num)
            if num > 0 and num <= 50:
                self.length = num
            else:
                self.enterLength()
        except ValueError:
            self.enterLength()

    def createSequence(self):
        for option in self.options:
            if option == '#':
                self.sequence += string.digits
            elif option == 's':
                self.sequence += string.punctuation
            elif option == 'A':
                self.sequence += string.uppercase
            elif option == 'a':
                self.sequence += string.lowercase

    def createPassword(self):
        for i in range(self.length):
            self.password += random.choice(self.sequence)
        return self.password

if __name__ == "__main__":
    print "Welcome to Password Generator V 2.0"
    print "\nHere are options for creating your password:"
    print "\tEnter, seperated by a space, your selections:"
    print "\n\tA numerical value for length"
    print "\t's' for symbols"
    print "\t'A' for capital letters"
    print "\t'a' for lowercase letters"
    print "\t'#' for numbers"

    myPassword = Password(raw_input())
    print myPassword.createPassword()
