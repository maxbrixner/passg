# passg

A minimal password generator I wrote for personal use.

Passg can generate either passwords made up of random characters or
passphrases made up of random words (using the
[EFF long word list](https://www.eff.org/dice)).

## Features

- Generate random-character passwords using a choice of built-in alphabets
  (full, readable, reduced, alphanumeric, alphabetic, or numeric only).
- Generate diceware-style passphrases from a word list, with optional
  capitalization and custom word separators.
- Copy a single password or passphrase directly to the clipboard with
  `--copy`, without printing it to the terminal.
- Optionally print an entropy-based quality assessment for the generated
  password or passphrase with `--quality`.
- Word lists are downloaded once and cached locally for future runs.

## Prerequisites

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) (Python package manager)
- `xclip` (for `--copy` to work on Linux)

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

which is equivalent to:

```bash
passg password
```

Generate a list of random passphrases:

```bash
passg passphrase
```

To generate a single password or passphrase and copy it directly to the
clipboard instead of printing it, add `--copy`:

```bash
passg password --copy
passg passphrase --copy
```

To print an entropy-based quality assessment alongside the output, add
`--quality`:

```bash
passg password --quality
passg passphrase --quality
```

See all available options for each command:

```bash
passg password --help
passg passphrase --help
```
