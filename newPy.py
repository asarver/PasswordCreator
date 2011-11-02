#!/usr/bin/python

import random
import string

class Password:
    OPTIONS = {'#': string.digits, 'a': string.lowercase,
            'A': string.uppercase, 's': string.punctuation}

    def __init__(self, userInput):
        self.length = 0
        self.options = []
        self.password = ''
        self.sequence = ''

        self.checkOptions(userInput)
        self.createSequence()

    def checkOptions(self, userInput):
        for letter in set(userInput):
            if letter in Password.OPTIONS:
                self.options.append(letter)

        numFilter = lambda x: x in string.digits
        num = filter(numFilter, userInput)

        if num and 0 < int(num) <= 50:
            self.length = int(num)
        else:
            self.enterLength()

    def enterLength(self):
        print 'Enter in a length greater than zero but less than 50.'
        num = raw_input()

        try:
            num = int(num)
            if 0 < num <= 50:
                self.length = num
            else:
                self.enterLength()
        except ValueError:
            self.enterLength()

    def createSequence(self):
        for option in self.options:
            self.sequence += Password.OPTIONS[option]

    def createPassword(self):
        if self.sequence:
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
