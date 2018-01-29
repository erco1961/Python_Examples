#!/usr/bin/env python3

# an example Python program working with strings
# by Erin Coffey
# 24 January 2018

import sys
MODULES_DIR = "/Users/erin/Documents/Development/Python/modules/"
sys.path.append(MODULES_DIR)

# import local module for welcome message
import stringer
# import module for getting random words
import wordlist
# import module for tracking lost time
import timer

AUTHOR = "Erin Coffey"
NAME = "Hangman"
MAX_TRIES = 7

def get_word():
  word = wordlist.get_random_word()
  return word.upper()

# end get_word()

def add_spaces(word):
  word_with_spaces = " ".join(word)
  return word_with_spaces

# end add_spaces()

def draw_hangman(num_wrong):
  print("____")
  print("    |")
  if num_wrong > 0:
    print("    O")
  if num_wrong >= 4:
    print("   \|/")
  elif num_wrong == 4:
    return
  elif num_wrong == 3:
    print("    |/")
    return
  elif num_wrong == 2:
    print("    | ")
    return
  elif num_wrong == 1:
    return
  if num_wrong >= 5:
    print("    |")
  if num_wrong == 5:
    return
  elif num_wrong == 6:
    print("     \\")
    return
  elif num_wrong == 7:
    print("   / \\")
  else:
    print()
#end draw_hangman()

def draw_screen(num_wrong, num_guesses, letters_guessed, displayed_word):
  draw_hangman(num_wrong)
  print("-" * 79)
  print("Word:", add_spaces(displayed_word),
        "  Guesses:", num_guesses,
        "  Wrong:", num_wrong,
        "  Tried:", add_spaces(letters_guessed))
  
# end draw_screen()

def get_letter(letters_guessed):
  while True:
    guess = input("Guess a letter: ").strip().upper()

    if guess == "" or len(guess) > 1:
      print("Invalid entry. Please enter one and only one letter.")
      continue
    elif guess in letters_guessed:
      print("You already tried that letter.")
      continue
    else:
      return guess

# end get_letter()

def play_game():
  word = get_word()
  word_length = len(word)
  remaining_letters = word_length
  displayed_word = "_" * word_length

  num_wrong = num_guesses = 0
  letters_guessed = ""

  draw_screen(num_wrong, num_guesses, letters_guessed, displayed_word)

  while num_wrong < MAX_TRIES and remaining_letters > 0:
    guess = get_letter(letters_guessed)
    letters_guessed += guess

    pos = word.find(guess, 0)
    if pos != -1: # the letter is in the word
      displayed_word = ""
      remaining_letters = word_length
      for char in word:
        if char in letters_guessed:
          displayed_word += char
          remaining_letters -= 1
        else:
          displayed_word += "_"
    else:
      num_wrong += 1
    num_guesses += 1

    draw_screen(num_wrong, num_guesses, letters_guessed, displayed_word)

    print("-" * 79)
  if remaining_letters == 0:
    print("Congratulations! You guessed the word in",
           num_guesses, " guesses.")
  else:
    print("You are a loser!")
    print("The word was '" + word + "'")

# end play_game()

def main():
  myTimer = timer.begin_timer()
  stringer.show_welcome(NAME)
  print()
  print("Play the HANGMAN game")


  while True:
    print()
    play_game()
    print()
    
    choice = input("Try \'" + NAME + "\' program again? (y/n): ")
    if choice.lower() != "y":
      break

  # end while loop
  timer.stop_timer(myTimer)
# end main()
print("Bye!")


#if the current module is the main module
if __name__ == "__main__":
  main()
