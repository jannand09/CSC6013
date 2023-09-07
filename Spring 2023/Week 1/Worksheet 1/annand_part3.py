#Part 3
#Swap elements in a vector

def create_vector(length):
    '''
    Creates vector with defined length from 0 to lenght minus one in numerical order
    Parameters:
        int, length of vector
    Returns:
        list, vector
    ''' 
    new_vector = []
    #iterate through numbers from 0 to length minus one and add them to the vector
    for i in range(length):
        new_vector.append(i)
    return new_vector


def swap_vector(vector):
    '''
    Swaps every two values in a vector
    Parameters:
        list, vector
    Returns:
        None, prints original and modified vector
    ''' 
    print("Original Vector:")
    print(vector)
    #Iterate through vector and swap every other value
    for i in range(0,len(vector),2):
        vector[i],vector[i+1] = vector[i+1],vector[i]
    print("New Vector")
    print(vector)


def main():
    '''
    Creates a vector whose length is based on input value and swaps every other value within the vector
    Parameters:
        None
    Returns:
        None
    ''' 
    #Create loop for user to repeatedly use program or exit
    while True:
        #Ask user for length of vector and convert to int
        vector_length = eval(input("Please give an EVEN number between 9 and 21 OR enter 0 to EXIT: "))
        #break from loop if user enters exit value
        if vector_length == 0:
            break
        #create vector and swap values if user gives valid input
        elif vector_length > 21 or vector_length < 9 or vector_length % 2 != 0:
            print("Invalid entry.")
        #notify user that entry was invalid
        else:
            swap_vector(create_vector(vector_length))


main()
        
            


            

