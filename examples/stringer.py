"""
A module to use for the welcome message and
the log functions

*** NOTE ***
    ERROR (type) CHECKING SHOULD BE PERFORMED BY THE CALLER!!!
*** NOTE ***
"""

# by Erin Coffey
# 15 January 2018

def show_welcome(program_name = "test", author = "Erin Coffey"):
    """
    Accepts string program_name
    Accepts string author
    """
    myLang = " PYTHON "
    numStars = len(author)
    numStars2 = len(program_name)
    middleLine = "**   "+author+"\'s " + program_name + " program   **"
    middleLineLength = len(middleLine)
#    print("The middle line will be:\t " + middleLine)
#    print("The length of the middleLine is:\t" + str(middleLineLength))
    numStarsNeeded = int((middleLineLength - len(myLang)) / 2)
#    print("We willneed " + str(numStarsNeeded) + " stars on either side of python")

 #   print("*************** PYTHON **************")
    myStars = printStars(numStarsNeeded)
    myStars2 = myStars
    if middleLineLength % 2 != 0:
        myStars2 += "*"
        
    print(myStars, end='')
    print(myLang, end='')
    print(myStars2)
    print("**   "+author+"\'s " + program_name + " program   **")
    print(myStars, end='')
    print(myLang, end='')
    print(myStars2)
# end show_welcome()

def printStars(num_Stars):
    stars = ""
    for i in range(num_Stars):
        stars +="*"
    return stars

# use main for testing the functions in this module
def main():
    print("Running test...\n")
    show_welcome()
    print("\nSuccess!")

# if this is the main module, run the tests in main()
if __name__ == "__main__":
    main()
