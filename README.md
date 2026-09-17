# passg

A minimal password generator I wrote for personal use.

Passg can either generate passwords consisting of random characters or passphrases consisting of random words.

## Prerequisites

- Python 3.14+
- uv (Python package manager)
- xclip (For copying to clipboard using `--copy` on Linux)

## Installation

```bash
uv tool install .
uv tool update-shell
```

## Usage

Generate a list of random passwords:

```bash
passg 
```

which is equivalent to

```bash
passg password
```

Generate a list of random passphrases:

```bash
passg passphrase
```

To just generate a single password or passphrase and directly copy it to the
clipboard without displaying it in the terminal, add `--copy` to the command:

```bash
passg password --copy
passg passphrase --copy
```

See all command line options:

```bash
passg password --help
passg passphrase --help
```
