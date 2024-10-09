#Exception Within A While Loop
while True:
    try: #This Would Check If The Value Added Is Integer or Not
        x=int(input('Enter A Number : '))
    except ValueError: # This Checks If The Type Of The Variable Is Correct Or Not
        print('This Is Not A Integer') 
    else:
        break # The Loop Would End Until A Integer Is Ended
    
print(f'Integer Value : {x}')  # This would only be printed if value is type of integer        