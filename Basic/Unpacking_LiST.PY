# Function that calculates the volume of a cuboid given its dimensions
def calculate_volume(length, width, height):
    return length * width * height

# List storing the dimensions of the cuboid
dimensions = [5, 10, 3]  # length = 5, width = 10, height = 3

# Unpack the list and pass its elements as arguments to the function
volume = calculate_volume(*dimensions)

print(f"The volume of the cuboid is: {volume} cubic units")
