#!/usr/bin/env python3

# an example Python program
# by Erin Coffey
# 16 January 2018

# import stringer module for welcome message
import stringer

import random

AUTHOR = "Erin Coffey"
NAME = "Meta Data"
MAX = 50

def generate_random_list(random_list):
  for i in range(len(random_list)):
    random_list[i] = random.randint(0, MAX)
  random_list.sort()

# end generate_random_list()

def get_duplicates(data):
  dups = []
  for i in range(MAX + 1):
    count = data.count(i)#count the number of occurences
    if count >= 2:
      dups.append(i)
  return dups

# end get_duplicates()

def get_meta_data(data):
  total = 0
  for number in data:
    total += number

  average = round(total / len(data))
  # get med index by divide and truncate
  median_index = len(data) // 2
  median_value = data[median_index]
  minimum_value = min(data)
  maximum_value = max(data)
  duplicates = get_duplicates(data)

  print("Average =", average,
        "Median =", median_value,
        "Min =", minimum_value,
        "Max =", maximum_value,
        "Duplicates =", duplicates)

# end get_meta_data()

def main():
  stringer.show_welcome(NAME)
  random_list = [0] * 11
  fixed_tuple = (0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
  print("TUPLE DATA: ", fixed_tuple)
  get_meta_data(fixed_tuple)
  print()

  while True:
    generate_random_list(random_list)
    print()
    print("RANDOM DATA: ", random_list)
    get_meta_data(random_list)
    print()

    choice = input("Try again? (y/n): ")
    if choice.lower() != "y":
      break
  # end while loop
  print("Bye!")
# end main()


#if the current module is the main module
if __name__ == "__main__":
  main()
