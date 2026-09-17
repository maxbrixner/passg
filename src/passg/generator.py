import math
import secrets


def generate_password(alphabet: str, length: int) -> str:
    """
    Generate a random password of the specified length.
    """
    return "".join(secrets.choice(alphabet) for _ in range(length))


def generate_passphrase(
    words: list[str],
    length: int,
    capitalize: bool,
    separator: str,
) -> str:
    """
    Generate a random passphrase consisting of random words.
    """
    chosen_words = [secrets.choice(words) for _ in range(length)]

    if capitalize:
        chosen_words = [word.capitalize() for word in chosen_words]

    return separator.join(chosen_words)


def calculate_entropy(sample_size: int, pool_size: int) -> float:
    """
    Calculates entropy in bits.
    """
    if sample_size <= 0 or pool_size <= 1:
        return 0.0

    return sample_size * math.log2(pool_size)


def assess_quality(sample_size: int, pool_size: int) -> str:
    """
    Assesses the quality of a password/passphrase based on its entropy.
    """
    entropy = calculate_entropy(sample_size=sample_size, pool_size=pool_size)

    if entropy <= 40:
        assessment = "very weak"
    elif entropy <= 59:
        assessment = "weak"
    elif entropy <= 79:
        assessment = "fair"
    elif entropy <= 99:
        assessment = "strong"
    else:
        assessment = "very strong"

    return f"{assessment} (entropy: {entropy:.2f} bits)"
