import math
import secrets


def generate_password(alphabet: str, length: int) -> str:
    """
    Generate a random password of the specified length.
    """
    return "".join(secrets.choice(alphabet) for _ in range(length))


def calculate_entropy(length: int, alphabet_size: int) -> float:
    """
    Calculates password entropy in bits.
    """
    if length <= 0 or alphabet_size <= 1:
        return 0.0

    return length * math.log2(alphabet_size)


def assess_password_quality(length: int, alphabet_size: int) -> str:
    """
    Assesses the quality of a password based on its entropy.
    """
    entropy = calculate_entropy(length, alphabet_size)

    if entropy <= 40:
        return "very weak"
    elif entropy <= 59:
        return "weak"
    elif entropy <= 79:
        return "fair"
    elif entropy <= 99:
        return "strong"
    else:
        return "very strong"
