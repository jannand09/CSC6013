#Create a zigzag function

def zigzag(a,b,c):
    '''
    Determines if values form a zigzag (a<b>c or a>b<c)
    Parameters:
        a,b,c (int or float)
    Returns:
        Boolean
    '''    
    if a < b:
        if b > c:
            return True
        else:
            return False
    elif a > b:
        if b < c:
            return True
        else:
            return False

def main():
    '''
    Asks for three values from user and determines if they form a zigzag
    Parameters:
        None
    Returns:
        None, prints whether or not values form a zigzag to the console
    ''' 
    #Ask for three values
    first = eval(input("Enter first value: "))
    second = eval(input("Enter second value: "))
    third = eval(input("Enter third value: "))

    #Determine if values form zigzag and print appropriate
    if zigzag(first,second,third):
        print("Values form a zigzag.")
    else:
        print("Values do not form a zigzag.")

main()