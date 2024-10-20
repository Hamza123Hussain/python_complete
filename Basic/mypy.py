# Function with type hints for parameters and return value
def add_numbers(a: int, b: int) -> int:
    return a + b

# Function with optional types and None
def greet(name: str = None) -> str:
    if name:
        return f"Hello, {name}!"
    return "Hello, stranger!"

def main():
    print(add_numbers(3, 5))  # Valid
    print(greet("Alice"))     # Valid
    print(greet())            # Valid with default value

if __name__ == "__main__":
    main()
