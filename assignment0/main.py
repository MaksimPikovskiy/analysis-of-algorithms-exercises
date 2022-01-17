# This is the functions and their helpers for the project questions
# from the Assignment #0
# Functions: r -> find a reverse of the list
#            prod -> find the product of two numbers
#            fastPow -> find the power of the number
#            prodAccum -> multiplies natural numbers
#            minChange -> find the minimum change with coins
#            greedyMinChange -> find the minimum change with coins, greedily
#            powIt - computer the power of the number using a while loop
# Helpers: head -> return the first element of the list
#          tail -> return the elements of the list, excluding the first one
#          min -> modified minimum function that works with "Failure"
#          plus -> add two numbers; works with "Failure
#          rem -> find the remainder
#          quo -> find the quotient
#
# Author: Maksim Pikovskiy, mp8671
# CSCI 261
# 9/3/2021

# Returns the first element of the list
# The complexity of this code is O(1)
def head(xs):
    return xs[0]


# Returns the elements of the list, excluding the first one
# The complexity of this code is O(k), where k is size of the slice
def tail(xs):
    return xs[1::]


# Finds the smallest number; works with "Failure"
def min(m, n):
    if m == -1 and n == -1:
        return -1
    elif n == -1:
        return m
    elif m == -1:
        return n
    else:
        if m < n:
            return m
        else:
            return n


# Adds two numbers; works with "Failure
def plus(m, n):
    if m == -1 or n == -1:
        return -1
    else:
        return m + n


# Finds the remainder
def rem(m, n):
    return m % n


# Finds the quotient
def quo(a, d):
    return int(a / d)


# Question #3
# Finds a reverse of the list
# The complexity of the concatenation is O(k), where k is the size of the concatenated list
def r(xs):
    if xs == []:
        return []
    else:
        return r(tail(xs)) + [head(xs)]


# Question #4
# Finds the product of two numbers
def prod(m, n):
    if m == 0:
        return 0
    else:
        return prod(m - 1, n) + n


# Question #5
# Finds the power of the number
def fastPow(b, n):
    if n == 0:
        return 1
    else:
        if n % 2 == 0:
            return fastPow(b*b, n/2)
        else:
            return fastPow(b*b, (n-1)/2) * b


# Question #6
# Multiplies the natural numbers
def prodAccum(m, n, a):
    if m == 0:
        return a
    else:
        return prodAccum(m - 1, n, n + a)


# Question #7
# Finds the number of coins needed for the minimum change
def minChange(a, ds):
    if a == 0:
        return 0
    elif ds == []:
        return -1
    else:
        for d in ds:
            if d > a:
                return minChange(a, tail(ds))
            else:
                return min(plus(1, minChange(a - d, ds)), minChange(a, tail(ds)))


# Question #8
# Greedily finds the number of coins needed for the minimum change
def greedyMinChange(a, ds):
    if a == 0:
        return 0
    elif ds == []:
        return -1
    else:
        for d in ds:
            if d > a:
                return greedyMinChange(a, tail(ds))
            else:
                return plus(quo(a, d), greedyMinChange(rem(a, d), tail(ds)))


# Question #9d
# Computes the power of the number using a while loop
def powIt(b, n):
    a = 1
    while n != 0:
        a = b * a
        n = n - 1
    return a


# Main function that tests all of the functions for the project questions
def main() -> None:
    print("r function:")
    print("[4, 3, 2, 1] -> ", r([4, 3, 2, 1]))
    print("[6, 2, 7, 10, 57] -> ", r([6, 2, 7, 10, 57]))

    print("\nprod function:")
    print("(5, 3) -> ", prod(5, 3))
    print("(1, 4) -> ", prod(1, 4))

    print("\nfastPow function:")
    print("(7, 4) -> ", fastPow(7, 4))
    print("(2, 9) -> ", fastPow(2, 9))

    print("\nprodAccum function:")
    print("(6, 4, 2) -> ", prodAccum(6, 4, 2))
    print("(7, 2, 9) -> ", prodAccum(7, 2, 9))

    print("\nminChange function:")
    print("(65, [1, 5, 10, 25, 50]) -> ", minChange(65, [1, 5, 10, 25, 50]))
    print("(57, [1, 5, 10, 25, 50]) -> ", minChange(57, [1, 5, 10, 25, 50]))

    print("\ngreedyMinChange function:")
    print("(65, [50, 25, 10, 5, 1]) -> ", greedyMinChange(65, [50, 25, 10, 5, 1]))
    print("(57, [50, 25, 10, 5, 1]) -> ", greedyMinChange(57, [50, 25, 10, 5, 1]))

    print("\npowIt function:")
    print("(7, 3) -> ", powIt(7, 3))
    print("(6, 4) -> ", powIt(6, 4))


# only run this program if it is not being imported by another main module
if __name__ == '__main__':
    main()
