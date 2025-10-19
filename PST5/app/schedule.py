import json
from app.student import StudentUser
# Corrected Import: TeacherUser and Course now come from the same file.
from app.teacher import TeacherUser, Course
import csv
import datetime
class ScheduleManager:
    """The main controller for all business logic and data handling."""
    def __init__(self, data_path="data/msms.json"):
        self.data_path = data_path
        self.students = []
        self.teachers = []
        self.courses = []
        self.attendance_log = []
        self.finance_log = []
        self.next_lesson_id = 1
        self.next_student_id = 1
        self.next_teacher_id = 1
        self.next_course_id = 1
        self._load_data()

    def _load_data(self):
        """Loads data from the JSON file and populates the object lists."""
        try:
            with open(self.data_path, 'r') as f:
                data = json.load(f)
                # Load students
                for student_data in data.get("students", []):
                    student_id = student_data.get("id")
                    name = student_data.get("name")
                    student = StudentUser(student_id, name)
                    student.enrolled_course_ids = student_data.get("enrolled_course_ids", [])
                    self.students.append(student)
                # Load teachers
                for teacher_data in data.get("teachers", []):
                    teacher_id = teacher_data.get("id")
                    name = teacher_data.get("name")
                    speciality = teacher_data.get("speciality")
                    teacher = TeacherUser(teacher_id, name, speciality)
                    self.teachers.append(teacher)
                # Load courses
                for course_data in data.get("courses", []):
                    course_id = course_data.get("id")
                    name = course_data.get("name")
                    instrument = course_data.get("instrument")
                    teacher_id = course_data.get("teacher_id")
                    course = Course(course_id, name, instrument, teacher_id)
                    course.enrolled_student_ids = course_data.get("enrolled_student_ids", [])
                    course.lessons = course_data.get("lessons", [])
                    self.courses.append(course)

                # Load attendance log
                self.attendance_log = data.get("attendance", [])
                # Load finance log
                self.finance_log = data.get("finance", [])
                # Load next_id counters
                self.next_student_id = data.get("next_student_id", 1)
                self.next_teacher_id = data.get("next_teacher_id", 1)
                self.next_course_id = data.get("next_course_id", 1)
        except FileNotFoundError:
            print("Data file not found. Starting with a clean state.")
    
    def _save_data(self):
        """Converts object lists back to dictionaries and saves to JSON."""
        data_to_save = {
            "students": [
                {
                    "id": student.user_id,
                    "name": student.name,
                    "enrolled_course_ids": student.enrolled_course_ids
                }
                for student in self.students
            ],
            "teachers": [
                {
                    "id": teacher.user_id,
                    "name": teacher.name,
                    "speciality": teacher.speciality
                }
                for teacher in self.teachers
            ],
            "courses": [
                {
                    "id": course.course_id,
                    "name": course.name,
                    "instrument": course.instrument,
                    "teacher_id": course.teacher_id,
                    "enrolled_student_ids": course.enrolled_student_ids,
                    "lessons": course.lessons
                }
                for course in self.courses
            ],
            "attendance": self.attendance_log,
            "finance": self.finance_log,
            "next_student_id": self.next_student_id,
            "next_teacher_id": self.next_teacher_id,
            "next_course_id": self.next_course_id
        }
        
        with open(self.data_path, 'w') as f:
            json.dump(data_to_save, f, indent=4)

    def record_payment(self, student_id, amount, method):
        """Adds a payment record to the finance log."""
        # Find the student to ensure they exist.
        student_exist = False
        for student in self.students:
            if student.user_id == student_id:
                student_exist = True
                break
        if not student_exist:
            print(f"Error: Student with ID {student_id} does not exist.")
            return
        # Create a payment dictionary with student_id, amount, method, and a timestamp.
        payment_record = {
            "student_id": student_id,
            "amount": amount,
            "method": method,
            "timestamp": datetime.datetime.now().isoformat()
        }
        # Append the record to self.finance_log and save the data.
        self.finance_log.append(payment_record)
        self._save_data()
        print(f"Payment of {amount} for student {student_id} recorded.")

    def get_payment_history(self, student_id):
        """Returns a list of all payments for a given student."""
        # Use a list comprehension to filter self.finance_log
        # and return only the records that match the student_id.
        return [p for p in self.finance_log if p['student_id'] == student_id]

    def export_report(self, kind, out_path):
        """Exports a log to a CSV file."""
        print(f"Exporting {kind} report to {out_path}...")
        # Use an if/elif block to select the correct data list based on 'kind'.
        if kind == "finance":
            data_to_export = self.finance_log
            headers = ["student_id", "amount", "method", "timestamp"]
        elif kind == "attendance":
            data_to_export = self.attendance_log
            headers = ["student_id", "course_id", "timestamp"]
        else:
            print("Error: Unknown report type.")
            return

        # Use Python's 'csv' module to write the data.
        # Open the file, create a csv.DictWriter, write the header, then write all the rows.
        with open(out_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data_to_export)
        
        print(f"Report successfully exported to {out_path}")