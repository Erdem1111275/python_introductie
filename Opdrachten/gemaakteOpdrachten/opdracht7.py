# Rekenmachine # Rekenmachine met extra output
def subtract(first_number, second_number):
    print(first_number - second_number)

def add(first_number, second_number):
    print(first_number + second_number)

def multiply(first_number, second_number):
    print(first_number * second_number)

def divide(first_number, second_number):
    print(first_number / second_number)

def calculation(first_number, operator, second_number, debug):
    if debug == "yes":
        print(f"{first_number} {operator} {second_number} = ")
    if operator == "-":
        subtract(first_number, second_number)
    elif operator == "+":
        add(first_number, second_number)
    elif operator == "*":
        multiply(first_number, second_number)
    elif operator == "/":
        divide(first_number, second_number)
    else:
        print("error, verkeerde invoer")
        

input1 = input("voer het eerste getal in: ")
operator = input("voer een in operator (+, -, * of /): ")
input2 = input("voer het tweede getal in: ")
debug = input("debug yes/no: ").lower()


calculation(int(input1),  operator, int(input2), debug)

#Refactoring
burgers = ["hamburger", "cheeseburger", "bic mac", "quarter pounder"]
warme_drankjes = ["koffie", "cappucino", "chocolademelk"]
koude_drankjes = ["coca cola", "cola zero", "7-up", "fanta", "fristi"]

dine_in = False

question_1 = ""
question_2 = ""
question_3 = ""

def question(input_question, list):
    question_anwser = input(input_question + " [" + ", ".join(list) + "]: ").lower()
    if question_anwser in list:
        print(question_anwser)
    else:
        question(input_question, list)

print("Welkom bij de Mac Donald's")

while question_1 != "opeten" or question_1 != "meenemen":
    question_1 = input("Hier opeten of meenemen? [Opeten/Meenemen]: ").lower()

    if question_1 == "meenemen":
        print("Meenemen")
        eat_in = False

    elif question_1 == "opeten":
        print("Hier opeten")
        eat_in = True


while question_2 != "burgers" or question_2 != "drankjes":
    question_2 = input("Burgers of drankjes? [Burgers/Drankjes]: ").lower()

    if question_2 == "burgers":
        question("Burgers", burgers)

    elif question_2 == "drankjes":

        while question_3 != "koude" and question_3 != "warme":
            question_3 = input("Drankjes [Warme/Koude]: ").lower()

            if question_3 == "warme":
                question("Warme drankjes", warme_drankjes)

            elif question_3 == "koude":
                question("Koude drankjes", koude_drankjes)

if eat_in:
    print("Bedankt voor uw bestelling en eet smakelijk in ons restaurant.")
else:
    print("Bedankt voor uw bestelling, goede reis en eet smakelijk.")

# Student raport

students_per_classroom = {
    "SWDVT-2023-1A": [
        {
            "naam": "Diederik de Vries",
            "resultaten": {
                "WP1": "uitstekend",
                "WP2": "voldoende",
                "WP3": "uitstekend",
                "WP4": "voldoende",
            },
        },
        {
            "naam": "Veysel Altinok",
            "resultaten": {
                "WP1": "goed",
                "WP2": "goed",
                "WP3": "goed",
                "WP4": "goed",
            },
        },
    ],

    "SWDVT-2023-1B": [
        {
            "naam": "Mark Otting",
            "resultaten": {
                "WP1": "onvoldoende",
                "WP2": "voldoende",
                "WP3": "voldoende",
                "WP4": "onvoldoende",
            },
        },
        {
            "naam": "Jelle van der Loo",
            "resultaten": {
                "WP1": "voldoende",
                "WP2": "uitstekend",
                "WP3": "goed",
                "WP4": "voldoende",
            },
        },
    ],
}


def is_student_excellent(student):
    excellent = False
    excellent_count = 0
    no_low_grades = True

    for result in student["resultaten"]:
        if student["resultaten"][result] == "uitstekend":
            excellent_count += 1
        if student["resultaten"][result] == "onvoldoende" or student["resultaten"][result] == "voldoende":
            no_low_grades = False

    if no_low_grades or excellent_count > 1:
        excellent = True

    return excellent


def excellent_students(students):
    excellent_students = []

    for student in students:
        if is_student_excellent(student):
            excellent_students.append(student)

    return excellent_students


def most_excellent_classroom(students_per_classroom):
    best_classroom = None
    best_classroom_count = -1

    for classroom in students_per_classroom:
        excellent_students = excellent_students(students_per_classroom[classroom])

        if len(excellent_students) > best_classroom_count:
            best_classroom = classroom
            best_classroom_count = len(excellent_students)

        elif len(excellent_students) == best_classroom_count:
            best_classroom = f"{best_classroom}, {classroom}"

    return best_classroom


def calculate_score_per_student(student):
    score = 0

    for result in student["resultaten"]:
        if student["resultaten"][result] == "uitstekend":
            score += 3
        if student["resultaten"][result] == "goed":
            score += 2
        if student["resultaten"][result] == "voldoende":
            score += 1

    return score


def best_scoring_classroom(students_per_classroom):
    best_classroom = ""
    best_classroom_score = 0

    for classroom in students_per_classroom:
        classroom_score = 0

        for student in students_per_classroom[classroom]:
            classroom_score += calculate_score_per_student(student)

        if classroom_score > best_classroom_score:
            best_classroom = classroom
            best_classroom_score = classroom_score

        elif classroom_score == best_classroom_score:
            best_classroom = f"{best_classroom}, {classroom}"

    return best_classroom


def failed_students(students, min_score=3):
    failed_students = []

    for student in students:
        score = calculate_score_per_student(student)

        if score < min_score:
            student["score"] = score
            failed_students.append(student)

    return failed_students


def full_report(students_per_classroom):
    all_students = []

    for classroom in students_per_classroom:
        for student in students_per_classroom[classroom]:
            all_students.append(student)

    print("----- Report -----")
    print("Excellente studenten:")

    excellent_students = excellent_students(all_students)
    for student in excellent_students:
        print(f'\t{student["naam"]}')

    print("Klas met de meeste excellente studenten:")
    
    best_classroom = most_excellent_classroom(students_per_classroom)
    print(f"\t{best_classroom}")

    print("Klas met de hoogste scores gemiddeld:")

    best_classroom = best_scoring_classroom(students_per_classroom)
    print(f"\t{best_classroom}")

    print("Studenten met inhaalopdracht:")

    failed_students = failed_students(all_students)
    for student in failed_students:
        print(f'\t{student["naam"]}')
        
        for subject, result in student["resultaten"].items():
            print(f"\t\t{subject}: {result}")


full_report(students_per_classroom)

