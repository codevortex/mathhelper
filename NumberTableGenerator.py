#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 08:26:13 2021

@author: amu
"""
"""
Welcome to Table Printer!

Where you can print number tables!

:) :) :) 
"""

user_input = int(input("What number table do you want today? Please enter: "))
length = int(input("Do you want this table to go to 10 or 12? Please enter: "))
print("Thank You! Your table shall be generated in a few moments, please wait")


while (True):
    num1 = 0
    if length == 10:
        while (num1 < 10):
            num1 = num1 + 1
            print(str(num1) + " X " + str(user_input) + " = " + str(num1 * user_input))
        if num1 == 10:
            user_choice = int(input("Enter 0 to exit program. Enter 1 to print another number table: "))
            if user_choice == 0:
                print("Thank You!")
                break
            if user_choice == 1:
                user_input = int(input("What number table do you want today? Please enter: "))
                length = int(input("Do you want this table to go to 10 or 12? Please enter: "))
                print("Thank You! Your table shall be generated in a few moments, please wait")
                num1 = 0
                break
    if user_choice == 0:
        break
    if length == 12:
        num1 = 0
        while (num1 < 12):
            num1 = num1 + 1
            print(str(num1) + " X " + str(user_input) + " = " + str(num1 * user_input))
        if num1 == 12:
            user_choice = int(input("Enter 0 to exit program. Enter 1 to print another number table: "))
            if user_choice == 0:
                print("Thank You!")
                break
            if user_choice == 1:
                user_input = int(input("What number table do you want today? Please enter: "))
                length = int(input("Do you want this table to go to 10 or 12? Please enter: "))
                print("Thank You! Your table shall be generated in a few moments, please wait")
                break
    if user_choice == 0:
        break
                