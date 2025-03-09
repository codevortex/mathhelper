'''
Top Level File
'''

'''

        "A class is a piece of code with well defined parameters and attributes and has
            methods that interact with those parameters and attributes."

'''

#Importing Menu*
import class_menu
from class_menu import *

#Importing Linear Math Functions
import ClassLinear
from ClassLinear import *

#Importing Quadratic Math Functions
import ClassQuadratic
from ClassQuadratic import *

#Importing GCD Math Functions
import class_gcd
from class_gcd import *

#Importing LCM Math Functions
import class_lcm
from class_lcm import *

#Importing Factorial Math Functions
import class_factorial
from class_factorial import *

#Importing Sequence Math Functions
import ClassSequence_Helper
from ClassSequence_Helper import *

#Importing Compound and Simple Interest math functions*
import class_compound_and_simple_interest
from class_compound_and_simple_interest import *

#Importing Mean/Avereage Math Functions
import class_mean_calculation
from class_mean_calculation import *

#Importing Triangle functions
import Triangle
from Triangle import *

while True:

    USER_CHOICE = menu_return_value()

    if USER_CHOICE == 0:
        print("Thank You!")
        break

    elif USER_CHOICE == (1):
        Linear_answer = linear_return_value()
        print(Linear_answer)

    elif USER_CHOICE == (2):
        Quadratic_answer = quadratic_return_value()
        print(Quadratic_answer)

    elif USER_CHOICE == (3):
        Factorial_answer = factorial_return_value()
        print(Factorial_answer)

    elif USER_CHOICE == (4):
        Lcm_answer = lcm_return_value()
        print(Lcm_answer)

    elif USER_CHOICE == (5):
        Gcd_answer = gcd_return_value()
        print(Gcd_answer)

    elif USER_CHOICE == (6):
        Sequence_answer = sequence_return_value()
        print(Sequence_answer)

    elif USER_CHOICE == (7):
        Interest_answer = interest_return_value()
        print(Interest_answer)

    elif USER_CHOICE == (8):
        mean = mean_return_value()
        print(mean)

    elif USER_CHOICE ==(9):
        Triangle_answer = triangle_return_value()
        print(Triangle_answer)

    else:
        print("You have not selected from the list I gave you.")
