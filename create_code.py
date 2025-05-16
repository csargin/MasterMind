import random

def create_code(min_number=1,max_number=9, digit = 4):
    #returns a list of 4 numbers between 1 (included) and 9 (included)

    secret_code = []

    a = [1, 2, 3, 4, 5, 6] 

    secret_code = random.sample(range(min_number, max_number +1 ), digit)
   
    return secret_code

    


