##########################################
# Name: Amena Akbary
# Pledge: I pledge my honor that I have abided by the Stevens honor system
##########################################

# Import reduce from the functools package
from functools import reduce

#######################################################################################
# Task 1: Use reduce to determine if all elements in a boolean list are true
def check_true(a,b):
    return a==b
def all_true(lst):
    # TODO: Implement
    return(reduce(check_true, lst))


the_lst=[True,True]
print(all_true(the_lst))
#######################################################################################
# Task 1.1: Use reduce to determine if AT LEAST one element in a boolean list is true
# Hint: Should be very similar to the above function
def all_true(a,b):
    return a or b == True
def one_true(lst):
    # TODO: Implement
    return(reduce(all_true,lst))

num_list_2=[True,True,False]
print(one_true(num_list_2))

#######################################################################################
# Task 2: Use map and reduce to return how many elements are True in a boolean list

def count_true(lst):
    # TODO: Implement
    def num_true(a):
        if a==True:
            return 1
        else:
            return 0
    map(num_true,lst)
    def count(a, b):
        return a+b
    return(reduce(count,map(num_true,lst)))

the_lists=[True,False,True,False,True]
print(count_true(the_lists))

# This function is provided for you
# Gets a list of strings through the command line
# Input is accepted line-by-line
def getInput():
    lst = []
    txt = input()

    while(len(txt) != 0):
        lst.append(txt)
        txt = input()

    return lst
he
# Task 3: Get the longest string in the list using map and reduce, and print it out
# 'strings' is a list of input strings e.g. [ 'hello', 'world' ]
# Hint: The 'map' part of your program should take a string s into a length-2 list MAP[len(s), s].
def big(a,b):
    if a[0]>b[0]:
        return a
    else:
        return b
def getLongestString():
    strings = getInput()
    def counting(a):
        return[len(a),a]
    map(counting,strings)
    return reduce(big,map(counting,strings))[1]

print(getLongestString())
