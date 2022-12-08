#!/usr/bin/python3

"""
function that replaces all occurrences of an element by another in a new list.
@my_list: is the initial list
@search: is the element to replace in the list
@replace: is the new element
Return: the new list

"""
def search_replace(my_list, search, replace):
    return [i if i != search else replace for i in my_list]	
