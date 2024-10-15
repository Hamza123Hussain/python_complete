# Define the Student class
class Student:
    # Initialize the Student object with student name and house
    def __init__(self, student, House):
        # If House is not provided, raise a ValueError to prompt the user
        if not House:
            raise ValueError('ENTER A HOUSE FOR THE STUDENT')
        # Assign the provided student name and house to the object attributes
        self.student = student
        self.House = House
    
    # Define how the object should be represented as a string
    def __str__(self):
        # Return a formatted string showing the student name and their house
        return f" {self.student} is from {self.House}"

# Define the main function where the program's execution starts
def main():
    print('hello')  # Greet the user
    # Call CREATE_Student function to get a new student instance
    Student = CREATE_Student()
    # Print the string representation of the created student object
    print(Student)

# Define the function to create a new student
def CREATE_Student():
    # Ask the user to input the student's name
    student = input('Enter Name : ')
    # Ask the user to input the student's house
    House = input('Enter House : ')
    # Create a new Student object with the provided details
    New_Student = Student(student, House)
    # Return the newly created student object
    return New_Student

# This code block ensures that main() is only called when the script is run directly
if __name__ == '__main__':
    main()  # Call the main function to start the program
