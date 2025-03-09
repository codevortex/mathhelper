class Sequence_Calculator():
    def __init__(self):
        pass
    def arithmetic_sequence_sum(self):
        #Input for number of terms, first term, common difference, and output is sum.
        #First Term Inputnumber_of_terms = int(input("What is the number of terms in the Sequence?"))
        first_term = float(input("What is the first term?"))
        #Input for last term
        last_term = float(input("What is the last term?"))
        #Input for number of terms
        number_of_terms = int(input("What is the number of terms in the Sequence?"))
        #Calculates arithmetic sequence sum
        arithmetic_sum = float(number_of_terms*((first_term + last_term)/2))
        return arithmetic_sum
    
    def arithmetic_nth_term(self):
        #Input for number of terms, first term, and common difference. Output/return is the last/nth term.
        #First Term Input
        first_term = float(input("What is the first term?"))
        #Number of terms input
        number_of_terms = int(input("What is the number of terms in the Sequence?"))
        #Common difference input
        common_difference = float(input("What is the common difference?"))
        #Calculating last term
        last_term  = float(first_term + ((number_of_terms - 1)*common_difference))
        return last_term
        
    def geometric_sequence_sum(self):
        #First Term Input
        first_term = float(input("What is the first term?"))
        #Common ratio Input
        common_ratio = float(input("What is the common ratio (cannot be 1)?"))
        if common_ratio != 1:
            #Number of terms input
            number_of_terms = int(input("What is the number of terms in the Sequence?"))
            sum_of_sequence = float((first_term * (1 - common_ratio ** number_of_terms)/(1 - common_ratio)))
            return sum_of_sequence
        else:
            return ("The common ratio cannot be equal to one.")
    
    def geometric_nth_term(self):
       # Input for first term, common ratio and nth term.
       #First Term Input
       first_term = float(input("What is the first term?"))
       #Common ratio Input 
       common_ratio = float(input("What is the common ratio (cannot be 1)?"))
       if common_ratio != 1:
           nth_term = float(input("What is the nth term's number in the sequence?"))
           answer = float(first_term * (common_ratio ** (nth_term - 1))) 
           return answer
       else:
           return("Common ratio cannot be 1.")
       
       
    
    def sequence_helper(self):
        #Menu asks user if user wants to find sum of sequence or nth term
        print("1  Find the Sum of a Arithmetic sequence")
        print("2  Find nth term of a Arithmetic sequence")
        print("3  Find the Sum of a Geometric sequence")
        print("4  Find the nth term of a Geometric sequence")
        user_choice = int(input("Enter a number: "))
    
        if user_choice == 1:
            print_value = self.arithmetic_sequence_sum()
            return print_value
        elif user_choice == 2:
            print_value = self.arithmetic_nth_term()
            return print_value
        elif user_choice == 3:
            print_value = self.geometric_sequence_sum()
            return print_value
        elif user_choice == 4:
            print_value = self.geometric_nth_term()
            return print_value
        else:
            return ("You have not chosen from the list given to you.")
def sequence_return_value():        
    output = Sequence_Calculator()
    output = output.sequence_helper()
    return(output)