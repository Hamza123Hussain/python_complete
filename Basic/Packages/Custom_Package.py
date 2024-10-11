# Define the HelloFromMe function locally, printing a message
def HelloFromMe():
    # Print a message indicating that the function has been called
    print('HELLO FROM IMPORTED FUNCTION')

# Define a function that returns the square of a number (incorrect logic for demonstration)
def Sqaureme(num):
    # Return the number added to itself instead of squaring (incorrect behavior to be caught by tests)
    return num * num

# Define a function to check if Sqaureme() returns the correct square of the number
def CheckSqaure(num):
    try:
        # Check if Sqaureme() equals the actual square of num (this will fail as the logic is intentionally incorrect)
        assert(Sqaureme(num) == num * num)
    except AssertionError:
        # Print an error message when the assertion fails
        print('THERE IS AN ERROR WITH YOUR INPUT')
