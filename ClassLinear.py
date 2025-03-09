'''
File for Linear functions
'''
class Linear():
    '''
    Class for Linear fuctions
    '''
    def __init__(self):
        pass
    #Author: Animesh Bodhak
    #linear math function file
    #Slope
    def linear_math_tool(self):
        '''
        Function for Linear math functions
        Includes User Menu
        '''
        #Line Equation Menu for selection
        print("\n *** Line-Equation Menu *** \n")
        print("1 Slope from 2 points")
        print("2 Calculating X-Coordinate from Slope, Y-intercept and Y-Coordinate")
        print("3 Calculating Y-Coordinate from Slope, Y-intercept and X-Coordinate")
        print("4 Calculating Y-intercept from Slope, Y-Coordinate and X-Coordinate")
        Q1 = int(input("Enter Number here: "))
        if Q1 == (1):
            #User selected Slope
            x_coordinate1 = float(input("What is x1?"))
            x_coordinate1 = x_coordinate1 * 1.0
            y_coordinate1 = float(input("What is y1?"))
            y_coordinate1 = y_coordinate1 * 1.0
            x_coordinate2 = float(input("What is x2?"))
            x_coordinate2 = x_coordinate2 * 1.0
            y_coordinate2 = int(input("What is y2?"))
            y_coordinate2 = y_coordinate2 * 1.0
            m = float(float((y_coordinate2 - y_coordinate1)/(x_coordinate2 - x_coordinate1)))
            #Prints value of slope
            return("The slope is {m1: .4f}.".format(m1 = m))  
        elif Q1 == (2):
            #User selected X Coordinate    
            m = float(input("What is the slope? Please enter it as a decimal: "))
            y = float(input("What is the y coordinate? Please enter it as a decimal: "))
            y_intercept = float(input("What is the y-intercept? Please enter it as a decimal: "))
            x = float((y/(m)) - (y_intercept))
            #Prints Value of x    
            return("The value of x is {x1: .4f}.".format(x1 = x))    
        elif Q1 == (3):
            #User selected Y Coordinate    
            m = float(input("What is the the Slope? Please enter it as a floating point number: "))
            x = float(input("What is the x coordinate? Please enter it as a floating point number: "))
            y_intercept = float(input("What is the y-intercept? Please enter it as a decimal: "))
            y = float((m*x) + (y_intercept))
            #Prints value of y    
            return("The value of y is {y1: .4f}.".format(y1 = y))
        elif Q1 == (4):
            #User selected y-intercept
            m = float(input("What is the the Slope? Please enter it as a floating point number: "))    
            x = float(input("What is the x coordinate? Please enter it as a floating point number: "))
            y = float(input("What is the y coordinate? Please enter it as a decimal: "))
            y_intercept = float((y) - (m * x))
            return("The value of the y-intercept is {y: .4f}.".format(y = y_intercept))
        else:
            return("You have not chosen from the list I gave you.")
def linear_return_value():
    '''
    Function for returning value to Top level
    '''
    output = Linear()
    output = output.linear_math_tool()
    return output            
