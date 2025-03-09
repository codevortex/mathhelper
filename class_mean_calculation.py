'''
File for calculating mean fucntion
'''
class Mean():
    '''
    Class for calculating Mean
    '''
    def __init__(self, num_list):
        '''
        Num list variable for mean calculation list
        '''
        self.num_list = num_list
    #Author: Animesh Bodhak
    #Calculating Mean/average
    #Function for doing the actual calculation
    #Function for mean calculation
    def mean_calculation(self):
        '''
        Calculates Mean
        '''
        #List of numbers for mean computation
        #Finds number of terms in list and stores in variable
        length_of_list = len(self.num_list)
        #numbers_in_list = length_of_list
        sum_of_list = sum(self.num_list)
        return_value = sum_of_list/length_of_list
        return 'The average of the numbers is ' + str(return_value)
#To get user list use below comments:
#user_question = ("What are the list of numbers you want to find the mean/average of?")
#list(map(float,input(user_question).split()))
def mean_return_value():
    '''
    Function for returning mean value
    '''
    user_question = ("What are the list of numbers you want to find the mean/average of?")
    num_list = list(map(float, input(user_question).split()))
    number_list = num_list
    output = Mean(number_list)
    output = output.mean_calculation()
    return output
            