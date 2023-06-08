# Provide the user with a list of reasons why their password is 'weak'

from password_checker.core.checker import check_strength
from password_checker.core.constants import (
    LESS_THEN_7,
    LESS_THEN_10,
    NO_LETTERS,
    NO_NUMBERS,
    NO_SPECIAL,
)
from password_checker.core.enums import PasswordStrength, UserType

all_numbers = 1234567
all_characters = "abcdefg"
short_length = "123ab!"
valid_user = "123abcd"
valid_admin = "12345abcd!"


def test_that_a_password_with_a_length_of_7_or_more_is_strong():
    password_strength = check_strength(valid_user)
    assert password_strength[0] == PasswordStrength.STRONG


def test_that_a_password_with_a_length_of_6_or_less_is_weak():
    password_strength = check_strength(short_length)
    assert password_strength[0] == PasswordStrength.WEAK
    assert LESS_THEN_7 in password_strength[1]


def test_that_a_password_with_1_or_more_characters_is_strong():
    password_strength = check_strength(valid_user)
    assert password_strength[0] == PasswordStrength.STRONG


def test_that_a_password_with_no_characters_is_weak():
    password_strength = check_strength(all_numbers)
    assert password_strength[0] == PasswordStrength.WEAK
    assert NO_LETTERS in password_strength[1]


def test_that_a_password_with_1_or_more_number_is_strong():
    password_strength = check_strength(valid_user)
    assert password_strength[0] == PasswordStrength.STRONG


def test_that_a_password_with_no_numbers_is_weak():
    password_strength = check_strength(all_characters)
    assert password_strength[0] == PasswordStrength.WEAK
    assert NO_NUMBERS in password_strength[1]


def test_that_admin_password_with_a_length_of_10_or_more_is_strong():
    password_strength = check_strength(valid_admin, UserType.ADMIN)
    assert password_strength[0] == PasswordStrength.STRONG


def test_that_admin_password_with_a_length_of_9_or_less_is_weak():
    password_strength = check_strength(short_length, UserType.ADMIN)
    assert password_strength[0] == PasswordStrength.WEAK
    assert LESS_THEN_10 in password_strength[1]


def test_that_admin_password_with_a_special_character_is_strong():
    password_strength = check_strength(valid_admin, UserType.ADMIN)
    assert password_strength[0] == PasswordStrength.STRONG


def test_that_admin_password_with_no_special_character_is_weak():
    password_strength = check_strength(valid_user, UserType.ADMIN)
    assert password_strength[0] == PasswordStrength.WEAK
    assert NO_SPECIAL in password_strength[1]
