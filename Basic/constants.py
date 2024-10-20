# Define a constant for the speed of light in vacuum (in meters per second)
SPEED_OF_LIGHT = 299792458

# Function to calculate the energy of an object given its mass
def calculate_energy(mass):
    # Use the constant in the calculation (E = mc^2)
    energy = mass * SPEED_OF_LIGHT ** 2
    return energy

def main():
    mass = 1.0  # 1 kg object
    print(f"Energy of a {mass} kg object: {calculate_energy(mass)} joules")

if __name__ == "__main__":
    main()
