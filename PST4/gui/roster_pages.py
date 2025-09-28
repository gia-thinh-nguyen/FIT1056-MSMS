# gui/roster_pages.py
import streamlit as st
import pandas as pd

def show_roster_page(manager):
    """Renders the daily roster and check-in functionality."""
    st.header("Daily Roster")

    # --- View Roster Section (remains the same) ---
    day = st.selectbox("Select a day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
    # ... (code to display the dataframe) ...
    roster_data = []
    for course in manager.courses:
        for lesson in course.lessons:
            if lesson["day"] == day:
                # Get teacher name
                teacher = next((t for t in manager.teachers if t.id == course.teacher_id), None)
                teacher_name = teacher.name if teacher else "Unknown"
                
                # Get enrolled students for this course
                enrolled_students = [s.name for s in manager.students if course.id in s.enrolled_course_ids]
                
                roster_data.append({
                    "Time": lesson["start_time"],
                    "Course": course.name,
                    "Instrument": course.instrument,
                    "Teacher": teacher_name,
                    "Room": lesson["room"],
                    "Students": ", ".join(enrolled_students) if enrolled_students else "No students enrolled"
                })
    
    if roster_data:
        # Create and display the DataFrame
        df = pd.DataFrame(roster_data)
        df = df.sort_values("Time")  # Sort by time
        st.dataframe(df, use_container_width=True)
    else:
        st.info(f"No lessons scheduled for {day}")
    # --- Student Check-in Section (now works correctly) ---
    st.subheader("Student Check-in")
    with st.form("check_in_form"):
        # To make this user-friendly, we should populate the dropdowns dynamically.
        # Get lists of student names and course names from the manager.
        student_list = {s.name: s.id for s in manager.students}
        course_list = {c.name: c.id for c in manager.courses}
        
        selected_student_name = st.selectbox("Select Student", student_list.keys())
        selected_course_name = st.selectbox("Select Course", course_list.keys())
        
        submitted = st.form_submit_button("Check-in Student")

        if submitted:
            # Convert the selected names back to IDs
            student_id = student_list[selected_student_name]
            course_id = course_list[selected_course_name]

            # This call now works because we implemented the method in PST3.
            success = manager.check_in(student_id, course_id)

            if success:
                st.success(f"Checked in {selected_student_name} for {selected_course_name}!")
            else:
                # The manager's print statements will go to the console, but we can add a GUI error too.
                st.error("Check-in failed. See console for details. (Is the student enrolled in that course?)")