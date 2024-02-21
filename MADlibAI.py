# Get user input
largeObject = input("Enter a large object: ")
largeObjects = input("Enter large objects (plural): ")
adjective = input("Enter an adjective: ")
bodyPart = input("Enter a body part: ")
restaurant = input("Enter a restaurant: ")
food = input("Enter a food: ")
otherFood = input("Enter another food: ")

# Create a paragraph without f-string
paragraph = "I've had a very " + adjective + " day. This morning, I dropped a box of " + largeObjects + " on my " + bodyPart + ". Then, at lunch, I went to " + restaurant + " for their delicious " + food + ", but the waiter brought me a " + otherFood + ", which I was not hungry for. Finally, on my way home, I was cut off by a van with a large " + largeObject + " strapped to the roof."

# Print the paragraph
print(paragraph)