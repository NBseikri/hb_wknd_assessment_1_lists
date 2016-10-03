"""List Assessment 

Edit the functions until all of the doctests pass when
you run this file.
"""


def all_odd(numbers):
    """Return a list of only the odd numbers in the input list.

    For example::

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []
    """
    """This docstring would normally go under the function declaration
    but I don't want to interfere with the doctest. This function returns
    a list of the odd numbers in an input list."""

    all_odd = []
    #Creates a variable to hold all numbers that are appended below
    for number in numbers:
    #Evaluates each number in numbers
        if number % 2 == 1:
        #If number is divisible by 2 with a remainder of one it is odd and 
        #the condition here is met
            all_odd.append(number)
            #The odd number is appended to the all_odd list
        else:
        #Handles even numbers
            pass
            #Does nothing with even numbers

    return all_odd
    #Returns the all_odd list

def print_indices(items):
    """Print index of each item in list, followed by item itself.

    Do this without using a "counting variable" --- that is, don't
    do something like this::

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this::

        >>> print_indices(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo
    """
    
    """This docstring would normally go under the function declaration
    but I don't want to interfere with the doctest. This function prints 
    the position of an item and the item itself contained in an input list."""

    for item in items:
    #Evaluates each item in items
        print items.index(item), item
        #Finds the index of each item alongside the item itself

def foods_in_common(foods1, foods2):
    """Find foods in common.

    Given 2 lists of foods, return the items that are in common
    between the two, sorted alphabetically.

    **NOTE**: for this problem, you're welcome to use any of the
    Python data structures you've been introduced to (not just
    lists). Is there another that would be a good idea?

    For example::

        >>> foods_in_common(
        ...     ["cheese", "bagel", "cake", "kale"],
        ...     ["hummus", "beets", "bagel", "lentils", "kale"]
        ... )
        ['bagel', 'kale']

    If there are no foods in common, return an empty list::

        >>> foods_in_common(
        ...     ["lamb", "chili", "cheese"],
        ...     ["cake", "ice cream"]
        ... )
        []

    """
    """This docstring would normally go under the function declaration
    but I don't want to interfere with the doctest. This function returns
    a list items in two inputted lists"""

    foods_in_common = []
    #Variable to hold all identified commin foods

    for item in foods1:
    #Evaluates each item in the foods1 list
        if item in foods2:
        #Evaluates if the item in foods1 is also in foods2
            foods_in_common.append(item)
            #When item is in both lists, that item is appended to the 
            #foods_in_common list

    print foods_in_common
    #This line prints the list contained in the foods_in_common variable

    #The doctest notes and instructions indicate that a list is expected: 
    #   From instructions: ['bagel', 'kale']
    #   From doctest: Expected: []
    #The only way to pass this doctest is to use a foods_in_common
    #list (which I did). Am I missing something with regard to the note that
    #we can use any data structure *except* a list?

def every_other_item(items):
    """Return every other item in `items`, starting at first item.

    For example::

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(
       ...   ["you", "z", "are", "z", "good", "z", "at", "x", "code"]
       ... )
       ['you', 'are', 'good', 'at', 'code']
    """
    """This docstring would normally go under the function declaration
    but I don't want to interfere with the doctest. This function returns the
    every other item in an inputted list"""

    return items[::2]
    #This line returns every other item in the list by using a 2 step

def largest_n_items(items, n):
    """Return the `n` largest integers in list, in ascending order.

    You can assume that `n` will be less than the length of the list.

    For example::

        >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
        [59, 700, 6006]

    It should work when `n` is 0::

        >>> largest_n_items([3, 4, 5], 0)
        []

    If there are duplicates in the list, they should be counted
    separately::

        >>> largest_n_items([3, 3, 3, 2, 1], 2)
        [3, 3]
    """
    """This docstring would normally go under the function declaration
    but I don't want to interfere with the doctest. This function returns the
    nth largest numbers in an inputted list of numbers"""

    largest_n_items = []
    #Variable to hold each appended item from below

    n = int(-n)
    #Sets n to a negative number for use with reverse index counting

    if n == 0:
    #Handles when n is zero
        return largest_n_items
    else:
    #Handles when n is a number other than zero
        for item in items:
        #Evaluates each item in items
            largest_n_items.append(item)
            #Appends each item to the largest_n_items list

    largest_n_items = sorted(largest_n_items)
    #Sorts the now populated largest_n_items list
    return largest_n_items[n:]
    #Returns the list from the -nth index through the end (the largest n indices)


#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
