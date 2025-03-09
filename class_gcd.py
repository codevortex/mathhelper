'''
file for calculating GCD
'''
class GCD():
    '''
    Class for calculating GCD
    '''
    def __init__(self, my_list):
        self.my_list = my_list
#gcd math functions
    def gcd(self, num_1, num_2):
        '''
        Calculates GCD of two numbers
        '''
        #Finds GCD of 2 numbers
        while num_1 != num_2:
            while num_1 > num_2:
                num_1 = num_1 - num_2
            while num_1 < num_2:
                num_2 = num_2 - num_1
        if num_1 == num_2:
            return num_1
    def long_gcd(self, my_list):
        '''
        Fuction which adds number from above function to list
        '''
        #GCD number list
        while len(my_list) > 1:
            #Finds Gcd of two numbers
            num1 = my_list.pop(0)
            num2 = my_list.pop(0)
            gcd_final = self.gcd(num1, num2)
            #Adds GCD to list
            my_list.append(gcd_final)
        if len(my_list) == 1:
            #Returns final GCD
            my_final_gcd = my_list.pop(0)
            #print('My Final GCD = ' + str(my_final_gcd))
            return my_final_gcd
        else:
            #print('Not Enough numbers for GCD')
            return 'Error: No numbers given for calculating gcd'
    def gcd_math_function(self):
        '''
        Function for returning GCD
        '''
        final_gcd = self.long_gcd(self.my_list)
        #Below comment for debugging purposes
        #Prints final GCD
        return 'The final GCD is ' + str(final_gcd)
#my_list = list(map(int,input("What are the numbers you want to find the G.C.D of?").split()))
#a = my_list
def gcd_return_value():
    '''
    Function for return GCD to top level
    '''
    my_list = list(map(int, input("What are the numbers you want to find the G.C.D of?").split()))
    user_list = my_list
    output = GCD(my_list = user_list)
    output = output.gcd_math_function()
    return output
#Below Comments for debugging purposes...
#List of numbers for GCD
#my_list = list(map(int,input("What are the numbers you want to find the G.C.D of?").split()))
#Below Comment for debugging purposes...
#print(my_list)
#Variable for final GCD
