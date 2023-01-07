def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Use the elif statments.
    Temp<0: "Freezing"
    Temp 1-10: ""
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"
    Args:
        temp: Temperature in Celsius.
    Returns:
        str: return answer.
    """
    if 1<=temp<=10:
        i='Very Cold'
    elif 11<=temp<=20:
        i='Cold'
    elif 21<=temp<=30:
        i='Normal'
    elif 31<=temp<=40:
        i='Hot'
    elif temp>40:
        i='Very Hot'
    elif temp<0:
        i='Freezing'
    return i
print(main(15))