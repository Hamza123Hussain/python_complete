def Main(): 
    '''This Is The Main Function.
    Add All The Body Of The Code Within it.'''
    Name=input('Enter A Name')
    Hello(Name)
    Number=int(input('Enter A Number'))
    print (f"The Number Has Been Squared : {SQAURE(Number)}")
    
    
'''We Just Have Make The Main Function At The Top
And Then We Can Make The Other Functions AnyWhere We Want To 
And Can Acess Those Functions In the Main Function Body.'''    
def Hello(Name="hamza"): #How Normal Function is Defined In Python
    print(F"THE Name Of The User -> {Name}") # Body Of The Function
    
    
def SQAURE(Number): #How Normal Function is Defined In Python
    return Number * Number
        
        
Main()        