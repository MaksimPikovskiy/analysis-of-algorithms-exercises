# This is the function and helper function for the project question from the Assignment #2
# Functions: fibPow -> finds nth Fibonacci number, using a matrix representation, L
# Helpers: nthPower -> raises a matrix to nth power
#
# Author: Maksim Pikovskiy, mp8671
# CSCI 261
# 10/1/2021


# Question #4a
# 2x2 matrix representation for L
# this matrix allows for L(a,b) = (b, a + b) to be true
L = [[0, 1],  # b       when matrix is multiplied by (a, b)^T
     [1, 1]]  # a + b   when matrix is multiplied by (a, b)^T


# Question #4b
# A function that raises a matrix to nth power
def nthPower(matrix, n):
    # base case #1
    if n == 0:
        return [[0, 0],
                [0, 0]]
    # base case #2
    elif n == 1:
        return matrix
    # n is even case
    elif n % 2 == 0:
        tempMatrix = nthPower(matrix, n / 2)
        return [[tempMatrix[0][0] * tempMatrix[0][0] + tempMatrix[0][1] * tempMatrix[1][0],
                 tempMatrix[0][0] * tempMatrix[0][1] + tempMatrix[0][1] * tempMatrix[1][1]],
                [tempMatrix[1][0] * tempMatrix[0][0] + tempMatrix[1][1] * tempMatrix[1][0],
                 tempMatrix[1][0] * tempMatrix[0][1] + tempMatrix[1][1] * tempMatrix[1][1]]]
    # n is odd case
    else:
        tempMatrix = nthPower(matrix, n // 2)
        tempMatrix = [[tempMatrix[0][0] * tempMatrix[0][0] + tempMatrix[0][1] * tempMatrix[1][0],
                       tempMatrix[0][0] * tempMatrix[0][1] + tempMatrix[0][1] * tempMatrix[1][1]],
                      [tempMatrix[1][0] * tempMatrix[0][0] + tempMatrix[1][1] * tempMatrix[1][0],
                       tempMatrix[1][0] * tempMatrix[0][1] + tempMatrix[1][1] * tempMatrix[1][1]]]
        return [[L[0][0] * tempMatrix[0][0] + L[0][1] * tempMatrix[1][0],
                 L[0][0] * tempMatrix[0][1] + L[0][1] * tempMatrix[1][1]],
                [L[1][0] * tempMatrix[0][0] + L[1][1] * tempMatrix[1][0],
                 L[1][0] * tempMatrix[0][1] + L[1][1] * tempMatrix[1][1]]]


# Question #4c
# A function for finding nth Fibonacci number, using a matrix representation, L
def fibPow(n):
    Ln = nthPower(L, n)
    a = 0
    b = 1
    # for n and n + 1 Fibonacci number
    # return (Ln[0][0] * a + Ln[0][1] * b), (Ln[1][0] * a + Ln[1][1] * b)
    return Ln[0][0] * a + Ln[0][1] * b


# Main function that tests the function for the project question
def main() -> None:
    print("For n == 0, fibonacci is 0, the fibPow(0) results in:", fibPow(0))
    print("For n == 1, fibonacci is 1, the fibPow(1) results in:", fibPow(1))
    print("For n == 5, fibonacci is 5, the fibPow(5) results in:", fibPow(5))
    print("For n == 10, fibonacci is 55, the fibPow(10) results in:", fibPow(10))
    print("For n == 20, fibonacci is 6765, the fibPow(20) results in:", fibPow(20))
    print("For n == 50, fibonacci is 12586269025, the fibPow(50) results in:", fibPow(50))


# only run this program if it is not being imported by another main module
if __name__ == '__main__':
    main()
