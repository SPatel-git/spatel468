#!/usr/bin/env python3
''' template for ops435 assignment 1 script
    put your script level docstring here...
    you can have more than one line of docstring.
    Please personlize the following author declaration:
-----------------------------------------------------------------------
OPS435 Assignment 1 - Winter 2021
Program: a1_spatel468.py
Author: "Shyam Patel"
The python code in this file (a1_spatel468.py) is original work written by
"Shyam Patel". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''
import os
import sys

def leap_year(obj):
    '''
    This function takes in a object of type integer in the "YYYY" format.
    It will determine if the integer given is a leap year, and it returns
    true if it is a leap year and it will return False if it is not.
    '''

    status = False
    if obj%4 ==0:
        status = True
        if obj%4 == 0 and obj%100 == 0:
            status = False
            if obj%400 == 0:
                status = True
    return status

def sanitize(obj1,obj2):
    '''
    This function takes in two string objects, obj1 being the string to
    sanitize, and obj2 the allowed characters of the string. Every character
    of obj1 that is not in obj2 will be removed and the final string is returned
    '''
    
    results = ""
    for character in obj1:
        if character in obj2:
            results = results + character
    return results

def size_check(obj, intobj):
    '''
    This function will take in a two arguements, the first being 
    an collection data type and the second arguement being an
    integer. If the collection data type is the specified length
    from the integer arguement, this function will return true, if 
    not it will return false.
    '''

    status = False
    if len(obj) == intobj:
        status = True

    return status

def range_check(obj1, obj2):
    '''
    This function takes in two arguements, one of them is a integer and the other
    arguement is a tuple with two integer values. This function will return True
    if the first arguement is between the two values in the tuple object, and it
    will return false if it isn't.
    '''

    low = obj2[0]
    high = obj2[1]
    status = False
    if low <= obj1 <= high:
        status = True
    return status
    
def usage():    
    '''
    This function will output a string that describes how
    to utilize this script.
    '''
    
    status = 'This script requires the user to enter ONE arguement which is the date in YYYYMMDD, YYYY/MM/DD, YYYY-MM-DD, or YYYY.MM.DD format.\nIt will then print the date in mmm d, yyyy, where "mmm" is the three letter abbreviated months name, d is a one or two-digit day of the month, and yyyy is the four-digit year\n(ex. 20201007 -> Oct 7, 2020)'
    return status

if __name__ == "__main__":
   # step 1
   if len(sys.argv) != 2:
      print(usage())
      sys.exit()
   # step 2
   month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                 'Jul','Aug','Sep','Oct','Nov','Dec']
   days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
   user_raw_data = sys.argv[1]
   # step 3
   allow_chars = '0123456789'
   dob = sanitize(user_raw_data, allow_chars)
   print('Sanitized user data:', dob)
   # setp 4
   result = size_check(dob,8)
   if result == False:
       print("Error 09: wrong data entered")
       sys.exit()
   # step 5
   year = int(dob[0:4])
   month = int(dob[4:6])
   day = int(dob[6:])
   # step 6
   result = range_check(year,(1900,9999))
   if result == False:
       print("Error 10: year out of range, must be 1900 or later")
       sys.exit()
   result = range_check(month,(1,12))
   if result == False:
       print("Error 02: Wrong month entered")
       sys.exit()
   result = leap_year(year)
   if result == True:
       days_in_month[2] = 29
   result = range_check(day, (1, days_in_month[month]))
   if result == False:
       print("Error 03: wrong day entered")
       sys.exit()
   # step 7
   new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)
   # step 8
   print("Your date of birth is:", new_dob)  
