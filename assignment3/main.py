# These are the functions and helper functions for the project questions from the Assignment #3
# Functions: search -> finds if target value is present in the array using virtual slicing.
#            sortedHasSum -> searches for a pair of numbers in a sorted array S of n numbers whose sum is x.
#            hasSum -> searches for a pair of numbers in an array S whose sum is x.
#            quicksort -> sorts a given array, that has stack size of O(log(n)) regardless of running time.
# Helpers:   partition -> puts the elements in their correct position in sorted array.
#
# Author: Maksim Pikovskiy, mp8671
# CSCI 261
# 10/15/2021
from math import floor


# Helper for Question #6 function
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


# Question #1
# A function that searches virtual array slices to find if the target value is present.
def search(a, v):
    l = 0
    h = len(a) - 1
    while l <= h:
        m = l + floor((h - l) / 2)
        if v == a[m]:
            return True
        elif v < a[m]:
            h = m - 1
        else:
            l = m + 1
    return False


# Question #4a
# A function that searches for a pair of numbers in a sorted array S of n numbers whose sum is x.
# Time Complexity: O(n)
def sortedHasSum(S, n, x):
    left = 0
    right = n - 1
    while left <= right:
        sum = S[left] + S[right]
        if sum == x:
            return True
        elif sum < x:
            left += 1
        else:
            right -= 1
    return False


# Question #4b
# A function that searches for a pair of numbers in an array S whose sum is x.
# Time Complexity: O(nlog(n))
def hasSum(S, n, x):
    S.sort()
    return sortedHasSum(S, n, x)
    # As hasSum has to sort the array, it is O(nlog(n)).
    # As the array gets sorted, hasSum has same implementation as sortedHasSum(S, n, x)
    # left = 0
    # right = n - 1
    # while left <= right:
    #     sum = S(left) + S(right)
    #     if sum == x:
    #         return True
    #     elif sum < x:
    #         left += 1
    #     else:
    #         right -= 1
    # return False


# Question #6
# A function that sorts a given array, that has stack size of O(log(n)) regardless of running time.
def quicksort(a, l, h):
    if l < h:
        m = partition(a, l, h)
        quicksort(a, l, m - 1)
        quicksort(a, m + 1, h)
        return a
    else:
        return None


# Main function that tests the function for the project question
def main() -> None:
    print("search()-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    a = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    print("Let a = [10,20,30,40,50,60,70,80,90], target = 30: search(a, 30) -> ", search(a, 30))
    a = [1, 2, 4, 6]
    print("Let a = [1, 2, 4, 6], target = 3: search(a) -> ", search(a, 3))

    print("sortedHasSum()-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    a = [1, 2, 3, 4, 5]
    print("Let a = [1, 2, 3, 4, 5], target = 5: sortedHasSum(a, 5, 5) -> ", sortedHasSum(a, 5, 5))
    a = [1, 2, 3, 4, 5, 6]
    print("Let a = [1, 2, 3, 4, 5, 6], target = 11: sortedHasSum(a, 6, 11) -> ", sortedHasSum(a, 6, 11))
    print("Let a = [1, 2, 3, 4, 5, 6], target = 13: sortedHasSum(a, 6, 13) -> ", sortedHasSum(a, 6, 13))

    print("hasSum()-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    a = [3, 5, 6, 1, 2, 4]
    print("Let a = [3, 5, 6, 1, 2, 4], target = 8: hasSum(a, 6, 8) -> ", hasSum(a, 6, 8))

    print("quicksort()-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    a = [1, 5, 6, 2, 3, 8, 7, 4]
    print("Let a = [1, 5, 6, 2, 3, 8, 7, 4], quicksort(a, 0, |a| - 1) -> ", quicksort(a, 0, len(a) - 1))


# only run this program if it is not being imported by another main module
if __name__ == '__main__':
    main()
