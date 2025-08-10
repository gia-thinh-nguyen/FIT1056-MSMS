This is a simple Music School Management System (MSMS.py)
It lets a front-desk receptionist:
+Register new students
+Enroll existing students
+Search and list all students and teachers

-Data models:
+Student: id, name and enrolled instruments
+Teacher: id, name and speciality

-In memory database:
+student_db: stores Student objects.
+teacher_db: stores Teacher objects.
+next_student_id / next_teacher_id – to assign unique IDs.

-Helper functions:
+add_teacher(name, speciality): adds a new teacher object given name and speciality.
+list_students / list_teachers: show all students and teachers objects
+find_students(term): find students by name
+find_teachers(term): find teachers by name or speciality
+front_desk_lookup(term): search both students and teachers for any matches

-Front desk functions:
+front_desk_register(name,instrument) - register and enrol a student.
+front_desk_enrol(student_id, instrument) - add an instrument to an existing student.
+find_student_by_id(student_id) - retreives a student object through id.


The program is ran through the terminal and shown with print statements.