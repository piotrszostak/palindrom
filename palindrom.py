def palindrom(arg):
    """
    Checks if an argument is a string,
    then it checks if a reversed string is eaqual to the string passed.
    """
    if type(arg) == str:
        rev = arg[::-1]
        return arg == rev
    else:
        return False
print(palindrom("121"))
