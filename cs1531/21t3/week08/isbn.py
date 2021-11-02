def isValid(isbn):
    """
    Determines whether the ISBN is valid or not
    Returns True/False
    """
    product_sum = 0
    for i, val in enumerate(isbn[:9]):
        # print(f"i={i}, val={val}")
        product_sum += (i+1) * int(val)
    product_sum %= 11

    if product_sum == 10:
        return isbn[-1] == 'X'
    else:
        return int(isbn[-1]) == product_sum

if __name__ == "__main__":
    print(isValid(input("What is the ISBN? ")))
