#Part 1
#Is it cold in Canada today?

def convert_to_celsius(temp):
    '''
    Convert a temperature from Fahrenheit to Celsius
    Parameters:
        int, temp
    Returns:
        int, temp in degrees Celsius
    ''' 
    return (5/9)*(temp-32)


def main():
    '''
    Determine if the current temperature is too cold for a user in Canada
    Parameters:
        None
    Returns:
        None
    '''
    #Ask user what temperature is too cold in Celsius and convert to int 
    threshold = eval(input("Hey Canadian! What temperature is TOO cold for you in Celsius? "))
    #Ask user what the temperature is in Fahrenheit and convert to int
    fahrenheit = eval(input("what's today's temperature in Fahrenheit? "))

    #Determine if it is too cold for the user
    if convert_to_celsius(fahrenheit) < threshold:
        print("It is COLD in Canada today!")
    else:
        print("It is NOT cold in Canada today.")


main()