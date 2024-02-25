# Friday-Project-Due-2-25
This repo includes AI generated versions of the past three Friday projects. 

The MadlibAI.py program collects user input for various prompts and utilizes the information to dynamically construct a descriptive paragraph. It then outputs the personalized paragraph, providing a playful and interactive experience by incorporating the user's input into a predefined narrative structure.
    The steps include:
        Get user input.
        Create a paragraph without f-string.
        Print paragraph.

The PowerballAI.py program asks the user if they want Powerball numbers. If yes, it generates 5 random main numbers (1-69) and 1 Powerball number (1-26), displaying them. If no, it prints "Maybe next time."
    The steps include:
        Ask user if they want Powerball numbers.
        Check user's response.
        Generate 5 random numbers from 1 to 69.
        Generate 1 random number from 1 to 26.
        Display the generated numbers with commas and spaces.

The TriviaAI.py program is a trivia quiz program. It defines a set of trivia questions and their correct answers in a dictionary. It then quizzes the user, checking their answers and keeping track of the score. After all questions are answered, it prints the user's final score out of the total number of questions.
    The steps include:
        Define a dictionary with trivia questions and their answers
        Initialize the user's score to 0
        Iterate through each question in the dictionary
        Ask the user the current question and get their answer
        Check if the user's answer is correct (case-insensitive)
        Display the user's final score