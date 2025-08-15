# pst2_main.py - The Persistent Application

import json
import datetime

DATA_FILE = "msms.json"
app_data = {} # This global dictionary will hold ALL our data.

# --- Core Persistence Engine ---
def load_data(path=DATA_FILE):
    """Loads all application data from a JSON file.
    path: The file path to load data from. (by default: msms.json)
    """
    global app_data
    try:
        # Open the file at 'path' in read mode ('r').
        with open(path, 'r') as f:
            #Use json.load(f) to load the file's content into the global 'app_data' variable.
            app_data = json.load(f)
            print("Data loaded successfully.")
    except FileNotFoundError:
        print("Data file not found. Initializing with default structure.")
        # If the file doesn't exist, initialize 'app_data' with a default dictionary.
        # It should have keys like: "students", "teachers", "attendance", "next_student_id", "next_teacher_id".
        # The lists should be empty and the IDs should start at 1.
        app_data = {
            "students": [],
            "teachers": [],
            "attendance": [],
            "next_student_id": 1,
            "next_teacher_id": 1
        }

def save_data(path=DATA_FILE):
    """Saves all application data to a JSON file.
    path: The file path to load data from. (by default: msms.json)
    """
    # Open the file at 'path' in write mode ('w').
    # Use json.dump() to write the global 'app_data' dictionary to the file.
    # Use the 'indent=4' argument in json.dump() to make the file readable.
    with open(path, 'w') as f:
        json.dump(app_data, f, indent=4)
    print("Data saved successfully.")

def add_teacher(name, speciality):
    """Adds a teacher dictionary to the data store.
    name: The name of the teacher (str)
    speciality: The speciality of the teacher (str)
    """
    # Get the next teacher ID from app_data['next_teacher_id'].
    teacher_id = app_data['next_teacher_id']
    # Create a new teacher dictionary with 'id', 'name', and 'speciality' keys.
    new_teacher = {"id": teacher_id, "name": name, "speciality": speciality}
    # Append the new dictionary to the app_data['teachers'] list.
    app_data['teachers'].append(new_teacher)
    # Increment the 'next_teacher_id' in app_data.
    app_data['next_teacher_id'] += 1
    print(f"Core: Teacher '{name}' added.")

def update_teacher(teacher_id, **fields):
    """Finds a teacher by ID and updates their data with provided fields.
    teacher_id: The ID of the teacher to update (int)
    **fields: The fields to update (dict)
    """
    # Loop through the app_data['teachers'] list (teachers)
    for teacher in app_data['teachers']:
        # If a teacher's 'id' matches teacher_id:
        if teacher['id'] == teacher_id:
            # Use the .update() method on the teacher dictionary to apply the 'fields'.
            teacher.update(fields)
            print(f"Teacher {teacher_id} updated.")
            return
    print(f"Error: Teacher with ID {teacher_id} not found.")

def remove_teacher(teacher_id):
    """Removes a teacher from the data store.
    teacher_id: The ID of the teacher to remove (int)
    """
    # Use a list comprehension to filter out the teacher with the matching ID.
    app_data['teachers'] = [t for t in app_data['teachers'] if t['id'] != teacher_id]
    print(f"Teacher {teacher_id} removed.")

def update_student(student_id, **fields):
    """Finds a student by ID and updates their data with provided fields.
    student_id: The ID of the student to update (int)
    **fields: The fields to update (dict)
    """
    # Loop through the app_data['students'] list (students)
    for student in app_data['students']:
        # If a student's 'id' matches student_id:
        if student['id'] == student_id:
            # Use the .update() method on the student dictionary to apply the 'fields'.
            student.update(fields)
            print(f"Student {student_id} updated.")
            return
    print(f"Error: Student with ID {student_id} not found.")

def remove_student(student_id):
    """Removes a student from the data store.
    student_id: The ID of the student to remove (int)
    """
    # Use a list comprehension to filter out the student with the matching ID.
    app_data['students'] = [s for s in app_data['students'] if s['id'] != student_id]
