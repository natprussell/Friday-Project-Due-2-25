
import random

# Ask the user if they want Powerball numbers
response = input("Do you want Powerball numbers? (yes/no): ")

# Check the user's response
if response.lower() == "yes":
    # Generate 5 random numbers from 1 to 69
    main_numbers = random.sample(range(1, 70), 5)
    
    # Generate 1 random number from 1 to 26
    powerball_number = random.randint(1, 26)
    
    # Display the generated numbers with commas and spaces
    print(*main_numbers, "", powerball_number)
else:
    print("Maybe next time.")