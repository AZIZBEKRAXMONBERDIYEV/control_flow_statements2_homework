def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>b>c or a<b<c:
        i=b
    elif b>a>c or c>a>b:
        i=a
    elif b<c<a or  b>c>a:
        i=c
    return i
print(main(1,2,3))