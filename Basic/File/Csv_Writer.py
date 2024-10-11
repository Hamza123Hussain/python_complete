import csv  # Import the csv module to handle CSV file operations

# Prompt user to input a name
name = input('Enter Name: ')
# Prompt user to input an area
Area = input('Enter Area: ')

# Open the 'New.csv' file in append mode ('a' mode adds to the file without overwriting)
with open('New.csv', 'a', newline='') as file:
    # Create a DictWriter object to write a dictionary to the CSV file
    writer = csv.DictWriter(file, fieldnames=['name', 'Area'])  # Specify the column names (headers)
    
    # Write a row to the CSV file using the user input as a dictionary
    writer.writerow({'name': name, 'Area': Area})  # Adds the name and area as a row

# Open the same file again in append mode ('a')
with open('New.csv', 'a', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)
    
    # Write a row with 'name' and 'Area' (but this line has an issue as it writes a set)
    # You should pass a list or tuple instead of a set to avoid incorrect output.
    writer.writerow(['name', 'Area'])  # Writes the column headers to the file as a row
