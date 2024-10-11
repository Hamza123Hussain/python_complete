# Import the HelloFromMe function from the Custom_Package module
from Custom_Package import HelloFromMe
# Import the CheckSqaure function from Custom_Package as well
from Custom_Package import CheckSqaure

# Main function to execute HelloFromMe and CheckSqaure
def main():
    # Prompt user for a number input and convert it to an integer
    Number = int(input('Enter A Number'))
    # Call the HelloFromMe function (imported from Custom_Package)
    HelloFromMe()
    # Check if the number input squares correctly using the CheckSqaure function
    CheckSqaure(Number)

# Boilerplate to run the main() function when this script is executed directly
if __name__ == "__main__":
    # Calls main() function
    main()
