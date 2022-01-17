# This is the functions and their helpers for the project questions
# from the Assignment #1
# Functions: fib -> finds nth Fibonacci number
#            fibIt -> finds nth Fibonacci number through a different
#                     method
# Helper: fibItHelper -> does all the calculations for fibIt function
#
# Author: Maksim Pikovskiy, mp8671
# CSCI 261
# 9/17/2021


# Recursively finds the nth Fibonacci number
# Time Complexity: T(n) = T(n-1) + T(n-2) [exponential]
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# Question #7
# A helper recursive function that calculates nth Fibonacci number
def fibItHelper(n, a, b,):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibItHelper(n - 1, b, a + b)


# Question #7
# A main function for finding nth Fibonacci number, using a different technique
def fibIt(n):
    return fibItHelper(n, 0, 1)


# Main function that tests all of the functions for the project questions
def main() -> None:
    print("-=-fib()-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("n = 0 -> ", fib(0))
    print("n = 1 -> ", fib(1))
    print("n = 5 -> ", fib(5))
    print("n = 15 -> ", fib(15))
    print("n = 30 -> ", fib(30))
    print("This is the point where one can see \n"
          "that the fib() function is running slowly. \n"
          "n = 30 has a slight delay.\n"
          "Everything above is running slower and slower.")
    print("\n-=-fibIt() and fibItHelper()-=-=-=-=-=-=-=-=-=-")
    print("n = 0 -> ", fibIt(0))
    print("n = 1 -> ", fibIt(1))
    print("n = 5 -> ", fibIt(5))
    print("n = 15 -> ", fibIt(15))
    print("n = 30 -> ", fibIt(30))
    print("n = 50 -> ", fibIt(50))
    print("n = 100 -> ", fibIt(100))
    print("fibIt does not run slowly on the value of n \n"
          "(n = 30) that makes fib() function run slowly.\n"
          "Everything above the number runs at optimal \n"
          "speed as well.")


# only run this program if it is not being imported by another main module
if __name__ == '__main__':
    main()
