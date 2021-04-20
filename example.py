def add(a, b):
    '''
    >>> add(1, 2)
    3
    >>> add(5, 10)
    maybe 15
    '''

    return a + b


if __name__ == '__main__':
    import doctest
    import sys

    sys.exit(doctest.testmod()[0])
