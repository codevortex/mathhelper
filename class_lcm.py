'''
File which calculates LCM of a list of numbers
'''
class LCM():
    '''
    Class which calculates LCM of a list of numbers
    '''
    def __init__(self, my_list):
        self.my_list = my_list
    def lcm(self, num_1, num_2):
        '''
        Calculates lcm of two numbers and returns number
        '''
        #Finds LCM of 2 numbers
        first_no = num_1
        second_no = num_2
        while num_1 != num_2:
            while num_1 > num_2:
                num_1 = num_1 - num_2
            while num_1 < num_2:
                num_2 = num_2 - num_1
        if num_1 == num_2:
            gcd = num_1
            #print("The G.C.D is " + str(num_1))
            lcm1 = int((first_no * second_no)/gcd)
            return lcm1
    def long_lcm(self, my_list):
        '''
        Function that adds the number from above function to list
        '''
        while len(my_list) > 1:
            #Finds LCM of first two numbers
            num1 = my_list.pop(0)
            num2 = my_list.pop(0)
            lcm_final = self.lcm(num1, num2)
            #Adds LCM to list
            my_list.append(lcm_final)
        if len(my_list) == 1:
            #Final LCM
            my_final_lcm = my_list.pop(0)
            #print('My Final GCD = ' + str(my_final_gcd))
            return my_final_lcm
        else:
            #print('Not Enough numbers for GCD')
            return 'Error: No valid numbers given for calculating gcd'
    def lcm_math_function(self):
        '''
        Function which returns LCM
        '''
        final_lcm = self.long_lcm(self.my_list)
        #Returns the final LCM
        return "The final lcm is " + str(final_lcm) + "."
#my_list = list(map(int,input("What are the numbers you want to find the L.C.M of?").split()))
#user_input = my_list
def lcm_return_value():
    '''
    Function which sends value to Top Level
    '''
    my_list = list(map(int, input("What are the numbers you want to find the L.C.M of?").split()))
    user_input = my_list
    output = LCM(user_input)
    output = output.lcm_math_function()
    return output
#For debugging purposes:-
#List of numbers for LCM
#my_list = list(map(int,input("What are the numbers you want to find the L.C.M of?").split()))
#print(my_list)
