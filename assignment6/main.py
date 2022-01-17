# These are the functions and helper functions for the project questions from the Assignment #5
# Functions: find_truth_assignment() -> finds truth assignments for variables for Question #5 problem.
#
# Author: Maksim Pikovskiy, mp8671
# CSCI 261
# 12/03/2021

# Question #5
# Finds truth assignments for 3 variables of the problem in Question #5
# Returns False if nothing could be found.
def find_truth_assignment():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print("(", x, ", ", y, ", ", z, ") -> ", end='')
                if(((bool(x) or bool(y)) and bool(z))
                        and ((bool(x) and bool(y) and not bool(z)) or bool(z))
                        and (bool(x) and bool(y) and not bool(z))):
                    print("true")
                    return x, y, z
                print("false")
    return False


# Main function that tests the function for the project question
def main() -> None:
    print("find_truth_assignment()-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("For ((x or y) and z) and ((x and y and not z) or z) and (x and y and not z), "
          "\nthe truth values gotten using "
          "find_truth_assignment() are (False if none are found): ")
    print("\tEnd Result -> ", find_truth_assignment())


# only run this program if it is not being imported by another main module
if __name__ == '__main__':
    main()
