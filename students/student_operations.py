
from datetime import datetime as dt
from sys import path
from os import system
from tabulate import tabulate
clear=lambda:system("cls")

from json import load
try:
    with open("active_students.json","r") as storage:
        active_students= load(storage)
    with open("graduated_students.json","r") as storage1:
        graduated_students= load(storage1)
except(FileNotFoundError):
    active_students=[]
    graduated_students=[]

def check_codemelli(code_melli):
    if len(code_melli) != 10:
        return False
    for student in active_students:
        if student["code_melli"]==code_melli:
            return False
    return True

def check_studentcode(student_code):
    if len(student_code) != 5:
        return False
    for student in active_students:
        if student["student_code"]==student_code:
            return False
    return True

def add_student():
    clear()
    student={}
    student["first_name"]=input("please enter student's first name: ")
    if not student["first_name"].isalpha(): 
        input("\nstudent's firstname is wrong! ")
        return False
    student["last_name"]=input("please enter student's last name: ")
    if not student["last_name"].isalpha(): 
        input("\nstudent's lastname is wrong! ")
        return False
    while True:
        try:
            student["birthday"]=dt.strptime(input("plase enter student's birthday (yyyy/mm/dd): "),"%Y/%m/%d")
            student["birthday"]=student["birthday"].strftime("%Y/%m/%d")
            break
        except(ValueError):
            print("\nbirthday is wrong\n")

    student["code_melli"]=input("please enter student's code_melli: ")
    if not check_codemelli(student["code_melli"]):
        input("\ncode_melli must be a non-repetitive 10 digit number")
        return False

    student["student_code"]=input("please enter student code: ")
    if not check_studentcode(student["student_code"]):
        input("\nstudent_code must be a non-repetitive 5 digit number")
        return False

    student["courses"]=[]
    student["grade"]=[]
    while True:
        course_name = input("Enter course name: ")
        student["courses"].append(course_name)
        while True:
            try:
                grade = float(input("Enter grade : "))
                break
            except(ValueError):
                input("\nwrong grade! press enter to go back. ")
        student["grade"].append(grade)
        another_course = input("Enter another course ? (y/n Enter=Yes) ")
        if another_course.upper() != "Y":
            break
    active_students.append(student)
    input("student successfully has been added press enter to continue ")

def find_student():
    clear()
    student_code=input("\nEnter the student_code you want to find: ")
    for student in active_students:
        if student["student_code"] == student_code:
            print(student["first_name"])
            print(student["last_name"])
            print(student["birthday"])
            print(student["code_melli"])
            print(student["student_code"])
            print(student["courses"])
            print(student["grade"])
            input("\npress enter to go back to menu ")
    else:
        input("\nthis student could not be found! press enter to continue")

def remove_student():
    clear()
    student_code=input("\nEnter the student_code you want to move or delete: ")
    for student in active_students:
        if student["student_code"] == student_code:
            choice1=input("\nmove this student to graduated or delete it for ever? (d/m) ").upper()
            if choice1 == "M":
                check_move=input("\nAre you sure about moving this student? (y/n) ").upper()
                if check_move=="Y":
                    active_students.remove(student)
                    graduated_students.append(student)
                    input("the student has been moved ")
                if check_move== "N":
                    break
            if choice1 == "D":
                check_delete=input("\nAre you sure about deleting this student? (y/n) ").upper()
                if check_delete=="Y":
                    active_students.remove(student)
                    input("the student has been deleted")
                    break
                if check_delete== "N":
                    break
    else:
        input("\nThis student was not in the list! press enter to continue: ")

def  list_students():
    clear()
    print("-----------------------------------Active Student----------------------------------------------")
    print(tabulate(active_students,headers="keys"))
    print("\n\n\n\n\n\n")
    print("-----------------------------------Graduated Student----------------------------------------------")
    print(tabulate(graduated_students,headers="keys"))    
    input("\nPress enter to continue ")

def change_courses():
    clear()
    student_code=input("\nEnter the student_code you want to change: ")
    for student in active_students:
        if student["student_code"] == student_code:
            choice2= input("do you want to delete a course or add one? (d/a) ").upper()
            if choice2=="D":
                course_name = input("\nEnter the course you want to remove: ")
                if course_name in student["courses"]:
                    index = student["courses"].index(course_name)
                    student["courses"].pop(index)
                    student["grade"].pop(index)
                    input("\nThe course has been removed")
                else:
                    input("The course is not in list. press enter to continue")
                break
            if choice2 == "A":
                student["courses"].append(input("\nEnter the course you want to add. "))
                while True:
                    try:
                        student["grade"].append(float(input("\nEnter the grade of the course you added. ")))
                        break
                    except(ValueError):
                        input("\nThe grade must be a float. ")
                input("\nthe course has been added")
                break
    else:
        input("\nThis student was not in the list! press enter to continue: ")



def save_students():
    from json import dump
    try: 
        with open("active_students.json","w") as storage:
            dump(active_students,storage, indent=4)
            input("\nactive_students has been saved successfully. ")
        with open("graduated_students.json","w") as storage:
            dump(graduated_students,storage, indent=4)
            input("\ngraduated_students has been saved successfully. ")
    except(PermissionError):
        input("\nthese can not be saved in this drive! press enter to continue ")

