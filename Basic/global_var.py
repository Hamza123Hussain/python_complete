# Declare a global variable
count = 0

# Function that modifies the global variable
def increment_count():
    global count  # Use the global keyword to modify the global variable
    count += 1

# Main function to demonstrate global variable behavior
def main():
    print("Initial count:", count)
    increment_count()
    print("Count after incrementing:", count)

if __name__ == "__main__":
    main()
