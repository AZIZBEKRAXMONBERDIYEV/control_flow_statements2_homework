def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    if a==b:
        i=0
        if a!=b:
            if a>b:
                i=a
            else:
                i=b

    return i
print(main(2,2))