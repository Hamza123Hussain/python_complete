# Prompt the user to input a name and store it in the 'name' variable
name = input('Enter A Name: ')

# Open (or create) a file named 'names.text' in write mode ('w')
file = open('names.text', 'w')

# Write the entered name to the file
file.write(name)

# Close the file to ensure all data is written and resources are released
file.close()
