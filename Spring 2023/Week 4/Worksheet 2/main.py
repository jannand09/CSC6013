# Worksheet for Week 4

import math


def log_base_two(n):
    return round(math.log2(n))


def square_root(n):
    return round(math.sqrt(n))


def product_log_two(n):
    return round(n*math.log2(n))


def squared(n):
    return round(n**2)


def cubed(n):
    return round(n**3)


def exponential(n):
    return round(2**n)


def factorial(n):
    return round(math.factorial(n))


def main():
    logs = []
    roots = []
    products = []
    squares = []
    cubes = []
    exponentials = []
    factorials = []

    for x in range(1,11,1):
        a = log_base_two(x)
        logs.append(a)

        b = square_root(x)
        roots.append(b)

        c = product_log_two(x)
        products.append(c)

        d = squared(x)
        squares.append(d)

        e = cubed(x)
        cubes.append(e)

        f = exponential(x)
        exponentials.append(f)

        g = factorial(x)
        factorials.append(g)

    print(logs)
    print(roots)
    print(products)
    print(squares)
    print(cubes)
    print(exponentials)
    print(factorials)


main()

