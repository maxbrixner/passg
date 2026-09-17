import typing

import pyperclip
import typer

from passg.alphabet import Alphabet, alphabet_mapping
from passg.generator import (
    assess_quality,
    generate_passphrase,
    generate_password,
)
from passg.words import get_word_list

app = typer.Typer()

EFF_WORD_LIST_URL = (
    "https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt"
)


@app.command()
def password(
    length: typing.Annotated[
        int,
        typer.Option(
            "--length",
            "-l",
            min=1,
            max=500,
            help="Length of the passwords to generate",
        ),
    ] = 20,
    count: typing.Annotated[
        int,
        typer.Option(
            "--count",
            "-c",
            min=1,
            max=9999,
            help="Number of passwords to generate",
        ),
    ] = 20,
    alphabet: typing.Annotated[
        Alphabet,
        typer.Option(
            "--alphabet",
            "-a",
            help="Alphabet to use for generating passwords.",
        ),
    ] = Alphabet.reduced_readable,
    copy: typing.Annotated[
        bool,
        typer.Option(
            "--copy",
            "-y",
            help="Copy a password to the clipboard without displaying it.",
        ),
    ] = False,
    quality: typing.Annotated[
        bool,
        typer.Option(
            "--quality",
            "-q",
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
        password_quality = assess_quality(
            sample_size=length, pool_size=len(set(alphabet_chars))
        )
        print(f"\nPassword quality: {password_quality}")


@app.command()
def passphrase(
    length: typing.Annotated[
        int,
        typer.Option(
            "--length",
            "-l",
            min=1,
            max=20,
            help="Number of wordss in the passphrase",
        ),
    ] = 5,
    count: typing.Annotated[
        int,
        typer.Option(
            "--count",
            "-c",
            min=1,
            max=9999,
            help="Number of passwords to generate",
        ),
    ] = 20,
    capitalize: typing.Annotated[
        bool,
        typer.Option(
            "--capitalize",
            "-C",
            help="Capitalize the first letter of each word in the passphrase.",
        ),
    ] = True,
    separator: typing.Annotated[
        str,
        typer.Option(
            "--separator",
            "-s",
            help="Separator to use between words in the passphrase.",
        ),
    ] = "",
    url: typing.Annotated[
        str,
        typer.Option(
            "--url",
            "-u",
            help="URL to the word list to use for generating passphrases.",
        ),
    ] = EFF_WORD_LIST_URL,
    copy: typing.Annotated[
        bool,
        typer.Option(
            "--copy",
            "-y",
            help="Copy a password to the clipboard without displaying it.",
        ),
    ] = False,
    quality: typing.Annotated[
        bool,
        typer.Option(
            "--quality",
            "-q",
            help="Print Password quality assessment.",
        ),
    ] = False,
) -> None:
    """
    Generate a specified number of passphrases consisting of a given number ofrandom words.
    """
    word_list = get_word_list(url)

    if copy:
        pyperclip.copy(
            generate_passphrase(
                words=word_list,
                length=length,
                capitalize=capitalize,
                separator=separator,
            )
        )
        print("Passphrase copied to clipboard.")
    else:
        for _ in range(count):
            print(
                generate_passphrase(
                    words=word_list,
                    length=length,
                    capitalize=capitalize,
                    separator=separator,
                )
            )

    if quality:
        passphrase_quality = assess_quality(
            sample_size=length, pool_size=len(word_list)
        )
        print(f"\nPassphrase quality: {passphrase_quality}")


@app.callback(invoke_without_command=True)
def callback(ctx: typer.Context):
    """
    Generate passwords and passphrases.
    """
    if ctx.invoked_subcommand is None:
        ctx.invoke(password)


def main() -> None:
    """
    Main entry point for the passg CLI.
    """
    app()
