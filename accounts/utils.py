import secrets
import string


def random_N_chars_str(n: int) -> string:
    return (''.join(secrets.choice(string.ascii_uppercase + string.digits + string.digits) for _ in range(n)))

