# main.py - The View Layer
from app.schedule import ScheduleManager
import os

current_directory = os.path.dirname(__file__)
os.chdir(current_directory)

def front_desk_daily_roster(manager, day):
    """Displays a pretty table of all lessons on a given day.
    manager: ScheduleManager instance
    day: Day of the week to display lessons
    """
    print(f"\n--- Daily Roster for {day} ---")
    # Notice: This code does not need to change. It doesn't care where the Course class lives.
    # It only talks to the manager.
    # Call a method on the manager to get the day's lessons and print them.
    for course in manager.courses:
        for lesson in course.lessons:
            if lesson['day'].lower() == day.lower():
                teacher = manager.find_teacher_by_id(course.teacher_id)
                print(f"Course: {course.name}, Teacher: {teacher.name}, Day: {lesson['day']}, Time: {lesson['start_time']}, Room: {lesson['room']}")

    

def switch_course(manager, student_id, from_course_id, to_course_id):
    """Switches a student from one course to another.
    manager: ScheduleManager instance
    student_id: ID of the student to switch
    from_course_id: ID of the course to switch from
    to_course_id: ID of the course to switch to
    """
    # TODO: Implement the logic to switch a student by calling methods on the manager.
    student = manager.find_student_by_id(student_id)
    from_course = manager.find_course_by_id(from_course_id)
    to_course = manager.find_course_by_id(to_course_id)

    if not student or not from_course or not to_course:
        print("Error: Invalid student or course ID.")
        return

    # Remove student from the old course and add to the new course.
    from_course.enrolled_student_ids.remove(student_id)
    to_course.enrolled_student_ids.append(student_id)
    # Update the student's enrolled courses.
    student.enrolled_course_ids.remove(from_course_id)
    student.enrolled_course_ids.append(to_course_id)
    manager._save_data()
    print(f"Success: Student {student.name} switched from {from_course.name} to {to_course.name}.")


def main():
    """Main function to run the MSMS application."""
    manager = ScheduleManager() # Create ONE instance of the application brain.
    
    while True:
        print("\n===== MSMS v3 (Object-Oriented) =====")
        print("1. View Daily Roster")
        print("2. Switch Student Course")
        print("3. Check-in Student")
        print("q. Quit")
        # TODO: Create a menu for the new PST3 functions.
        # Get user input and call the appropriate view function, passing 'manager' to it.
        choice = input("Enter choice: ")
        if choice == '1':
            day = input("Enter day (e.g., Monday): ")
            front_desk_daily_roster(manager, day)
        elif choice.lower() == 'q':
            break
        elif choice == '2':
            student_id = int(input("Enter student ID: "))
            from_course_id = int(input("Enter course ID to switch from: "))
            to_course_id = int(input("Enter course ID to switch to: "))
            switch_course(manager, student_id, from_course_id, to_course_id)
        elif choice == '3':
            student_id = int(input("Enter student ID: "))
            course_id = int(input("Enter course ID to check into: "))
            manager.check_in(student_id, course_id)
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()