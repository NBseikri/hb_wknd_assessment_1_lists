"""List Practice

Edit the functions until all of the doctests pass when
you run this file.
"""


def print_list(items):
    """Print each item in the input list.

    For example::

        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9

    """
    #If I were writing this function from scratch, I would include the following docstring immediately after declaring the function:
    #"""This function evaluates and prints each item in an input list"""
    #(Including my docstring within the docstring above interfered with the doctest so I am including it here as a comment instead)

    for item in items:
    # Iterates through items (a list) and evaluates each item contained within the list
        print item
        # Prints each item in the list

def long_words(words):
    """Return words in input list that longer than 4 characters.

    For example::

        >>> long_words(["hello", "a", "b", "hi", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

    (If there are duplicates, show both --- notice "bacon" appears
    twice in output)

    If no words are longer than 4 characters, return an empty list::

        >>> long_words(["all", "are", "tiny"])
        []
    """

    #If I were writing this function from scratch, I would include the following docstring immediately after declaring the function:
    #"""This function evaluates each item in a list and print those items with more than four letters"""
    #(Including my docstring within the docstring above interfered with the doctest so I am including it here as a comment instead)

    long_words = []
    #Creates a long_words variable for a list that will be populated with words exceeding four letters from the for loop below

    for word in words:
    #Iterates through words (a list) and evaluates each item contained within the list
        if len(word) > 4:
        #Examines whether a word in the words list is greater than four letters
            long_words.append(word)
            #If the condition above is met, the word will be added to the new long_words list

    return long_words
    # Returns a list of words from the input list that meet the condition in the for loop




    #This could be done more concisely with list comprehensions in an alternate function:
    #def long_words(words):
    #"""This function evaluates each item in the input list and returns a new list of words greater than four letters"""

        #long_words = [word for word in words if len(word) > 4]
        #This function will assign the words from the input list to this long_words variable if the > 4 condition is met.
        #If the > 4 condition is not met, the function will return an empty long_words list as instructed
        #If, however, you wanted to create a new, separate list of short words that are equal to or less than four letters, you could use the following list comprehension:
        #short_words = [word for word in words if len(word) <= 4]
        #This list comprehension for short words assigns the words from the input list to short_words if the <= 4 condition is met
        #return long_words, short_words
        #This returns the newly populated long_words and short_words lists

def n_long_words(words, n):
    """Return words in list longer than `n` characters.

    For example::

        >>> n_long_words(
        ...     ["hello", "hey", "spam", "spam", "bacon", "bacon"],
        ...     3
        ... )
        ['hello', 'spam', 'spam', 'bacon', 'bacon']

        >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
        ['apples', 'bananas']
    """
    #If I were writing this function from scratch, I would include the following docstring immediately after declaring the function:
    #"""This function evaluates each item in a list and prints the largest number"""
    #(Including my docstring within the docstring above interfered with the doctest so I am including it here as a comment instead)

    n_long_words = []
    #Creates a n_long_words variable for a list that will be populated with words exceeding n letters from the for loop below

    for word in words:
    #Iterates through words (a list) and evaluates each item contained within the list
        if len(word) > int(n):
        #Examines whether a word in the words list is greater than n letters; n is set to an intger to ensure it's properly treated as a number or so the user gets terminal error if not a number
            n_long_words.append(word)

    return n_long_words
    # Returns a list of words from the input list that meet the condition in the for loop




    #This could be done more concisely with list comprehensions in an alternate function:
    #def long_words(words):
    #"""This function evaluates each item in the input list and returns a new list of words greater than n characters (n is passed through by the user when the function is executed)"""

        #n_long_words = [word for word in words if len(word) > n]
        #This function will assign the words from the input list to this n_long_words variable if the > n condition is met.
        #If the > 4 condition is not met, the function will return an empty long_words list as instructed
        #If, however, you wanted to create a new, separate list of short words that are equal to or less than n letters, you could use the following list comprehension:
        #short_words = [word for word in words if len(word) <= n]
        #This list comprehension for short words assigns the words from the input list to short_words if the <= n condition is met
        #return long_words, short_words
        #This returns the newly populated n_long_words and short_words lists

def smallest_int(numbers):
    """Find the smallest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `min()`!

    For example::

        >>> smallest_int([-5, 2, -5, 7])
        -5

        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return `None`::

        >>> smallest_int([]) is None
        True
    """
    #If I were writing this function from scratch, I would include the following docstring immediately after declaring the function:
    #"""This function evaluates each item in a list and prints the smallest number"""
    #(Including my docstring within the docstring above interfered with the doctest so I am including it here as a comment instead)

    if numbers == []:
        #This condition first checks to see if the input list is empty
        return None
        #If the list is empty, it returns None

    #Assuming the input list is populated and the condition above is not met, the function will evaluate the list below

    smallest_int = numbers[0]
    #This variable is set to the first number in the numbers list and will change as smaller numbers appear in the input list

    for number in numbers:
    #Evaluates each number in the input list
        if number < smallest_int:
        #Evaluates whether the number is less than smallest_int (which is initially set as the first number in the input list)
            smallest_int = number
            #The variable smallest_int is intially set at numbers[0] and will be replaced as soon as the for loop encounters a number smaller than numbers[0]. Each time the loop runs and a new number in the list appears that is less than the the number that was last assigned to smallest_int, it will then replace the value of the smallest_int variable. 

    return smallest_int
    #Returns the smallest number in the input list

def largest_int(numbers):
    """Find the largest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `max()`!

    For example::

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None::

        >>> largest_int([]) is None
        True
    """
    #If I were writing this function from scratch, I would include the following docstring immediately after declaring the function:
    #"""This function evaluates each item in a list and prints the largest number"""
    #(Including my docstring within the docstring above interfered with the doctest so I am including it here as a comment instead)

    if numbers == []:
        #This condition first checks to see if the input list is empty.
        return None
        #If the list is empty, it returns None.

    #Assuming the input list is populated and the condition above is not met, the function will evaluate the list below.

    largest_int = 0
    #This variable is set at zero and will change as 

    for number in numbers:
    #Evaluates each number in the input list
        if number > largest_int:
        #Evaluates whether the number is greater than largest_int (which is initially set at zero)
            largest_int = number
            #The variable largest_int is intially set at zero and will be replaced as soon as the for loop encounters a number greater than zero. Each time the loop runs and a new number in the list is greater than the the number that was last assigned to largest_int appears, it will then replace the value of the largest_int variable. 

    return largest_int
    #Returns the largest number in the input list



    #This function could also work by assigning largest_int[0] to the largest_int variable before starting the for loop like the smallest_int function above. This would captures the largest number in a list input where all numbers were below zero.

def halvesies(numbers):
    """Return list of numbers from input list, each divided by two.

    For example::

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off
    the half::

        >>> halvesies([1, 5])
        [0.5, 2.5]
    """
    #If I were writing this function from scratch, I would include the following docstring immediately after declaring the function:
    #"""This function evaluates each number in a list and prints that quotient of that number divided by two"""
    #(Including my docstring within the docstring above interfered with the doctest so I am including it here as a comment instead)

    halved_numbers = []
    #Created a list to house all of the halved numbers that emerge from the for loop

    for number in numbers:
    #Evaluates each number in the inputted numbers list
        number = float(number) / 2
        #Reassigns number to the quotient of itself divided by two; float is with regard to number so as to avoide the default rounding
        halved_numbers.append(number)
        #Adds the newly halved number the the halved_numbers list above
    
    return halved_numbers
    #Returns a list of each halved number in the number list



    #To enhance this code, you could include a conditional either ignores or addresses list entries that not integers

def word_lengths(words):
    """Return the length of words in the input list.

    For example::

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]
    """

    word_lengths = []
    #Creates a list to house the lengths of all words in the inputted words list
    
    for word in words:
    #Evaluates each word in the inputted words list
        word_lengths.append(len(word))
        #Appends the length of each word to the word_lengths list above
    
    return word_lengths
    #Returns the newly populated word_lengths list



    #To enhance this code you could include a conditional that either ignores or addresses list items that are not words

def sum_numbers(numbers):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does
    this --- but for this exercise, you should not use it.

    For example::

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero::

        >>> sum_numbers([])
        0
    """

    return None


def mult_numbers(numbers):
    """Return product (result of multiplication) of numbers in list.

    For example::

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in input, the product is zero::

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product,
    if the list is empty, the product should be 1::

        >>> mult_numbers([])
        1
    """

    return None


def join_strings(words):
    """Return a string of all input strings joined together.

    Python has a built-in method, `list.join()` --- but for
    this exercise, **you should not use it**.

    For example::

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string::

        >>> join_strings([])
        ''
    """

    return "Not the right thing"


def average(numbers):
    """Return the average (mean) of the list of numbers given.

    For example::

        >>> average([2, 4])
        3.0

    This should handle cases where the result isn't an integer::

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty;
    it's fine if this raises an error when given an empty list.

    (Think of the best way to handle an empty input list, though,
    a feel free to provide a good solution here.)
    """

    return 0


def join_strings_with_comma(words):
    """Return ['list', 'of', 'words'] like "list, of, words".

    For example::

        >>> join_strings_with_comma(
        ...     ["Labrador", "Poodle", "French Bulldog"]
        ...     )
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course::

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'
    """

    return ""


def reverse_list(items):
    """Return the input list, reversed.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']

    You should do this without changing the original list::

        >>> orig = ["apple", "berry", "cherry"]
        >>> reverse_list(orig)
        ['cherry', 'berry', 'apple']
        >>> orig
        ['apple', 'berry', 'cherry']
    """

    return []


def reverse_list_in_place(items):
    """Reverse the input list `in place`.

    Reverse the input list given, but do it "in place" --- that is,
    do not create a new list and return it, but modify the original
    list.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> orig = [1, 2, 3]
        >>> reverse_list_in_place(orig)
        >>> orig
        [3, 2, 1]

        >>> orig = ["cookies", "love", "I"]
        >>> reverse_list_in_place(orig)
        >>> orig
        ['I', 'love', 'cookies']
    """

    return []


def duplicates(items):
    """Return list of words from input list which were duplicates.

    Return a list of words which are duplicated in the input list.
    The returned list should be in ascending order.

    For example::

        >>> duplicates(
        ...     ["apple", "banana", "banana", "cherry", "apple"]
        ... )
        ['apple', 'banana']

        >>> duplicates([1, 2, 2, 4, 4, 4, 7])
        [2, 4]

    You should do this without changing the original list::

        >>> orig = ["apple", "apple", "berry"]
        >>> duplicates(orig)
        ['apple']

        >>> orig
        ['apple', 'apple', 'berry']
    """

    return []


def find_letter_indices(words, letter):
    """Return list of indices where letter appears in each word.

    Given a list of words and a letter, return a list of integers
    that correspond to the index of the first occurrence of the letter
    in that word.

    **DO NOT** use the `list.index()` method.

    For example::

        >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
        [0, 1, 2]

    ("o" is at index 0 in "odd", is at index 1 in "dog", and at
    index 2 in "who")

    If the letter doesn't occur in one of the words, use `None` for
    that word in the output list. For example::

        >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
        [0, 1, 2, None]

    ("o" does not appear in "jumps", so the result for that input is
    `None`.)
    """

    return []

#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
