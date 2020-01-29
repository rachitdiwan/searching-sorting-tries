def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    start = 0
    end = number
    while start <= end:
        midpoint = (start+end)//2
        if (midpoint*midpoint) == number :
            return midpoint
        elif (midpoint*midpoint) < number and number<((midpoint+1)*(midpoint+1)):
            return midpoint
        elif (midpoint*midpoint) < number:
            start = midpoint+1
        else:
            end = midpoint-1


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")