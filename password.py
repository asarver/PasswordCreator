#!/usr/bin/python

class Password:
    """A Class to make random passwords any length with any characters"""

    def makePassword():
        pass

    def setOptions(self, options):
        self.options = options;

    def getOptions(self):
        return self.options

    def checkInput(self, userInput):
        options = userInput.split(" ")
        for option in options:
            if int(option) <= 0 or int(option) >= 50:
                if option != '#' or option != 's' or option != 'A' or option != 'a':
                    self.tryAgain()
                    break
        self.setOptions(userInput)

    def tryAgain(self):
        print "Sorry, your input was invalid. Try again (Y or N)?"
        try:
            input = raw_input()[0]
            if input == 'y' or input == 'Y':
                self.__init__()
                return
        except IndexError:
            pass
        
        print "Good bye."
        return

    def __init__(self):
        self.options_avail = ['#', 's', 'A', 'a']
        print "Welcome to Password Generator V 2.0" 
        print "\nHere are options for creating your password:"
        print "\tEnter, seperated by a space, your selections:"
        print "\n\tA numerical value for length"
        print "\t's' for symbols"
        print "\t'A' for capital letters"
        print "\t'a' for lowercase letters"
        print "\t'#' for numbers"
        self.checkInput(raw_input())


if __name__ == "__main__":
    myPassword = Password()
