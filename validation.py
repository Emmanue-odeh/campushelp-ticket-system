def validate_email(email):
    email = email.strip()

    if email == "":
        return False

    if "@" not in email:
        return False

    if "." not in email:
        return False

    return True


def validate_name(name):
    name = name.strip()

    if name == "":
        return False
    else:
        return True

