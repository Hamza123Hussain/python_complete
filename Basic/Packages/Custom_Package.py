# Define the main function to execute HelloFromMe and print a message
def main():
    # Call the HelloFromMe function
    HelloFromMe()
    # Print an additional message after calling HelloFromMe
    print('Hello')

# Define the HelloFromMe function locally, printing a message
def HelloFromMe():
    print('HELLO FROM IMPORTED FUNCTION')

# Boilerplate to run the main() function when this script is executed directly
if __name__ == "__main__":
    main()  # Calls main() function

def Sqaureme(num):
    return num+num

def CheckSqaure(num):
    assert(Sqaureme(num)==num*num)
        
        