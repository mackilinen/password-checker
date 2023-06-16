import re
from typing import Callable, Tuple

from password_checker.core.constants import (
    LESS_THEN_7,
    LESS_THEN_10,
    NO_LETTERS,
    NO_NUMBERS,
    NO_SPECIAL,
)
from password_checker.core.enums import PasswordStrength, UserType

special_char = re.compile("[@_!#$%^&*()<>?/\\|}{~:]")


def check_strength(
    password: str, user_type: UserType = UserType.USER
) -> Tuple[PasswordStrength, list[str]]:
    error_list = []

    for rule in get_rules(user_type):
        result = rule(password)
        if result[0] is False:
            error_list.append(result[1])

    return (
        PasswordStrength.WEAK if error_list else PasswordStrength.STRONG,
        error_list,
    )


def check_user_length(string: str) -> Tuple[bool, str]:
    valid = len(string) >= 7
    return (valid, "" if valid else LESS_THEN_7)


def check_admin_length(string: str) -> Tuple[bool, str]:
    valid = len(string) >= 10
    return (valid, "" if valid else LESS_THEN_10)


def check_character(string: str) -> Tuple[bool, str]:
    valid = any(char.isalpha() for char in string)
    return (valid, "" if valid else NO_LETTERS)


def check_number(string: str) -> Tuple[bool, str]:
    valid = any(char.isnumeric() for char in string)
    return (valid, "" if valid else NO_NUMBERS)


def check_special_character(string: str) -> Tuple[bool, str]:
    valid = True if special_char.search(string) else False
    return (valid, "" if valid else NO_SPECIAL)


def get_rules(user_type: UserType) -> list[Callable[[str], Tuple[bool, str]]]:
    if user_type == UserType.USER:
        return [check_user_length, check_character, check_number]
    elif user_type == UserType.ADMIN:
        return [
            check_admin_length,
            check_character,
            check_number,
            check_special_character,
        ]
    else:
        return []
