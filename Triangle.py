#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 15:54:54 2021

@author: amu

This Class is for computing the third angle in a triangle
"""



class Triangle():
    def __init__(self):
        pass


    def Triangle_Menu(self):
           print("1) Calcuate the last angle of the triangle")
           print("2) Categorize the triangle based on side lengths")
           print("3) Categorize the triangle based on angle measures")
           user_input = int(input("What is your choice? "))
           while True:
               if user_input == 1:
                   third_angle = self.last_angle()
                   return third_angle
                   break
               elif user_input == 2:
                   triangle_side_type = self.triangle_type_by_side()
                   return(triangle_side_type)
                   break
               elif user_input == 3:
                   triangle_angle_type = self.triangle_type_by_angle()
                   return triangle_angle_type
                   break
               else:
                   print("You have not chosen from the list I have given you.")



    # Below function calculates the last angle of the triangle.
    def last_angle(self):
        angle1 = int(input("What is the first angle's degree? "))
        angle2 = int(input("What is the second angle's degree? "))

        # Calculate and return last angle
        angle3 = int(180-(angle1 + angle2))
        return angle3

    # Below function categorizes triangles based on the side lengths.
    def triangle_type_by_side(self):
        side1 = int(input("What is the length of one of the sides of the triangle?"))
        side2 = int(input("What is the length of one of the other sides of the triangle? "))
        side3 = int(input("What is the length of the remaining side of the triangle? "))

        # Checks if the triangle is actually a triangle
        if side1+side2>side3 and side1+side3>side2 and side2+side3>side1:

            # Checks if triangle is scalene
            if side1!=side2!=side3:
                return"This triangle is scalene"

            if side1==side2 or side2==side3 or side3==side1:

                # Checks if the triangle is an equilateral triangle
                if side1==side2==side3:
                    return "This triangle is an equilateral triangle"

                # Checks if the triangle is isosceles
                else:
                    return "This trianlge is an isosceles triangle"
            else:
                print()
        else:
            return "This is not a triangle"

    # Below function categorizes traingles based on angle lengths.
    def triangle_type_by_angle(self):
        angle1 = int(input("What is the degree of one of the angles of the triangle? "))
        angle2 = int(input("What is the degree of one of the other angles of the triangle? "))

        # Calls last angle function to calculate 3rd angle
        angle3 = self.last_angle()

        if angle1+angle2+angle3 == 180: # Checks if triangle is a triangle
            if angle1<90 and angle2<90 and angle3<90: # Checks if triangle is acute
                return "This triangle is an acute triangle"

            if angle1==90 or angle2==90 or angle3==90: # Checks if triangle is right
                return "This triangle is a right triangle"

            if angle1>90 or angle2>90 or angle3>90: # Checks if triangle is obtuse
                return "This triangle is an obtuse triangle"
            else:
                print()
        else:
            return "This is not a triangle"

def triangle_return_value():
    output = Triangle()
    output = output.Trianlge_Menu()
    return output


