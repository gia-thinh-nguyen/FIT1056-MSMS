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
    def __init__(self, course_id, name, instrument, teacher_id, enrolled_student_ids=None, lessons=None):
        self.id = course_id
        self.name = name
        self.instrument = instrument
        self.teacher_id = teacher_id
        # Initialize two empty lists: 'enrolled_student_ids' and 'lessons' if not provided.
        self.enrolled_student_ids = enrolled_student_ids if enrolled_student_ids is not None else []
        self.lessons = lessons if lessons is not None else []