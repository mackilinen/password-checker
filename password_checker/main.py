from core.checker import check_strength
from core.enums import UserType


def main():
    print("Enter user type (user or admin)")
    user_type = input()
    print("Enter password to check strength:")
    password = input()
    password_strength = check_strength(password, UserType[user_type.upper()])
    print(f"The password is {password_strength[0].value}. {password_strength[1]}")


if __name__ == "__main__":
    main()
