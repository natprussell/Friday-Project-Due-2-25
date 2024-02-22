
import random


response = input("Do you want Powerball numbers? (yes/no): ")

if response.lower() == "yes":
    
    main_numbers = random.sample(range(1, 70), 5)
    
    
    powerball_number = random.randint(1, 26)
    
    
    print(*main_numbers, "", powerball_number)
else:
    print("Maybe next time.")