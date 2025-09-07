import json
from app.student import StudentUser
from app.teacher import TeacherUser, Course
import datetime

class ScheduleManager:
    """The main controller for all business logic and data handling."""
    def __init__(self, data_path="data/msms.json"):
        self.data_path = data_path
        self.students = []
        self.teachers = []
        self.courses = []
        # Initialize the new attendance_log attribute as an empty list.
        self.attendance_log = []
        # ... (next_id counters) ...
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
                self.students = [StudentUser(**student) for student in data.get("students", [])]
                # Load teachers
                self.teachers = [TeacherUser(**teacher) for teacher in data.get("teachers", [])]
                # Load courses
                self.courses = [Course(**course) for course in data.get("courses", [])]

                # Correctly load the attendance log.
                # Use .get() with a default empty list to prevent errors if the key doesn't exist.
                self.attendance_log = data.get("attendance", [])
                # Load next_id counters
                self.next_student_id = data.get("next_student_id", 1)
                self.next_teacher_id = data.get("next_teacher_id", 1)
                self.next_course_id = data.get("next_course_id", 1)
        except FileNotFoundError:
            print("Data file not found. Starting with a clean state.")
    
    def _save_data(self):
        """Converts object lists back to dictionaries and saves to JSON."""
        # Create a 'data_to_save' dictionary.
        data_to_save = {
            "students": [s.__dict__ for s in self.students],
            "teachers": [t.__dict__ for t in self.teachers],
            "courses": [c.__dict__ for c in self.courses],
            # Add the attendance_log to the dictionary to be saved.
            # Since it's already a list of dicts, no conversion is needed.
            "attendance": self.attendance_log,
            # ... (next_id counters) ...
            "next_student_id": self.next_student_id,
            "next_teacher_id": self.next_teacher_id,
            "next_course_id": self.next_course_id
        }
        # Write 'data_to_save' to the JSON file.
        with open(self.data_path, 'w') as f:
            json.dump(data_to_save, f, indent=4)
    
    def check_in(self, student_id, course_id):
        """Records a student's attendance for a course after validation.
        student_id: ID of the student checking in
        course_id: ID of the course for which the student is checking in
        returns: True if check-in is successful, False otherwise
        """
        # This implementation remains the same, but it will now function correctly.
        student = self.find_student_by_id(student_id)
        course = self.find_course_by_id(course_id)
        
        if not student or not course:
            print("Error: Check-in failed. Invalid Student or Course ID.")
            return False
            
        timestamp = datetime.datetime.now().isoformat()
        check_in_record = {"student_id": student_id, "course_id": course_id, "timestamp": timestamp}
        
        # This line will now work without causing an AttributeError.
        self.attendance_log.append(check_in_record)
        # Increase next_student_id to ensure unique IDs.
        self.next_student_id += 1
        self._save_data() # This will now correctly save the attendance log.
        print(f"Success: Student {student.name} checked into {course.name}.")
        return True
    
    def find_student_by_id(self, student_id):
        """Helper method to find a student by their ID.
        student_id: ID of the student to find
        returns: StudentUser object if found, None otherwise
        """
        for student in self.students:
            if student.id == student_id:
                return student
        return None
    def find_course_by_id(self, course_id):
        """Helper method to find a course by its ID.
        course_id: ID of the course to find
        returns: Course object if found, None otherwise
        """
        for course in self.courses:
            if course.id == course_id:
                return course
        return None