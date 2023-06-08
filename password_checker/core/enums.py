from enum import Enum


class PasswordStrength(Enum):
    STRONG = "strong"
    WEAK = "weak"


class UserType(Enum):
    ADMIN = "admin"
    USER = "user"
