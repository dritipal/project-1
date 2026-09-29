def get_non_empty_input(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("Input cannot be empty.")


def get_integer_input(message):
    while True:
        value = input(message).strip()

        try:
            return int(value)
        except ValueError:
            print("Please enter a valid number.")


def get_email_input(message):
    while True:
        email = input(message).strip()

        if "@" in email and "." in email:
            return email

        print("Please enter a valid email address.")
