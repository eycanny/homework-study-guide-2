class Student():
    """Student data."""

    def __init__(self, first_name, last_name, address):
        """Instantiate an object with a Student class."""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question():
    """Question data."""

    def __init__(self, question, correct_answer):
        "Instantiate an object with a Question class."

        self.question = question
        self.correct_answer = correct_answer


    def ask_and_evaluate(self):
        """Ask user for answer and evaluate answer."""

        user_answer = input(f"{self.question} > ")
        if user_answer == self.correct_answer:
            return True
        else:
            return False


    def __repr__(self):
        return f"{self.question},{self.correct_answer}"

class Exam():
    """Exam data."""
    
    questions = []

    def __init__(self, name):
        """Instantiate an object with class Exam attributes."""

        self.name = name


    def add_question(self, question):
        """Add question to an exam's list of questions."""

        self.questions.append(question)

        return self.questions


    def administer(self):
        """Administer all questions of an exam."""

        correct_answers = 0
        i = 0

        for question in self.questions[::1]:
            answer = question.ask_and_evaluate()
            if answer == True:
                correct_answers += 1
        
        correct_percent = float(correct_answers / len(self.questions[::1]) * 100)

        return f"You scored a {correct_percent:.2f}%!"



    def __repr__(self):
        """Returns list of available questions in an exam."""

        return f"Question List: {self.questions}"


##Test##
# exam = Exam('midterm')
# set_q = Question('What is the method for adding an element to a set?', '.add()')
# exam.add_question(set_q)
# pwd_q = Question('What does pwd stand for?', 'print working directory')
# exam.add_question(pwd_q)
# list_q = Question('Python lists are mutable, iterable, and what?', 'ordered')
# exam.add_question(list_q)
