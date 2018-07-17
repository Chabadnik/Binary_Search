# Created by: Dennis Yankovsky
# Due Date: March 23rd 2018
# Binary Search Program

import time
total_time = 0 # Total_time global variable used later


def binary_search(a, n):    # function that does the binary search algorithm. a = array, n = number you want to find in array
    if len(a) == 1:         # base case for a list with length 1
        if n == a[0]:
            return True
        else:
            return False
    if len(a) == 2:         # base case for a list with length 2
        if n == a[0] or a[1]:
            return True
        else:
            return False

    mid_i = int(len(a)) // 2    # the middle index of the array (// is modularity)
    mid = a[int(len(a)) // 2]   # the value of the middle index of the array

    if n == mid:                # base case if your number is the middle index
        return True
    elif (n > a[mid_i - 1] and n < a[mid_i]) or (n < a[mid_i + 1] and n > a[mid_i]): # base case for if your number is between middle index -1 and middle index or middle index and middle index + 1
        return False
    elif n < a[0] or n > a[len(a) - 1]: # if your number is less than the smallest value or greater than the largest value
        return False
    else:
        if n > mid:                     # if your number is larger than the middle number, return the larger half of the array
            del a[0:mid_i]
            return binary_search(a, n)
        else:                           # if your number is less than the middle number, return the smaller half of the array
            del a[mid_i:]
            return binary_search(a, n)


def make_table():                       # function that makes the output table
    global total_time                   # total time variable

    for i in range(1, 15):              # for 14 different length of lists (list length increases by a factor of 2 each time)
        array = []
        for k in range(0, 2 ** i):      # makes the list
            array.append(k)

        for j in range(1, int(1e5)):    # run the program 1e5 times
            test_val = array[0]  # worst possible case that requires the most recursion
            start_time = time.clock()  # The clock function
            binary_search(array, test_val)      # run the program
            time1 = (time.clock() - start_time)
            total_time += time1             # add to final time
        if i < 10:
            print("x = 2 ^", i, " and y =", float(format(total_time, '.4f')))   # prints the time with 4 decimal places, extra space before "and so that table looks neat
        else:
            print("x = 2 ^", i, "and y =", float(format(total_time, '.4f')))    # prints the time with 4 decimal places


print("Hi Mr. Rottmann! Enter numbers with spaces between them as your list (ie 1 2 3 4)")
Rottmann1 = [int(x) for x in input().split()]   # turns input into a list
Rottmann2 = int(input("Hello again, give me a number to search in your list! "))    # number you are testing for
print("")
if (binary_search(Rottmann1, Rottmann2)) == True:       # If the number appears in the list
    print("True, your number appears in the list")
else:                                                   # If the number doesn't appear in the list
    print("False, your number does not appear in the list")
print("")
print("Table of values:")
print("x represents the length of list and y represents time for search to finish")
print("")

make_table()
