#!/usr/bin/env python3

# an example Python program
# by Erin Coffey
# 16 January 2018

# import stringer module for welcome message
import stringer
# import validation module for taking valid user input
import validation

import copy
import random

AUTHOR = "Erin"
NAME = "List Processing"

def display_menu():
  print("\n******************************")
  print("**       COMMAND MENU       **")
  print("******************************\n")
  print("**\tlist - List all movies")
  print("**\tadd  - Add a movie to the list")
  print("**\tdel  - Delete a movie from the list")
  print("**\tcnt  - Display the number of [items] in the list")
  print("**\thelp - Display the Command Menu")
  print("**\ttest - Run automated tests on various lists")
  print("**\texit - Exit program\n")

# end display_menu()

def print_movie_list(movies_list):
  message = "The movie"
  suffix = ""
  if len(movies_list) > 1:
    suffix = "s in the list are:\n"
  elif len(movies_list) == 1:
    suffix = " in the list is:\n"
  else:
    message = "There no movies in the list!"
  print(message + suffix)
  i = 1
  print("       NAME       |       GENRE       |       RATING\n\n")
  for movie in movies_list:
    print(str(i) + ". ", end="")
    index = 0
    entry = ""
    for item in movie:
      entry += str(item)
      if index < len(movie)-1:
        entry += " | "
      index += 1
    print(entry)
    i += 1
  print()

# end print_movie_list()

def add_movie_to_list(movies_list):
  #print("From add_movie_to_list()")
  movie_name = input("Name: ")
  if movie_name == "":
    movie = "Silent Movie"
  movie_genera = input("Genre: ")
  if movie_genera == "":
    movie_genera = "Other, non-specific"
  movie_rating = validation.get_float("Rating: ", 10)
  movie = [str(movie_name), str(movie_genera), movie_rating]
  movies_list.append(movie)
  print("\"" + str(movie) + "\" has been added to the list.")

# end add_movie_to_list()

def delete_movie_from_list(movies_list):
  if len(movies_list) == 0:
    print("There are no movies in the list!")
  else:
    index = validation.get_int("Movie Index: ", len(movies_list))
    movie = movies_list.pop(index-1)
    print(str(movie[0]) + " has been deleted.\n")
# end delete_movie_from_list()

def show_count_categories():
  print("\n******************************")
  print("**       CATEGORIES      **")
  print("******************************\n")
  print("**\ttot  - Total number of movies")
  print("**\tgen  - Number of genres")
  print("**\trat  - Number of movies above the given rating")
# end show_count_categories()

def count_genres(movies_list):
  #initialize the list
  movies = [["","",0]]
  genre = input("What Genre? ")
  genre = genre.rstrip()
  for movie in movies_list:
    if str(movie[1]).lower() == genre.lower():
      movies.append(movie)
  # remove the initial element
  movies.pop(0)
  print("There are " + str(len(movies)) + " movies of the genre \"" + str(genre) + "\" in the list.")
  if len(movies) > 0:
    print_movie_list(movies)
# end count_generas()

def show_by_rating(movies_list):
  #initialize the list
  #movies = [[0, ["","",0]]]
  #movies_sorted = [["","",0]]
  movies_to_send = [["","",0]]
  # remove the initial element
  #movies.pop(0)
  #movies_sorted.pop(0)
  movies_to_send.pop()
  count = 0
  rating = validation.get_float("What is the lowest rated movie you want to see? ", 10)
  for movie in movies_list:
    #print("The movie is \"" + str(movie[0]) + "\" and, the rating is: " + str(movie[2]))
    if int(movie[2]) >= rating:
      #newMovie =[movie[2],[movie]]
      #movies.append(newMovie)
      movies_to_send.append(movie)
      count += 1

  
  if len(movies_to_send) > 0:
    print(str(len(movies_to_send)) + " movies found with a rating of at least " + str(rating))
    print_movie_list(movies_to_send)
  else:
    print("There are " + str(len(movies_to_send)) + " movies in the list with a rating of at least " + str(rating))
    #this algorithm for sorting by rating is not perfect yet!
    
##    for sorted in movies:
##      print("sorted[0][0]: ", end="")
##      print(sorted)
##      movies_sorted.append(sorted[1][0])
##    print("Movies_sorted: ", end="")

 #   print_movie_list(movies_sorted.sort())
      
# end show_by_rating()

def display_count(movies_list):
  show_count_categories()
  category = input("Category: ")
  category = category.rstrip()
  if category.lower() == "tot":
    print("There are " + str(len(movies_list)) + " movies in the list. Use \"list\" command to see them.")
  elif category.lower() == "gen":
    count_genres(movies_list)
  elif category.lower() == "rat":
    show_by_rating(movies_list)
  else:
    print("\""+ str(category) + "\" is not a valid selection. Please try again.\n")
# end display_count()

def run_shallow_copy():
  print("Running run_shallow_copy() tests...\n")
  print("A shallow copy example...\n")
  list_one = [1, 2, 3, 4, 5]
  print("list_one is: ",end = "")
  print(list_one)
  print("Set list_two = list_one...")
  list_two = list_one
  print("list_two is: ",end="")
  print(list_two)
  print("modify list_two as list_two[1] = 4")
  list_two[1] = 4
  print("list_one is: ",end = "")
  print(list_one)
  print("list_two is: ",end="")
  print(list_two)
  print()
  
# end run_shallow_copy()

def run_deep_copy():
  print("Running run_deep_copy() tests...\n")
  print("A deep copy example...\n")
  list_one = [1, 2, 3, 4, 5]
  print("list_one is: ",end = "")
  print(list_one)
  print("Set list_two as list_two = copy.deepcopy(list_one)...")
  list_two = copy.deepcopy(list_one)
  print("list_two is: ",end="")
  print(list_two)
  print("modify list_two as list_two[1] = 4")
  list_two[1] = 4
  print("list_one is: ",end = "")
  print(list_one)
  print("list_two is: ",end="")
  print(list_two)
  print()
  
# end run_deep_copy()

def min_max_choice_shuffle():
  print("Running min_max_choice_shuffle() tests...\n")
  list_one = [1, 2, 3, 4, 5]
  print("list_one is: ",end = "")
  print(list_one)
  print()
  print("A minimum value example...")
  print("min(list_one) is: ",end="")
  print(min(list_one))
  print()
  print("A maximum value example...")
  print("max(list_one) is: ",end="")
  print(max(list_one))
  print()
  print("A random choice example...")
  print("random.choice(list_one) is: ",end="")
  print(random.choice(list_one))
  print()
  print("A shuffle example...")
  print("The results of random.shuffle(list_one) is: ",end="")
  random.shuffle(list_one)
  print(list_one)
  print()
# end min_max_choice_shuffle()

def work_with_tuples():
  print("Running work_with_tuples() tests...\n")
  print("A tuple is an immutable list...")
  print("Create a single element tuple as my_int_tuple = (99,)")
  my_int_tuple = (99,)
  print("Create a multi element tuple as my_float_tuple = (48.0, 33.9, 22.0, 100.0, 53.9)")
  my_float_tuple = (48.0, 33.9, 22.0, 100.0, 53.9)
  print("Create a multi element tuple of various type items as my_varied_tuple = (\"lavander\", 10, \"peach\", 100.0, True)")
  my_varied_tuple = ("lavander", 10, "peach", 100.0, True)

  print("Show first item in my_float_tuple as my_float_tuple[0]")
  print(my_float_tuple[0])
  print("Show last item in my_float_tuple as my_float_tuple[-1]")
  print(my_float_tuple[-1])
  print("Show items 1-3 in my_varied_tuple as my_varied_tuple[1:4]")
  print(my_varied_tuple[1:4])
  print("Unpack items from my_varied_tuple as a, b, c, d, e = my_varied_tuple")
  a, b, c, d, e = my_varied_tuple
  print("value of variable 'a' is: ",end="")
  print(a)
  print("value of variable 'e' is: ",end="")
  print(e)
  

# end work_with_tuples()


def run_tests():
  print("Running various list tests...")

  run_shallow_copy()
  run_deep_copy()
  min_max_choice_shuffle()
  work_with_tuples()

 # end run_tests() 

def main():
  stringer.show_welcome(NAME)
  movies_list = [["It's a good life", "Drama", 9.5],
                 ["Blade Runner", "Science Fiction", 10],
                 ["Shrek", "Animation", 8.5]]

  display_menu()

  while True:
    command = input("\nBye Your Command:\t")
    command = command.rstrip()
    if command.lower() == "list":
      print_movie_list(movies_list)
    elif command.lower() == "add":
      add_movie_to_list(movies_list)
    elif command.lower() == "del":
      delete_movie_from_list(movies_list)
    elif command.lower() == "help":
      display_menu()
    elif command.lower() == "cnt":
      display_count(movies_list)
    elif command.lower() == "test":
      run_tests()
    elif command.lower() == "exit":
      break
    else:
      print("\""+ str(command) + "\" is not a valid selection. Please try again.\n")
  # end while loop
  print("Bye!")
# end main()


#if the current module is the main module
if __name__ == "__main__":
  main()
