def is_positive(num):
    """
    is this number positive?
    if yes result is True
    if no result is False
    """


    if num >= 0:
        return True
    return False


result = int(input("insert number: "))
print(is_positive(result))
