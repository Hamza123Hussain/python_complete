# Function that accepts three named arguments
def display_info(name, age, city):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")

# Dictionary containing information to be passed as arguments
person_info = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

# Unpack the dictionary and pass its items as arguments to the function
display_info(**person_info)
