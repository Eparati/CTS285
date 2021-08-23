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
        print("The sum of your numbers is: ",diffNum)
        sumSelect = int(input("Enter 1 to repeat, or any other number to return to main menu.\n"))
        if sumSelect == 1:
            print("Repeating..")
        else:
            repeaterDiff = False
main()
