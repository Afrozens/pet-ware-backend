import secrets

USER_VERIFY_ACCOUNT = 'verify-account'
FORGOT_PASSWORD = "password-reset"
SPECIAL_CHARACTERS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>']

def is_password_strong_enough(password: str) -> bool:
    if len(password) < 8:
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False

    if not any(char.isdigit() for char in password):
        return False

    if not any(char in SPECIAL_CHARACTERS for char in password):
        return False

    if len(password) > 15:
        False

    return True

def unique_string(byte: int = 8) -> str:
    return secrets.token_urlsafe(byte)
