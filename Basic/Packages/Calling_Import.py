# Import the HelloFromMe function from the Custom_Package module
from Custom_Package import HelloFromMe
from Custom_Package import CheckSqaure
# Main function to execute HelloFromMe
def main():
    # Call the HelloFromMe function (imported from Custom_Package)
    HelloFromMe()
    CheckSqaure(4)
    

# Boilerplate to run the main() function when this script is executed directly
if __name__ == "__main__":
    main()  # Calls main() function
