# Initialize an empty list to store student dictionaries
students = []

# Open the 'Student.csv' file for reading
with open('Student.csv') as file:
    # Iterate through each line in the file
    for line in file:
        # Remove trailing whitespace and split the line by commas into 'name' and 'place'
        name, place = line.rstrip().split(',')
        # Create a dictionary for each student with 'name' and 'place' keys
        student = {'name': name, 'place': place}  # Dictionary with student info
        # Append the dictionary to the students list
        students.append(student)

# Define a function to return the 'name' from a student dictionary (used for sorting)
def getname(student):
    return student['name']  # Accesses the 'name' key of each student dictionary

# Sort the students by name using the getname() function and print them
for student in sorted(students, key=getname):
    print('All Students:', student['name'])  # Print the 'name' of each student

# Alternatively, using a lambda function to directly access the 'name' key for sorting
for student in sorted(students, key=lambda student: student['name']):
    print('All Students:', student['name'])  # Print the 'name' of each student
