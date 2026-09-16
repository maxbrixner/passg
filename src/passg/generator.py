import secrets


def generate_password(alphabet: str, length: int) -> str:
    """
    Generate a random password of the specified length.
    """
    return "".join(secrets.choice(alphabet) for _ in range(length))
