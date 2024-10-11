# Initialize an empty list to store names
names = []

# Open the 'names.txt' file for reading
# with open('names.txt') as file:
#     # Read all lines from the file and extend the names list with the lines
#     names.extend(file.readlines())  # Use extend() to add each line to the names list

# # Iterate through the names list
# for name in names:
#     # Print each name after removing any trailing whitespace characters, including newlines
#     print('All DATA:', name.rstrip())

# cleaner version
# Initialize an empty list to store names
names = []

# Open the 'names.txt' file for reading
with open('names.txt') as file:
    # Iterate through each line in the file
    for line in file:
        # Remove trailing whitespace characters (including newlines) and add the cleaned line to the names list
        names.append(line.rstrip())

# Print all names stored in the names list
print('ALL DATA IN FILE:', names)
