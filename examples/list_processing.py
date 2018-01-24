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
import os.path
import csv
import pickle # use for binary files access

AUTHOR = "Erin Coffey"
NAME = "List Processing"
MOVIE_FILE_TXT = "saved_movies.txt"
MOVIE_FILE_CSV = "saved_movies.csv"
MOVIE_FILE_BIN = "saved_movies.bin"
DEBUG = False

def pick_mode():
  print("\n******************************")
  print("**          MODES           **")
  print("******************************\n")
  print("**\ttxt - Program uses .txt file for movie storage")
  print("**\tcsv - Program uses .csv file for movie storage")
  print("**\tbin - Program uses .bin file for movie storage")

# end pick_mode()

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
  if DEBUG:
    print("From print_movie_list, the length is " + str(len(movies_list)))
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
  print("\n")
  #use field widths to align results
  print("   {:20} {:5} {:20} {:5} {:10}".format("NAME", "|", "GENRE", "|", "RATING"))
  print("\n\n")
  for movie in movies_list:
    print(str(i) + ". ", end="")
##    index = 0
##    entry = ""
##    for item in movie:
##      entry += str(item)
##      if index < len(movie)-1:
##        entry += " | "
##      index += 1
##    print(entry)
    i += 1

    name = movie[0]
    genre = movie[1]
    rating = movie[2]
    print("{:20} {:5} {:20} {:5} {:3}".format(name, "|", genre, "|", str(rating)))
  print()

# end print_movie_list()

def add_movie_to_list(movies_list, mode):
  if DEBUG:
    print("From add_movie_to_list(), mode is: " + mode)
  movie_name = input("Name: ")
  if movie_name == "":
    movie = "Silent Movie"
  movie_name = movie_name.title()#make title case so the initial char is capitol
  movie_name = movie_name[0:20]#limit to 20 chars
  movie_genre = input("Genre: ")
  if movie_genre == "":
    movie_genre = "Other, non-specific"
  movie_genre = movie_genre.title()
  movie_genre = movie_genre[0:20]#limit to 20 chars
  movie_rating = validation.get_float("Rating: ", 10)
  movie = [str(movie_name), str(movie_genre), movie_rating]
  movies_list.append(movie)
  if mode != "txt":
    replace_movies_in_file(movies_list, mode)#write entire list
  else:
    save_movie_to_file(movie)#append the movie
  print("\"" + str(movie) + "\" has been added to the list.")

# end add_movie_to_list()

def delete_movie_from_list(movies_list, save_mode):
  if len(movies_list) == 0:
    raise ValueError("There are no movies in the list!")
  else:
    index = validation.get_int("Movie Index: ", len(movies_list))
    #double check theuser's intention to delete the movie
    choice = input("Are you sure you want to delete the movie (y/n)?")
    if choice.lower() == "y":
      movie = movies_list.pop(index-1)
      replace_movies_in_file(movies_list, save_mode)
      print(str(movie[0]) + " has been deleted.\n")
# end delete_movie_from_list()

def show_count_categories():
  print("\n******************************")
  print("**       CATEGORIES      **")
  print("******************************\n")
  print("**\ttot  - Total number of movies")
  print("**\tgen  - Number of genres")
  print("**\trat  - Number of movies above the given rating")
  print("**\tbeg  - Number of movies with Name begining with specified string")
  print("**\tend  - Number of movies with Name ending with specified string")
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
  movies_to_send = [["","",0]]
  # remove the initial element
  movies_to_send.pop()
  count = 0
  rating = validation.get_float("What is the lowest rated movie you want to see? ", 10)
  for movie in movies_list:
    if int(movie[2]) >= rating:
      movies_to_send.append(movie)
      count += 1
      
  if len(movies_to_send) > 0:
    print(str(len(movies_to_send)) + " movies found with a rating of at least " + str(rating))
    print_movie_list(movies_to_send)
  else:
    print("There are no movies in the list with a rating of at least " + str(rating))
      
# end show_by_rating()

def show_by_beginning(movies_list):
  #initialize the list
  movies_to_send = [["","",0]]
  # remove the initial element
  movies_to_send.pop()
  count = 0
  beginning = input("Search string? ")
  for movie in movies_list:
    if movie[0].startswith(beginning):
      movies_to_send.append(movie)
      count += 1
      
  if len(movies_to_send) > 0:
    print(str(len(movies_to_send)) + " movies found with Name beginning with " + beginning)
    print_movie_list(movies_to_send)
  else:
    print("There are NO movies in the list with with Name beginning with " + beginning)
      
# end show_by_beginning()

def show_by_ending(movies_list):
  #initialize the list
  movies_to_send = [["","",0]]
  # remove the initial element
  movies_to_send.pop()
  count = 0
  ending = input("Search string? ")
  for movie in movies_list:
    if movie[0].endswith(ending):
      movies_to_send.append(movie)
      count += 1
      
  if len(movies_to_send) > 0:
    print(str(len(movies_to_send)) + " movies found with a Name ending with " + ending)
    print_movie_list(movies_to_send)
  else:
    print("There are NO movies in the list with with a Name ending with " + ending)
      
# end show_by_ending()

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
  elif category.lower() == "beg":
    show_by_beginning(movies_list)
  elif category.lower() == "end":
    show_by_ending(movies_list)
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

def read_movies_file_txt(movies_list):
  if DEBUG:
    print("From read_movies_file_txt, the save file is " + MOVIE_FILE_TXT)
  movie = []
  try:
    with open(MOVIE_FILE_TXT) as file:
      for line in file:
        if line.isspace():
          continue
        line = line.replace("\n", "")
        data = line.split(",")
        name = data[0].strip()
        genre = data[1].strip()
        rating = data[2].strip()
        movie = [name, genre, float(rating)]
        movies_list.append(movie)
  except IOError as e:
    print("IOError:", e)
  except OSError as e:
    print("OSError:", e)
  except Exception as e:
    print(type(e), e)
    

# end read_movies_file_txt(movies_list, file):

def read_movies_file_csv(movies_list):
  if DEBUG:
    print("From read_movies_file_csv, the save file is " + MOVIE_FILE_CSV)
  movie = []
  try:
    with open(MOVIE_FILE_CSV, newline="") as file:
      reader = csv.reader(file)
      for data in reader:
        name = data[0]
        genre = data[1]
        rating = data[2]
        movie = [name, genre, float(rating)]
        movies_list.append(movie)
  except IOError as e:
    print("IOError:", e)
  except OSError as e:
    print("OSError:", e)
  except Exception as e:
    print(type(e), e)
# end read_movies_file_csv(movies_list, file):

def read_movies_file(movies_list, save_mode):
  movies = []
  if DEBUG:
    print("From read_movies_file, the movie save_mode is " + save_mode + " and, the movies file is " + MOVIE_FILE_BIN)
  if save_mode == "txt":
    read_movies_file_txt(movies_list)
  elif save_mode == "csv":
    read_movies_file_csv(movies_list)
  else:#must be in binary mode
    if os.stat(MOVIE_FILE_BIN).st_size != 0:#don't read from empty file
      if DEBUG:
        print(MOVIE_FILE_BIN + " has size: " + str(os.stat(MOVIE_FILE_BIN).st_size))
      try:
        with open(MOVIE_FILE_BIN, "rb") as file:
          movies = pickle.load(file)
      except IOError as e:
        print("IOERROR:", e)
      except OSError as e:
        print("OSERROR:", e)
      except Exception:
        print(type(e), e)
    else:
      print(MOVIE_LIST_BIN + " is empty!")
    if DEBUG:
      print("From read_movies_file, we read " + str(len(movies))+ " movies from the binary file.")
    for i in range(len(movies)):
      movie = movies[i]
      movies_list.append(movie)
 
# end read_movies_file

def save_movie_to_file(movie):
  if DEBUG:
    print("From save_movie_to_file...")
  try:
    name = movie[0]
    genre = movie[1]
    rating = movie[2]
    try:
      with open(MOVIE_FILE_TXT, "a") as file:
        file.write(name + ", " + genre + ", " + str(rating) + "\n")
    except IOError as e:
      print("IOError:", e)
    except OSError as e:
      print("OSError:", e)
  except Exception as e:
    print(type(e), e)
# end save_movie_to_file()

def replace_movies_in_txt_file(movies_list):
  if DEBUG:
    print("From replace_movies_in_txt_file...")
  try:
    with open(MOVIE_FILE_TXT, "w") as file:
      if len(movies_list) == 0:
        print("Empty movies list! Creating Empty movies file.")
        file.write("")
      else:
        for movie in movies_list:
          name = movie[0]
          genre = movie[1]
          rating = movie[2]
          file.write(name + ", " + genre + ", " + str(rating) + "\n")
  except IOError as e:
    print("IOError:", e)
  except OSError as e:
    print("OSError:", e)
  except Exception as e:
    print(type(e), e)

# end replace_movies_in_txt_file(movies_list):

def replace_movies_in_csv_file(movies_list):
  if DEBUG:
    print("From replace_movies_in_csv_file...")
  try:
    with open(MOVIE_FILE_CSV, "w", newline="") as file:
      writer = csv.writer(file)
      writer.writerows(movies_list)
  except IOError as e:
    print("IOError:", e)
  except OSError as e:
    print("OSError:", e)
  except Exception as e:
    print(type(e), e)

# end replace_movies_in_csv_file(movies_list):

def replace_movies_in_file(movies_list, save_mode):
  if DEBUG:
    print("From replace_movies_in_file, the save_mode is "+save_mode)
  if save_mode == "txt":
    replace_movies_in_txt_file(movies_list)
  elif save_mode == "csv":
    replace_movies_in_csv_file(movies_list)
  else:
    try:
      with open(MOVIE_FILE_BIN, "wb") as file:
        pickle.dump(movies_list, file)
    except IOError as e:
      print("IOError:", e)
    except OSError as e:
      print("OSError:", e)
    except Exception as e:
      print(type(e), e)
  
# end replace_movies_in_file()

def initialize_movie_data(movies_list, save_mode):
  if DEBUG:
    print("From initialize_movie_data, the save_mode is " + save_mode)
  # the MOVIE_FILE did not exist where we expected it
  # initialize the list
  movie = ["It's a good life", "Drama", 9.5]
  movie2 = ["Blade Runner", "Science Fiction", 10]
  movie3 = ["Shrek", "Animation", 8.5]
  movies_list.append(movie)
  movies_list.append(movie2)
  movies_list.append(movie3)
  if DEBUG:
    print("From initialize_movie_data, the movies are: ", end="")
    print(movies_list)
  # see if we can write the data to the file
  replace_movies_in_file(movies_list, save_mode)

# end initialize_movie_data()

def get_save_file(save_mode):
  if save_mode == "txt":
    return MOVIE_FILE_TXT
  elif save_mode == "csv":
    return MOVIE_FILE_CSV
  else:
    return MOVIE_FILE_BIN
  
 # end get_save_file() 

def main():
  stringer.show_welcome(NAME)
  movies_list = [[]]#initialize empty list with correct structure
  movies_list.pop()#remove empty element
  save_mode = ""
  file_to_find = ""

  pick_mode()#show user the types of files we can save the movies in

  while True:
    save_mode = input("\nMode?\t")
    save_mode = save_mode.rstrip()
    if save_mode.lower() == "txt":
      print("From main(), txt file selected by user.")
      break
    elif save_mode.lower() == "csv":
      print("From main(), csv file selected by user.")
      break
    elif save_mode.lower() == "bin":
      print("From main(), bin file selected by user.")
      break
    else:
      print("\""+ str(save_mode) + "\" is not a valid selection. Please try again.\n")

  # let's see if the MOVIE_FILE exists or not
  file_to_find = get_save_file(save_mode)
  if os.path.isfile(file_to_find):
    # the MOVIE_FILE is where we expected it
    read_movies_file(movies_list, save_mode)
  else:
    # the file does not exist where it is expected
    # initialize data and try to create the file
    initialize_movie_data(movies_list, save_mode)

  display_menu()
  try:
    while True:
      command = input("\nBye Your Command:\t")
      command = command.rstrip()
      if command.lower() == "list":
        print_movie_list(movies_list)
      elif command.lower() == "add":
        add_movie_to_list(movies_list, save_mode)
      elif command.lower() == "del":
        delete_movie_from_list(movies_list, save_mode)
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
  except ValueError as e:
    print("ValueError:", e)
  finally:
    print("Bye!")
# end main()


#if the current module is the main module
if __name__ == "__main__":
  main()
