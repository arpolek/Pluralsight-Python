students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")


def read_file():
    try:
        f = open("students.txt", "r")
        content = f.readlines()
        print(content)
        f.close()
    except Exception:
        print("Could not read file")


def yes_or_no(question):
    answer = str(input((question+' (y/n): '))).lower().strip()
    try:
        if answer[:1] == 'y':
            return True
        elif answer[:1] == 'n':
            return False
        else:
            print('Wrong answer, type \'y\' or \'n\'')
            return yes_or_no(question)
    except Exception as error:
        print('Please enter valid input')
        print(error)
        return yes_or_no(question)


def add_student():
    """
    Adds the student to the student list.
    :param name: string - student name
    :param student_id: integer - optional student ID
    :return:
    """
    reply = True
    while reply is True:
        reply = yes_or_no('Do you want to add a student?')
        if reply is True:
            student_name = input('Enter student name: ') or "-1"
            student_id = input('Enter student id: ') or "-1"
            student = {"name": student_name, "student_id": student_id}
            students.append(student)
            save_file(student_name)


read_file()
print_students_titlecase()
add_student()