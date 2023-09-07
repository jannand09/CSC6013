# "Is it cold in Canada today?"

def convertToCelsius(temp):
    '''
    Converts Fahrenheit temperature to Celsius
    Parameters:
        temp(int or float)
    Returns:
        Returns temp converted to Celsius (int or float)
    '''    
    return (5/9)*(temp - 32)

def main():
    '''
    Determines if the current temperature is colder than a Canadian's threshold temp
    Parameters:
        None
    Returns:
        None, prints output to console
    '''
    #Ask user for threshold temperature and todays temperature in Celsius and Fahrenheit, respectively
    threshold = eval(input("What is cold to you in degrees Celsius? "))
    todaysTemp = eval(input("What is the temperature today in degrees Fahrenheit? "))

    #Compare threshold temperature and today's temperature in Celsius and print appropriate output
    if threshold > convertToCelsius(todaysTemp):
        print("It is cold for a Canadian!")
    else:
        print("It is not cold for a Canadian.")

main()