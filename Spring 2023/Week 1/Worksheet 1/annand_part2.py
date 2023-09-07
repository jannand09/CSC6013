#Part 2
#Check for a zig zag

def zigzag(first, second, third):
    '''
    Determines if the parameter values form a zigzag pattern
    Parameters:
        int
    Returns:
        Boolean
    ''' 
    if first > second and second < third:
        return True
    elif first < second and second > third:
        return True
    else:
        return False


def main():
    '''
    Check if user inputs form a zigzag pattern
    Parameters:
        None
    Returns:
        None, prints 
    '''
    #Ask user for three numbers and convert to int
    a = eval(input("Please give integer value for 'a': "))
    b = eval(input("Please give integer value for 'b': "))
    c = eval(input("Please give integer value for 'c': "))
    #print result
    print(zigzag(a,b,c))


main()