import typing

import pyperclip
import typer

from passg.alphabet import Alphabet, alphabet_mapping
from passg.generator import assess_password_quality, generate_password

app = typer.Typer()


@app.command()
def generate(
    length: typing.Annotated[
        int,
        typer.Option(
            min=1,
            max=500,
            help="Length of the passwords to generate",
        ),
    ] = 20,
    count: typing.Annotated[
        int,
        typer.Option(min=1, max=9999, help="Number of passwords to generate"),
    ] = 20,
    alphabet: typing.Annotated[
        Alphabet,
        typer.Option(
            help="Alphabet to use for generating passwords.",
        ),
    ] = Alphabet.reduced_readable,
    copy: typing.Annotated[
        bool,
        typer.Option(
            help="Copy a password to the clipboard without displaying it.",
        ),
    ] = False,
    quality: typing.Annotated[
        bool,
        typer.Option(
            help="Print Password quality assessment.",
        ),
    ] = False,
) -> None:
    """
    Generate a specified number of passwords of a given length using a specified alphabet.
    """
    if not alphabet.value in alphabet_mapping:
        raise typer.BadParameter(f"Invalid alphabet: {alphabet}")

    alphabet_chars = alphabet_mapping[alphabet.value]

    if copy:
        pyperclip.copy(
            generate_password(alphabet=alphabet_chars, length=length)
        )
        print("Password copied to clipboard.")
    else:
        for _ in range(count):
            print(generate_password(alphabet=alphabet_chars, length=length))

    if quality:
        password_quality = assess_password_quality(
            length=length, alphabet_size=len(set(alphabet_chars))
        )
        print(f"\nPassword quality: {password_quality}")


def main() -> None:
    """
    Main entry point for the passg CLI.
    """
    app()
