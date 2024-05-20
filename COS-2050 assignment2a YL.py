#COS-2050 assignment2a YL
#A program to calculate the area of a triangle
#Given the sides' lengths inputted by the user
#Assuming those lengths are valid

import math #makes the math library available


def main():
    print("This program calculates the of area triangle")#describes the purpose of the program to the user

    a = float(input("Enter the length of side a: "))#prompts user to input the length of side a, records the following input, and assigns it the value a
    b = float(input("Enter the length of side b: "))#prompts user to input the length of side b, records the following input, and assigns it the value b
    c = float(input("Enter the length of side c: "))#prompts user to input the length of side c, records the following input, and assigns it the value c
   

    # Calculate the semiperimeter of the triangle based on the length of the three sides, user's input
    s = (a + b + c)/2

    # Calculate the area of the triangle using the semperimeter and the length of the three sides via Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print("The area of the triangle is: {}".format(area))

if __name__ == "__main__":
    main()
