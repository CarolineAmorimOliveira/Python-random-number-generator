import random
import math

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Use the modulo operator to check if the number is even or odd
kind = "even" if number % 2 == 0 else "odd"

# Use a math function: calculate the square root of the number
square_root = math.sqrt(number)

# Print the results
print("Random number generated:", number)
print("This number is:", kind)
print("The square root is:", round(square_root, 2))
