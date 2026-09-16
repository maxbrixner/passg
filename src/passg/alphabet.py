import enum

# Full alphabet, i.e. letters, digits, and punctuation
FULL_ALPHABET = (
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
)

# Readable alphabet, i.e. letters, digits, and punctuation without
# zero, O, o, 1 and l.
READABLE_ALPHABET = (
    "abcdefghijkmnpqrstuvwxyz"
    "ABCDEFGHIJKLMNPQRSTUVWXYZ"
    "23456789"
    "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
)

# Reduced alphabet, i.e. letters, digits and punctuation that are commonly
# allowed in passwords
REDUCED_ALPHABET = (
    "abcdefghijkmnpqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ0123456789#$%!-_"
)

# Only letters
ALPHA_ALPHABET = "abcdefghijkmnpqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ"

# Only letters and digits
ALPHANUM_ALPHABET = (
    "abcdefghijkmnpqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ0123456789"
)

# Only digits
NUM_ALPHABET = "0123456789"


alphabet_mapping = {
    "full": FULL_ALPHABET,
    "readable": READABLE_ALPHABET,
    "reduced": REDUCED_ALPHABET,
    "alpha": ALPHA_ALPHABET,
    "alphanum": ALPHANUM_ALPHABET,
    "num": NUM_ALPHABET,
}


class Alphabet(str, enum.Enum):
    full = "full"
    readable = "readable"
    reduced = "reduced"
    alpha = "alpha"
    alphanum = "alphanum"
    num = "num"
