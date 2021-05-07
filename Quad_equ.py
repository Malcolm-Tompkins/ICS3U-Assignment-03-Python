#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on May 5, 2021
# Solves user input quadratic equations

import math


def main():
    # Function that does the calculating and output
    print("Welcome to the quadratic equation calculator")
    print("Simply input your variables and let the program find the zeros")
    # User input
    user_var_A = int(input("Input the A value of your quadratic equation: "))
    user_var_B = int(input("Input the B value of your quadratic equation: "))
    user_var_C = int(input("Input the C value of your quadratic equation: "))
    # Process
    discriminant = (user_var_B ** 2) - (4 * user_var_A * user_var_C)

    if (discriminant > 0):

        # Process
        solution1 = (-user_var_B + math.sqrt(discriminant) / (2 * user_var_A))
        solution2 = (-user_var_B - math.sqrt(discriminant) / (2 * user_var_A))
        # Output
        print("Your solutions are: {0:,.2f} and {1:,.2f}"
              .format(solution1, solution2))

    elif (discriminant == 0):

        # Process
        solution1 = solution2 = -user_var_B / (2 * user_var_A)
        # Output
        print("Your two solutions are: {0:,.2f} and {1:,.2f}"
              .format(solution1, solution2))

    else:

        # Process
        solution1 = solution2 = -user_var_B / (2 * user_var_A)
        imaginary_solution = math.sqrt(-discriminant) / (2 * user_var_A)
        # Output
        print("First solution: {0:,.2f} + {1:,.2f}"
              .format(solution1, imaginary_solution))
        print("Second solution: {0:,.2f} - {1:,.2f}"
              .format(solution2, imaginary_solution))


if __name__ == "__main__":
    main()
