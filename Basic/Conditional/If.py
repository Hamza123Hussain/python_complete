def Main(): 
    '''This Is The Main Function.
    Add All The Body Of The Code Within it.'''

    Number=int(input('Enter A Number'))
    print (f"The Number Has Been Squared : {SQAURE(Number)}")
    
    

    
    
def SQAURE(Number): #How Normal Function is Defined In Python
    
    #A simple way of using if and else in python
    # if(Number==2):
    #     return Number**2
    # elif(Number==4):
    #     return Number**3
    # else:
    #     return Number
    
    # Using OR AND AND IN IF ELSE CONDTIONAL
    if(Number>0 or Number<=2):# only one condtion is to be fulfilled
        return Number**2
    elif(Number>2 and Number<=4): # both condtions have to be fulfilled
        return Number**3
    else:
        return Number
    
        
        
Main()        