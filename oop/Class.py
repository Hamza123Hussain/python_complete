# Define the Student class
class Student:
    # Class attribute to keep track of the number of Student instances created
    student_count = 0
    
    # Initialize the Student object with student name and house
    def __init__(self, student, House):
        # If House is not provided, raise a ValueError to prompt the user
        if not House:
            raise ValueError('ENTER A HOUSE FOR THE STUDENT')
        # These are private attributes (indicated by the leading underscore)
        # Using private attributes allows control over access through getter and setter methods
        self._student = student
        self._House = House

        # Increment the student_count each time a new student is created
        Student.student_count += 1
    
    # Define how the object should be represented as a string
    def __str__(self):
        # Return a formatted string showing the student name and their house
        return f"{self._student} is from {self._House}"
    
    # Getter method for student attribute
    @property
    def student(self):
        # This method returns the private _student attribute when accessed
        return self._student
    
    # Setter method for student attribute
    @student.setter
    def student(self, value):
        # If the new value is empty or invalid, raise a ValueError
        if not value:
            raise ValueError('Student name cannot be empty')
        # Otherwise, set the new value to the private _student attribute
        self._student = value
    
    # Getter method for House attribute
    @property
    def House(self):
        # This method returns the private _House attribute when accessed
        return self._House
    
    # Setter method for House attribute
    @House.setter
    def House(self, value):
        # If the new value is empty or invalid, raise a ValueError
        if not value:
            raise ValueError('House cannot be empty')
        # Otherwise, set the new value to the private _House attribute
        self._House = value

    # Class method to create a Student instance from a dictionary
    @classmethod
    def from_dict(cls, data):
        """
        Creates a Student instance from a dictionary.
        The dictionary should contain 'student' and 'House' keys.
        """
        return cls(student=data.get('student'), House=data.get('House'))
    
    # Class method to get the total number of students created
    @classmethod
    def total_students(cls):
        """
        Returns the total number of Student instances created.
        """
        return cls.student_count




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
