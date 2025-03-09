#Author: Animesh Bodhak
'''
File for menu
'''
class Menu():
    '''
    This class is for the user selection menu for MathHelper
    '''
    def __init__(self):
        pass
    def select_math_opp(self):
        '''
        Menu is below
        '''
        menu_value = 0
        while True:
            print("\n ***  Menu: *** \n")
            print("0 Exit Program")
            print("1 Linear Equation (Slope, X or Y coordinate)")
            print("2 Quadratic Equation(Vertex, Parabola)")
            print("3 Find the factorial of a number")
            print("4 Find L.C.M")
            print("5 Find G.C.D")
            print("6 Arithmetic and Geometric Sequence's nth term and sum")
            print("7 Compound and Simple Intrest's Interest and Total amount")
            print("8 Calculate the Mean or average of a list of numbers")
            print("9 Calculate the last angle or categorize triangles based on side lengths or angles")
            menu_value = int(input("Enter a number from the list above: "))
            if not(menu_value >= 0 and menu_value <= 8):
                print("You have not selected from the above list. ")
            else:
                break
        return menu_value
def menu_return_value():
    '''
    Function for returning menu selection
    '''
    user_choice = Menu()
    user_choice = user_choice.select_math_opp()
    return user_choice
#Bug Check (2 comments below)
#user_choice = select_math_opp()
#print('User Choice = ' + str(user_choice))
