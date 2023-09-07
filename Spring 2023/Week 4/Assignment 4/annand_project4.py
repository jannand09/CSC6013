# Create functions to count all the numbers in a list divisible by a given integer; find the smallest difference
# between any two numbers in a list; and the product of two size nxn matrices

def count_multiples(array, integer):
    """
    Determines the number of elements in a given array that are multiples of a given integer value
    Parameters:
        array (list): list of numbers to check
        integer (int): integer value
    Returns:
        count (int): number of elements in array that are divisible by integer
    """
    count = 0
    for x in array:
        if x % integer == 0:
            count = count + 1
    return count


def find_smallest_gap(array):
    """
    Determines the smallest difference between any two elements in a list of numbers
    Parameters:
        array (list): list of numbers
    Returns:
        gap (float): smallest difference between any two elements in array
    """
    gap = 0
    for i in range(0, len(array) - 1):
        for j in range(i + 1, len(array)):
            difference = abs(array[i] - array[j])
            if gap == 0 or gap > difference:
                gap = difference
    return gap


def matrix_multiplier(n, a, b):
    """
    Calculates the product of two nxn matrices
    Parameters:
        n (int): size of the matrices
        a (list): size nxn matrix of numbers
        b (list): size nxn matrix of numbers
    Returns:
        c (list): size nxn matrix of numbers and product of A and B
    """
    c = [[] * 0 for _ in range(n)]

    for row in range(len(a)):
        for col in range(n):
            total = 0
            for x in range(n):
                product = a[row][x] * b[x][col]
                total = total + product
            c[row].append(total)

    return c


def main():
    """
    Produces answers for programming assignment #4 questions
    Returns:
        prints answers
    """

    # Initialize list for Question 1a
    q1a = [20, 21, 25, 28, 33, 34, 35, 36, 41, 42]
    # Pass arguments for Question 1a through function
    q1a_answer = count_multiples(q1a, 7)

    # Initialize list for Question 1b
    q1b = [18, 54, 76, 81, 36, 48, 99]
    # Pass arguments for Question 1b through function
    q1b_answer = count_multiples(q1b, 9)

    print("Answers to Question 1: ")
    print(q1a_answer)
    print(q1b_answer)
    print("-----------------------")

    # Initialize list for Question 2a
    q2a = [50, 120, 250, 100, 20, 300, 200]
    # Pass arguments for Question 2a through function
    q2a_answer = find_smallest_gap(q2a)

    # Initialize list for Question 2b
    q2b = [12.4, 45.9, 8.1, 79.8, -13.64, 5.09]
    # Pass arguments for Question 2b through function
    q2b_answer = find_smallest_gap(q2b)

    print("Answers to Question 2:")
    print(q2a_answer)
    print(q2b_answer)
    print("----------------------")

    # Initialize matrices for Question 3a
    q3a_matrix_a = [[2, 7], [3, 5]]
    q3a_matrix_b = [[8, -4], [6, 6]]
    # Pass arguments for Question 3a through function
    q3a_answer = matrix_multiplier(2, q3a_matrix_a, q3a_matrix_b)

    # Initialize matrices for Question 3b
    q3b_matrix_a = [[1, 0, 2], [3, -2, 5], [6, 2, -3]]
    q3b_matrix_b = [[.3, .25, .1], [.4, .8, 0], [-.5, .75, .6]]
    # Pass arguments for Question 3b through function
    q3b_answer = matrix_multiplier(3, q3b_matrix_a, q3b_matrix_b)

    print("Answers to Question 3:")
    print(q3a_answer)
    print(q3b_answer)
    print("----------------------")


main()
