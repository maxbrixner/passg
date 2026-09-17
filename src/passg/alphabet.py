import enum

# Full alphabet, i.e. letters, digits, and punctuation
FULL_ALPHABET = (
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
)

# Readable alphabet, i.e. letters, digits, and punctuation without
# ambiguous characters: 0, O, o, 1, l, I
READABLE_ALPHABET = (
    "abcdefghijkmnpqrstuvwxyz"
    "ABCDEFGHJKLMNPQRSTUVWXYZ"
    "23456789"
    "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
)

# Reduced alphabet, i.e. letters, digits and punctuation that are commonly
# allowed in passwords
REDUCED_ALPHABET = (
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%,-.:;?_"
)

# Reduced readable alphabet, i.e. letters, digits and punctuation that are commonly
# allowed in passwords without ambiguous characters: 0, O, o, 1, l, I
REDUCED_READABLE_ALPHABET = (
    "abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789!#$%,-.:;?_"
)

# Only letters
ALPHA_ALPHABET = "abcdefghijkmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Only letters and digits
ALPHANUM_ALPHABET = (
    "abcdefghijkmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
)

# Only digits
NUM_ALPHABET = "0123456789"


alphabet_mapping = {
    "full": FULL_ALPHABET,
    "readable": READABLE_ALPHABET,
    "reduced": REDUCED_ALPHABET,
    "reduced-readable": REDUCED_READABLE_ALPHABET,
    "alpha": ALPHA_ALPHABET,
    "alphanum": ALPHANUM_ALPHABET,
    "num": NUM_ALPHABET,
}


class Alphabet(str, enum.Enum):
    full = "full"
    readable = "readable"
    reduced = "reduced"
    reduced_readable = "reduced-readable"
    alpha = "alpha"
    alphanum = "alphanum"
    num = "num"
