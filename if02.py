def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a<b  and a<c:
        i=a
    elif b<a and b<c:
        i=b
    elif c<a and c<b:
        i=c
    return i
print(main(-8,-5,-7))