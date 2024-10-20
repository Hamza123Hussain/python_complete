# Base class Person
class Person:
    def __init__(self, name, age):
        # Initialize the Person with a name and an age
        self.name = name
        self.age = age
    
    # A method that describes the person
    def describe(self):
        return f"{self.name} is {self.age} years old."
    
    # A method to greet someone
    def greet(self):
        return f"Hello, my name is {self.name}."
    
# Derived class Student inheriting from Person
class Student(Person):
    def __init__(self, name, age, student_id, grade):
        # Call the initializer of the base class (Person)
        super().__init__(name, age)
        # Initialize specific attributes for Student
        self.student_id = student_id
        self.grade = grade
    
    # Overriding the describe method from the Person class
    def describe(self):
        # Call the original describe method from Person using super()
        base_description = super().describe()
        # Extend the description for a student
        return f"{base_description} They are a student with ID {self.student_id} in grade {self.grade}."
    
    # A new method specific to the Student class
    def study(self):
        return f"{self.name} is studying hard in grade {self.grade}."

# Further inheritance example with a derived class GraduateStudent
class GraduateStudent(Student):
    def __init__(self, name, age, student_id, grade, thesis_title):
        # Call the initializer of the Student class (which also calls Person's)
        super().__init__(name, age, student_id, grade)
        # Initialize specific attributes for GraduateStudent
        self.thesis_title = thesis_title
    
    # Override the describe method again
    def describe(self):
        # Call the describe method from Student class
        base_description = super().describe()
        # Extend the description for a graduate student
        return f"{base_description} They are working on a thesis titled '{self.thesis_title}'."
    
    # New method for GraduateStudent
    def defend_thesis(self):
        return f"{self.name} is defending their thesis: {self.thesis_title}."

# Demonstration of inheritance

# Create a Person object
person = Person('John Doe', 40)
print(person.describe())  # Output: John Doe is 40 years old.
print(person.greet())     # Output: Hello, my name is John Doe.

# Create a Student object (inherits from Person)
student = Student('Jane Smith', 20, 'S12345', 'Sophomore')
print(student.describe())  # Output: Jane Smith is 20 years old. They are a student with ID S12345 in grade Sophomore.
print(student.greet())     # Output: Hello, my name is Jane Smith.
print(student.study())     # Output: Jane Smith is studying hard in grade Sophomore.

# Create a GraduateStudent object (inherits from Student)
grad_student = GraduateStudent('Alice Brown', 25, 'G98765', 'Graduate', 'Machine Learning in Healthcare')
print(grad_student.describe())  # Output: Alice Brown is 25 years old. They are a student with ID G98765 in grade Graduate. They are working on a thesis titled 'Machine Learning in Healthcare.'
print(grad_student.defend_thesis())  # Output: Alice Brown is defending their thesis: Machine Learning in Healthcare.
