class Student():
    """Student data."""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question():
    """Question data."""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def __repr__(self):
        return f" Question: {self.question}\nAnswer:{self.correct_answer}"

class Exam():
    """Exam data."""
    questions = []

    def __init__(self, name):
        self.name = name


    def add_question(self, question):
        self.questions.append(question)

        return self.questions


    def __repr__(self):
        return f"Question List: {self.questions}"