# These are the functions and helper functions for the project questions from Question #5 of the Assignment #5
# Functions: extraSpace -> calculates how many extra spaces there are after the limit\
#            badnessLine -> calculates the line badness
#            minBad -> computes the minimum paragraph badness
#            minBadDynamic -> computes the minimum paragraph badness using dynamic programming
#            minBadDynamicChoice -> computes the minimum paragraph badness and the choices made using
#                                   dynamic programming
#            printParagraph -> prints the paragraph using words in S and maximum number of characters per line, M
# Helpers: summation -> sums the lengths of words in a given range
# Author: Maksim Pikovskiy, mp8671
# CSCI 261
# 11/12/2021


# Helper Question #5b function
# Sums the lengths of words in a given range
def summation(S, i, j):
    if i > j:
        return 0
    elif i == j:
        return len(S[i])
    else:
        return len(S[i]) + summation(S, i + 1, j)


# Question #5b
# Calculates how many extra spaces there are after the limit
# Can be negative (indicates that it is over the limit)
def extraSpace(S, M, i, j):
    if len(S) == 0:
        return 0
    elif M == 0:
        return 0
    else:
        return M - j + i - summation(S, i, j)


# Question #5d
# Calculates the line badness
def badnessLine(S, M, i, j):
    if len(S) == 0:
        return 0
    elif M == 0:
        return float('inf')
    else:
        extraSpaces = extraSpace(S, M, i, j)
        if extraSpaces < 0:
            return float('inf')
        else:
            return extraSpaces


# Question #5g
# Computes the minimum paragraph badness
def minBad(S, M, i):
    if badnessLine(S, M, i, len(S) - 1) != float('inf'):
        return 0
    else:
        champ = float('inf')

        for k in range(i + 1, len(S)):
            min = minBad(S, M, k) + badnessLine(S, M, i, k - 1)
            if min < champ:
                champ = min

        return champ


# Question #5h
# Dynamically computes the minimum paragraph badness
def minBadDynamic(S, M):
    # all of the line badness'es
    cost = [float('inf') for i in range(len(S))]

    for i in range(0, len(S)):
        if badnessLine(S, M, 0, i) != float('inf'):
            cost[i] = badnessLine(S, M, 0, i)
            if i == len(S) - 1:
                return 0  # everything fits on one line
        else:
            champ = float('inf')
            for k in range(0, i):
                min = cost[k] + badnessLine(S, M, k + 1, i)
                if i == len(S) - 1 and badnessLine(S, M, k + 1, i) != float('inf'):
                    min = cost[k]
                if min < champ:
                    champ = min

            cost[i] = champ

    return cost[len(S) - 1]


# Question #5i
# Dynamically computes the minimum paragraph badness and the choices made
def minBadDynamicChoice(S, M):
    cost = [float('inf') for i in range(len(S))]

    choice = [[] for i in range(len(S))]

    for i in range(0, len(S)):
        if badnessLine(S, M, 0, i) != float('inf'):
            cost[i] = badnessLine(S, M, 0, i)
            choice[i] = [(0, i)]
            if i == len(S) - 1:
                return 0, [(0, i)]
        else:
            champ = float('inf')
            choiceCandidate = []
            for k in range(0, i):
                min = cost[k] + badnessLine(S, M, k + 1, i)
                if i == len(S) - 1 and badnessLine(S, M, k + 1, i) != float('inf'):
                    min = cost[k]
                if min < champ:
                    choiceCandidate = choice[k] + [(k + 1, i)]
                    champ = min

            choice[i] = choiceCandidate
            cost[i] = champ

    return cost[len(S) - 1], choice[len(S) - 1]


# Question #5i
# Prints the paragraph using words in S and maximum number of characters per line, M
# The asymptotic running time of this algorithm is O(n^2).
def printParagraph(S, M):
    cost, choice = minBadDynamicChoice(S, M)

    for i in range(0, len(choice)):
        for j in range(choice[i][0], choice[i][1] + 1):
            print(S[j], end=" ")
        print()


# Main function that tests the function for the project question
def main() -> None:
    S1 = ["What is the asymptotic running time of your algorithm?"]
    S1 = S1[0].split()

    S2 = ["Hello", "World"]

    print("extraSpace()-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    M = 10
    i, j = 0, len(S1) - 1
    print("Let M = 10, i = 0, and j = len(S) - 1: extraSpace(S, M, i, j) -> ", extraSpace(S1, M, i, j))

    M = 10
    i, j = 0, len(S2) - 1
    print("Let M = 10, i = 0, and j = len(S) - 1: extraSpace(S, M, i, j) -> ", extraSpace(S2, M, i, j))
    M = 15
    print("Let M = 15, i = 0, and j = len(S) - 1: extraSpace(S, M, i, j) -> ", extraSpace(S2, M, i, j))

    print("\n\nbadnessLine()-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    M = 10
    i, j = 0, len(S1) - 1
    print("Let M = 10, i = 0, and j = len(S) - 1: badnessLine(S, M, i, j) -> ", badnessLine(S1, M, i, j))

    M = 10
    i, j = 0, len(S2) - 1
    print("Let M = 10, i = 0, and j = len(S) - 1: badnessLine(S, M, i, j) -> ", badnessLine(S2, M, i, j))
    M = 15
    print("Let M = 15, i = 0, and j = len(S) - 1: badnessLine(S, M, i, j) -> ", badnessLine(S2, M, i, j))

    print("\n\nminBad()-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    M = 10
    i = 0
    print("Let M = 10 and i = 0: minBad(S, M, i) -> ", minBad(S1, M, i))

    M = 10
    i = 0
    print("Let M = 10, i = 0,: minBad(S, M, i) -> ", minBad(S2, M, i))
    M = 15
    print("Let M = 15 and i = 0: minBad(S, M, i) -> ", minBad(S2, M, i))

    print("\n\nminBadDynamic()-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    M = 10
    print("Let M = 10 and i = 0: minBadDynamic(S, M) -> ", minBadDynamic(S1, M))
    M = 10
    print("Let M = 10, i = 0,: minBadDynamic(S, M) -> ", minBadDynamic(S2, M))
    M = 15
    print("Let M = 15 and i = 0: minBadDynamic(S, M) -> ", minBadDynamic(S2, M))

    print("\n\nminBadDynamicChoice()-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    M = 10
    print("Let M = 10 and i = 0: minBadDynamicChoice(S, M) -> ", minBadDynamicChoice(S1, M))
    M = 10
    print("Let M = 10, i = 0,: minBadDynamicChoice(S, M) -> ", minBadDynamicChoice(S2, M))
    M = 15
    print("Let M = 15 and i = 0: minBadDynamicChoice(S, M) -> ", minBadDynamicChoice(S2, M))

    print("\n\nprintParagraph()-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    M = 10
    print("Let M = 10 and i = 0: printParagraph(S, M) -> ")
    printParagraph(S1, M)
    M = 10
    print("\nLet M = 10, i = 0,: printParagraph(S, M) -> ")
    printParagraph(S2, M)
    M = 15
    print("\nLet M = 15 and i = 0: printParagraph(S, M) -> ")
    printParagraph(S2, M)

    print("\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    S = ["Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It’s not a story the Jedi would "
         "tell you. It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could "
         "use the Force to influence the midichlorians to create life... He had such a knowledge of the dark side that "
         "he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many "
         "abilities some consider to be unnatural. He became so powerful... the only thing he was afraid of was losing "
         "his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, "
         "then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself."]
    S = S[0].split()
    M = 50
    printParagraph(S, M)
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")


# only run this program if it is not being imported by another main module
if __name__ == '__main__':
    main()
