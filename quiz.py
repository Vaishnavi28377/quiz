import random

def load_questions_and_answers(question_file, answer_file):
    """
    Loads questions and answers from separate files.

    Args:
        question_file (str): Path to the file containing questions (one question per line).
        answer_file (str): Path to the file containing answers (one answer per line, matching the question order).

    Returns:
        tuple: A tuple containing two lists: `questions` and `answers`. Returns None, None on error.
    """
    try:
        with open(question_file, 'r') as qf, open(answer_file, 'r') as af:
            questions = [line.strip() for line in qf]
            answers = [line.strip() for line in af]

        if len(questions) != len(answers):
            print("Error: The number of questions and answers do not match.")
            return None, None  # Indicate an error

        return questions, answers

    except FileNotFoundError:
        print("Error: One or both of the question/answer files were not found.")
        return None, None
    except Exception as e:
        print(f"An error occurred while loading files: {e}")
        return None, None

def run_quiz(questions, answers, num_questions=10):
    """
    Runs a quiz with a specified number of questions.

    Args:
        questions (list): A list of quiz questions.
        answers (list): A list of corresponding answers.
        num_questions (int): The number of questions to include in the quiz (default is 10).
    """

    if not questions or not answers:
        print("Error: Questions or answers are empty.  Quiz cannot start.")
        return

    if num_questions > len(questions):
        print(f"Warning: Requested {num_questions} questions, but only {len(questions)} available.  Using all available questions.")
        num_questions = len(questions)
        
    # Randomly select questions
    question_indices = random.sample(range(len(questions)), num_questions) # Ensure we don't repeat questions.
    quiz_questions = [questions[i] for i in question_indices]
    quiz_answers = [answers[i] for i in question_indices] # Ensure answers match the shuffled questions

    score = 0

    for i in range(num_questions):
        print(f"\nQuestion {i + 1}: {quiz_questions[i]}")
        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == quiz_answers[i].lower():  # Case-insensitive comparison
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {quiz_answers[i]}")

    print(f"\nQuiz complete! Your score: {score}/{num_questions}")

# Example Usage:
if __name__ == "__main__":
    question_file = "questions.txt"  # Replace with your actual file name
    answer_file = "answers.txt"  # Replace with your actual file name

    questions, answers = load_questions_and_answers(question_file, answer_file)

    if questions and answers:
        run_quiz(questions, answers, num_questions=10)  # Change the number of questions if desired