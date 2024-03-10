class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list


    def still_has_question(self):
        if self.question_number< len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        self.question = self.question_list[self.question_number].text
        self.answer = input(f"Q.{self.question_number+1}: {self.question} (True/False)\n")
        if self.answer == self.question_list[self.question_number].answer:
            print("Your answer is correct")
            self.score +=1
        else:
            print("Your answer is wrong")
        self.question_number += 1
        print(f"Your score is {self.score}/{self.question_number}\n")


