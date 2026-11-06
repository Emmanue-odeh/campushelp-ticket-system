from users import (
    register_student,
    register_staff,
    students,
    staff_members
)


def setup_function():
    students.clear()
    staff_members.clear()


def test_register_student():
    result = register_student("Emmanuel", "emmanuel@gmail.com")

    assert result == True
    assert len(students) == 1
    assert students[0]["student_id"] == 1


def test_duplicate_student_email():
    register_student("Emmanuel", "emmanuel@gmail.com")

    result = register_student("John", "emmanuel@gmail.com")

    assert result == False
    assert len(students) == 1


def test_register_staff():
    result = register_staff("John", "john@gmail.com")

    assert result == True
    assert len(staff_members) == 1


def test_invalid_student_name():
    result = register_student("   ", "john@gmail.com")

    assert result == False