def palindrom(arg):
    if type(arg) != str:
        return False
    return arg == arg[::-1]
print(palindrom("121"))