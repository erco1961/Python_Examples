#!/usr/bin/env python3

# an example Python program working with strings
# by Erin Coffey
# 24 January 2018

# import local module for welcome message
import stringer

AUTHOR = "Erin Coffey"
NAME = "Working with String objects"

def show_ordinal_values():
    myString = "The ordinal value of the unicode character "
    print(myString + "'5' is: ", ord("5"))
    print(myString + "'A' is: ", ord("A"))
    print(myString + "'a' is: ", ord("a"))
    print()
    print("The string we will now loop over is: '" + myString + "'")
    total_value = 0
    for char in myString:
        print(char, " = " + str(ord(char)))
        total_value += ord(char)
    print("The total ordinal value of the string is: '" + str(total_value) + "'\n")

    words = myString.split()# split on space
    print("The words in the string are: ")
    for word in words:
        print(word)
    print()

    segments = myString.split("e")
    print("If we split on the letter 'e'... ")
    for segment in segments:
        print(segment.lstrip())#remove space to the left of the segmentß
    print()
    
# end show_ordinal_values

def demonstrate_string_indices_and_slices():
    i = 3
    myString = "Howdy from the \'demonstrate_string_indices_and_slices()\' method!"
    print("The string to work with is: " + "\"" + myString + "\"\n")
    while i >= 0:
        try:
            if i == 3:
                i -= 1
                print("The char at index '0' is: ",end="")
                print(myString[0])

                print("The char at index '-1' is: ",end="")
                print(myString[-1])

                print("Accessing the char at index '99' yields: ",end="")
                # cause exception
                print(myString[99])

            if i == 2:
                i -= 1
                print("Try to change the char at index '0' as myString[0] = J yields: ",end="")
                # cause exception
                myString[0] = "J"

            if i == 1:
                i -= 1
                # multi-line example with return charachters embedded
                myQuery = '''SELECT categoryID, name AS categaoryName
                             FROM Category WHERE categoryID = ?'''
                print("\nA multi-line string as SQL query example:\n" + myQuery)

            if i == 0:
                i -= 1
                print()

            i -= 1
        except Exception as e:
            print(type(e), e)
            
    mySoLong = "Goodbye " + myString[6:]#take a slice
    myStars = "*" * len(mySoLong)
    print(myStars)
    print(mySoLong)
    print(myStars)
    print()

# end demonstrate_string_indices()

def demonstrate_string_searches():
    myString = "Howdy from the 'demonstrate_string_searches()' method!"
    print("The string to work with is: " + "\"" + myString + "\"\n")

    print("Search for 'string' in the String and...")
    search_string = "string"
    if search_string in myString:
        print("Yes, '" + search_string + "' is in the String!")
    else:
        print("Nope, '" + search_string + "' is NOT in the String!")

    search_string = "String"
    print("But, search for " + search_string + " in the String and...")
    if search_string in myString:
        print("Yes, '" + search_string + "' is in the String!")
    else:
        print("Nope, '" + search_string + "' is NOT in the String!")

    while True:
        print()
        search_string = input("Enter a search term: ")
        if search_string in myString:
            print("Yes, '" + search_string + "' is in the String at position: "+"["+str(myString.find(search_string))+"]")
        else:
            print("Nope, '" + search_string + "' is NOT in the String!")

        choice = input("Try 'demonstrate_string_searches()' method again? (y/n): ")
        if choice.lower() != "y":
          break
    
    mySoLong = "Goodbye " + myString[6:]#take a slice
    myStars = "*" * len(mySoLong)
    print()
    print(myStars)
    print(mySoLong)
    print(myStars)
    print()
 
# end demonstrate_string_searches()

def play_with_strings():
    myString = "Howdy from the 'play_with_strings()' method!"
    print("The string to work with is: " + "\"" + myString + "\"\n")

    while True:
        print()
        sub_string = input("Which part of the string do you want to replace? ")
        if myString.find(sub_string) == -1:
            print("'"+sub_string+"' is NOT part of the string. Please try again.")
            continue
            
        substitute = input("What do you want to replace it with? ")
        myString = myString.replace(sub_string, substitute)

        print("The String is now: '"+myString+"'")

        choice = input("Try 'play_with_strings()' method again? (y/n): ")
        if choice.lower() != "y":
          break
    
    mySoLong = "Goodbye " + myString[6:]#take a slice
    myStars = "*" * len(mySoLong)
    print()
    print(myStars)
    print(mySoLong)
    print(myStars)
    print()
 
# end demonstrate_string_searches()

def main():
  stringer.show_welcome(NAME)

  while True:
    print()
    show_ordinal_values()
    demonstrate_string_indices_and_slices()
    demonstrate_string_searches()
    play_with_strings()


    choice = input("Try \'" + NAME + "\' program again? (y/n): ")
    if choice.lower() != "y":
      break

  # end while loop
# end main()
print("Bye!")

#if the current module is the main module
if __name__ == "__main__":
  main()
