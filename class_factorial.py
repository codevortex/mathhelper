'''
Calculates Factorial
'''
#num = int(input("What is the positive integer you want the factorial of?"))
#a = num
class Factorial():
    '''
    Class for calculating factorial
    '''
    #num = int(input("What is the positive integer you want the factorial of?"))
    def __init__(self, number):
        '''
        number for calculating factorial
        '''
        self.number = number
    def calculate_factorial(self):
        '''
        Function which calculates factorial
        '''
        total = 1
        num = self.number
        while num:
            total = total * num
            num = num - 1
        return total
def factorial_return_value():
    '''
    returns Factorial of number
    '''
    num = int(input("What is the positive integer you want the factorial of?"))
    factorial_number = num
    answer = Factorial(factorial_number)
    output = answer.calculate_factorial()
    return output
