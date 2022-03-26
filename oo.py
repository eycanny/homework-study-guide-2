class Student():
    """A student."""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question():
    """A question in an exam."""

    def __init__(self, question, correct_answer):
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
        self.name = name


    def add_question(self, question):
        """Add question to an exam's list of questions."""

        self.questions.append(question)

        # return self.questions


    def administer(self):
        """Administer all questions of an exam."""

        correct_answers = 0
        i = 0

        for question in self.questions[::1]:
            answer = question.ask_and_evaluate()
            if answer == True:
                correct_answers += 1
        
        correct_percent = float(correct_answers / len(self.questions[::1]) * 100)

        return correct_percent



    def __repr__(self):
        """Returns list of available questions in an exam."""

        return f"Question List: {self.questions}"

class Quiz(Exam):
    """Quiz data"""

    def administer(self):
        """Administer a quiz"""

        score = super().administer(self)
        if score < 50:
            return 0

        else:
            return 1


class StudentExam():
    """Student and exam data"""

    def __init__(self):
        """Instantiate an object of the StudentExam class"""

        self.student = student
        self.exam = exam

    def take_test(self, exam):
        """Administer exam and assign score to a StudentExam instance"""

        self.score = exam.administer()

        print(f"You got a score of {score:.2f}.")


def example():
    exam1 = Exam("Example")
    
    set_q = Question('What is the method for adding an element to a set?', '.add()')
    exam.add_question(set_q)

    pwd_q = Question('What does pwd stand for?', 'print working directory')
    exam.add_question(pwd_q)

    list_q = Question('Python lists are mutable, iterable, and what?', 'ordered')
    exam.add_question(list_q)

    student = Student("FName", "LName", "Address")

    studentexam1 = StudentExam(student, exam1)

