# Define a Point class to represent a 2D point
class Point:
    def __init__(self, x, y):
        # Initialize the point's coordinates
        self.x = x
        self.y = y

    # Overload the + operator to add two points
    def __add__(self, other):
        # Create a new Point object by adding the coordinates of two points
        return Point(self.x + other.x, self.y + other.y)

    # Overload the - operator to subtract two points
    def __sub__(self, other):
        # Create a new Point object by subtracting the coordinates of two points
        return Point(self.x - other.x, self.y - other.y)

    # Overload the * operator to multiply a point by a scalar
    def __mul__(self, scalar):
        # Create a new Point object by multiplying the coordinates by a scalar
        return Point(self.x * scalar, self.y * scalar)

    # Overload the str() function for a more readable string representation
    def __str__(self):
        # Return a string representing the point's coordinates
        return f"({self.x}, {self.y})"

# Demonstration of operator overloading

# Create two Point objects
point1 = Point(2, 3)
point2 = Point(5, 7)

# Add two points using the overloaded + operator
result_add = point1 + point2
print("Result of point1 + point2:", result_add)  # Output: (7, 10)

# Subtract two points using the overloaded - operator
result_sub = point1 - point2
print("Result of point1 - point2:", result_sub)  # Output: (-3, -4)

# Multiply a point by a scalar using the overloaded * operator
result_mul = point1 * 3
print("Result of point1 * 3:", result_mul)  # Output: (6, 9)
