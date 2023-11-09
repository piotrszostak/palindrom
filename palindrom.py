def palindrom(arg):
    """
    Checks if a reversed string is eaqual to the string passed.
    """
    rev = arg[::-1]
    return arg == rev
print(palindrom('a'))
