# this function will fail the test since it takes an extra positional arguement not in the test
"""
def full_names(first, middle, last):

    full_name = '{0} {1} {2}'.format(first, middle, last)
    return full_name.title()
    
    """

# this modified function will pass the test

# understand the nuance that not all persons have three names; hence factoring that in your program will help
# your program pass the test and be more functional and scalable.


def full_names(first, last, middle=''):

    if middle:
        all_names = '{0} {1} {2}'.format(first, middle, last)
    else:
        all_names = '{0} {1}'.format(first, last)

    return all_names.title()
