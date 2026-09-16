import typing

import typer

from passg.alphabet import Alphabet, alphabet_mapping
from passg.generator import generate_password

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
    ] = Alphabet.reduced,
) -> None:
    """
    Generate a specified number of passwords of a given length using a specified alphabet.
    """
    if not alphabet.value in alphabet_mapping:
        raise typer.BadParameter(f"Invalid alphabet: {alphabet}")

    alphabet_chars = alphabet_mapping[alphabet.value]
    for _ in range(count):
        print(generate_password(alphabet=alphabet_chars, length=length))


def main() -> None:
    """
    Main entry point for the passg CLI.
    """
    app()
