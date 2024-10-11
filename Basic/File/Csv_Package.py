import csv  # Import the csv module to handle CSV file reading

# Initialize an empty list to store student dictionaries
students = []

# Open the 'New.csv' file for reading
with open('New.csv') as file:
    # Use csv.DictReader to read the CSV file into dictionaries where keys are the column headers
    reader = csv.DictReader(file)
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Append a dictionary with 'name' and 'Area' extracted from each row
        students.append({'name': row['name'], 'Area': row['Area']})

# Sort the students by name and print each student's name and area
for student in sorted(students, key=lambda student: student['name']):
    # Print the student's name and area using formatted string literals (f-strings)
    print(f"Name: {student['name']}, Area: {student['Area']}")
