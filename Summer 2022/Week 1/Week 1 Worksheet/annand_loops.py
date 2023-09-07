#Create a loop that swaps elements in a vector

def main():
    '''
    Creates vector with swapped values
    Parameters:
        None
    Returns:
        None, prints vector with swapped values to console
    ''' 
    #Asks user for size of vector
    vector_size = eval(input("Enter even integer between 9 and 21 for size of the vector: "))
    #Initialize vector as empty list
    vector = []

    #Determine if vector size is betwene 9 and 21 and even
    if vector_size > 20 or vector_size < 9 or vector_size % 2 != 0:
        print("Invalid input.")
    else:
        #Create vector with user inputted size vector size
        for x in range(vector_size):
            vector.append(x)
        #Swap every two elements in the vector
        for y in range(0,len(vector),2):
            vector[y], vector[y+1] = vector[y+1], vector[y]
        print(vector)

main()