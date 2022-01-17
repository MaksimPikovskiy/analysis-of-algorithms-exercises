# These are the functions and helper functions for the project questions from the Assignment #4
# Functions: max2 -> finds a maximum of two numbers without using comparison operations
#            fSelect -> finds a specified element of the list
#            iSelect -> finds a specified element of the list using partition
# Helpers:   partition -> puts the elements in their correct position in sorted array
#            head -> return the first element of the list
#            tail -> return the elements of the list, excluding the first one
#            iSelectHelper -> uses partition to function to find an element in array using an index
# Author: Maksim Pikovskiy, mp8671
# CSCI 261
# 10/29/2021


# Returns the first element of the list
def head(xs):
    return xs[0]


# Returns the elements of the list, excluding the first one
def tail(xs):
    return xs[1::]


# Helper for Question #3 function
# Partition function for quicksort function
def partition(a, l, h):
    x = a[h]
    i = l - 1
    j = l
    while j < h:
        if a[j] <= x:
            i += 1
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
        j += 1
    temp = a[i + 1]
    a[i + 1] = a[h]
    a[h] = temp
    return i + 1


# Helper for Question #3 function
# A recursive function that uses partition function to find an element with its index
def iSelectHelper(a, i, l, h):
    if len(a) == 0:
        return -1  # returns an error "Bad index"
    elif l <= h:
        m = partition(a, l, h)
        if i < m:
            return iSelectHelper(a, i, l, m - 1)
        elif i > m:
            return iSelectHelper(a, i, m + 1, h)
        else:
            return a[m]
    else:
        return None


# Question #1
# A function that finds a maximum of two numbers without comparison
def max2(a, b):
    return (a + b + abs(a - b)) // 2


# Question #2
# A function that finds a specified element of the list
def fSelect(xs, i):
    if len(xs) == 0:
        return -1  # returns an error "Bad index"
    else:
        x = head(xs)
        ys = tail(xs)

        l = []
        s = []
        m = []
        s.append(x)
        # O(n) time
        for y in ys:
            if y < x:
                l.append(y)
            elif y == x:
                s.append(y)
            else:
                m.append(y)

        if i < len(l):
            return fSelect(l, i)
        elif len(l) <= i < (len(l) + len(s)):
            return x
        else:
            return fSelect(m, i - (len(l) + len(s)))


# Question #3
# A function that finds a specified element of the list using partition
def iSelect(a, i):
    return iSelectHelper(a, i, 0, len(a) - 1)


# Main function that tests the function for the project question
def main() -> None:
    print("max2()-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Let a = 1 and b = 5: max2(1, 5) -> ", max2(1, 5))
    print("Let a = 11 and b = 6: max2(11, 6) -> ", max2(11, 6))
    print("Let a = 75 and b = 23: max2(75, 23) -> ", max2(75, 23))
    print("Let a = 4 and b = 98: max2(4, 98) -> ", max2(4, 98))

    a = [5, 1, 3, 2, 4]

    print("fSelect()-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Let a = [5, 1, 3, 2, 4], index = 0: fSelect(a, 0) -> ", fSelect(a, 0))
    print("Let a = [5, 1, 3, 2, 4], index = 4: fSelect(a, 4) -> ", fSelect(a, 4))
    print("Let a = [5, 1, 3, 2, 4], index = 2: fSelect(a, 2) -> ", fSelect(a, 2))
    print("Let a = [5, 1, 3, 2, 4], index = 3: fSelect(a, 3) -> ", fSelect(a, 3))
    print("Let a = [5, 1, 3, 2, 4], index = 1: fSelect(a, 1) -> ", fSelect(a, 1))

    print("iSelect()-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Let a = [5, 1, 3, 2, 4], index = 0: iSelect(a, 0) -> ", iSelect(a, 0))
    print("Let a = [5, 1, 3, 2, 4], index = 4: iSelect(a, 4) -> ", iSelect(a, 4))
    print("Let a = [5, 1, 3, 2, 4], index = 2: iSelect(a, 2) -> ", iSelect(a, 2))
    print("Let a = [5, 1, 3, 2, 4], index = 3: iSelect(a, 3) -> ", iSelect(a, 3))
    print("Let a = [5, 1, 3, 2, 4], index = 1: iSelect(a, 1) -> ", iSelect(a, 1))


# only run this program if it is not being imported by another main module
if __name__ == '__main__':
    main()
