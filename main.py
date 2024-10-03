from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

counter = 0
for item in question_data:
    question_text = question_data[counter]['text']
    question_answer = question_data[counter]['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    counter += 1

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was {quiz.user_score}/{quiz.question_number}")