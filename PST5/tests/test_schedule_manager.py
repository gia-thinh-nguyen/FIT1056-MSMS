# tests/test_schedule_manager.py
import pytest
import os
from app.schedule import ScheduleManager

from app.student import StudentUser
# A pytest fixture creates a clean environment for each test function.
@pytest.fixture
def fresh_manager():
    """Creates a fresh ScheduleManager instance using a temporary test data file."""
    test_file = "test_data.json"
    # ARRANGE: Ensure no old test file exists.
    if os.path.exists(test_file):
        os.remove(test_file)
    return ScheduleManager(data_path=test_file)

def test_create_course(fresh_manager):
    # ARRANGE: We have a fresh manager from the fixture.
    # ACT: Call the method we want to test.
    fresh_manager.create_course("Beginner Piano", "Piano", 1)
    # ASSERT: Check if the outcome is what we expect.
    assert len(fresh_manager.courses) == 1
    assert fresh_manager.courses[0].name == "Beginner Piano"

def test_record_payment_and_history(fresh_manager):
    # ARRANGE: Add a dummy student to the manager for the test.
    # This test verifies the core financial logic you added in Fragment 5.1.
    student_id_to_test = 1
    test_student = StudentUser(student_id_to_test, "Test Student")
    fresh_manager.students.append(test_student)

    # ACT: Record a payment for that student.
    fresh_manager.record_payment(student_id_to_test, 100.00, "Credit Card")
    
    # ACT 2: Get the payment history.
    history = fresh_manager.get_payment_history(student_id_to_test)

    # ASSERT: Check the results.
    assert len(history) == 1
    assert history[0]['amount'] == 100.00
    assert history[0]['method'] == "Credit Card"
    
def test_get_payment_history_no_results(fresh_manager):
    # ARRANGE: Create a student with no payments recorded.
    student_id_to_test = 2
    test_student = StudentUser(student_id_to_test, "Student With No Payments")
    fresh_manager.students.append(test_student)
    
    # ACT: Get the payment history for this student.
    history = fresh_manager.get_payment_history(student_id_to_test)
    
    # ASSERT: Verify that an empty list is returned.
    assert len(history) == 0
    assert history == []

# tests/test_schedule_manager.py
# ... (fixture setup) ...
