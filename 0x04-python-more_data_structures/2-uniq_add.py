#!/usr/bin/python3
# function that adds all unique integers in a list (only once for each integer).

def uniq_add(my_list=[]):

    # new_list = []
    new_list = set(my_list)
    sum = 0
    for i in new_list:
      #  if i not in new_list:
         sum += i
     #   new_list.append(i)
    return sum
