from validation import validate_name, validate_email


def test_valid_name():
    assert validate_name("Emmanuel") == True


def test_empty_name():
    assert validate_name("") == False


def test_spaces_only_name():
    assert validate_name("   ") == False


def test_valid_email():
    assert validate_email("john@gmail.com") == True


def test_email_without_dot():
    assert validate_email("john@gmail") == False


def test_email_without_at():
    assert validate_email("john.com") == False