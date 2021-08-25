# -*- coding: utf-8 -*-
"""
CSC 221
M1HW1
Robert Land
8/18/2021
"""
def main():
    repeater = True
    while repeater == True:
        print("1. Add")
        print("2. Subtract")
        print("3. Divide")
        print("4. Multiply")
        print("5. Exit")
        menuSelect = int(input("Enter selected number: "))
        if menuSelect == 1:
            adder()
        elif menuSelect == 2:
            subtractor()
        elif menuSelect == 3:
            divider()
        elif menuSelect == 4:
            multiplier()
        elif menuSelect ==5:
            repeater = False
        else:
            print("Please enter one of the specified numbers.\n")
def adder():
    repeaterSum=True
    while repeaterSum == True:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter a second number: "))
        sumNum = num1+num2
        print("The sum of your numbers is: ",sumNum)
        sumSelect = int(input("Enter 1 to repeat, or any other number to return to main menu.\n"))
        if sumSelect == 1:
            print("Repeating..")
        else:
            repeaterSum = False
def subtractor():
    repeaterDiff=True
    while repeaterDiff == True:
        print("Your first number will be subtracted by your second number. Example: 3 - 2 = 1 ")
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter a second number: "))
        diffNum = num1-num2
        print("The difference of your numbers is: ",diffNum)
        subSelect = int(input("Enter 1 to repeat, or any other number to return to main menu.\n"))
        if subSelect == 1:
            print("Repeating..")
        else:
            repeaterDiff = False
def divider():
    repeaterDiv=True
    while repeaterDiv == True:
        print("Your first number will be divided by your second number. Example: 3 / 2 = 1.5 ")
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter a second number: "))
        divNum = num1/num2
        print("The quotient of your numbers is: ",divNum)
        divSelect = int(input("Enter 1 to repeat, or any other number to return to main menu.\n"))
        if divSelect == 1:
            print("Repeating..")
        else:
            repeaterDiv = False
def multiplier():
    repeaterMult=True
    while repeaterMult == True:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter a second number: "))
        multNum = num1*num2
        print("The product of your numbers is: ",multNum)
        multSelect = int(input("Enter 1 to repeat, or any other number to return to main menu.\n"))
        if multSelect == 1:
            print("Repeating..")
        else:
            repeaterMult = False
main()
