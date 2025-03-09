#quadratic math functions file
import math

class Quadratic():
    def __init__(self):
        pass
    #Author: Animesh Bodhak
    
    
    def quadratic(self):
        #Quadratic menu
        print("\n *** Quadratic Equation Menu *** \n")
        print("1 Calculate Vertex")
        print("2 Parabola Direction")
        print("3 Calculate Y-Coordinate")
        print("4 Calculate Coefficient of x^2(a) in y = ax^2 + bx + c")
        print("5 Calculate Coefficient of x(b) in y = ax^2 + bx + c")
        print("6 Calculate y intercept(c) in y = ax^2 + bx + c")
        print("7 Calculate X-Coordinate")
        user_choice = int(input("Please enter a number: "))
        if user_choice == (1):
            #calculate vertex -b/2a
            a = float(input("What is the value of x^2 coefficient(a)?"))
            a = a * 1.0
            b = float(input("What is the value of x coefficient(b)?"))
            b = b * 1.0
            vertex = float((-(b)/(2*a)))
            return ("The value of the vertex is " + str(vertex) + ".")
        elif user_choice == (2):
            #Parabola direction (a<0 or a>0)
            a = float(input("What is the value of x^2 coefficient(a)?"))
            a = a * 1.0
            b = float(input("What is the value of x coefficient(b)?"))
            b = b * 1.0
            if a > 0:
                return ("The parabola opens up.")
            else:
                return ("The parabola opens down.")
        elif user_choice == (3):
            #Calculate y coordinate using y = ax^2 + bx + c
            x = float(input("What is the value of x?"))
            x = x * 1.0
            a = float(input("What is the value of x^2 coefficient(a)?"))
            a = a * 1.0
            b = float(input("What is the value of x coefficient(b)?"))
            b = b * 1.0
            c = float(input("What is the value of the y-intercept(c)?"))
            c = c * 1.0
            a = float(x * (a*x + b))
            a = float(a + c)
            y = a
            return ("The value of y is " + str(y) + ".")
        elif user_choice == (4):
            #Calculate a in y = ax^2 + bx + c
            x = float(input("What is the value of x?"))
            x = x * 1.0
            b = float(input("What is the value of x coefficient(b)?"))
            b = b * 1.0
            c = float(input("What is the value of the y-intercept(c)?"))
            c = c * 1.0
            y = float(input("What is the value of y?"))
            y = y * 1.0
            b = float(b*x)
            x = float(x ** 2)
            y = float(y - c)
            y = float(y - b)
            y = float(y/x)
            a = y
            return ("The value of x^2 coefficient is " + str(a) + ".")
        elif user_choice == (5):
            #Calculate b in y = ax^2 + bx + c
            x = float(input("What is the value of x?"))
            x = x * 1.0
            a = float(input("What is the value of x^2 coefficient(a)?"))
            a = a * 1.0
            c = float(input("What is the value of the y-intercept(c)?"))
            c = c * 1.0
            y = float(input("What is the value of y?"))
            y = y * 1.0
            a = float(a * x ** 2)
            y = float(y-c)
            y = float(y - a)
            y = float(y/x)
            b = float(y)
            return ("The value of x coefficient(b) is " + str(b) + ".")
        elif user_choice == (6):
            #Calculate c in y = ax^2 + bx + c
            x = float(input("What is the value of x?"))
            x = x * 1.0
            a = float(input("What is the value of x^2 coefficient(a)?"))
            a = a * 1.0
            b = float(input("What is the value of x coefficient(b)?"))
            b = b * 1.0
            y = float(input("What is the value of y?"))
            y = y * 1.0
            a = float(a * x ** 2)
            b = float(b * x)
            a = float(a + b)
            y = float(y-a)
            c = float(y)
            return ("The value of the y-intercept(c) is " + str(c) + ".")
        elif user_choice == (7):
            #Calculate x coordinate using Quadratic Formula
            a = float(input("What is the value of x^2 coefficient(a)?"))
            a = a * 1.0
            b = float(input("What is the value of x coefficient(b)?"))
            b = b * 1.0
            c = float(input("What is the value of the y-intercept(c)?"))
            c = c * 1.0
            bsqr_minus_4ac = float((b ** 2) - (4*(a)*(c)))
            if bsqr_minus_4ac >= 0:
                #The square root is not imaginary
                sqr_root = math.sqrt(bsqr_minus_4ac)
                x1 = ((-(b) + sqr_root)/(2 * a))
                x2 = ((-(b) - sqr_root)/(2 * a))
                #String formatting for only 4 digits after decimal point
                x1_str = ("The values for x are {x1: .4f} and {x2: .4f}".format(x1 = x1, x2 = x2))
                return(x1_str)
                
            else:
                #The square root is imaginary
                 sqr_root = -1 * (bsqr_minus_4ac)
                 sqr_root = math.sqrt(bsqr_minus_4ac)
                 x1 = ((-(b) + sqr_root)/2 * a)
                 x2 = ((-(b) - sqr_root)/2 * a)
                 #String formatting for only 4 digits after decimal point
                 re_val = ("The values for x are {x1: .4f}i and {x2: .4f}i".format(x1 = x1, x2 = x2))
                 side_note = ("Note: i stands for imaginary.")
                 return (re_val + side_note)
            
        else:
            #User did not select from menu
            return("You have not chosen from the list I gave you.")

def quadratic_return_value():             
    output = Quadratic()
    output = output.quadratic()
    return(output)
            
            