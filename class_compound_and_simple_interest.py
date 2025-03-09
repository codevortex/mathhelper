'''
File for calculating compound and simple interest
'''
class Compound_SimpleInterest():
    '''
    Calculates compound and simple interest
    '''
    def __init__(self):
        pass
    #Author: Animesh Bodhak
    # Compound Interest and Simple Interest
    #First Compound Interest
    #I = P(1 + r/n) ** nt
    #I = interest
    #P = Principle
    #r = rate
    #n = number of times it is compounded
    #t = time
    def calculate_compound_interest(self):
        '''
        Calculates and returns compound Interest
        '''
        #Principle input
        principle = float(input("What is the principle?"))
        #Rate input
        rate = float(input("What is the rate?"))
        #Input for the number of times it is compounded (n)
        num_interest = float(input("What is the number of times the interest is compounded?"))
        #Input for time (in years)
        time = float(input("How many years?"))
        #Finds the total to be paid
        total = principle * (1 + (rate/num_interest)) ** (num_interest * time)
        #Finds what the interest is
        interest = total - principle
        #Variable for what the total is
        total_to_be_paid = ("The total which is to be paid is " + str(total) + ",")
        #Variable for what the total and interest is
        return_statement = (total_to_be_paid + " and Interest is " + str(interest) + ".")
        #Returns print_statement
        return return_statement
    #Now Simple Interest
    #I = Prt
    def calculate_simple_interest(self):
        '''
        Calculates and returns simple interest
        '''
        #Principle input
        principle = float(input("What is the principle?"))
        #Rate input
        rate = float(input("What is the rate?"))
        #Time input
        time = float(input("What is the time?"))
        #Interest
        interest = principle * rate * time
        #Total
        total = interest + principle
        #Sentence for Interest
        interest_sentence = ("The total interest is " + str(interest) + ",")
        #Sentence for total
        total_sentence = (" and the total money to be paid is " + str(total) + ".")
        #What should be returned
        return_statement = (interest_sentence + total_sentence)
        #Returns return_statement
        return return_statement
    #Function for Top Level
    def compound_and_simple_interest(self):
        '''
        Calculates and returns simple Interest
        '''
        #Interest Menu
        print(" \n *** Interest Menu *** \n")
        print("1 Calculate Compound Interest's Interest and Total")
        print("2 Calculate Simple Interest's Interest and Total")
        menu_value = int(input("Enter Number from Menu:"))
        if menu_value == 1:
            return_value = self.calculate_compound_interest()
            return return_value
        elif menu_value == 2:
            return_value = self.calculate_simple_interest()
            return return_value
        else:
            return "You have not selected from the list."
def interest_return_value():
    '''
    Function for returning Interest value
    '''
    output = Compound_SimpleInterest()
    output = output.compound_and_simple_interest()
    return output
