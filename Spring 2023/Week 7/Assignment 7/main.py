import math


def mean(arr, n):
    """
    Determines the mean of all numbers in an array
    :param arr: list of numbers (list)
    :param n: length of the array (int)
    :return: mean of the elements in the array (float)
    """
    if n == 1:
        return arr[0]
    else:
        return ((n - 1) / n) * mean(arr[:n], n - 1) + (1 / n) * arr[n - 1]


def descending_binary_search(arr, start, end, k):
    """
    Locates a search key in an array using binary search
    :param arr: list of elements to search through (list)
    :param start: index at which to begin searching (int)
    :param end: index at which to stop searching (int)
    :param k: search key (any)
    :return: index of search key (int) or None
    """
    m = math.floor((end + start) / 2)
    if start > end:
        print(k, " not found in list.")
        return None
    else:
        print("Index checked: ", m)
        if arr[m] == k:
            return m
        elif arr[m] > k:
            return descending_binary_search(arr, m + 1, end, k)
        else:
            return descending_binary_search(arr, start, m - 1, k)


def euclidean_gcd(a, b):
    """
    Determine the greatest common divisor of two integers using Euclidean algorithm
    :param a: first integer (int)
    :param b: second integer (int)
    :return: the greatest common divisor (int)
    """
    print("Input Parameters: ", a, b)
    if b == 0:
        return a
    else:
        return euclidean_gcd(b, a % b)


def main():
    # Answers to Question 1b:
    a1 = [12, 23, 37, 45, 63, 82, 47, 75, 91, 88, 102]
    a2 = [-1.7, 6.5, 8.2, 0.0, 4.7, 6.3, 9.5, 12.2, 37.9, 53.2]

    x = mean(a1, 11)
    y = mean(a2, 10)

    print("Answers for Question 1:")
    print("Mean a1:", x, " Mean a2:", y)
    print("***********************")

    # Answers to Question 2b
    a3 = [100, 87, 85, 80, 72, 67, 55, 50, 48, 42, 40, 31, 25, 22, 18]

    print("Answers for Question 2:")
    print("Search for 87:")
    descending_binary_search(a3, 0, len(a3) - 1, 87)
    print("--------------")
    print("Search for 48:")
    descending_binary_search(a3, 0, len(a3) - 1, 48)
    print("--------------")
    print("Search for 33:")
    descending_binary_search(a3, 0, len(a3) - 1, 33)
    print("--------------")
    print("Search for 10:")
    descending_binary_search(a3, 0, len(a3) - 1, 10)
    print("**************")

    # Answers to Question 3b
    print("Answers for Question 3:")

    print("Calls for 3bi:")
    z = euclidean_gcd(2468, 1357)
    print("Result 3bi: ", z)

    print("Calls for 3bii:")
    w = euclidean_gcd(111, 378)
    print("Result 3bii: ", w)

    print("Calls for 3biii:")
    s = euclidean_gcd(123456789, 987654321)
    print("Result 3biii: ", s)


main()
