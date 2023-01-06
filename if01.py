def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a > b :
        if a > c :
            i= a 
        else :
            i= c
    else :
        if b > c :
            i= b 
        else:
            i= c
        return i  
print(main(2,54,67))  

