from data import question_data
from quiz_brain import QuizBrain

class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

question_bank = []
for i in range(0,len(question_data)):
    text = question_data[i]["question"]
    answer = question_data[i]["correct_answer"]
    question_bank.append(Question(text,answer))

quiz = QuizBrain(question_bank)
while quiz.still_has_question :
    quiz.next_question()

