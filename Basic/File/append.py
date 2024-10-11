# Prompt the user to input a name and store it in the 'name' variable
name = input('Enter A Name: ')

# Open (or create) a file named 'names.txt' in append mode ('a') using a context manager
with open('names.txt', 'a') as file:
    # Write the entered name to the file, followed by a newline character
    file.write(f'{name}\n')
