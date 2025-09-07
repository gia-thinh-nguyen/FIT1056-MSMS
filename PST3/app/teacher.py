from app.user import User

class TeacherUser(User):
    """Represents a teacher."""
    # Implement the TeacherUser class, inheriting from User.
    # It should have an additional 'speciality' attribute in its __init__.
    def __init__(self, user_id, name, speciality):
        # Call the parent class's __init__ method using super().
        super().__init__(user_id, name)
        # Initialize the 'speciality' attribute.
        self.speciality = speciality

class Course:
    """Represents a single course offered by the school, linked to a teacher."""
    def __init__(self, course_id, name, instrument, teacher_id):
        self.id = course_id
        self.name = name
        self.instrument = instrument
        self.teacher_id = teacher_id
        # Initialize two empty lists: 'enrolled_student_ids' and 'lessons'.
        self.enrolled_student_ids = []
        self.lessons = [] # This will hold lesson dictionaries