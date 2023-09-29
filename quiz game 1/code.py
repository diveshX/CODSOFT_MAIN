import random

# Quiz questions and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["London", "Berlin", "Paris", "Madrid"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Mars", "Venus", "Jupiter", "Saturn"],
        "correct_answer": "Mars"
    },
    {
        "question": "What is the largest mammal on Earth?",
        "choices": ["Elephant", "Giraffe", "Blue Whale", "Hippopotamus"],
        "correct_answer": "Blue Whale"
    }
]

# Function to ask a question
def ask_question(question_data):
    question = question_data["question"]
    choices = question_data["choices"]
    correct_answer = question_data["correct_answer"]

    print(question)
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    user_answer = input("Enter the number of your answer: ")

    if user_answer.isnumeric() and 1 <= int(user_answer) <= len(choices):
        user_choice = choices[int(user_answer) - 1]
        if user_choice == correct_answer:
            print("Correct!")
            return 1
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}")
            return 0
    else:
        print("Invalid input. Please enter the number of your answer.")
        return 0

# Function to calculate the final score
def calculate_score(results):
    return sum(results)

# Function to display final results
def display_results(score, total_questions):
    print(f"Your final score is: {score}/{total_questions}")
    if score == total_questions:
        print("Congratulations! You got all the questions correct.")
    elif score >= total_questions // 2:
        print("Well done! You did a good job.")
    else:
        print("Keep practicing. You can do better next time!")

# Main game loop
def main():
    print("Welcome to the Quiz Game!")
    print("You will be asked multiple-choice questions.")
    print("Enter the number of your answer.")
    print()

    total_questions = len(quiz_questions)
    random.shuffle(quiz_questions)
    user_results = []

    for question_data in quiz_questions:
        user_results.append(ask_question(question_data))

    final_score = calculate_score(user_results)
    display_results(final_score, total_questions)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        main()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    main()
