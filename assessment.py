"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE: Write your own function declarations - Part 1 questions aren't
included in the doctest.

PART TWO:

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    >>> calculate_price(25, "CA")
    27.0

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0)
    150

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

PART THREE: Write your own function declarations - Part 3 questions aren't
included in the doctest.

"""

###############################################################################

# PART ONE

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

def town_name(town):
    """checks if town is your hometown"""

    your_town = "San Francisco"

    if town == your_town:
        return True

    else:
        return False

town_name("Boston")

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

def name(first, last):
    """returns your first and last name"""

    return first + last

name("Amee", "Covarrubias")

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', where are you from?" depending on what the function from part
#        (a) evaluates to.

def your_information(town, first, last):
    """returns your hometown and full name"""

    town_status = town_name(town)
    get_name = name(first, last)
    if town_status == True:
        print "Hi, '%s here', we're from the same place!" % (name)
    else:
        print "Hi, %d where are you from?: " % (name)

your_information("San Francisco", "Amee", "Covarrubias")
    



###############################################################################

# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry."


def is_berry(fruit):
    """Determines if fruit is a berry"""

    if fruit == "blackberry":
        return True

    elif fruit == "cherry":
        return True

    elif fruit == "strawberry":
        return True

    else:
        return False

is_berry("cherry")
    

# (b) Write another function, shipping_cost(), which calculates shipping cost
#     by taking a fruit name as a string and calling the is_berry() function
#     within the shipping_cost() function. Your function should return 0 if
#     is_berry() == True, and 5 if is_berry() == False.

def shipping_cost(fruit):
    """Calculates shipping cost of fruit"""

    if is_berry() == True:
        return 0

    else:
        return 5

shipping_cost("cherry")
   


# 2. Make a function that takes in a number and a list of numbers. It should
#    return a new list containing the elements of the input list, along with
#    given number, which should be at the end of the new list.

def append_to_list(lst, num):
    """Creates a new list consisting of the old list with the given number
       added to the end."""

    new_num = n
    nums_list = [1 ,2, 3, 4, 5, 6, 7, 8, 9, 10]
    nums_list.append(new_num)

    print nums_list

    append_to_list("5")



# 3. Write a function calculate_price to calculate an item's total cost by
#    adding tax, and any fees required by state law.

#    Your function will take as parameters (in this order): the base price of
#    the item, a two-letter state abbreviation, and the tax percentage (as a
#    two-digit decimal, so, for instance, 5% will be .05). If the user does not
#    provide a tax rate it should default to 5%.

#    CA law requires stores to collect a 3% recycling fee, PA requires a $2
#    highway safety fee, and in MA, there is a commonwealth fund fee of $1 for
#    items with a base price under $100 and $3 for items $100 or more. Fees are
#    added *after* the tax is calculated.

#    Your function should return the total cost of the item, including tax and
#    fees.

def calculate_price(a, b, c):
    item_price = raw_input("How much does your item cost?: ")
    state = raw_input("What state was the item purchased?: (Use two letter abbreviation.").upper()
    tax = raw_input("What is the tax percentage of the item? If you're unsure, type: unknown")

    if tax == "unknown":
        tax = 0.5
    
    if  state == "CA":
        total = item_price * tax * 0.3
        return total

    if state == "PA":
        total = (item_price * tax) + 2
        return total

    if state == "MA":
        if item_price > 3 < 100:
            total = (item_price * tax) + 1
            return total 

        elif item_price > 100:
            total = (item_price * tax) + 3
            return total 
calculate_price()


###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


# 1. Make a new function that takes in a list and any number of additional
# arguments, appends them to the list, and returns the entire list. Hint: this
# isn't something we've discussed yet in class; you might need to google how to
# write a Python function that takes in an arbitrary number of arguments.

#psuedo code
# 1. make function with list parameter, and a, b, c parameters
# 2. create variable that appends item to list
# 3. return list 


# # 2. Make a new function with a nested inner function.
# # The outer function will take in a word.
# # The inner function will multiply that word by 3.
# # Then, the outer function will call the inner function.
# # Output will be the original function argument and the result of the inner
# # function.

# 1. create two functions
# 2. nest one function into another as a parameter
# 3. the outer function takes parameter, word. 
# 4. the outer function calls inner function 
# 5 return outer function
# # Example:


#>>> outer("Balloonicorn")
#('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')


###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
