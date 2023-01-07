def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    a=n//10000
    s=n//1000%10
    c=n//100%10
    x=n%100//10
    d=n%10
    r=a
    if r>s:
        i=r
    else:
        i=s
    if r>c:
        i=r
    else:
        i=c
    if r>x:
        i=r
    else:
        i=x
    if r>d:
        i=r
    else:
        i=d


    return i
print(main(12345))