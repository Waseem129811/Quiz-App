# This Python code simulates the backend logic for a quiz application.
# In a real-world scenario, this logic would run on a server (e.g., using Flask, FastAPI, or Django)
# and interact with a database to store questions, user scores, etc.

class QuizBackend:
    def __init__(self):
        # Hardcoded quiz questions. In a real backend, these would be fetched from a database.
        self.questions_data = [
            {
                "id": "q1",
                "question": "What is the capital of France?",
                "options": ["Berlin", "Madrid", "Paris", "Rome"],
                "correct_answer": "Paris",
            },
            {
                "id": "q2",
                "question": "Which planet is known as the Red Planet?",
                "options": ["Earth", "Mars", "Jupiter", "Venus"],
                "correct_answer": "Mars",
            },
            {
                "id": "q3",
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "correct_answer": "Pacific Ocean",
            },
            {
                "id": "q4",
                "question": "Who painted the Mona Lisa?",
                "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"], # Fixed: Added missing ']'
                "correct_answer": "Leonardo da Vinci",
            },
            {
                "id": "q5",
                "question": "What is the chemical symbol for water?",
                "options": ["O2", "H2O", "CO2", "NaCl"],
                "correct_answer": "H2O",
            },
        ]
        # Create a dictionary for quick lookup of questions by ID
        self.questions_by_id = {q["id"]: q for q in self.questions_data}

    def get_all_questions(self):
        """
        Retrieves all quiz questions.
        In a real API, this might return a subset or be paginated.
        It should ideally *not* send the correct answers to the frontend directly.
        """
        # Return a copy to prevent external modification
        return [
            {"id": q["id"], "question": q["question"], "options": q["options"]}
            for q in self.questions_data
        ]

    def check_answer(self, question_id: str, user_answer: str) -> bool:
        """
        Checks if the user's provided answer for a specific question is correct.

        Args:
            question_id (str): The ID of the question.
            user_answer (str): The answer provided by the user.

        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        question = self.questions_by_id.get(question_id)
        if not question:
            print(f"Error: Question with ID '{question_id}' not found.")
            return False
        return user_answer == question["correct_answer"]

    def calculate_score(self, user_responses: list[dict]) -> int:
        """
        Calculates the total score based on a list of user responses.

        Args:
            user_responses (list[dict]): A list of dictionaries, where each dict
                                         contains 'question_id' and 'user_answer'.
                                         Example: [{'question_id': 'q1', 'user_answer': 'Paris'}]

        Returns:
            int: The total score.
        """
        score = 0
        for response in user_responses:
            question_id = response.get("question_id")
            user_answer = response.get("user_answer")

            if question_id and user_answer is not None:
                if self.check_answer(question_id, user_answer):
                    score += 1
            else:
                print(f"Warning: Invalid response format in user_responses: {response}")
        return score

# Example Usage (how you would use this logic in a Python script or server endpoint):
if __name__ == "__main__":
    backend = QuizBackend()

    # 1. Simulate fetching questions (e.g., for frontend display)
    print("--- All Questions (without correct answers for frontend) ---")
    questions_for_frontend = backend.get_all_questions()
    for q in questions_for_frontend:
        print(f"ID: {q['id']}, Q: {q['question']}, Options: {q['options']}")

    print("\n--- Simulating Answer Checks ---")
    # 2. Simulate checking individual answers (e.g., when user submits an answer)
    q1_correct = backend.check_answer("q1", "Paris")
    print(f"Is 'Paris' correct for q1? {q1_correct}") # Expected: True

    q2_incorrect = backend.check_answer("q2", "Earth")
    print(f"Is 'Earth' correct for q2? {q2_incorrect}") # Expected: False

    q_non_existent = backend.check_answer("q99", "Random")
    print(f"Is 'Random' correct for q99? {q_non_existent}") # Expected: False (and error message)

    print("\n--- Simulating Score Calculation ---")
    # 3. Simulate calculating final score (e.g., after quiz completion)
    user_quiz_session_answers = [
        {"question_id": "q1", "user_answer": "Paris"},
        {"question_id": "q2", "user_answer": "Mars"},
        {"question_id": "q3", "user_answer": "Atlantic Ocean"}, # Incorrect
        {"question_id": "q4", "user_answer": "Leonardo da Vinci"},
        {"question_id": "q5", "user_answer": "H2O"},
    ]

    final_score = backend.calculate_score(user_quiz_session_answers)
    print(f"Final score for the simulated session: {final_score}") # Expected: 4
