from quiz_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for adata in question_data:
    question_bank.append(Question(adata["text"], adata["answer"]))


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print("\nYou've have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
