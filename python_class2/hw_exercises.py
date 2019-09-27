"""Exercises"""


def dash_stringify(word_list):
    """Given a list of word strings, return a single string with all the
        strings together, with ' - ' in between the words."""
    # Put the code here
    result = word_list[0]
    for index in range(1,len(word_list)):
        result = result + '-' + word_list[index]
    return result


def is_perfect_square(number):
    """Given a number, return True if it is a perfect square,
        else return False"""
    # Put the code here
    root = number ** 0.5
    return root.is_integer()


def last_n_reversed(sequence, n):
    """Given a sequence and a number n, return the last n elements of the
        sequence in reversed order"""
    # Use a slice
    return sequence[:-n-1:-1]


def power_list(numbers):
    """Given a list of numbers, return a new list where each element is the
        corresponding element of the list to the power of the list index"""
        # nums = [1, 3, 5, 7]
        # result = [1, 3, 25,343]
        # [nums[0]**0, nums[1]**1, nums[2]**2, etc]
    return [num ** index for index, num in enumerate(numbers)]


def rotate_list(some_list):
    """Take a list as input and remove the first item from the list and add it
        to the end of the list. Return the item moved"""
    first = some_list.pop(0)
    some_list.append(first)
    return first


def matrix_fill(n_rows, n_cols):
    """Given number of rows and number of columns, create a matrix (list of
        lists) where each element is sequentially numbered"""
    # matrix_fill(2, 3) returns [[1, 2, 3], [4, 5, 6]]
    # Use a list comprehension
    result = []
    for row in range(n_rows):
        row_list = []
        for col in range(n_cols):
            row_list.append(row * n_cols + col + 1)
        result.append(row_list)
    return result

def matrix_fill2(n_rows, n_cols):
    """Given number of rows and number of columns, create a matrix (list of
        lists) where each element is sequentially numbered"""
    # matrix_fill(2, 3) returns [[1, 2, 3], [4, 5, 6]]
    return[
        [row * n_cols + col for col in range(1,n_cols + 1)]
        for row in range(n_rows)
    ]

def squash(matrix):
    """Return squashed list from list of lists"""
    # [[1, 2, 3], [4, 5, 6]] returns [1, 2, 3, 4, 5, 6]
    return [item for row in matrix for item in row]

def get_word_codes(words):
    result = {
        word: {ord(char) for char in word}
        for word in words
    }
    return result

def switch_dict(dictionary):
    return {
        value : key for value, key in dictionary.items()
    }

def reverse_iter(sequence):
    #for item in sequence[::-1]:
    #   yield item
    yield from sequence[::-1]