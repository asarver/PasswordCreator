#!/usr/bin/python

import sys
import random

class Password:
    """A Class to make random passwords any length with any characters"""

    def checkInput(self, userInput):
        options = userInput.split(" ")
        for option in options:
            print option
            if option != "#" and option != "s" and option != "A" and option != "a":
                try:
                    if option <= "0" or option >= "50":
                        self.tryAgain()
                        return
                except ValueError:
                    self.tryAgain()
                    return 
        self.options = options

    def tryAgain(self):
        print "Sorry, your input was invalid. Try again (Y or N)?"
        try:
            input = raw_input()[0]
            if input == "y" or input == "Y":
                self.__init__()
                return
        except IndexError:
            pass
        
        print "Good bye."
        sys.exit(0)

    
    def createPassword(self):
        print "Creating your password..."
        self.createSequence()

    def createSequence(self):
        for option in self.options:
            if option == "#":
                for i in range(48, 58):
                    self.sequence.append(i)
            elif option == "s":
                for i in range(33, 48):
                    self.sequence.append(i)
                for i in range(58, 65):
                    self.sequence.append(i)
                for i in range(91, 97):
                    self.sequence.append(i)
                self.sequence.append(123)
                self.sequence.append(125)
            elif option == "A":
                for i in range(65, 91):
                    self.sequence.append(i)
            elif option == "a":
                for i in range(97, 123):
                    self.sequence.append(i)
            else:
                self.length = int(option)
        print self.sequence
    
    def __init__(self):
       self.sequence = []
       self.length = 0
       self.options = []
       self.startUp()

    def startUp(self):
        print "Welcome to Password Generator V 2.0" 
        print "\nHere are options for creating your password:"
        print "\tEnter, seperated by a space, your selections:"
        print "\n\tA numerical value for length"
        print "\t's' for symbols"
        print "\t'A' for capital letters"
        print "\t'a' for lowercase letters"
        print "\t'#' for numbers"
        self.checkInput(raw_input())
        self.createPassword()

if __name__ == "__main__":
    myPassword = Password()
