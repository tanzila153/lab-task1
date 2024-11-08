import random

def read_student_ids(student_ids):
    with open('student_ids.txt', 'r') as file:
        student_ids = [line.strip() for line in file if line.strip()]
    return student_ids
def reset_student_list():
    return read_student_ids('student_ids.txt')
def select_student(student_list):
    while student_list:
        selected_student = random.choice(student_list)
        print("Selected students: ", selected_student)
        student_list.remove(selected_student)
def viva_selection():
    student = reset_student_list()
    select_student(student)
    print("All students have been selected. Resetting the list.")
viva_selection()