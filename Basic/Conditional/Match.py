def Main(): 
    '''This Is The Main Function.
    Add All The Body Of The Code Within it.'''

    Number=int(input('Enter A Number'))
    print (f"The Number Has Been Squared : {SQUARE(Number)}")
    
    

    
def SQUARE(Number):  # Normal function definition in Python
    # match is mostly used with strings
    
    # Using match-case with conditions
    match Number:
        case _ if Number > 4:  # If the number is greater than 4, return its square
            return Number ** 2
        case _ if Number > 2:  # If the number is greater than 2 but less than or equal to 4, return its cube
            return Number ** 3
        case _:  # Default case: if the number is less than or equal to 2, return the number itself
            return Number

        
        
Main()        