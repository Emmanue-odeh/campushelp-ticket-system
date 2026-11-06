from validation import validate_name, validate_email

students = []
staff_members = []


def view_students():
    for student in students:
        print(student)


def register_student(name, email):
    if not validate_name(name):
        return False

    if not validate_email(email):
        return False

    for student in students:
        if student["email"] == email:
            return False

    student = {
        "student_id": len(students) + 1,
        "name": name.strip(),
        "email": email.strip()
    }
    students.append(student)
    return True

def find_student(student_id):
    for student in students:
        if student["student_id"] == student_id:
            return student

    return None
def view_staff():
    for staff in staff_members:
        print(staff)


def register_staff(name, email):
    if not validate_name(name):
        return False

    if not validate_email(email):
        return False

    for staff in staff_members:
        if staff["email"] == email:
            return False

    staff = {
        "staff_id": len(staff_members) + 1,
        "name": name.strip(),
        "email": email.strip()
    }

    staff_members.append(staff)
    return True
