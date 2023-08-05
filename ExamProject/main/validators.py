from django.core.exceptions import ValidationError
import re


def atleast_one_digit(value):
    pattern = r'(?=.*\d)(.*[!@#$%^&*?])'
    check_pattern = re.search(pattern, value)

    if not check_pattern:
        raise ValidationError('Password should contain at least one digit and one special symbol [!@#$%^&*?]')
    return value


def check_password_are_same(value):
    if value != atleast_one_digit:
        raise ValidationError("Password did not match")