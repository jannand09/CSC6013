#Part 1
#Is it cold in Canada today?

def convert_to_celsius(temp):
    return (5/9)*(temp-32)

threshold = eval(input("Hey Canadian! What temperature is TOO cold for you in Celsius? "))
fahrenheit = eval(input("what's today's temperature in Fahrenheit? "))

if convert_to_celsius(fahrenheit) < threshold:
    print("It is COLD in Canada today!")
else:
    print("It is NOT cold in Canada today.")


#Part 2
#Check for a zig zag

def zigzag(first, second, third):
    if first > second and second < third:
        return True
    elif first < second and second > third:
        return True
    else:
        return False


a = eval(input("Please give value for 'a': "))
b = eval(input("Please give value for 'b': "))
c = eval(input("Please give value for 'c': "))

print(zigzag(a,b,c))

#Part 3
#Swap elements in a vector

def create_vector(length):
    new_vector = []
    for i in range(length):
        new_vector.append[i]
    return new_vector


def swap_vector(vector):
    for i in range(0,len(vector),2):
        vector[i],vector[i+1] = vector[i+1],vector[i]
    print(vector)


vector_length = eval(input("Please give an EVEN number between 9 and 21: "))
