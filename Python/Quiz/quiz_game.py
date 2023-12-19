import random


def ask_question(question, correct_answer):
    user_answer = input(question).lower()
    if user_answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        print(f"The correct answer is {correct_answer}")
        return 0


def start_quiz():
    print("Welcome to my Quiz Game!")

    playing = input("Do you want to play the game? ").lower()
    if playing not in ["yes", "y"]:
        quit()

    print("Okay! Let's play :)")
    total_questions = int(input("How many questions do you want to answer? [10-20] "))
    if total_questions not in range(10, 21):
        print("Please enter a number between 10 and 20")
        quit()

    questions = {
        "What does CPU stand for? ": "central processing unit",
        "What does GPU stand for? ": "graphics processing unit",
        "What does RAM stand for? ": "random access memory",
        "What does PSU stand for? ": "power supply unit",
        "What does HDD stand for? ": "hard disk drive",
        "What does SSD stand for? ": "solid state drive",
        "What does IP stand for? ": "internet protocol",
        "What does HTTP stand for? ": "hypertext transfer protocol",
        "What does FTP stand for? ": "file transfer protocol",
        "What does DNS stand for? ": "domain name system",
        "What does HTML stand for? ": "hypertext markup language",
        "What does CSS stand for? ": "cascading style sheets",
        "What does JS stand for? ": "javascript",
        "What does SQL stand for? ": "structured query language",
        "What does API stand for? ": "application programming interface",
        "What does SDK stand for? ": "software development kit",
        "What does IDE stand for? ": "integrated development environment",
        "What does GUI stand for? ": "graphical user interface",
        "What does CLI stand for? ": "command line interface",
        "What does RGB stand for? ": "red green blue",
        "What does ASCII stand for? ": "american standard code for information interchange",
        "What does UTF-8 stand for? ": "unicode transformation format 8-bit",
        "What does JSON stand for? ": "javascript object notation",
        "What does XML stand for? ": "extensible markup language",
        "What does HTML5 stand for? ": "hypertext markup language 5",
        "What does CSS3 stand for? ": "cascading style sheets 3",
        "What does JSX stand for? ": "javascript xml",
        "What does SQL3 stand for? ": "structured query language 3",
        "What does API3 stand for? ": "application programming interface 3",
        "What does SDK3 stand for? ": "software development kit 3",
        "What does IDE3 stand for? ": "integrated development environment 3",
        "What does GUI3 stand for? ": "graphical user interface 3",
        "What does CLI3 stand for? ": "command line interface 3",
        "What does RGB3 stand for? ": "red green blue 3",
        "What does ASCII3 stand for? ": "american standard code for information interchange 3",
        "What does UTF-83 stand for? ": "unicode transformation format 8-bit 3",
        "What does JSON3 stand for? ": "javascript object notation 3",
        "What does XML3 stand for? ": "extensible markup language 3",
        "What does HTML53 stand for? ": "hypertext markup language 53",
        "What does CSS33 stand for? ": "cascading style sheets 33",
        "What does JSX3 stand for? ": "javascript xml 3",
        "What does SQL33 stand for? ": "structured query language 33",
        "What does API33 stand for? ": "application programming interface 33",
        "What does SDK33 stand for? ": "software development kit 33",
        "What does IDE33 stand for? ": "integrated development environment 33",
        "What does GUI33 stand for? ": "graphical user interface 33",
        "What does CLI33 stand for? ": "command line interface 33",
        "What does RGB33 stand for? ": "red green blue 33",
        "What does ASCII33 stand for? ": "american standard code for information interchange 33",
        "What does UTF-833 stand for? ": "unicode transformation format 8-bit 33",
        "What does JSON33 stand for? ": "javascript object notation 33",
        "What does XML33 stand for? ": "extensible markup language 33",
        "What does HTML533 stand for? ": "hypertext markup language 533",
        "What does CSS333 stand for? ": "cascading style sheets 333",
        "What does JSX333 stand for? ": "javascript xml 333",
        "What does SQL333 stand for? ": "structured query language 333",
        "What does API333 stand for? ": "application programming interface 333",
        "What does SDK333 stand for? ": "software development kit 333",
        "What does IDE333 stand for? ": "integrated development environment 333",
        "What does GUI333 stand for? ": "graphical user interface 333",
        "What does CLI333 stand for? ": "command line interface 333",
        "What does RGB333 stand for? ": "red green blue 333",
        "What does ASCII333 stand for? ": "american standard code for information interchange 333",
        "What does UTF-8333 stand for? ": "unicode transformation format 8-bit 333",
        "What does JSON333 stand for? ": "javascript object notation 333",
        "What does XML333 stand for? ": "extensible markup language 333",
    }

    selected_questions = random.sample(list(questions.items()), total_questions)

    score = 0
    for question, correct_answer in selected_questions:
        score += ask_question(question, correct_answer)

    print(f"Your score is {score}/" + str(total_questions))


start_quiz()
