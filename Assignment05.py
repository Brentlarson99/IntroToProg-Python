# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log:
#   Brent Larson,2/11/2024,Assignment 05
# ------------------------------------------------------------------------------------------ #

# Constants
MENU = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

FILE_NAME = "Enrollments.json"

# Variables
student_first_name = ""
student_last_name = ""
course_name = ""
json_data = ""
file = None
menu_choice = ""
student_data: dict = {}
students: list = []

# Input/Output

# Reading 'Enrollments.json'
import json

try:
    file = open(FILE_NAME, "r")
    student_data = json.load(file)
    students = student_data.get("students", [])
    file.close()
except (FileNotFoundError, json.decoder.JSONDecodeError):
    students = []
    print(f"File {FILE_NAME} not found, starting with empty list")


# Display Main Menu
while MENU:
    print(MENU)
    menu_choice = input("Please select an option: ")

    # Menu Choice 1
    if menu_choice == "1":
        student_first_name = input("Please enter the student first name: ").strip()
        while not student_first_name:
            student_first_name = input("Please enter a valid name")
        student_last_name = input("Please enter the student last name: ").strip()
        while not student_last_name:
            student_last_name = input("Please enter a valid name")
        course_name = input(f"Please enter the course name for {student_first_name} {student_last_name}: ").strip()
        while not course_name:
            course_name = input("Please enter a valid course name")
        new_student = {"first_name": student_first_name, "last_name": student_last_name, "course_name": course_name}
        students.append(new_student)


    elif menu_choice == "2":
        if not students:
            print("No students have been registered yet")
        else:
            print("Current students who are registered:")
            for student in students:
                print(f"{student['first_name']} {student['last_name']} {student['course_name']}")
        

    elif menu_choice == "3":
        student_data = {"students": students}
        try:
            file = open(FILE_NAME, "w")
            json.dump(student_data, file)
            file.close()
            print("You have now saved the current students into the file")
        except FileNotFoundError:
            students = []
            print(f"File {FILE_NAME} not found, starting with empty list")

    elif menu_choice == "4":
        print("You are exiting the program")
        break

    else:
        print("Invalid")



